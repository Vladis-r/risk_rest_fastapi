import os
from contextlib import asynccontextmanager
import uvicorn
import dotenv
from fastapi import FastAPI, APIRouter


from app import exceptions
from app.deposit.router import deposit_router
from app.database import init_db
from logger import app_logger

dotenv.load_dotenv()


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Загрузка БД, при необходимости"""
    app_logger.debug('Start application')
    # init_db()
    yield
    app_logger.info('App stopped')


app = FastAPI(lifespan=lifespan)

main_api_router = APIRouter()
main_api_router.include_router(deposit_router, prefix='/deposit', tags=['deposit'])
app.include_router(main_api_router)

exceptions.include_exc(app)


if __name__ == "__main__":
    uvicorn.run(os.getenv('APP_NAME'), host=os.getenv('APP_HOST'), port=int(os.getenv('APP_PORT')), log_level="info")
