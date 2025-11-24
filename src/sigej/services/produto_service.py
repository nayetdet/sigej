from typing import Optional, List
from src.sigej.daos.categoria_material_dao import CategoriaMaterialDAO
from src.sigej.daos.marca_dao import MarcaDAO
from src.sigej.daos.produto_dao import ProdutoDAO
from src.sigej.daos.unidade_medida_dao import UnidadeMedidaDAO
from src.sigej.models.produto import Produto

class ProdutoService:
    def __init__(
        self,
        produto_dao: ProdutoDAO,
        categoria_dao: CategoriaMaterialDAO,
        unidade_dao: UnidadeMedidaDAO,
        marca_dao: MarcaDAO,
    ):
        self.__produto_dao = produto_dao
        self.__categoria_dao = categoria_dao
        self.__unidade_dao = unidade_dao
        self.__marca_dao = marca_dao

    def listar(self) -> List[Produto]:
        return self.__produto_dao.list_all()

    def criar(
        self,
        descricao: str,
        categoria_id: Optional[int],
        unidade_medida_id: Optional[int],
        marca_id: Optional[int],
    ) -> int:
        if categoria_id and not self.__categoria_dao.find_by_id(categoria_id):
            raise ValueError("Categoria não encontrada.")
        if unidade_medida_id and not self.__unidade_dao.find_by_id(unidade_medida_id):
            raise ValueError("Unidade de medida não encontrada.")
        if marca_id and not self.__marca_dao.find_by_id(marca_id):
            raise ValueError("Marca não encontrada.")

        produto = Produto(
            descricao=descricao,
            categoria_id=categoria_id,
            unidade_medida_id=unidade_medida_id,
            marca_id=marca_id,
        )
        return self.__produto_dao.insert(produto)
