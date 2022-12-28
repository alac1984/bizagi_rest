from pydantic import BaseModel
from .compra import CompraShow


class FornecedorCreate(BaseModel):
    name: str
    rating: int


class FornecedorShow(BaseModel):
    forn_id: int
    name: str
    rating: int

    compras: list[CompraShow] = []
