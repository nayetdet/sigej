from typing import Optional, List
from src.sigej.daos.pessoa_dao import PessoaDAO
from src.sigej.models.pessoa import Pessoa

class PessoaService:
    def __init__(self, pessoa_dao: PessoaDAO):
        self.__pessoa_dao = pessoa_dao

    def cadastrar(
        self,
        nome: str,
        cpf: Optional[str] = None,
        matricula: Optional[str] = None,
        email: Optional[str] = None,
        telefone: Optional[str] = None,
    ) -> int:
        pessoa = Pessoa(nome=nome, cpf=cpf, matricula_siape=matricula, email=email, telefone=telefone)
        return self.__pessoa_dao.insert(pessoa)

    def listar(self) -> List[Pessoa]:
        return self.__pessoa_dao.list_all()

    def buscar(self, pessoa_id: int) -> Optional[Pessoa]:
        return self.__pessoa_dao.find_by_id(pessoa_id)
