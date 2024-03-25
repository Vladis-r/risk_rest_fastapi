import asyncio
from typing import AsyncGenerator

import pytest
from httpx import AsyncClient, ASGITransport

from main import app


@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope='module')
async def ac_client() -> AsyncGenerator[AsyncClient, None]:
    async with AsyncClient(transport=ASGITransport(app=app), base_url='http://test') as ac_client:
        yield ac_client
