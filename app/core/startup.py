import requests

from app.core.logger import logger


def verify_ollama():

    try:

        response = requests.get(
            "http://localhost:11434/api/tags",
            timeout=5
        )

        if response.status_code == 200:

            logger.info(
                "Ollama connection successful"
            )

        else:

            logger.warning(
                "Ollama unavailable"
            )

    except Exception as e:

        logger.error(
            f"Ollama check failed: {e}"
        )