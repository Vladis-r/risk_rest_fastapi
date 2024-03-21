from logger import app_logger
import os
from contextlib import asynccontextmanager

import uvicorn
import dotenv
from fastapi import FastAPI

dotenv.load_dotenv()


@asynccontextmanager
async def lifespan(app: FastAPI):
    app_logger.info('Start application')
    yield
    app_logger.info('App stopped')


app = FastAPI(lifespan=lifespan)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


if __name__ == "__main__":
    uvicorn.run(os.getenv('APP_NAME'), host=os.getenv('APP_HOST'), port=int(os.getenv('APP_PORT')), log_level="info")
