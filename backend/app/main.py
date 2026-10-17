from fastapi import FastAPI
from pydantic import BaseModel

from app.routers.pyszne import router as pyszne_router


class HealthResponse(BaseModel):
    status: str


class MessageResponse(BaseModel):
    message: str


app = FastAPI(title="Pizzka API", version="0.1.0")
app.include_router(pyszne_router)


@app.get("/", response_model=MessageResponse)
async def read_root() -> MessageResponse:
    return MessageResponse(message="Pizzka API is running")


@app.get("/health", response_model=HealthResponse)
async def read_health() -> HealthResponse:
    return HealthResponse(status="ok")
