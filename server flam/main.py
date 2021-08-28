from typing import Optional
from loguru import logger
from fastapi import FastAPI
from uvicorn import run
from routes.server_router import router


app = FastAPI()

app.include_router(router)


@app.on_event('startup')
async def init_process():
    logger.info('flam server started')


if __name__ == '__main__':

    run("main:app", host="127.0.0.1", port=5002, reload=True)
