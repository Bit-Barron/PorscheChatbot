import requests
from bs4 import BeautifulSoup
from flask import Flask
from utils.helper import remove_umlaut

app = Flask(__name__)

user_input = input("What do you want to scrape?: 1: Connect, 2: E-Mobility, 3: My Porsche")

url_paths = {
    "1": "connect",
    "2": "e-mobility",
    "3": "my-porsche"
}

if user_input in url_paths:
    base_url = f"https://ask.porsche.com/de/de-DE/{url_paths[user_input]}/"
    print(f"The URL to scrape is: {base_url}")
else:
    print("Invalid input")

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

def scrapeData(url):
    questions_and_links = question_and_links(url)
    QUESTION_URL = "https://ask.porsche.com"
    
    with open("output.txt", "w", encoding="utf-8") as file:
        for question, link in questions_and_links:
            full_url = QUESTION_URL + link
            answer = get_full_answer(full_url)

            question = remove_umlaut(question)
            answer = remove_umlaut(answer)

            file.write(f"Frage: {question}\n")
            file.write(f"Antwort: {answer}\n")
            file.write("----------\n")

scrapeData(base_url)
