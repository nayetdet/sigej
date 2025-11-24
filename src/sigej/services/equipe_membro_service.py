from datetime import date
from typing import Optional, List
from src.sigej.daos.equipe_manutencao_dao import EquipeManutencaoDAO
from src.sigej.daos.equipe_membro_dao import EquipeMembroDAO
from src.sigej.daos.funcionario_dao import FuncionarioDAO
from src.sigej.models.equipe_membro import EquipeMembro

class EquipeMembroService:
    def __init__(
        self,
        equipe_membro_dao: EquipeMembroDAO,
        equipe_dao: EquipeManutencaoDAO,
        funcionario_dao: FuncionarioDAO,
    ):
        self.__equipe_membro_dao = equipe_membro_dao
        self.__equipe_dao = equipe_dao
        self.__funcionario_dao = funcionario_dao

    def listar_por_equipe(self, equipe_id: int) -> List[EquipeMembro]:
        return self.__equipe_membro_dao.list_by_equipe(equipe_id)

    def adicionar_membro(
        self,
        equipe_id: int,
        funcionario_id: int,
        data_inicio: date,
        funcao: Optional[str] = None,
        data_fim: Optional[date] = None,
    ) -> int:
        if not self.__equipe_dao.find_by_id(equipe_id):
            raise ValueError("Equipe não encontrada.")
        if not self.__funcionario_dao.find_by_id(funcionario_id):
            raise ValueError("Funcionário não encontrado.")
        membro = EquipeMembro(
            equipe_id=equipe_id,
            funcionario_id=funcionario_id,
            data_inicio=data_inicio,
            data_fim=data_fim,
            funcao=funcao,
        )
        return self.__equipe_membro_dao.insert(membro)
