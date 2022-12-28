from sqlalchemy.orm import Session
from repository.models import Fornecedor, Compra
from schemas.fornecedor import FornecedorShow
from schemas.compra import CompraShow


def retrieve_fornecedor_by_id(forn_id: int, session: Session):
    forn = session.query(Fornecedor).filter(Fornecedor.forn_id == forn_id).one()
    compras = session.query(Compra).filter(Compra.forn_id == forn_id).all()
    compras_show = []
    for compra in compras:
        compras_show.append(
            CompraShow(
                com_id=compra.com_id,
                date=compra.date,
                item=compra.item,
                value=compra.value,
            )
        )

    return FornecedorShow(
        forn_id=forn.forn_id, name=forn.name, rating=forn.rating, compras=compras_show
    )
