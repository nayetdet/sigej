from typing import Optional

class ParseUtils:
    @classmethod
    def to_int(cls, value: str) -> Optional[int]:
        value = value.strip()
        return int(value) if value else None
