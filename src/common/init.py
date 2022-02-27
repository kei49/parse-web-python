from src.db.database import engine, Session
from src.db.models import Base


def init():
    Base.metadata.create_all(engine)
    session = Session()

    return session
