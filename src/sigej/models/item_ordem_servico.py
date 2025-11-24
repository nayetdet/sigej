from typing import Optional
from dataclasses import dataclass
from decimal import Decimal

@dataclass
class ItemOrdemServico:
    id: Optional[int] = None
    os_id: Optional[int] = None
    produto_variacao_id: Optional[int] = None
    quantidade_prevista: Optional[Decimal] = None
    quantidade_usada: Optional[Decimal] = None
