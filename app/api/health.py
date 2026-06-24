from fastapi import APIRouter

from app.core.config import settings

router = APIRouter()


@router.get("/health")
def health():

    return {
        "status": "healthy",
        "model": settings.MODEL_NAME,
        "vector_store": settings.CHROMA_DB_PATH
    }