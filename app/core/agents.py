from app.core.rag import ask_rag
from app.core.tools import check_available_slots


APPOINTMENT_KEYWORDS = [
    "appointment",
    "book",
    "schedule",
    "slot",
    "availability"
]


def is_appointment_query(question: str) -> bool:

    question = question.lower()

    return any(
        keyword in question
        for keyword in APPOINTMENT_KEYWORDS
    )


def detect_department(question: str) -> str:

    question = question.lower()

    if "cardiology" in question:
        return "cardiology"

    if "neurology" in question:
        return "neurology"

    return "general"


def handle_question(question: str):

    if is_appointment_query(question):

        department = detect_department(question)

        tool_result = check_available_slots(
            department=department
        )

        return {
            "answer": (
                f"Available {department.title()} "
                f"appointment slots are: "
                f"{', '.join(tool_result['available_slots'])}"
            ),
            "sources": [],
            "confidence": "high",
            "route": "appointment_tool"
        }

    rag_result = ask_rag(question)

    rag_result["route"] = "rag"

    return rag_result