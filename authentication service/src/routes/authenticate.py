from logging import log
from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm.session import Session
from . import get_db, get_session
from pydantic import BaseModel
from src.db.models import User
from loguru import logger

router = APIRouter()


class UserCreate(BaseModel):
    username: str
    hashed_password: str


@router.post('/createuser', status_code=status.HTTP_201_CREATED)
def create_user(
        newuser: UserCreate, db: Session = Depends(get_db)):

    try:
        response = db.query(User).filter_by(username=newuser.username).all()

        if len(response) != 0:
            logger.error('user already exists')
            raise HTTPException(
                status_code=status.HTTP_405_METHOD_NOT_ALLOWED, detail='user already exists')

        else:
            new_entry = User(
                username=newuser.username,
                password=newuser.hashed_password
            )
            db.add(new_entry)
            db.commit()
            logger.info('new user created successfully!')

    except Exception as e:
        logger.critical(f'{e}')
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=f'{e}')
