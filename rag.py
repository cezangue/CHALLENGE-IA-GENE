import os
from openai import OpenAI

# Initialisation du client OpenAI
client = OpenAI(api_key=os.environ['OPENAI_API_KEY'])

def generate_response(user_query, documents):
    context = " ".join([doc['content'] for doc in documents])
    combined_input = f"{context}\n\nQuestion: {user_query}"
    
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": combined_input}]
    )
    return response.choices[0].message.content
