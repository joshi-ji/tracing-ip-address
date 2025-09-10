import pytest
from src.app.services.detector import Detector

@pytest.mark.asyncio
async def test_detector_stub(monkeypatch):
    async def fake_provider(ip):
        return {
            "as_number": "12345",
            "as_name": "FAKE-AS",
            "isp": "FakeOrg",
            "country_name": "ZZ",
            "proxy": True,
            "tor": False
        }

    detector = Detector()
    detector.provider.classify_ip = fake_provider

    result = await detector.classify("1.2.3.4")
    assert result is not None
    assert result["ip"] == "1.2.3.4"
    assert result["is_privacy"] is True
    assert result["type"] in ["vpn", "proxy", "hosting", "tor"]
    assert "confidence" in result
