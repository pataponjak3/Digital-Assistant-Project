from dataclasses import dataclass
from typing import Literal, Optional

@dataclass
class LLMResponse:
    type: Literal["response", "function_call"]
    content: Optional[str] = None
    function: Optional[str] = None
    module: Optional[str] = None
    arguments: Optional[str] = None
