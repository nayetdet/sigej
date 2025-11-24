from typing import List
from src.sigej.daos.tipo_ordem_servico_dao import TipoOrdemServicoDAO
from src.sigej.models.tipo_ordem_servico import TipoOrdemServico

class TipoOSService:
    def __init__(self, tipo_os_dao: TipoOrdemServicoDAO):
        self.__tipo_os_dao = tipo_os_dao

    def listar(self) -> List[TipoOrdemServico]:
        return self.__tipo_os_dao.list_all()

    def criar(self, descricao: str) -> int:
        tipo = TipoOrdemServico(descricao=descricao)
        return self.__tipo_os_dao.insert(tipo)
