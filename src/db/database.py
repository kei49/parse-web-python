from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from . import config

engine = create_engine(config.SQLALCHEMY_DATABASE_URL, echo=True, future=True)
Session = sessionmaker(engine)
Base = declarative_base()
