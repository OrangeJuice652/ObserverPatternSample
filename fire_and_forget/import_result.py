import dataclass
from typing import List, Optional


class SkuInput:
    name: Optional[str]
    sku_code: Optional[str]
    jan_code: Optional[str]
    price: Optional[int]


@dataclass
class ImportResult:
    SKU_UPSERT: int = 0
    VALIDATE_ERROR: int = 1

    event_code: int
    error_messages: List[str]
    sku: SkuInput

