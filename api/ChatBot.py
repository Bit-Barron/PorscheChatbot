import openai
import os
from flask_cors import CORS
from flask import Flask, request, jsonify

openai.api_key = os.getenv('OPENAI_API_KEY')

app = Flask(__name__)
CORS(app, origins="*")  

@app.route("/ask/", methods=['POST'])
def get_solution():
    while True:
        data = request.json
        question = data.get('question')
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a Porsche expert and answer questions about Porsche."},
                {"role": "user", "content": question},
            ],
        )

        return jsonify({"solution": response.choices[0].message.content})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
