import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from repository.base import Base
from repository.models import Fornecedor, Compra

test_db_uri = "sqlite:///:memory:"
engine = create_engine(test_db_uri)

SessionTesting = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(scope="module")
def create_tables():
    Base.metadata.create_all(engine)


@pytest.fixture(scope="function")
def session(create_tables):
    session = SessionTesting()
    yield session
    session.close()


@pytest.fixture(scope="function")
def init_db(session):
    forn1 = Fornecedor(name="forn1", rating=5)
    session.add(forn1)
    session.commit()
