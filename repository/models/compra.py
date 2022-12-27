from repository.base import Base
from datetime import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float
from sqlalchemy.orm import backref, relationship


class Compra(Base):
    __tablename__ = "tb_compra"

    com_id = Column(Integer(), primary_key=True)
    forn_id = Column(ForeignKey("tb_forn.forn_id"))
    date = Column(DateTime(), default=datetime.now)
    item = Column(String(), nullable=False)
    value = Column(Float(), nullable=False)

    forn = relationship("Fornecedor", backref=backref("compras", order_by=date))  # type: ignore

    def __repr__(self):
        return (
            f"Compra(id={self.com_id}, forn_id={self.forn_id}, "
            f"date={self.date}, item={self.item}, "
            f"value={self.value})"
        )
