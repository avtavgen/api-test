import os
from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import create_async_engine
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.orm import sessionmaker

engine = create_async_engine(os.environ.get("DATABASE_URL"), echo=False)

AsyncSessionLocal = create_async_engine(
    os.environ.get("DATABASE_URL"),
    echo=True,
    future=True,
    poolclass=NullPool
)


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        yield session
