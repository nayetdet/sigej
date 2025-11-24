from typing import Optional
from dataclasses import dataclass

@dataclass
class Setor:
    id: Optional[int] = None
    nome: Optional[str] = None
    sigla: Optional[str] = None
