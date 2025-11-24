from typing import Optional
from dataclasses import dataclass

@dataclass
class Marca:
    id: Optional[int] = None
    nome: Optional[str] = None
