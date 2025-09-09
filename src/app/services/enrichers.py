from typing import Dict, Any

def enrich_asn_org(data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Normalize and extract ASN, org, country, hosting and tor flags from provider response.
    """
    # This example assumes ip2location data format; adjust per provider
    enriched = {
        "asn": int(data.get("as_number", 0)),
        "as_name": data.get("as_name", ""),
        "org": data.get("isp", ""),
        "country": data.get("country_name", ""),
        "hosting_flag": data.get("proxy", False),
        "tor_flag": data.get("tor", False),
    }
    return enriched
