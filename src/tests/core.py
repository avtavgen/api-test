import asyncio
import os
from contextlib import asynccontextmanager
from typing import AsyncGenerator

import anyio
import pytest_asyncio
from alembic import command, context
from alembic.config import Config
from asgi_lifespan import LifespanManager
from fastapi import FastAPI, Depends, HTTPException, status
from httpx import AsyncClient, ASGITransport
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncConnection
from sqlmodel.ext.asyncio.session import AsyncSession
from uvicorn import lifespan

from src.db.core import get_session
from src.main import app
from src.service.security import API_KEY_SECURITY, key_sec

alembic_ini_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../alembic.ini"))

TEST_DATABASE_URL = "sqlite+aiosqlite:///:memory:"
TEST_AUTH_TOKEN = "TestToken"
TEST_USER_DATA = {"name": "test_user", "email": "test@email", "password": "12345"}

engine_test = create_async_engine(TEST_DATABASE_URL)
AsyncSessionTest = async_sessionmaker(bind=engine_test, class_=AsyncSession, expire_on_commit=False)


async def get_test_session() -> AsyncGenerator:
    async with AsyncSessionTest() as session:
        yield session


async def mock_key_sec(x_api_key: str = API_KEY_SECURITY) -> bool | None:
    if not x_api_key:
        return None
    return x_api_key == TEST_AUTH_TOKEN


def run_upgrade(connection: AsyncConnection, cfg: Config) -> None:
    cfg.attributes["connection"] = connection
    command.upgrade(cfg, "head")


async def run_async_upgrade() -> None:
    async with engine_test.begin() as conn:
        await conn.run_sync(run_upgrade, Config(alembic_ini_path))


@pytest_asyncio.fixture
async def async_client() -> AsyncGenerator:
    app.dependency_overrides[get_session] = get_test_session  # type: ignore[attr-defined]
    app.dependency_overrides[key_sec] = mock_key_sec  # type: ignore[attr-defined]
    # app.dependency_overrides[lifespan] = test_lifespan(app)  # type: ignore[attr-defined]
    await run_async_upgrade()

    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        yield client

    app.dependency_overrides.clear()  # type: ignore[attr-defined]
