from typing import Optional, List
from src.sigej.daos.funcionario_dao import FuncionarioDAO
from src.sigej.daos.local_estoque_dao import LocalEstoqueDAO
from src.sigej.models.local_estoque import LocalEstoque

class LocalEstoqueService:
    def __init__(self, local_dao: LocalEstoqueDAO, funcionario_dao: FuncionarioDAO):
        self.__local_dao = local_dao
        self.__funcionario_dao = funcionario_dao

    def listar(self) -> List[LocalEstoque]:
        return self.__local_dao.list_all()

    def criar(self, descricao: str, responsavel_id: Optional[int] = None) -> int:
        if responsavel_id and not self.__funcionario_dao.find_by_id(responsavel_id):
            raise ValueError("Funcionário responsável não encontrado.")

        local = LocalEstoque(descricao=descricao, responsavel_id=responsavel_id)
        return self.__local_dao.insert(local)
