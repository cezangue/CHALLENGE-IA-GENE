import os
import time
from openai import OpenAI

# Initialisation du client OpenAI
client = OpenAI(api_key=os.environ['OPENAI_API_KEY'])

def generate_response(user_query, processed_articles):
    while True:
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": user_query}],
            )
            return response.choices[0].message['content']
        except openai.error.RateLimitError:
            print("Rate limit exceeded. Retrying in 10 seconds...")
            time.sleep(10)  # Attendre 10 secondes avant de réessayer
