import openai
import os

openai.api_key = os.getenv('OPENAI_API_KEY')

def create_voice(solution):
    response = openai.audio.speech.create(model="tts-1", voice="echo", input=solution)

    print("RESPONSE FOR CREATE VOICE:", response)

    with open("solution.mp3", "wb") as file:
        file.write(response.read())


def get_solutions(question):
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Du bist ein Porsche-Experte und beantwortest Fragen zu Porsche."},
            {"role": "user", "content": question},
        ],
    )
    content = response.choices[0].message.content
    
    create_voice(content)



