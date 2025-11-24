from typing import Optional
from dataclasses import dataclass

@dataclass
class TipoOrdemServico:
    id: Optional[int] = None
    descricao: Optional[str] = None
