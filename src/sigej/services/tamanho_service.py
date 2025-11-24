from typing import List

from src.sigej.daos.tamanho_dao import TamanhoDAO
from src.sigej.models.tamanho import Tamanho

class TamanhoService:
    def __init__(self, tamanho_dao: TamanhoDAO):
        self.__tamanho_dao = tamanho_dao

    def listar(self) -> List[Tamanho]:
        return self.__tamanho_dao.list_all()

    def criar(self, descricao: str) -> int:
        tamanho = Tamanho(descricao=descricao)
        return self.__tamanho_dao.insert(tamanho)
