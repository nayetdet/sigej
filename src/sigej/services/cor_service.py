from typing import List

from src.sigej.daos.cor_dao import CorDAO
from src.sigej.models.cor import Cor

class CorService:
    def __init__(self, cor_dao: CorDAO):
        self.__cor_dao = cor_dao

    def listar(self) -> List[Cor]:
        return self.__cor_dao.list_all()

    def criar(self, nome: str) -> int:
        cor = Cor(nome=nome)
        return self.__cor_dao.insert(cor)
