import pytest
from src.app.services.detector import Detector

@pytest.mark.asyncio
async def test_detector_vpn_asn(monkeypatch):
    # Simulate a known VPN ASN hit
    async def fake_provider(ip):
        return {
            "as_number": "10000",
            "as_name": "VPN-ASN",
            "isp": "VPN Provider",
            "country_name": "AB",
            "proxy": True,
            "tor": False
        }
    detector = Detector()
    detector.provider.classify_ip = fake_provider
    # Pretend 10000 is known VPN ASN for this test
    detector.known_vpn_asns = {10000}
    result = await detector.classify("5.6.7.8")
    assert result["type"] == "vpn"
    assert result["confidence"] >= 0.8

@pytest.mark.asyncio
async def test_detector_tor_exit(monkeypatch):
    # Simulate a Tor exit node IP
    async def fake_provider(ip):
        return {
            "as_number": "99999",
            "as_name": "TOR-ASN",
            "isp": "Tor ISP",
            "country_name": "CD",
            "proxy": True,
            "tor": True
        }
    detector = Detector()
    detector.provider.classify_ip = fake_provider
    detector.tor_exit_nodes = {"9.9.9.9"}
    result = await detector.classify("9.9.9.9")
    assert result["type"] == "tor"
    assert result["confidence"] >= 0.7
