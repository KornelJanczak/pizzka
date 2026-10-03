from fastapi import FastAPI
from pydantic import BaseModel


class HealthResponse(BaseModel):
    status: str


class MessageResponse(BaseModel):
    message: str


app = FastAPI(title="Pizzka API", version="0.1.0")


@app.get("/", response_model=MessageResponse)
async def read_root() -> MessageResponse:
    return MessageResponse(message="Pizzka API is running")


@app.get("/health", response_model=HealthResponse)
async def read_health() -> HealthResponse:
    return HealthResponse(status="ok")
