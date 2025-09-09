import csv
from pathlib import Path
from typing import Dict, Any, Optional, List

from .providers import get_provider
from .enrichers import enrich_asn_org
from .scoring import calculate_confidence

TOR_EXIT_NODES_FILE = Path(__file__).parent / "data" / "tor_exit_nodes.txt"
KNOWN_VPN_ASN_FILE = Path(__file__).parent / "data" / "known_vpn_asn.csv"
KNOWN_HOSTING_ASN_FILE = Path(__file__).parent / "data" / "hosting_asn.csv"

class Detector:
    def __init__(self):
        self.provider = get_provider()
        self.tor_exit_nodes = self._load_tor_exit_nodes()
        self.known_vpn_asns = self._load_asn_list(KNOWN_VPN_ASN_FILE)
        self.known_hosting_asns = self._load_asn_list(KNOWN_HOSTING_ASN_FILE)

    def _load_tor_exit_nodes(self) -> set:
        if not TOR_EXIT_NODES_FILE.exists():
            return set()
        with open(TOR_EXIT_NODES_FILE, encoding="utf-8") as f:
            return set(line.strip() for line in f if line.strip())

    def _load_asn_list(self, filepath: Path) -> set:
        if not filepath.exists():
            return set()
        asns = set()
        with open(filepath, newline="", encoding="utf-8") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if row:
                    asns.add(int(row[0]))
        return asns

    async def classify(self, ip: str) -> Optional[Dict[str, Any]]:
        raw = await self.provider.classify_ip(ip)
        if not raw:
            return None
        enriched = enrich_asn_org(raw)

        reasons: List[str] = []
        heuristics: List[str] = []

        # Heuristic checks
        if ip in self.tor_exit_nodes:
            heuristics.append("tor_exit_node")
            reasons.append("IP is a Tor exit node")
        asn = enriched.get("asn", 0)
        if asn in self.known_vpn_asns:
            heuristics.append("known_vpn_asn")
            reasons.append("ASN is known VPN ASN")
        if asn in self.known_hosting_asns:
            heuristics.append("known_hosting_asn")
            reasons.append("ASN is known hosting ASN")

        base_confidence = 0.5  # Starting base confidence
        confidence = calculate_confidence(base_confidence, heuristics)

        # Final determination type logic (simplified)
        if "tor_exit_node" in heuristics:
            ip_type = "tor"
        elif "known_vpn_asn" in heuristics or "known_hosting_asn" in heuristics:
            ip_type = "vpn"
        else:
            ip_type = "residential"

        result = {
            "ip": ip,
            "is_privacy": ip_type != "residential",
            "type": ip_type,
            "confidence": confidence,
            "reasons": reasons,
            "sources": [self.provider.__class__.__name__],
            **enriched,
        }
        return result
