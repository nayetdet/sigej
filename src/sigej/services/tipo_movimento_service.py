from typing import List

from src.sigej.daos.tipo_movimento_estoque_dao import TipoMovimentoEstoqueDAO
from src.sigej.models.tipo_movimento_estoque import TipoMovimentoEstoque

class TipoMovimentoService:
    def __init__(self, tipo_movimento_dao: TipoMovimentoEstoqueDAO):
        self.__tipo_movimento_dao = tipo_movimento_dao

    def listar(self) -> List[TipoMovimentoEstoque]:
        return self.__tipo_movimento_dao.list_all()

    def criar(self, descricao: str, sinal: str) -> int:
        sinal = (sinal or "").strip()
        if sinal not in {"+", "-"}:
            raise ValueError("Sinal deve ser '+' ou '-'.")
        tipo = TipoMovimentoEstoque(descricao=descricao, sinal=sinal)
        return self.__tipo_movimento_dao.insert(tipo)
