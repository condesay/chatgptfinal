import openai
import streamlit as st

# Définir la clé API OpenAI
openai.api_key = "YOUR_API_KEY_HERE"

# Définir l'ID du modèle OpenAI que nous allons utiliser
model_engine = "davinci-003"

# Demander à l'utilisateur de saisir la clé API OpenAI
api_key = st.text_input("Entrez votre clé API OpenAI")

# Vérifier que la clé API est valide
if api_key:
    openai.api_key = api_key
    try:
        # Vérifier que la clé API fonctionne en effectuant une demande de complétion avec un prompt de test
        response = openai.Completion.create(
            engine=model_engine,
            prompt="Bonjour, comment allez-vous ?",
            max_tokens=10,
            n=1,
            stop=None,
            temperature=0.5,
        )
    except openai.error.AuthenticationError:
        st.warning("Clé API OpenAI invalide. Veuillez entrer une clé API valide.")
    else:
        st.success("Clé API OpenAI valide. Vous pouvez maintenant poser des questions.")

        # Créer des listes vides pour stocker les questions et les réponses précédentes
        questions = []
        answers = []

        # Boucle principale pour poser des questions et recevoir des réponses
        while True:
            # Afficher une zone de texte pour poser des questions
            question = st.text_input("Posez une question")

            # Vérifier si l'utilisateur a cliqué sur le bouton "Envoyer"
            if st.button("Envoyer"):
                # Créer un prompt en ajoutant la question à une phrase de démarrage
                prompt = f"Répondez à la question suivante : {question} \nRéponse :"

                # Envoyer la demande de complétion à l'API OpenAI
                response = openai.Completion.create(
                    engine=model_engine,
                    prompt=prompt,
                    max_tokens=50,
                    n=1,
                    stop=None,
                    temperature=0.5,
                )

                # Afficher la réponse de l'API OpenAI
                answer = response.choices[0].text.strip()
                st.write("Réponse : ", answer)

                # Ajouter la question et la réponse aux listes précédentes
                questions.append(question)
                answers.append(answer)

            # Afficher les questions et les réponses précédentes
            if questions and answers:
                st.write("Historique des questions et réponses :")
                for i in range(len(questions)):
                    st.write("Question : ", questions[i])
                    st.write("Réponse : ", answers[i])

            # Ajouter un bouton pour effacer l'historique des questions et réponses
            if st.button("Effacer l'historique"):
                questions = []
                answers = []

