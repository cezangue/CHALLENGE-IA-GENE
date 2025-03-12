import time
import openai  # Assurez-vous que cette ligne est présente

def generate_response(user_query, processed_articles):
    while True:
        try:
            response = openai.ChatCompletion.create(  # Assurez-vous d'utiliser le bon appel ici
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": user_query}],
            )
            return response.choices[0].message['content']
        except openai.error.RateLimitError:
            print("Rate limit exceeded. Retrying in 10 seconds...")
            time.sleep(10)  # Attendre 10 secondes avant de réessayer
        except Exception as e:
            print(f"An error occurred: {e}")
            break  # Quittez la boucle si une autre erreur se produit
