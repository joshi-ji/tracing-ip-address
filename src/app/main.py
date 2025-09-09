from fastapi import FastAPI
from .routes import ip, meta
from .config import settings

def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.app_name,
        version="0.1.0",
        description="API to classify IPs as VPN/Proxy/Tor/Hosting with provider enrichment.",
        docs_url="/docs",
        openapi_url="/openapi.json",
    )

    # Include routers
    app.include_router(meta.router, prefix="", tags=["meta"])
    app.include_router(ip.router, prefix="/api/v1", tags=["ip"])

    return app

app = create_app()
