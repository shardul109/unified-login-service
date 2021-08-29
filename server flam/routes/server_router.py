from logging import critical, log
from fastapi import APIRouter, HTTPException, Depends, status
from pydantic import BaseModel
from loguru import logger
from passlib.context import CryptContext
import requests
from requests import status_codes
from starlette import responses
from starlette.status import HTTP_401_UNAUTHORIZED, HTTP_406_NOT_ACCEPTABLE

router = APIRouter()

pwd_cxt = CryptContext(schemes=['bcrypt'] , deprecated = 'auto')

class UserCreate(BaseModel):
    username: str
    password: str

@router.post('/createuser' , status_code=status.HTTP_201_CREATED , tags=['create user'])
def create_user(
    newuser : UserCreate
):
    try:
        PARAMS = {
            'username' : newuser.username,
            'password' : newuser.password
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
        raise HTTP_406_NOT_ACCEPTABLE


@router.post('/authenticate' , tags=['authentication'] , status_code= status.HTTP_202_ACCEPTED)
def authenticate(
    userdata : UserCreate
):
    try:
        PARAMS = {
            'username' : userdata.username
        }
        response = requests.get('http://127.0.0.1:5001/authenticate', PARAMS)
        response = response.json()

        if pwd_cxt.verify(userdata.password , response['hashed_password']):
            return {'detail' : 'authorized'}

        else:
            logger.info('invalid password')
            raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED,detail='invalid password')

    except HTTPException as e:
        raise e
    except Exception as e:
        logger.critical('f{e}')
        raise e