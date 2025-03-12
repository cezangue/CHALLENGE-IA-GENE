import os
from openai import OpenAI

# Initialisation du client OpenAI
client = OpenAI(api_key=os.environ['OPENAI_API_KEY'])

def generate_response(user_query, processed_articles):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # Vérifiez que le modèle est correct
        messages=[{"role": "user", "content": user_query}],
        # Ajoutez d'autres paramètres si nécessaire
    )
    return response.choices[0].message['content']
