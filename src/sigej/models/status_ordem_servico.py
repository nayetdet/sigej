from typing import Optional
from dataclasses import dataclass

@dataclass
class StatusOrdemServico:
    id: Optional[int] = None
    descricao: Optional[str] = None
