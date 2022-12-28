from datetime import date
from pydantic import BaseModel


class CompraShow(BaseModel):
    com_id: int
    date: date
    item: str
    value: float
