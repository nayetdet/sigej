from typing import List

from src.sigej.daos.marca_dao import MarcaDAO
from src.sigej.models.marca import Marca

class MarcaService:
    def __init__(self, marca_dao: MarcaDAO):
        self.__marca_dao = marca_dao

    def listar(self) -> List[Marca]:
        return self.__marca_dao.list_all()

    def criar(self, nome: str) -> int:
        marca = Marca(nome=nome)
        return self.__marca_dao.insert(marca)
