from datetime import date
from pydantic import BaseModel


class CompraShow(BaseModel):
    codigoCompra: int
    dataCompra: date
    itemCompra: str
    valorCompra: float
