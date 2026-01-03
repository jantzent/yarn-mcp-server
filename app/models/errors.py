from dataclasses import dataclass
from typing import Any, Dict, Optional


@dataclass
class MCPError(Exception):
    message: str
    status_code: Optional[int] = None
    context: Optional[Dict[str, Any]] = None

    def __str__(self) -> str:
        return self.message
