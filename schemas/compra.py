from datetime import date
from pydantic import BaseModel, Field


class CompraShow(BaseModel):
    codigoCompra: int
    dataCompra: date
    itemCompra: str
    valorCompra: float


class CompraCreate(BaseModel):
    forn_id: int
    buy_date: date = Field(default=date.today(), required=True)
    item: str
    value: float
