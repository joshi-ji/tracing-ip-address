from typing import Dict, List

def calculate_confidence(base_confidence: float, heuristics: List[str]) -> float:
    """
    Adjust confidence based on heuristics triggered.
    """
    adjusted = base_confidence
    for h in heuristics:
        if h == "tor_exit_node":
            adjusted = min(1.0, adjusted + 0.2)
        elif h == "known_vpn_asn":
            adjusted = min(1.0, adjusted + 0.3)
        elif h == "known_hosting_asn":
            adjusted = min(1.0, adjusted + 0.2)
        elif h == "residential_asn":
            adjusted = max(0.0, adjusted - 0.3)
    return adjusted
