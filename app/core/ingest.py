from pathlib import Path

from langchain_core.documents import Document


from langchain_text_splitters import RecursiveCharacterTextSplitter


from app.core.vector_store import get_vector_store

from app.core.logger import logger


DATA_PATH = "data"


def ingest_documents():

    logger.info("Starting document ingestion")

    documents = []

    for file in Path(DATA_PATH).glob("*.txt"):

        content = file.read_text(encoding="utf-8")

        documents.append(
            Document(
                page_content=content,
                metadata={
                    "source": file.name
                }
            )
        )

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = splitter.split_documents(documents)

    vectordb = get_vector_store()

    vectordb.add_documents(chunks)

    logger.info(
        f"Ingested {len(documents)} docs and {len(chunks)} chunks"
    )

    return {
        "documents": len(documents),
        "chunks": len(chunks)
    }