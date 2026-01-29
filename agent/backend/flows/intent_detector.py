from config import client, MODEL

INTENT_PROMPT = """
You are an intent classifier for Blismos Academy chatbot.

Return ONLY one word from this list:
- registration
- greeting
- academy_query
- other

Rules:
- If user wants to enroll, join, admission, sign up, apply → registration
- If user greets → greeting
- If user asks about courses, fees, syllabus → academy_query
- Else → other

Return only the intent word.
"""

def detect_intent(message: str) -> str:
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": INTENT_PROMPT},
            {"role": "user", "content": message}
        ],
        temperature=0
    )

    return response.choices[0].message.content.strip().lower()
