from pydantic import BaseModel
from fastapi import APIRouter

from app.core.agents import handle_question

router = APIRouter()


class QuestionRequest(BaseModel):
    question: str


@router.post("/ask")
def ask(request: QuestionRequest):

    return handle_question(
        request.question
    )