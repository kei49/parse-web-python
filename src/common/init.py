from db.database import engine
from db.models import Base


def init():
    Base.metadata.create_all(engine)
