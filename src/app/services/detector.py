from typing import Dict, Any, Optional
from .providers import get_provider
from .enrichers import enrich_asn_org

class Detector:
    """
    Combines provider results with heuristics (added later)
    to classify IPs with confidence and reasons.
    """

    def __init__(self):
        self.provider = get_provider()

    async def classify(self, ip: str) -> Optional[Dict[str, Any]]:
        raw = await self.provider.classify_ip(ip)
        if not raw:
            return None
        enriched = enrich_asn_org(raw)

        # Placeholder for heuristics and scoring to come in next phase
        result = {
            "ip": ip,
            "is_privacy": enriched.get("hosting_flag", False),
            "type": "vpn" if enriched.get("hosting_flag") else "residential",
            "confidence": 0.9 if enriched.get("hosting_flag") else 0.1,
            "reasons": ["provider:ip2location"],
            "sources": [self.provider.__class__.__name__],
            **enriched,
        }
        return result
