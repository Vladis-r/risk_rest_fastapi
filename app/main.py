from contextlib import asynccontextmanager
import uvicorn
from fastapi import FastAPI, APIRouter


from app import exceptions
from app.deposit.router import deposit_router
from app.database import init_db
from app.logger import app_logger
from app.settings import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Загрузка БД, при необходимости"""
    app_logger.info('Start application')
    # init_db()
    yield
    app_logger.info('App stopped')


app = FastAPI(lifespan=lifespan)

main_api_router = APIRouter()
main_api_router.include_router(deposit_router, prefix='/deposit', tags=['deposit'])
app.include_router(main_api_router)

exceptions.include_exc(app)


if __name__ == "__main__":
    uvicorn.run(settings.app_name, host=settings.app_host, port=settings.app_port, log_level="info")
