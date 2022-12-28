from datetime import date
from repository.compra import create_compra
from schemas.compra import CompraShow, CompraCreate


def test_create_compra(session):
    com_data = CompraCreate(
        forn_id=1, date=date(2022, 1, 1), item="Carro", value="28324.42"
    )

    compra = create_compra(com_data, session)

    assert compra is not None
    assert isinstance(compra, CompraShow)
