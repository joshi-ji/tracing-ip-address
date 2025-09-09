from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Tracing IP Behind VPN"
    provider_name: str = "ip2location"
    ip2location_api_key: str = ""
    ipinfo_token: str = ""
    proxycheck_api_key: str = ""
    provider_timeout_ms: int = 2000
    cache_ttl_seconds: int = 900
    app_env: str = "development"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
