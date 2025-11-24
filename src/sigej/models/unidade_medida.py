from typing import Optional
from dataclasses import dataclass

@dataclass
class UnidadeMedida:
    id: Optional[int] = None
    sigla: Optional[str] = None
    descricao: Optional[str] = None
