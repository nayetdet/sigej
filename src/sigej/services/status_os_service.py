from typing import List
from src.sigej.daos.status_ordem_servico_dao import StatusOrdemServicoDAO
from src.sigej.models.status_ordem_servico import StatusOrdemServico

class StatusOSService:
    def __init__(self, status_dao: StatusOrdemServicoDAO):
        self.__status_dao = status_dao

    def listar(self) -> List[StatusOrdemServico]:
        return self.__status_dao.list_all()

    def criar(self, descricao: str) -> int:
        status = StatusOrdemServico(descricao=descricao.lower())
        return self.__status_dao.insert(status)
