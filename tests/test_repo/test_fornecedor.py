from repository.fornecedor import retrieve_fornecedor_by_id
from repository.fornecedor import create_fornecedor
from repository.models import Fornecedor
from schemas.fornecedor import FornecedorShow, FornecedorCreate, FornecedorShowFull


def test_retrieve_fornecedor_by_id(init_db, session):
    forn = retrieve_fornecedor_by_id(1, session)

    assert forn is not None
    assert isinstance(forn, FornecedorShow)
    assert len(forn.compras) == 2


def test_create_fornecedor(session):
    forn_create = FornecedorCreate(name="test", rating=5)
    forn = create_fornecedor(forn_create, session)

    created_forn = session.query(Fornecedor).filter(Fornecedor.forn_id == 1).one()

    assert forn is not None
    assert created_forn is not None
    assert isinstance(forn, FornecedorShowFull)
    assert isinstance(created_forn, Fornecedor)
    assert forn.forn_id == 1
    assert created_forn.forn_id == 1
