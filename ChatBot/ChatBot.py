import openai
import os
from fastapi import FastAPI

openai.api_key = os.getenv('OPENAI_API_KEY')

app = FastAPI()


@app.post("/ask/")
def get_solution():
    while True:
        question = input(">>Enter your question: ")
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a Porsche expert and answer questions about Porsche."},
                {"role": "user", "content": question},
            ],
        )

        print(response.choices[0].message.content)

get_solution()
