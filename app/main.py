from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.ask import router as ask_router
from app.api.ingest import router as ingest_router
from app.api.health import router as health_router

from app.core.middleware import (
    LoggingMiddleware
)

from app.core.exceptions import (
    global_exception_handler
)

from app.core.startup import (
    verify_ollama
)


@asynccontextmanager
async def lifespan(app):

    verify_ollama()

    yield


app = FastAPI(
    title="Healthcare AI Assistant",
    version="1.0.0",
    lifespan=lifespan
)

app.add_exception_handler(
    Exception,
    global_exception_handler
)

app.add_middleware(
    LoggingMiddleware
)

app.include_router(ask_router)
app.include_router(ingest_router)
app.include_router(health_router)


@app.get("/")
def root():

    return {
        "message": "Healthcare AI Assistant Running"
    }