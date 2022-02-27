from sqlalchemy import select

from db.models import Domain, DomainModel
from db.database import get_session


def create_domain(domain_str):
    session = get_session()
    with session.begin():
        domain = Domain(domain=domain_str)
        session.add(domain)

    return DomainModel.from_orm(domain)


def read_all_domains():
    session = get_session()
    with session.begin():
        statement = select(Domain)
        domains = [DomainModel.from_orm(domain) for domain in session.execute(
            statement).scalars().all()]
    return domains
