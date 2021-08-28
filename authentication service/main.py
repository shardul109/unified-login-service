from src.db.models import init_db
from typing import Optional
from loguru import logger
from fastapi import FastAPI
from uvicorn import run

app = FastAPI()

@app.on_event('startup')
async def init_process():
    init_db()
    logger.info('database initialized')


if __name__ == '__main__':

    run("main:app", host="127.0.0.1", port=5001, reload=True)
