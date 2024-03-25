from fastapi.exceptions import RequestValidationError
from fastapi.responses import ORJSONResponse

from db.db import init_db
from db.models import Deposit, DepositBase
from services.deposit import deposit_service
from logger import app_logger
import os
from contextlib import asynccontextmanager

import uvicorn
import dotenv
from fastapi import FastAPI, Request

dotenv.load_dotenv()


@asynccontextmanager
async def lifespan(app: FastAPI):
    app_logger.info('Start application')
    # init_db()
    yield
    app_logger.info('App stopped')


app = FastAPI(lifespan=lifespan)

# EXCEPTION HANDLER
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: [RequestValidationError|ValueError]):
    error_msg = {'error': str(exc)}
    return ORJSONResponse(error_msg, status_code=400)


# VIEWS
@app.post("/deposit_calculation", status_code=200)
async def get_deposit_calculation(deposit: DepositBase):
    return deposit_service.calculate_deposit(deposit)


@app.get("/")
async def root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run(os.getenv('APP_NAME'), host=os.getenv('APP_HOST'), port=int(os.getenv('APP_PORT')), log_level="info")
