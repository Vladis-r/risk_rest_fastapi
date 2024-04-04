import asyncio
import os

import pytest
from typing import AsyncGenerator
from httpx import AsyncClient, ASGITransport
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from app.main import app


@pytest.fixture(scope="session")
def event_loop():
    """Получаем loop для избежания проблем с асинхронными тестами"""
    loop = asyncio.get_event_loop()
    # loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope='module')
async def ac_client() -> AsyncGenerator[AsyncClient, None]:
    """Получить асинхронный клиент для тестирования"""
    async with AsyncClient(transport=ASGITransport(app=app), base_url='http://test') as ac_client:
        yield ac_client


@pytest.fixture(scope="session")
async def async_db_session():
    """Соединение с тестовой базой"""
    engine = create_async_engine(os.getenv('TEST_DB_URL'), future=True, echo=True)
    async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
    yield async_session()
