from langchain_community.llms import Ollama

from app.core.config import settings


def get_llm():

    return Ollama(
        model=settings.MODEL_NAME,
        base_url=settings.OLLAMA_BASE_URL,
        temperature=0
    )