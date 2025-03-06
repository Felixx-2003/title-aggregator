from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def scrape_the_verge():
    url = "https://www.theverge.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    articles = []
    for item in soup.find_all("h2", class_="font-bold text-lg"):  # Adjust selector if needed
        title = item.text.strip()
        link = item.find("a")["href"] if item.find("a") else "#"
        articles.append({"title": title, "link": link})
    
    return articles

@app.route("/")
def home():
    articles = scrape_the_verge()
    return render_template("index.html", articles=articles)

if __name__ == "__main__":
    app.run(debug=True)
