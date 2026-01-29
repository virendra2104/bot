from config import client, MODEL
from agent.knowledge import knowledge
from agent.scraper import scrape_website

ACADEMY_URL = "https://blismosacademy.com/"


async def knowledge_agent(message: str, context: str = None) -> str:
    prompt = f"""
ROLE:
You are Blismos Academy Assistant, a professional AI tutor.
CONTEXT (Short-term memory):
User previously said: {context if context else "None"}
STRICT RULES:
- If the query is short (like: advantage, future, scope, benefits),
  you MUST answer it based on the previous topic in the conversation,
- If the user greets (hi, hello, hey, hyy, hii):
  → Respond ONLY with a short greeting.
  → Do NOT mention courses or academy details.

- Answer ONLY questions related to Blismos Academy
  using the provided knowledge.

- If the answer is NOT clearly present in the knowledge:
  → Reply exactly: politely say you don’t have that information.

- Do NOT guess.
- Be concise.

KNOWLEDGE:
{knowledge}
"""

    # 🔹 SYNC CALL (safe)
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": message}
        ],
        temperature=0.2,
        max_tokens=300
    )

    answer = response.choices[0].message.content.strip()

    if not answer or answer in {"-", "*", "[1]"}:
        return "NOT_FOUND"

    return answer


async def web_agent(message: str) -> str:
    website_data = scrape_website(ACADEMY_URL)

    if not website_data or len(website_data.strip()) < 200:
        return "Please contact Blismos Academy support."

    prompt = f"""
ROLE:
You are Blismos Academy Assistant.

STRICT RULES:
- If the user greets:
  → Respond ONLY with a short greeting.

- Answer ONLY questions related to Blismos Academy
  using the provided website data.

- If the answer is NOT present:
  → Politely say you don’t have that information.

WEBSITE DATA:
{website_data}
"""

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": message}
        ],
        temperature=0.2,
        max_tokens=300
    )

    text = response.choices[0].message.content.strip()

    if not text or text in {"-", "*", "[1]"}:
        return "NOT_FOUND"

    return text
