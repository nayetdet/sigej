from dataclasses import dataclass

@dataclass
class ProdutoVariacao:
    id: int | None = None
    produto_id: int | None = None
    cor_id: int | None = None
    tamanho_id: int | None = None
    codigo_barras: str | None = None
    codigo_interno: str | None = None
