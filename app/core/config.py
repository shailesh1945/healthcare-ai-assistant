from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    MODEL_NAME: str = "mistral"

    OLLAMA_BASE_URL: str = (
        "http://localhost:11434"
    )

    CHROMA_DB_PATH: str = "./vector_store"

    EMBEDDING_MODEL: str = (
        "BAAI/bge-small-en-v1.5"
    )

    TOP_K: int = 3

    RETRIEVAL_THRESHOLD: float = 0.50

    class Config:
        env_file = ".env"


settings = Settings()