import openai
import streamlit as st

model_engine = "davinci"

# Liste de questions et réponses prédéfinies pour le chatbot
qa_pairs = {
    "Quel est votre nom ?": "Je suis un chatbot créé avec OpenAI.",
    "Comment allez-vous ?": "Je suis un programme informatique, donc je ne ressens rien. Mais je suis là pour vous aider !",
    "Pouvez-vous m'aider ?": "Bien sûr ! De quoi avez-vous besoin ?"
}

def generate_response(user_input, api_key):
    """Générer une réponse à partir de l'entrée de l'utilisateur en utilisant l'API OpenAI."""
    openai.api_key = api_key
    prompt = f"Q: {user_input}\nA:"
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response.choices[0].text.strip()

def chatbot():
    """Fonction principale pour l'interface utilisateur du chatbot."""
    st.title("Chatbot OpenAI")

    # Demander à l'utilisateur d'entrer sa clé API OpenAI
    api_key = st.text_input("Entrez votre clé API OpenAI :")

    # Afficher un message d'erreur si la clé API n'est pas valide
    if not api_key:
        st.warning("Veuillez entrer une clé API OpenAI valide.")
        return

    # Demander à l'utilisateur d'entrer une question
    user_input = st.text_input("Vous :", "")

    # Vérifier si l'utilisateur a envoyé une question
    if not user_input:
        st.info("Posez-moi une question pour commencer à discuter !")
        return

    # Vérifier si la question est prédéfinie dans la liste
    if user_input in qa_pairs:
        st.text_area("Bot :", value=qa_pairs[user_input], height=100, max_chars=None, key=None)
        return

    # Générer une réponse en utilisant l'API OpenAI
    bot_response = generate_response(user_input, api_key)

    # Afficher la réponse du chatbot
    st.text_area("Bot :", value=bot_response, height=200, max_chars=None, key=None)

if __name__ == "__main__":
    chatbot()
