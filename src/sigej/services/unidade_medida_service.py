from typing import List, Optional
from src.sigej.daos.unidade_medida_dao import UnidadeMedidaDAO
from src.sigej.models.unidade_medida import UnidadeMedida

class UnidadeMedidaService:
    def __init__(self, unidade_dao: UnidadeMedidaDAO):
        self.__unidade_dao = unidade_dao

    def listar(self) -> List[UnidadeMedida]:
        return self.__unidade_dao.list_all()

    def criar(self, sigla: str, descricao: Optional[str] = None) -> int:
        unidade = UnidadeMedida(sigla=sigla, descricao=descricao)
        return self.__unidade_dao.insert(unidade)
