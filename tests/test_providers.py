import pytest
from src.app.services.providers import BaseProvider

class DummyProvider(BaseProvider):
    async def classify_ip(self, ip: str):
        return {"as_number": "99999", "isp": "TestISP", "country_name": "ZZ"}

@pytest.mark.asyncio
async def test_dummy_provider():
    provider = DummyProvider()
    result = await provider.classify_ip("8.8.8.8")
    assert result["as_number"] == "99999"
    assert result["isp"] == "TestISP"
