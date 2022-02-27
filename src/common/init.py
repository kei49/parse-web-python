from db.database import engine, Session
from db.models import Base


def init():
    Base.metadata.create_all(engine)
    session = Session()

    return session
