import openai
import streamlit as st

# Interface utilisateur Streamlit
st.title("Bot intelligent")

# Demander la clé API OpenAI à l'utilisateur
api_key = st.text_input("Entrez votre clé API OpenAI : ")

# Vérifier si la clé API est valide et initialiser l'API OpenAI
def initialize_openai(api_key):
    try:
        openai.api_key = api_key
        models = openai.Model.list()
        model_id = None
        for model in models['data']:
            if model['id'] == 'davinci':
                model_id = model['id']
                break

        if model_id:
            st.write("Initialisation de Davinci...")
            return openai.Model(model_id)
        else:
            st.write("Impossible de trouver le modèle Davinci")
            return None
    except:
        st.write("Clé API invalide")
        return None

model = None
if api_key:
    model = initialize_openai(api_key)

# Fonction pour générer une réponse de Davinci
def generate_response(prompt):
    response = model.generate(prompt=prompt, max_tokens=1024)
    return response.choices[0].text.strip()

# Obtenir l'entrée utilisateur
user_input = st.text_input("Vous: ")

# Générer une réponse de Davinci et afficher la sortie
if user_input and model:
    st.write("Bot: ", generate_response(user_input))
