from typing import Optional
from dataclasses import dataclass

@dataclass
class TipoMovimentoEstoque:
    id: Optional[int] = None
    descricao: Optional[str] = None
    sinal: Optional[str] = None
