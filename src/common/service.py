from src.db.models import Domain, DomainModel


def create_domain(session, domain_str):
    with session.begin():
        domain = Domain(domain=domain_str)
        session.add(domain)


def read_all_domains(session):
    with session.begin():
        domains = session.query(Domain).all()

        print(domains)
        domains = [DomainModel.from_orm(domain) for domain in domains]

        print(domains)
