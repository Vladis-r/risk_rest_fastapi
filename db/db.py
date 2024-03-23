import os

import dotenv
from sqlmodel import create_engine, SQLModel
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from .models import *


dotenv.load_dotenv()

DATABASE_URL = os.environ.get("SQLA_DB_URL")
IS_DEBUG = bool(os.environ.get("IS_DEBUG"))

engine = create_async_engine(DATABASE_URL, echo=IS_DEBUG)
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


def init_db():
    e = create_engine(DATABASE_URL.replace('asyncpg', 'psycopg2'), echo=True)
    with e.begin() as conn:
        SQLModel.metadata.create_all(e)
    e.dispose()


async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session
