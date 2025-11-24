from typing import Optional
from src.sigej.daos.setor_dao import SetorDAO
from src.sigej.models.setor import Setor

class SetorService:
    def __init__(self, setor_dao: SetorDAO):
        self.__setor_dao = setor_dao

    def listar(self):
        return self.__setor_dao.list_all()

    def criar(self, nome: str, sigla: Optional[str] = None) -> int:
        setor = Setor(nome=nome, sigla=sigla)
        return self.__setor_dao.insert(setor)
