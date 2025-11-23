from dataclasses import dataclass
from decimal import Decimal

@dataclass
class ItemOrdemServico:
    id: int | None = None
    os_id: int | None = None
    produto_variacao_id: int | None = None
    quantidade_prevista: Decimal | None = None
    quantidade_usada: Decimal | None = None
