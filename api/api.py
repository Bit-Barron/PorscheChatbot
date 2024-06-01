# api.py
from flask import Flask
from chatbot.texttospeech import textToSpeech_bp
from chatbot.chatbot_service import chatbot_bp
from scraper.taskscraper import taskscraper_bp

app = Flask(__name__)
app.register_blueprint(textToSpeech_bp)
app.register_blueprint(chatbot_bp)
app.register_blueprint(taskscraper_bp)

if __name__ == "__main__":
    app.run(debug=True)
