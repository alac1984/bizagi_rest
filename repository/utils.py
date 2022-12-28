from sqlalchemy import desc
from sqlalchemy.orm import Session
from repository.models import Compra


def last_compra_date(forn_id: int, session: Session):
    last_compra = session.query(Compra).order_by(desc(Compra.buy_date)).first()

    return last_compra.buy_date if last_compra else None
