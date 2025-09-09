import httpx
from typing import Optional, Dict, Any
from ..config import settings

class BaseProvider:
    """
    Base class for IP intelligence providers.
    """

    def __init__(self, timeout_ms: int = 2000):
        self.timeout = timeout_ms / 1000.0  # convert ms to seconds

    async def classify_ip(self, ip: str) -> Optional[Dict[str, Any]]:
        """
        Query provider API to classify IP.
        Should be implemented by subclasses.
        """
        raise NotImplementedError

class IP2LocationProvider(BaseProvider):
    BASE_URL = "https://api.ip2location.com/v2/"

    def __init__(self, api_key: str, timeout_ms: int = 2000):
        super().__init__(timeout_ms)
        self.api_key = api_key

    async def classify_ip(self, ip: str) -> Optional[Dict[str, Any]]:
        url = f"{self.BASE_URL}?ip={ip}&key={self.api_key}&package=WS24"
        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                resp = await client.get(url)
                resp.raise_for_status()
                data = resp.json()
                return data
        except Exception:
            # Log error or handle gracefully in production
            return None

def get_provider() -> BaseProvider:
    name = settings.provider_name.lower()
    if name == "ip2location" and settings.ip2location_api_key:
        return IP2LocationProvider(settings.ip2location_api_key, settings.provider_timeout_ms)
    # Add other providers (ipinfo, proxycheck) here as needed
    raise RuntimeError(f"Unsupported or unconfigured provider '{name}'")
