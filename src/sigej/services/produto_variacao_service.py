from typing import Optional, List
from src.sigej.daos.cor_dao import CorDAO
from src.sigej.daos.produto_dao import ProdutoDAO
from src.sigej.daos.produto_variacao_dao import ProdutoVariacaoDAO
from src.sigej.daos.tamanho_dao import TamanhoDAO
from src.sigej.models.produto_variacao import ProdutoVariacao

class ProdutoVariacaoService:
    def __init__(
        self,
        variacao_dao: ProdutoVariacaoDAO,
        produto_dao: ProdutoDAO,
        cor_dao: CorDAO,
        tamanho_dao: TamanhoDAO,
    ):
        self.__variacao_dao = variacao_dao
        self.__produto_dao = produto_dao
        self.__cor_dao = cor_dao
        self.__tamanho_dao = tamanho_dao

    def listar_por_produto(self, produto_id: int) -> List[ProdutoVariacao]:
        return self.__variacao_dao.list_by_produto(produto_id)

    def listar_todas(self) -> List[ProdutoVariacao]:
        return self.__variacao_dao.list_all()

    def criar(
        self,
        produto_id: int,
        cor_id: Optional[int],
        tamanho_id: Optional[int],
        codigo_barras: Optional[str],
        codigo_interno: Optional[str],
    ) -> int:
        if not self.__produto_dao.find_by_id(produto_id):
            raise ValueError("Produto não encontrado.")
        if cor_id and not self.__cor_dao.find_by_id(cor_id):
            raise ValueError("Cor não encontrada.")
        if tamanho_id and not self.__tamanho_dao.find_by_id(tamanho_id):
            raise ValueError("Tamanho não encontrado.")

        variacao = ProdutoVariacao(
            produto_id=produto_id,
            cor_id=cor_id,
            tamanho_id=tamanho_id,
            codigo_barras=codigo_barras,
            codigo_interno=codigo_interno,
        )
        return self.__variacao_dao.insert(variacao)
