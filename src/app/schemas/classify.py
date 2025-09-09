from pydantic import BaseModel, IPvAnyAddress
from typing import List

class ClassifyRequest(BaseModel):
    ip: IPvAnyAddress

class ClassifyResponse(BaseModel):
    ip: str
    is_privacy: bool
    type: str  # e.g., "vpn", "proxy", "tor", "hosting", "residential"
    confidence: float  # from 0.0 to 1.0
    reasons: List[str]
    sources: List[str]
