from typing import Optional
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import validates  # , relationship
from sqlalchemy.types import BLOB
from pydantic import BaseModel, constr

from .database import Base
from util.regex import is_valid_domain, is_valid_url


class Domain(Base):
    __tablename__ = "domain"

    id = Column(Integer, primary_key=True, autoincrement=True)
    domain = Column(String(32))

    @validates("domain")
    def validate_domain(self, key, domain):
        is_valid_domain(domain)
        return domain


class Url(Base):
    __tablename__ = "url"

    id = Column(Integer, primary_key=True, autoincrement=True)
    domain_id = Column(Integer, ForeignKey("domain.id"), nullable=False)
    linked_from = Column(Integer, ForeignKey("url.id"), nullable=True)
    url = Column(String(128))

    @validates("url")
    def validate_domain(self, key, url):
        is_valid_url(url)
        return url


class RawTerms(Base):
    __tablename__ = "raw_terms"

    id = Column(Integer, primary_key=True, autoincrement=True)
    url_id = Column(Integer, ForeignKey("url.id"), nullable=False)
    domain_id = Column(Integer, ForeignKey("domain.id"), nullable=False)
    terms = Column(BLOB)


class DomainModel(BaseModel):
    id: int
    domain: constr(max_length=32)

    class Config:
        orm_mode = True


class UrlModel(BaseModel):
    id: int
    domain_id: int
    url: constr()
    linked_from: Optional[int]

    class Config:
        orm_mode = True


class RawTermsModel(BaseModel):
    id: int
    url_id: int
    domain_id: int
