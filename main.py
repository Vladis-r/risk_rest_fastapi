import os
from logger import app_logger
from contextlib import asynccontextmanager

import uvicorn
import dotenv
from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import ORJSONResponse

from db.db import init_db
from db.models import DepositBase
from services.deposit import deposit_service

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
@app.post("/deposit_calculation", status_code=200, responses={400: {'content': {'application/json': {'example': {'error': 'error message'}}}},
                                                                200: {'content': {'application/json': {'example': {'date': 'amount', 'date_x': 'amount_x'}}}}})
async def get_deposit_calculation(deposit: DepositBase):
    return deposit_service.calculate_deposit(deposit)


if __name__ == "__main__":
    uvicorn.run(os.getenv('APP_NAME'), host=os.getenv('APP_HOST'), port=int(os.getenv('APP_PORT')), log_level="info")
