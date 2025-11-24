from typing import Optional
from dataclasses import dataclass

@dataclass
class Fornecedor:
    id: Optional[int] = None
    nome: Optional[str] = None
    cnpj: Optional[str] = None
