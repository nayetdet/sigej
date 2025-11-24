from typing import Optional

from src.sigej.daos.andamento_ordem_servico_dao import AndamentoOrdemServicoDAO
from src.sigej.daos.area_campus_dao import AreaCampusDAO
from src.sigej.daos.categoria_material_dao import CategoriaMaterialDAO
from src.sigej.daos.cor_dao import CorDAO
from src.sigej.daos.equipe_manutencao_dao import EquipeManutencaoDAO
from src.sigej.daos.equipe_membro_dao import EquipeMembroDAO
from src.sigej.daos.estoque_dao import EstoqueDAO
from src.sigej.daos.fornecedor_dao import FornecedorDAO
from src.sigej.daos.funcionario_dao import FuncionarioDAO
from src.sigej.daos.item_ordem_servico_dao import ItemOrdemServicoDAO
from src.sigej.daos.local_estoque_dao import LocalEstoqueDAO
from src.sigej.daos.marca_dao import MarcaDAO
from src.sigej.daos.movimento_estoque_dao import MovimentoEstoqueDAO
from src.sigej.daos.ordem_servico_dao import OrdemServicoDAO
from src.sigej.daos.pessoa_dao import PessoaDAO
from src.sigej.daos.produto_dao import ProdutoDAO
from src.sigej.daos.produto_variacao_dao import ProdutoVariacaoDAO
from src.sigej.daos.relatorios_dao import RelatoriosDAO
from src.sigej.daos.setor_dao import SetorDAO
from src.sigej.daos.status_ordem_servico_dao import StatusOrdemServicoDAO
from src.sigej.daos.tamanho_dao import TamanhoDAO
from src.sigej.daos.tipo_area_campus_dao import TipoAreaCampusDAO
from src.sigej.daos.tipo_funcionario_dao import TipoFuncionarioDAO
from src.sigej.daos.tipo_movimento_estoque_dao import TipoMovimentoEstoqueDAO
from src.sigej.daos.tipo_ordem_servico_dao import TipoOrdemServicoDAO
from src.sigej.daos.unidade_medida_dao import UnidadeMedidaDAO

