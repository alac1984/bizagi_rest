from fastapi import FastAPI, Depends
from repository.session import get_db
from repository.fornecedor import retrieve_fornecedor_by_id
from repository.fornecedor import create_fornecedor
from sqlalchemy.orm import Session
from schemas.fornecedor import FornecedorShow, FornecedorCreate, FornecedorShowFull

app = FastAPI()


@app.get("/fornecedores/{forn_id}/historico", response_model=FornecedorShow)
def get_fornecedor_historico(forn_id: int, session: Session = Depends(get_db)):
    forn = retrieve_fornecedor_by_id(forn_id, session)

    return forn


@app.post("/fornecedores/criar", response_model=FornecedorShowFull)
def post_new_fornecedor(
    forn_data: FornecedorCreate, session: Session = Depends(get_db)
):
    forn = create_fornecedor(forn_data, session)

    return forn
