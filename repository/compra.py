from sqlalchemy.orm import Session
from repository.models import Compra
from schemas.compra import CompraShow, CompraCreate


def create_compra(com_data: CompraCreate, session: Session):
    compra = Compra(
        forn_id=com_data.forn_id,
        buy_date=com_data.buy_date,
        item=com_data.item,
        value=com_data.value,
    )

    session.add(compra)
    session.commit()

    return CompraShow(
        codigoCompra=compra.com_id,
        dataCompra=compra.buy_date,
        itemCompra=compra.item,
        valorCompra=compra.value,
    )
