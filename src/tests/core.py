from typing import AsyncGenerator

import pytest_asyncio
from httpx import AsyncClient, ASGITransport
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel

from src.db.core import get_session
from src.main import app

TEST_DATABASE_URL = "sqlite+aiosqlite:///:memory:"

engine_test = create_async_engine(TEST_DATABASE_URL, echo=True)
AsyncSessionTest = sessionmaker(bind=engine_test, class_=AsyncSession, expire_on_commit=False)


async def get_test_session() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionTest() as session:
        yield session

app.dependency_overrides[get_session] = get_test_session

@pytest_asyncio.fixture
async def async_client():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        async with engine_test.begin() as conn:
            await conn.run_sync(SQLModel.metadata.create_all)
        yield client
        async with engine_test.begin() as conn:
            await conn.run_sync(SQLModel.metadata.drop_all)
