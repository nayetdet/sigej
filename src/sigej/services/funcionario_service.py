from datetime import date

from src.sigej.daos.funcionario_dao import FuncionarioDAO
from src.sigej.daos.pessoa_dao import PessoaDAO
from src.sigej.daos.setor_dao import SetorDAO
from src.sigej.daos.tipo_funcionario_dao import TipoFuncionarioDAO
from src.sigej.models.funcionario import Funcionario
from src.sigej.models.pessoa import Pessoa

class FuncionarioService:
    def __init__(
            self,
            pessoa_dao: PessoaDAO,
            funcionario_dao: FuncionarioDAO,
            setor_dao: SetorDAO,
            tipo_funcionario_dao: TipoFuncionarioDAO
    ):
        self.__pessoa_dao = pessoa_dao
        self.__funcionario_dao = funcionario_dao
        self.__setor_dao = setor_dao
        self.__tipo_funcionario_dao = tipo_funcionario_dao

    def cadastrar_pessoa(self, pessoa: Pessoa) -> int:
        return self.__pessoa_dao.insert(pessoa)

    def admitir(self, pessoa_id: int, tipo_funcionario_id: int, setor_id: int, data_admissao: date) -> int:
        if not self.__pessoa_dao.find_by_id(pessoa_id):
            raise ValueError("Pessoa não encontrada.")
        if not self.__setor_dao.find_by_id(setor_id):
            raise ValueError("Setor não encontrado.")
        if not self.__tipo_funcionario_dao.find_by_id(tipo_funcionario_id):
            raise ValueError("Tipo de funcionário não encontrado.")

        funcionario = Funcionario(
            pessoa_id=pessoa_id,
            tipo_funcionario_id=tipo_funcionario_id,
            setor_id=setor_id,
            data_admissao=data_admissao,
        )

        return self.__funcionario_dao.insert(funcionario)

    def demitir(self, funcionario_id: int, data_demissao: date):
        if not self.__funcionario_dao.find_by_id(funcionario_id):
            raise ValueError("Funcionário não encontrado.")
        self.__funcionario_dao.demitir(funcionario_id, data_demissao)

    def listar(self):
        return self.__funcionario_dao.list_all()
