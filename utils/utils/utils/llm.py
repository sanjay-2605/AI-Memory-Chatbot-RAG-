from openai import OpenAI
client = OpenAI()

def generate_response(text):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": text}]
    )
    return response.choices[0].message.content
