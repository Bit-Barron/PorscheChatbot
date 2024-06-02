import requests
from bs4 import BeautifulSoup
from flask import Flask, Blueprint, request, jsonify

app = Flask(__name__)
taskscraper_bp = Blueprint('taskscraper', __name__)

BASE_URL = "https://ask.porsche.com/de/de-DE/"

@taskscraper_bp.route("/", methods=["GET"])
def index():
    return "Welcome to the Task Scraper API"

def question_and_links(url):
    resp = requests.get(url)
    resp.encoding = resp.apparent_encoding  
    soup = BeautifulSoup(resp.text, 'html.parser')

    questions = []
    for link in soup.find_all('a', href=True):
        text = link.text.strip()
        href = link['href']
        if text and "Mehr erfahren" in text:
            questions.append((text.replace("Mehr erfahren", "").strip(), href))
    
    return questions

def get_full_answer(url):
    resp = requests.get(url)
    resp.encoding = resp.apparent_encoding  
    soup = BeautifulSoup(resp.text, 'html.parser')
    article = soup.find('main', {'class': 'pcom-main'})
    if article:
        return article.get_text(separator=' ', strip=True)
    return "Keine Antwort gefunden"

@taskscraper_bp.route("/scrape_data", methods=["POST"])
def scrape_data():
    data = request.json
    section = data.get("section", "connect")
    url = f"{BASE_URL}{section}/"
    
    questions_and_links = question_and_links(url)
    QUESTION_URL = "https://ask.porsche.com"
    
    results = []
    for question, link in questions_and_links:
        full_url = QUESTION_URL + link
        answer = get_full_answer(full_url)
        results.append({
            "Frage": question,
            "Antwort": answer
        })
    
    return jsonify(results)

if __name__ == "__main__":
    app.register_blueprint(taskscraper_bp)
    app.run(debug=True)
