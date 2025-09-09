from fastapi import APIRouter
from fastapi.responses import JSONResponse
from datetime import datetime

router = APIRouter()

@router.get("/health", summary="Health Check")
async def health():
    return JSONResponse({"status": "ok", "timestamp": datetime.utcnow().isoformat()})

@router.get("/version", summary="API Version")
async def version():
    return {"version": "0.1.0"}
