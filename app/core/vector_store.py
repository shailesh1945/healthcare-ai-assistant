from langchain_chroma import Chroma

from app.core.embeddings import get_embedding_model
from app.core.config import settings


def get_vector_store():

    embeddings = get_embedding_model()

    return Chroma(
        persist_directory=settings.CHROMA_DB_PATH,
        embedding_function=embeddings
    )