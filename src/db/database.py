from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, scoped_session, sessionmaker

from . import config

engine = create_engine(config.SQLALCHEMY_DATABASE_URL, echo=True, future=True)

Base = declarative_base()


def get_session():
    session = scoped_session(sessionmaker(engine))
    return session
