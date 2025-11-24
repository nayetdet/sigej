from typing import List, Optional
from src.sigej.daos.fornecedor_dao import FornecedorDAO
from src.sigej.models.fornecedor import Fornecedor

class FornecedorService:
    def __init__(self, fornecedor_dao: FornecedorDAO):
        self.__fornecedor_dao = fornecedor_dao

    def listar(self) -> List[Fornecedor]:
        return self.__fornecedor_dao.list_all()

    def criar(self, nome: str, cnpj: Optional[str] = None) -> int:
        fornecedor = Fornecedor(nome=nome, cnpj=cnpj)
        return self.__fornecedor_dao.insert(fornecedor)
