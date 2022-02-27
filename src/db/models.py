from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from .database import Base


class Domain(Base):
    __tablename__ = "domain"

    id = Column(Integer, primary_key=True)
    domain = Column(String(32))


class Url(Base):
    __tablename__ = "url"

    id = Column(Integer, primary_key=True)
    domain_id = Column(Integer, ForeignKey("domain.id"), nullable=False)
    url = Column(String)
    linked_from = Column(Integer, ForeignKey(
        "Url", remote_side=["id"], backref='link_urls'))


class RawTerms(Base):
    __tablename__ = "raw_terms"

    id = Column(Integer, primary_key=True)
    url_id = Column(Integer, ForeignKey("url.id"), nullable=False)
    domain_id = Column(Integer, ForeignKey("domain.id"), nullable=False)
    terms = Column(String)

    addresses = relationship("Address", back_populates="user")
