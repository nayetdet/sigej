from datetime import datetime
from typing import Optional
from src.sigej.daos.andamento_ordem_servico_dao import AndamentoOrdemServicoDAO
from src.sigej.daos.area_campus_dao import AreaCampusDAO
from src.sigej.daos.equipe_manutencao_dao import EquipeManutencaoDAO
from src.sigej.daos.funcionario_dao import FuncionarioDAO
from src.sigej.daos.item_ordem_servico_dao import ItemOrdemServicoDAO
from src.sigej.daos.ordem_servico_dao import OrdemServicoDAO
from src.sigej.daos.pessoa_dao import PessoaDAO
from src.sigej.daos.status_ordem_servico_dao import StatusOrdemServicoDAO
from src.sigej.daos.tipo_ordem_servico_dao import TipoOrdemServicoDAO
from src.sigej.models.andamento_ordem_servico import AndamentoOrdemServico
from src.sigej.models.item_ordem_servico import ItemOrdemServico
from src.sigej.models.ordem_servico import OrdemServico
from src.sigej.models.status_ordem_servico import StatusOrdemServico

class OrdemServicoService:
    def __init__(
        self,
        os_dao: OrdemServicoDAO,
        item_dao: ItemOrdemServicoDAO,
        andamento_dao: AndamentoOrdemServicoDAO,
        pessoa_dao: PessoaDAO,
        area_dao: AreaCampusDAO,
        tipo_os_dao: TipoOrdemServicoDAO,
        equipe_dao: EquipeManutencaoDAO,
        funcionario_dao: FuncionarioDAO,
        status_dao: StatusOrdemServicoDAO
    ):
        self.__os_dao = os_dao
        self.__item_dao = item_dao
        self.__andamento_dao = andamento_dao
        self.__pessoa_dao = pessoa_dao
        self.__area_dao = area_dao
        self.__tipo_os_dao = tipo_os_dao
        self.__equipe_dao = equipe_dao
        self.__funcionario_dao = funcionario_dao
        self.__status_dao = status_dao

    def abrir_os(
        self,
        solicitante_id: int,
        area_campus_id: int,
        tipo_os_id: int,
        equipe_id: int,
        lider_id: int,
        prioridade: int,
        descricao_problema: str,
        data_prevista: Optional[datetime] = None,
        numero_sequencial: Optional[str] = None,
        itens: Optional[list[dict]] = None,
    ) -> int:
        if not self.__pessoa_dao.find_by_id(solicitante_id):
            raise ValueError("Solicitante não encontrado.")
        if not self.__area_dao.find_by_id(area_campus_id):
            raise ValueError("Área do campus não encontrada.")
        if not self.__tipo_os_dao.find_by_id(tipo_os_id):
            raise ValueError("Tipo de OS não encontrado.")
        if not self.__equipe_dao.find_by_id(equipe_id):
            raise ValueError("Equipe não encontrada.")
        if not self.__funcionario_dao.find_by_id(lider_id):
            raise ValueError("Líder não encontrado.")

        status_aberta = self.__status_dao.find_by_id(1)
        if status_aberta:
            status_id = status_aberta.id
        else:
            status_id = self.__status_dao.insert(StatusOrdemServico(descricao="aberta"))
        numero = numero_sequencial or f"OS-{int(datetime.now().timestamp())}"
        os = OrdemServico(
            numero_sequencial=numero,
            solicitante_id=solicitante_id,
            area_campus_id=area_campus_id,
            tipo_os_id=tipo_os_id,
            equipe_id=equipe_id,
            lider_id=lider_id,
            status_id=status_id,
            prioridade=prioridade,
            data_abertura=datetime.now(),
            data_prevista=data_prevista,
            descricao_problema=descricao_problema,
        )

        with self.__os_dao._connection() as conn:
            os_id = self.__os_dao.insert(os, conn=conn)
            if itens:
                for item in itens:
                    item_os = ItemOrdemServico(
                        os_id=os_id,
                        produto_variacao_id=item["produto_variacao_id"],
                        quantidade_prevista=item.get("quantidade_prevista"),
                        quantidade_usada=item.get("quantidade_usada"),
                    )
                    self.__item_dao.insert(item_os, conn=conn)

            andamento = AndamentoOrdemServico(
                os_id=os_id,
                data_hora=datetime.now(),
                status_anterior_id=None,
                status_novo_id=status_id,
                funcionario_id=lider_id,
                descricao="Abertura da OS",
            )

            self.__andamento_dao.insert(andamento, conn=conn)
            conn.commit()
            return os_id

    def atualizar_status(
        self,
        os_id: int,
        novo_status_id: int,
        funcionario_id: int,
        descricao: str,
        inicio_atendimento: Optional[datetime] = None,
        fim_atendimento: Optional[datetime] = None,
    ):
        os = self.__os_dao.find_by_id(os_id)
        if not os:
            raise ValueError("OS não encontrada.")
        if not self.__status_dao.find_by_id(novo_status_id):
            raise ValueError("Status inválido.")
        if not self.__funcionario_dao.find_by_id(funcionario_id):
            raise ValueError("Funcionário inválido.")

        with self.__os_dao._connection() as conn:
            self.__os_dao.update_status(os_id, novo_status_id, conn=conn)
            andamento = AndamentoOrdemServico(
                os_id=os_id,
                data_hora=datetime.now(),
                status_anterior_id=os.status_id,
                status_novo_id=novo_status_id,
                funcionario_id=funcionario_id,
                descricao=descricao,
                inicio_atendimento=inicio_atendimento,
                fim_atendimento=fim_atendimento,
            )
            self.__andamento_dao.insert(andamento, conn=conn)
            conn.commit()

    def timeline(self, os_id: int):
        return self.__andamento_dao.timeline(os_id)
