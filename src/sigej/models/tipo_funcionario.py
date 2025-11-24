from typing import Optional
from dataclasses import dataclass

@dataclass
class TipoFuncionario:
    id: Optional[int] = None
    descricao: Optional[str] = None
