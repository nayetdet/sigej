from datetime import datetime
from decimal import Decimal
from typing import Optional, List, Tuple
from src.sigej.daos.estoque_dao import EstoqueDAO
from src.sigej.daos.local_estoque_dao import LocalEstoqueDAO
from src.sigej.daos.movimento_estoque_dao import MovimentoEstoqueDAO
from src.sigej.daos.produto_variacao_dao import ProdutoVariacaoDAO
from src.sigej.daos.tipo_movimento_estoque_dao import TipoMovimentoEstoqueDAO
from src.sigej.models.estoque import Estoque
from src.sigej.models.movimento_estoque import MovimentoEstoque

class EstoqueService:
    def __init__(
        self,
        estoque_dao: EstoqueDAO,
        movimento_dao: MovimentoEstoqueDAO,
        tipo_movimento_dao: TipoMovimentoEstoqueDAO,
        produto_variacao_dao: ProdutoVariacaoDAO,
        local_estoque_dao: LocalEstoqueDAO
    ):
        self.__estoque_dao = estoque_dao
        self.__movimento_dao = movimento_dao
        self.__tipo_movimento_dao = tipo_movimento_dao
        self.__produto_variacao_dao = produto_variacao_dao
        self.__local_estoque_dao = local_estoque_dao

    def registrar_movimento(
        self,
        produto_variacao_id: int,
        local_id: int,
        quantidade: Decimal,
        tipo_movimento_id: int,
        funcionario_id: Optional[int] = None,
        os_id: Optional[int] = None,
        observacao: Optional[str] = None
    ) -> int:
        if not self.__produto_variacao_dao.find_by_id(produto_variacao_id):
            raise ValueError("Produto variação não encontrado.")
        if not self.__local_estoque_dao.find_by_id(local_id):
            raise ValueError("Local de estoque não encontrado.")

        tipo = self.__tipo_movimento_dao.find_by_id(tipo_movimento_id)
        if not tipo:
            raise ValueError("Tipo de movimento não encontrado.")

        delta = quantidade if tipo.sinal == "+" else -quantidade
        with self.__estoque_dao._connection() as conn:
            estoque_atual = self.__estoque_dao.find(produto_variacao_id, local_id, conn=conn)
            if not estoque_atual:
                estoque_atual = Estoque(produto_variacao_id=produto_variacao_id, local_estoque_id=local_id)
                self.__estoque_dao.upsert(estoque_atual, conn=conn)

            if tipo.sinal == "-" and estoque_atual.quantidade < quantidade:
                raise ValueError("Estoque insuficiente para saída.")

            movimento = MovimentoEstoque(
                produto_variacao_id=produto_variacao_id,
                local_estoque_id=local_id,
                tipo_movimento_id=tipo_movimento_id,
                quantidade=quantidade,
                data_hora=datetime.now(),
                funcionario_id=funcionario_id,
                ordem_servico_id=os_id,
                observacao=observacao,
            )
            movimento_id = self.__movimento_dao.insert(movimento, conn=conn)
            self.__estoque_dao.ajustar_quantidade(produto_variacao_id, local_id, delta, conn=conn)
            conn.commit()
            return movimento_id

    def materiais_abaixo_ponto_reposicao(self) -> List[Tuple]:
        return self.__estoque_dao.abaixo_ponto_reposicao()

    def listar_movimentos(self) -> List[Tuple]:
        return self.__movimento_dao.list_all()
