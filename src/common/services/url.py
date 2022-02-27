from sqlalchemy import select

from db.models import Url, UrlModel
from db.database import get_session


def create_url(url_string, domain_id):
    session = get_session()
    with session.begin():
        url = Url(url=url_string, domain_id=domain_id)
        session.add(url)

    return UrlModel.from_orm(url)


def read_all_domains():
    session = get_session()
    with session.begin():
        statement = select(Url)
        urls = [UrlModel.from_orm(url) for url in session.execute(
            statement).scalars().all()]

    return urls
