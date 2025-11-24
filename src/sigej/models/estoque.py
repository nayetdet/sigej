from typing import Optional
from dataclasses import dataclass
from decimal import Decimal

@dataclass
class Estoque:
    produto_variacao_id: Optional[int] = None
    local_estoque_id: Optional[int] = None
    quantidade: Decimal = Decimal("0")
    ponto_reposicao: Decimal = Decimal("0")
