from agent.scraper import scrape_website

url = "https://blismosacademy.com/"
data = scrape_website(url)

print("Length:", len(data) if data else 0)
print(data[:1500])
