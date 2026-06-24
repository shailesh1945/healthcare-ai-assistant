from app.core.vector_store import get_vector_store
from app.core.llm import get_llm
from app.core.prompts import RAG_PROMPT
from app.core.config import settings
from app.core.logger import logger


def calculate_confidence(score: float) -> str:
    """
    Convert retrieval score into human-readable confidence.
    """

    if score >= 0.80:
        return "high"

    if score >= 0.60:
        return "medium"

    return "low"


def ask_rag(question: str) -> dict:
    """
    RAG-based QA pipeline.

    Flow:
    Question
      ↓
    Similarity Search
      ↓
    Context Building
      ↓
    Prompt Creation
      ↓
    Mistral Generation
      ↓
    Answer + Sources
    """

    logger.info(f"Question received: {question}")

    vectordb = get_vector_store()

    results = vectordb.similarity_search_with_relevance_scores(
        question,
        k=settings.TOP_K
    )

    logger.info(f"Retrieved {len(results)} chunks")

    # No retrieval results
    if not results:
        logger.warning("No matching documents found")

        return {
            "answer": "I could not find this information in the provided documents.",
            "sources": [],
            "confidence": "low"
        }

    # Hallucination guard
    best_score = results[0][1]

    if best_score < settings.RETRIEVAL_THRESHOLD:
        logger.warning(
            f"Low retrieval score detected: {best_score}"
        )

        return {
            "answer": "I could not find this information in the provided documents.",
            "sources": [],
            "confidence": "low"
        }

    context_parts = []
    sources = []

    for doc, score in results:

        context_parts.append(doc.page_content)

        sources.append(
            {
                "document": doc.metadata.get(
                    "source",
                    "unknown"
                ),
                "chunk": doc.page_content[:250]
            }
        )

    context = "\n\n".join(context_parts)

    prompt = RAG_PROMPT.format(
        context=context,
        question=question
    )

    llm = get_llm()

    answer = llm.invoke(prompt)

    logger.info("Answer generated successfully")

    return {
        "answer": answer.strip(),
        "sources": sources,
        "confidence": calculate_confidence(best_score)
    }