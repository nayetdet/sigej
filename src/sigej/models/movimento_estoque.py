from typing import Optional
from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal

@dataclass
class MovimentoEstoque:
    id: Optional[int] = None
    produto_variacao_id: Optional[int] = None
    local_estoque_id: Optional[int] = None
    tipo_movimento_id: Optional[int] = None
    quantidade: Decimal = Decimal("0")
    data_hora: Optional[datetime] = None
    funcionario_id: Optional[int] = None
    ordem_servico_id: Optional[int] = None
    observacao: Optional[str] = None
