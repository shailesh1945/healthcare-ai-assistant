import time

from starlette.middleware.base import (
    BaseHTTPMiddleware
)

from app.core.logger import logger


class LoggingMiddleware(
    BaseHTTPMiddleware
):

    async def dispatch(
        self,
        request,
        call_next
    ):

        start_time = time.time()

        response = await call_next(request)

        duration = (
            time.time() - start_time
        )

        logger.info(
            f"{request.method} "
            f"{request.url.path} "
            f"{duration:.2f}s"
        )

        return response