class DAOInstance:
    __pessoa_dao: Optional[PessoaDAO] = None
    __funcionario_dao: Optional[FuncionarioDAO] = None
    __tipo_funcionario_dao: Optional[TipoFuncionarioDAO] = None
    __setor_dao: Optional[SetorDAO] = None
    __tipo_area_campus_dao: Optional[TipoAreaCampusDAO] = None
    __area_campus_dao: Optional[AreaCampusDAO] = None
    __equipe_manutencao_dao: Optional[EquipeManutencaoDAO] = None
    __equipe_membro_dao: Optional[EquipeMembroDAO] = None
    __categoria_material_dao: Optional[CategoriaMaterialDAO] = None
    __unidade_medida_dao: Optional[UnidadeMedidaDAO] = None
    __fornecedor_dao: Optional[FornecedorDAO] = None
    __marca_dao: Optional[MarcaDAO] = None
    __cor_dao: Optional[CorDAO] = None
    __tamanho_dao: Optional[TamanhoDAO] = None
    __produto_dao: Optional[ProdutoDAO] = None
    __produto_variacao_dao: Optional[ProdutoVariacaoDAO] = None
    __local_estoque_dao: Optional[LocalEstoqueDAO] = None
    __estoque_dao: Optional[EstoqueDAO] = None
    __tipo_movimento_estoque_dao: Optional[TipoMovimentoEstoqueDAO] = None
    __movimento_estoque_dao: Optional[MovimentoEstoqueDAO] = None
    __tipo_ordem_servico_dao: Optional[TipoOrdemServicoDAO] = None
    __status_ordem_servico_dao: Optional[StatusOrdemServicoDAO] = None
    __ordem_servico_dao: Optional[OrdemServicoDAO] = None
    __item_ordem_servico_dao: Optional[ItemOrdemServicoDAO] = None
    __andamento_ordem_servico_dao: Optional[AndamentoOrdemServicoDAO] = None
    __relatorios_dao: Optional[RelatoriosDAO] = None

    @classmethod
    def get_pessoa_dao(cls) -> PessoaDAO:
        if cls.__pessoa_dao is None:
            cls.__pessoa_dao = PessoaDAO()
        return cls.__pessoa_dao

    @classmethod
    def get_funcionario_dao(cls) -> FuncionarioDAO:
        if cls.__funcionario_dao is None:
            cls.__funcionario_dao = FuncionarioDAO()
        return cls.__funcionario_dao

    @classmethod
    def get_tipo_funcionario_dao(cls) -> TipoFuncionarioDAO:
        if cls.__tipo_funcionario_dao is None:
            cls.__tipo_funcionario_dao = TipoFuncionarioDAO()
        return cls.__tipo_funcionario_dao

    @classmethod
    def get_setor_dao(cls) -> SetorDAO:
        if cls.__setor_dao is None:
            cls.__setor_dao = SetorDAO()
        return cls.__setor_dao

    @classmethod
    def get_tipo_area_campus_dao(cls) -> TipoAreaCampusDAO:
        if cls.__tipo_area_campus_dao is None:
            cls.__tipo_area_campus_dao = TipoAreaCampusDAO()
        return cls.__tipo_area_campus_dao

    @classmethod
    def get_area_campus_dao(cls) -> AreaCampusDAO:
        if cls.__area_campus_dao is None:
            cls.__area_campus_dao = AreaCampusDAO()
        return cls.__area_campus_dao

    @classmethod
    def get_equipe_manutencao_dao(cls) -> EquipeManutencaoDAO:
        if cls.__equipe_manutencao_dao is None:
            cls.__equipe_manutencao_dao = EquipeManutencaoDAO()
        return cls.__equipe_manutencao_dao

    @classmethod
    def get_equipe_membro_dao(cls) -> EquipeMembroDAO:
        if cls.__equipe_membro_dao is None:
            cls.__equipe_membro_dao = EquipeMembroDAO()
        return cls.__equipe_membro_dao

    @classmethod
    def get_categoria_material_dao(cls) -> CategoriaMaterialDAO:
        if cls.__categoria_material_dao is None:
            cls.__categoria_material_dao = CategoriaMaterialDAO()
        return cls.__categoria_material_dao

    @classmethod
    def get_unidade_medida_dao(cls) -> UnidadeMedidaDAO:
        if cls.__unidade_medida_dao is None:
            cls.__unidade_medida_dao = UnidadeMedidaDAO()
        return cls.__unidade_medida_dao

    @classmethod
    def get_fornecedor_dao(cls) -> FornecedorDAO:
        if cls.__fornecedor_dao is None:
            cls.__fornecedor_dao = FornecedorDAO()
        return cls.__fornecedor_dao

    @classmethod
    def get_marca_dao(cls) -> MarcaDAO:
        if cls.__marca_dao is None:
            cls.__marca_dao = MarcaDAO()
        return cls.__marca_dao

    @classmethod
    def get_cor_dao(cls) -> CorDAO:
        if cls.__cor_dao is None:
            cls.__cor_dao = CorDAO()
        return cls.__cor_dao

    @classmethod
    def get_tamanho_dao(cls) -> TamanhoDAO:
        if cls.__tamanho_dao is None:
            cls.__tamanho_dao = TamanhoDAO()
        return cls.__tamanho_dao

    @classmethod
    def get_produto_dao(cls) -> ProdutoDAO:
        if cls.__produto_dao is None:
            cls.__produto_dao = ProdutoDAO()
        return cls.__produto_dao

    @classmethod
    def get_produto_variacao_dao(cls) -> ProdutoVariacaoDAO:
        if cls.__produto_variacao_dao is None:
            cls.__produto_variacao_dao = ProdutoVariacaoDAO()
        return cls.__produto_variacao_dao

    @classmethod
    def get_local_estoque_dao(cls) -> LocalEstoqueDAO:
        if cls.__local_estoque_dao is None:
            cls.__local_estoque_dao = LocalEstoqueDAO()
        return cls.__local_estoque_dao

    @classmethod
    def get_estoque_dao(cls) -> EstoqueDAO:
        if cls.__estoque_dao is None:
            cls.__estoque_dao = EstoqueDAO()
        return cls.__estoque_dao

    @classmethod
    def get_tipo_movimento_estoque_dao(cls) -> TipoMovimentoEstoqueDAO:
        if cls.__tipo_movimento_estoque_dao is None:
            cls.__tipo_movimento_estoque_dao = TipoMovimentoEstoqueDAO()
        return cls.__tipo_movimento_estoque_dao

    @classmethod
    def get_movimento_estoque_dao(cls) -> MovimentoEstoqueDAO:
        if cls.__movimento_estoque_dao is None:
            cls.__movimento_estoque_dao = MovimentoEstoqueDAO()
        return cls.__movimento_estoque_dao

    @classmethod
    def get_tipo_ordem_servico_dao(cls) -> TipoOrdemServicoDAO:
        if cls.__tipo_ordem_servico_dao is None:
            cls.__tipo_ordem_servico_dao = TipoOrdemServicoDAO()
        return cls.__tipo_ordem_servico_dao

    @classmethod
    def get_status_ordem_servico_dao(cls) -> StatusOrdemServicoDAO:
        if cls.__status_ordem_servico_dao is None:
            cls.__status_ordem_servico_dao = StatusOrdemServicoDAO()
        return cls.__status_ordem_servico_dao

    @classmethod
    def get_ordem_servico_dao(cls) -> OrdemServicoDAO:
        if cls.__ordem_servico_dao is None:
            cls.__ordem_servico_dao = OrdemServicoDAO()
        return cls.__ordem_servico_dao

    @classmethod
    def get_item_ordem_servico_dao(cls) -> ItemOrdemServicoDAO:
        if cls.__item_ordem_servico_dao is None:
            cls.__item_ordem_servico_dao = ItemOrdemServicoDAO()
        return cls.__item_ordem_servico_dao

    @classmethod
    def get_andamento_ordem_servico_dao(cls) -> AndamentoOrdemServicoDAO:
        if cls.__andamento_ordem_servico_dao is None:
            cls.__andamento_ordem_servico_dao = AndamentoOrdemServicoDAO()
        return cls.__andamento_ordem_servico_dao

    @classmethod
    def get_relatorios_dao(cls) -> RelatoriosDAO:
        if cls.__relatorios_dao is None:
            cls.__relatorios_dao = RelatoriosDAO()
        return cls.__relatorios_dao
