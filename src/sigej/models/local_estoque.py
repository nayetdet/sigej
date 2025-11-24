from typing import Optional
from dataclasses import dataclass

@dataclass
class LocalEstoque:
    id: Optional[int] = None
    descricao: Optional[str] = None
    responsavel_id: Optional[int] = None
