from sqlalchemy.orm import Session
from repository.models import Fornecedor, Compra
from repository.utils import last_compra_date
from schemas.fornecedor import FornecedorShow, FornecedorCreate, FornecedorShowFull
from schemas.compra import CompraShow


def retrieve_fornecedor_by_id(forn_id: int, session: Session):
    forn = session.query(Fornecedor).filter(Fornecedor.forn_id == forn_id).one()
    compras = session.query(Compra).filter(Compra.forn_id == forn_id).all()
    compras_show = []
    for compra in compras:
        compras_show.append(
            CompraShow(
                codigoCompra=compra.com_id,
                dataCompra=compra.buy_date,
                itemCompra=compra.item,
                valorCompra=compra.value,
            )
        )

    last_date = last_compra_date(forn_id, session)

    return FornecedorShow(
        dataUltimaCompra=last_date, rating=forn.rating, compras=compras_show
    )


def create_fornecedor(forn_data: FornecedorCreate, session: Session):
    forn = Fornecedor(name=forn_data.name, rating=forn_data.rating)

    session.add(forn)
    session.commit()

    return FornecedorShowFull(
        forn_id=forn.forn_id, name=forn.name, rating=forn.rating
    )
