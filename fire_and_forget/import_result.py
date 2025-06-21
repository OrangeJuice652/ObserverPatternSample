from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class SkuInput:
    name: Optional[str]
    sku_code: Optional[str]
    jan_code: Optional[str]
    price: Optional[int]


@dataclass
class ImportResult:
    SKU_UPSERT: int = 0
    VALIDATE_ERROR: int = 1

    event_code: int = -1
    error_messages: List[str] = field(default_factory=list)
    sku: Optional[SkuInput] = None

