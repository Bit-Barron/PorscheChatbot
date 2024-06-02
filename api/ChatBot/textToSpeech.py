import openai
import os
from flask_cors import CORS
from flask import Flask, Blueprint, request, jsonify

openai.api_key = os.getenv('OPENAI_API_KEY')

app = Flask(__name__)

textToSpeech_bp = Blueprint('textToSpeech', __name__)


def create_voice(solution):
    print("Creating Voice", solution)
    response = openai.audio.speech.create(model="tts-1", voice="echo", input=solution)

    with open("output.mp3", "wb") as file:
        file.write(response.read())

@textToSpeech_bp.route("/solutions", methods=["POST"])
def get_solutions():
        data = request.json
        question = data.get('question')
        print(question)
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Du bist ein Porsche-Experte und beantwortest Fragen zu Porsche."},
                {"role": "user", "content": question},
            ],
        )
        content = response.choices[0].message.content

        create_voice(content)

        return jsonify(content), 200


