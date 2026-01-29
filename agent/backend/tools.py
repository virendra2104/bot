from backend.agent.knowledge import ACADEMY_FAQ

def academy_info(query: str) -> str:
    q = query.lower()
    for key, value in ACADEMY_FAQ.items():
        if key in q:
            return value
    return "I don’t have information about that."
