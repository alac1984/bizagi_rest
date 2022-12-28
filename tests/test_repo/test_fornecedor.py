from repository.fornecedor import retrieve_fornecedor_by_id
from schemas.fornecedor import FornecedorShow


def test_retrieve_fornecedor_by_id(init_db, session):
    forn = retrieve_fornecedor_by_id(1, session)

    assert forn is not None
    assert isinstance(forn, FornecedorShow)
    assert forn.forn_id == 1
