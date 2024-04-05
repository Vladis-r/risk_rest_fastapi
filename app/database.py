from sqlmodel import create_engine, SQLModel
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from .deposit.models import *
from .settings import settings


engine = create_async_engine(settings.sqla_db_url, echo=settings.is_debug)
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


def init_db():
    e = create_engine(settings.sqla_db_url.replace('asyncpg', 'psycopg2'), echo=True)
    with e.begin() as conn:
        SQLModel.metadata.create_all(e)
    e.dispose()


async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session
