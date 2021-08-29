from logging import log
from fastapi import APIRouter, HTTPException, Depends, status
from pydantic import BaseModel
from loguru import logger
from passlib.context import CryptContext
import requests

router = APIRouter()

pwd_cxt = CryptContext(schemes=['bcrypt'] , deprecated = 'auto')

class UserCreate(BaseModel):
    username: str
    password: str

@router.post('/createuser' , status_code=status.HTTP_201_CREATED)
def create_user(
    newuser : UserCreate
):
    try:
        hashed_pass = pwd_cxt.hash(newuser.password)
        PARAMS = {
            'username' : newuser.username,
            'hashed_password' : hashed_pass
        }
        response = requests.post('http://127.0.0.1:5001/createuser' , json=PARAMS)

        if response.status_code == 201:
            return {'detail' : 'successfully created user'}

        elif response.status_code == 405:
            return {'detail' : 'user already exists'}

        else:
            return {'detail' : 'critical error'}

    except Exception as e:
        logger.critical(f'{e}')
