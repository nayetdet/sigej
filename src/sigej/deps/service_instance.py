from typing import Optional
from src.sigej.deps import DAOInstance
from src.sigej.services.estoque_service import EstoqueService
from src.sigej.services.funcionario_service import FuncionarioService
from src.sigej.services.ordem_servico_service import OrdemServicoService
from src.sigej.services.pessoa_service import PessoaService
from src.sigej.services.relatorios_service import RelatoriosService

class ServiceInstance:
    __pessoa_service: Optional[PessoaService] = None
    __funcionario_service: Optional[FuncionarioService] = None
    __ordem_servico_service: Optional[OrdemServicoService] = None
    __estoque_service: Optional[EstoqueService] = None
    __relatorios_service: Optional[RelatoriosService] = None

    @classmethod
    def get_pessoa_service(cls) -> PessoaService:
        if cls.__pessoa_service is None:
            cls.__pessoa_service = PessoaService(pessoa_dao=DAOInstance.get_pessoa_dao())
        return cls.__pessoa_service

    @classmethod
    def get_funcionario_service(cls) -> FuncionarioService:
        if cls.__funcionario_service is None:
            cls.__funcionario_service = FuncionarioService(
                pessoa_dao=DAOInstance.get_pessoa_dao(),
                funcionario_dao=DAOInstance.get_funcionario_dao(),
                setor_dao=DAOInstance.get_setor_dao(),
                tipo_funcionario_dao=DAOInstance.get_tipo_funcionario_dao(),
            )
        return cls.__funcionario_service

    @classmethod
    def get_ordem_servico_service(cls) -> OrdemServicoService:
        if cls.__ordem_servico_service is None:
            cls.__ordem_servico_service = OrdemServicoService(
                os_dao=DAOInstance.get_ordem_servico_dao(),
                item_dao=DAOInstance.get_item_ordem_servico_dao(),
                andamento_dao=DAOInstance.get_andamento_ordem_servico_dao(),
                pessoa_dao=DAOInstance.get_pessoa_dao(),
                area_dao=DAOInstance.get_area_campus_dao(),
                tipo_os_dao=DAOInstance.get_tipo_ordem_servico_dao(),
                equipe_dao=DAOInstance.get_equipe_manutencao_dao(),
                funcionario_dao=DAOInstance.get_funcionario_dao(),
                status_dao=DAOInstance.get_status_ordem_servico_dao(),
            )
        return cls.__ordem_servico_service

    @classmethod
    def get_estoque_service(cls) -> EstoqueService:
        if cls.__estoque_service is None:
            cls.__estoque_service = EstoqueService(
                estoque_dao=DAOInstance.get_estoque_dao(),
                movimento_dao=DAOInstance.get_movimento_estoque_dao(),
                tipo_movimento_dao=DAOInstance.get_tipo_movimento_estoque_dao(),
                produto_variacao_dao=DAOInstance.get_produto_variacao_dao(),
                local_estoque_dao=DAOInstance.get_local_estoque_dao(),
            )
        return cls.__estoque_service

    @classmethod
    def get_relatorios_service(cls) -> RelatoriosService:
        if cls.__relatorios_service is None:
            cls.__relatorios_service = RelatoriosService(relatorios_dao=DAOInstance.get_relatorios_dao())
        return cls.__relatorios_service
