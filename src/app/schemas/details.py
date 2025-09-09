from pydantic import BaseModel, IPvAnyAddress
from typing import List, Dict

class ProviderHit(BaseModel):
    name: str
    labels: List[str]

class DetailsResponse(BaseModel):
    ip: str
    asn: int
    as_name: str
    org: str
    country: str
    hosting_flag: bool
    tor_flag: bool
    provider_hits: List[ProviderHit]
