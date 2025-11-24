from typing import Optional
from dataclasses import dataclass

@dataclass
class AreaCampus:
    id: Optional[int] = None
    tipo_area_id: Optional[int] = None
    descricao: Optional[str] = None
    bloco: Optional[str] = None
