from dataclasses import dataclass

@dataclass
class AreaCampus:
    id: int | None = None
    tipo_area_id: int | None = None
    descricao: str | None = None
    bloco: str | None = None
