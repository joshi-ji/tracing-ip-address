from fastapi import APIRouter, HTTPException
from pydantic import IPvAnyAddress
from ..schemas.classify import ClassifyRequest, ClassifyResponse
from ..schemas.details import DetailsResponse

router = APIRouter()

@router.post("/classify", response_model=ClassifyResponse)
async def classify_ip(request: ClassifyRequest):
    """
    Stub handler for classifying an IP address.
    Returns a fixed dummy response for now.
    """
    ip = request.ip
    # TODO: Implement real detection logic here.
    return ClassifyResponse(
        ip=str(ip),
        is_privacy=True,
        type="vpn",
        confidence=0.85,
        reasons=["provider:vpn-label", "asn:known-vpn-asn"],
        sources=["provider:ip2location", "heuristic:hosting_asn"]
    )

@router.get("/details/{ip}", response_model=DetailsResponse)
async def get_ip_details(ip: IPvAnyAddress):
    """
    Stub handler for retrieving IP address details.
    Returns fixed dummy data for now.
    """
    # TODO: Implement enrichment lookup here.
    return DetailsResponse(
        ip=str(ip),
        asn=12345,
        as_name="EXAMPLE-DC",
        org="Example Hosting LLC",
        country="US",
        hosting_flag=True,
        tor_flag=False,
        provider_hits=[{"name": "ip2location", "labels": ["vpn", "dc"]}]
    )
