import openai
import streamlit as st

# Définir les paramètres de l'API OpenAI
openai.api_key = "YOUR_API_KEY_HERE"
model_engine = "text-davinci-003"

# Définir la fonction pour obtenir une réponse à partir de l'API OpenAI
def ask_question(prompt):
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    answer = response.choices[0].text.strip()
    return answer

# Définir la fonction principale pour l'interface utilisateur
def main():
    # Afficher le champ de texte pour la clé API
    api_key = st.text_input("Entrez votre clé API OpenAI :")

    # Vérifier si la clé API est correcte
    if api_key:
        openai.api_key = api_key
        try:
            openai.Completion.create(engine=model_engine, prompt="Test prompt", max_tokens=0)
        except Exception as e:
            st.error("La clé API est incorrecte. Veuillez entrer une clé valide.")
            return

        # Si la clé API est correcte, afficher le champ de texte pour la question et la réponse
        st.success("La clé API est valide. Vous pouvez maintenant poser des questions.")
        conversation_history = []
        while True:
            user_input = st.text_input("Vous :")
            if not user_input:
                continue
            conversation_history.append(f"Vous : {user_input}")
            bot_response = ask_question("\n".join(conversation_history))
            conversation_history.append(f"Bot : {bot_response}")
            st.write(f"Bot : {bot_response}")
            st.write("\n".join(conversation_history[-10:]))
            st.write("---")

if __name__ == "__main__":
    main()
