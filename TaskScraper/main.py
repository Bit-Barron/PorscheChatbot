import requests
from bs4 import BeautifulSoup

def remove_umlaut(string):
    u = 'ü'.encode()
    U = 'Ü'.encode()
    a = 'ä'.encode()
    A = 'Ä'.encode()
    o = 'ö'.encode()
    O = 'Ö'.encode()
    ss = 'ß'.encode()

    string = string.encode()
    string = string.replace(u, b'ue')
    string = string.replace(U, b'Ue')
    string = string.replace(a, b'ae')
    string = string.replace(A, b'Ae')
    string = string.replace(o, b'oe')
    string = string.replace(O, b'Oe')
    string = string.replace(ss, b'ss')

    string = string.decode('utf-8')
    return string

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
            print(text)
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
