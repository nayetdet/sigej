from typing import Optional
from dataclasses import dataclass

@dataclass
class ProdutoVariacao:
    id: Optional[int] = None
    produto_id: Optional[int] = None
    cor_id: Optional[int] = None
    tamanho_id: Optional[int] = None
    codigo_barras: Optional[str] = None
    codigo_interno: Optional[str] = None
