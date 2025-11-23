from dataclasses import dataclass
from decimal import Decimal

@dataclass
class Estoque:
    produto_variacao_id: int | None = None
    local_estoque_id: int | None = None
    quantidade: Decimal = Decimal("0")
    ponto_reposicao: Decimal = Decimal("0")
