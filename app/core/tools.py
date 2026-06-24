def check_available_slots(
    department: str,
    date: str = "next_available"
):
    """
    Mock appointment scheduling tool.
    """

    mock_slots = {
        "cardiology": [
            "10:00 AM",
            "02:00 PM",
            "04:30 PM"
        ],
        "neurology": [
            "09:00 AM",
            "01:00 PM"
        ],
        "general": [
            "11:00 AM",
            "03:00 PM"
        ]
    }

    department = department.lower()

    return {
        "department": department,
        "date": date,
        "available_slots": mock_slots.get(
            department,
            ["09:00 AM", "01:00 PM"]
        )
    }