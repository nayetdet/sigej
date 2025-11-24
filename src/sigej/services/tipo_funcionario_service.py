from typing import List
from src.sigej.daos.tipo_funcionario_dao import TipoFuncionarioDAO
from src.sigej.models.tipo_funcionario import TipoFuncionario

class TipoFuncionarioService:
    def __init__(self, tipo_funcionario_dao: TipoFuncionarioDAO):
        self.__tipo_funcionario_dao = tipo_funcionario_dao

    def listar(self) -> List[TipoFuncionario]:
        return self.__tipo_funcionario_dao.list_all()

    def criar(self, descricao: str) -> int:
        tipo = TipoFuncionario(descricao=descricao)
        return self.__tipo_funcionario_dao.insert(tipo)
