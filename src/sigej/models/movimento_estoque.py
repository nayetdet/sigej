from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal

@dataclass
class MovimentoEstoque:
    id: int | None = None
    produto_variacao_id: int | None = None
    local_estoque_id: int | None = None
    tipo_movimento_id: int | None = None
    quantidade: Decimal = Decimal("0")
    data_hora: datetime | None = None
    funcionario_id: int | None = None
    ordem_servico_id: int | None = None
    observacao: str | None = None
