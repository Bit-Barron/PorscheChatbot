from flask import Flask
from ChatBot.textToSpeech import textToSpeech_bp
from api.ChatBot.chatBot import chatbot_bp

app = Flask(__name__)
app.register_blueprint(textToSpeech_bp)
app.register_blueprint(chatbot_bp)

if __name__ == "__main__":
    app.run(debug=True)
