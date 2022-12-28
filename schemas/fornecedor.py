from datetime import date
from pydantic import BaseModel
from .compra import CompraShow


class FornecedorCreate(BaseModel):
    name: str
    rating: int


class FornecedorShow(BaseModel):
    dataUltimaCompra: date
    rating: int

    compras: list[CompraShow] = []
