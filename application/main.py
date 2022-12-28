from fastapi import FastAPI, Depends
from repository.session import get_db
from repository.fornecedor import retrieve_fornecedor_by_id
from sqlalchemy.orm import Session
from schemas.fornecedor import FornecedorShow

app = FastAPI()


@app.get("/")
def home():
    return {"result": "ok"}


@app.get("/fornecedores/{forn_id}/historico", response_model=FornecedorShow)
def get_fornecedor_historico(forn_id: int, session: Session = Depends(get_db)):
    forn = retrieve_fornecedor_by_id(forn_id, session)

    return forn
