from typing import List

from src.sigej.daos.categoria_material_dao import CategoriaMaterialDAO
from src.sigej.models.categoria_material import CategoriaMaterial

class CategoriaService:
    def __init__(self, categoria_dao: CategoriaMaterialDAO):
        self.__categoria_dao = categoria_dao

    def listar(self) -> List[CategoriaMaterial]:
        return self.__categoria_dao.list_all()

    def criar(self, nome: str) -> int:
        categoria = CategoriaMaterial(nome=nome)
        return self.__categoria_dao.insert(categoria)
