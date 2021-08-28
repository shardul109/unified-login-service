from sqlalchemy import create_engine, Column, ForeignKey, Integer, String, Date, DateTime, Boolean, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker


cdb = None
DBSession: sessionmaker = None
Base = declarative_base()


def init_db():
    global cdb, DBSession
    config_path = f'config'
    cdb = create_engine(
        f'sqlite:///{config_path}/config.db', connect_args={'check_same_thread': False})
    Base.metadata.create_all(cdb)
    Base.metadata.bind = cdb
    DBSession = sessionmaker(bind=cdb)


def get_session():
    if DBSession is not None:
        session = DBSession()
        return session
    else:
        return None


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
