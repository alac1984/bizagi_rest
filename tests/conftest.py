import pytest
from datetime import date
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from repository.base import Base
from repository.models import Fornecedor, Compra

test_db_uri = "sqlite:///:memory:"
engine = create_engine(test_db_uri)

SessionTesting = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(scope="function")
def session():
    Base.metadata.create_all(engine)
    session = SessionTesting()
    yield session
    session.close()
    Base.metadata.drop_all(engine)


@pytest.fixture(scope="function")
def init_db(session):
    forn1 = Fornecedor(name="forn1", rating=5)
    forn2 = Fornecedor(name="forn2", rating=3)
    com1 = Compra(
        forn_id=1, buy_date=date(2022, 1, 1), item="Computador", value=3400.01
    )
    com2 = Compra(forn_id=1, buy_date=date(2022, 9, 1), item="Carro", value=34580.72)
    session.add(forn1)
    session.add(forn2)
    session.add(com1)
    session.add(com2)
    session.commit()
