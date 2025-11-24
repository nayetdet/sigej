from typing import Optional
from dataclasses import dataclass

@dataclass
class Pessoa:
    id: Optional[int] = None
    nome: Optional[str] = None
    cpf: Optional[str] = None
    matricula_siape: Optional[str] = None
    email: Optional[str] = None
    telefone: Optional[str] = None
    ativo: bool = True
