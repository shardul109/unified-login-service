from typing import Optional

from fastapi import FastAPI
from uvicorn import run

app = FastAPI()


if __name__ == '__main__':

    run("main:app", host="127.0.0.1", port=5001, reload=True)
