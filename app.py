from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin  # Fix relative URLs

app = Flask(__name__)

def get_articles():
    url = "https://www.theverge.com/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }  # Mimic a real browser to prevent blocking

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    articles = []

    # 🔥 Find all articles using the correct selector for <a> tags
    for item in soup.select("a._1lkmsmo1"):  
        title = item.text.strip()
        link = urljoin(url, item["href"])  # Convert relative URL to full URL

        if title and link.startswith("https://www.theverge.com/news/"):
            articles.append({"title": title, "url": link})

    if not articles:
        print("⚠️ No articles found! The Verge might have changed its structure.")

    return articles

@app.route("/")
def home():
    articles = get_articles()
    return render_template("index.html", articles=articles)

if __name__ == "__main__":
    app.run(debug=True)
