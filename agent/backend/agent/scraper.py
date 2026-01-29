import requests
from bs4 import BeautifulSoup

def scrape_website(url: str) -> str:
    try:
        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        for tag in soup(["script", "style", "noscript"]):
            tag.decompose()

        text = soup.get_text(separator=" ")
        cleaned_text = " ".join(text.split())

        return cleaned_text[:4000]

    except Exception as e:
        return f"SCRAPING_ERROR: {e}"
