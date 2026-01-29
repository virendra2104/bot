def sanitize_input(text: str) -> str:
    blocked = ["ignore instructions", "system prompt", "jailbreak"]
    for word in blocked:
        if word.lower() in text.lower():
            return "Invalid input"
    return text
