import streamlit as st
from scraper import scrape_articles, process_articles
from rag import generate_response

# Titre de l'application
st.title("Agent Conversationnel Spécialisé")

# Récupération des articles
st.header("Récupération des Articles")
articles = scrape_articles()
processed_articles = process_articles(articles)

# Interface utilisateur pour les questions
st.header("Posez votre question")
user_query = st.text_input("Votre question:")

if st.button("Envoyer"):
    if user_query:
        response = generate_response(user_query, processed_articles)
        st.subheader("Réponse de l'agent :")
        st.write(response)
    else:
        st.warning("Veuillez entrer une question.")
