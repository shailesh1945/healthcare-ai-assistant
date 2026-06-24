from fastapi import APIRouter

from app.core.ingest import ingest_documents

router = APIRouter()


@router.post("/ingest")
def ingest():

    result = ingest_documents()

    return {
        "status": "success",
        "documents_processed": result["documents"],
        "chunks_created": result["chunks"]
    }