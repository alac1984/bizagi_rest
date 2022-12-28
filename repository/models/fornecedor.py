from repository.base import Base
from sqlalchemy import Column, Integer, String


class Fornecedor(Base):
    __tablename__ = "tb_forn"

    forn_id = Column(Integer(), primary_key=True)
    name = Column(String(), nullable=False)
    rating = Column(Integer())

    def __repr__(self):
        return (
            f"Fornecedor(id={self.forn_id}, name={self.name}, rating={self.rating})"
        )
