from typing import List

from src.sigej.daos.equipe_manutencao_dao import EquipeManutencaoDAO
from src.sigej.models.equipe_manutencao import EquipeManutencao

class EquipeService:
    def __init__(self, equipe_dao: EquipeManutencaoDAO):
        self.__equipe_dao = equipe_dao

    def listar(self) -> List[EquipeManutencao]:
        return self.__equipe_dao.list_all()

    def criar(self, nome: str, turno: str) -> int:
        equipe = EquipeManutencao(nome=nome, turno=turno)
        return self.__equipe_dao.insert(equipe)
