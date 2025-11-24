from typing import Optional
from dataclasses import dataclass

@dataclass
class Produto:
    id: Optional[int] = None
    descricao: Optional[str] = None
    categoria_id: Optional[int] = None
    unidade_medida_id: Optional[int] = None
    marca_id: Optional[int] = None
