import openai
import streamlit as st

def generate_response(prompt, model_engine, temperature, max_tokens, top_p, frequency_penalty, presence_penalty):
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=max_tokens,
        n=1,
        stop=None,
        temperature=temperature,
        top_p=top_p,
        frequency_penalty=frequency_penalty,
        presence_penalty=presence_penalty
    )
    message = completion.choices[0].text
    return message

def main():
    st.title("ChatGPT-Sayon Web App")
    
    # Ask the user for their OpenAI API key
    api_key = st.text_input("Enter your OpenAI API key:")
    openai.api_key = api_key
    
    # Storing the chat
    if 'chat_history' not in st.session_state:
        st.session_state['chat_history'] = []
    
    user_input = st.text_input("You:")
    
    if user_input:
        output = generate_response(user_input, 'text-davinci-002', st.session_state['vtemperature'], st.session_state['vtoken'], st.session_state['vtop'], st.session_state['vfreq_penalty'], st.session_state.get('vpres_penalty', 0.0))
        # Store the message in the chat history
        st.session_state['chat_history'].append({'user_input': user_input, 'bot_output': output})
    
    # Allow the user to configure parameters
    with st.sidebar:
        st.title('Paramétrages:')
        choix_modeles = st.radio('Modèles', ['Davinci'])
        if choix_modeles == 'Davinci':
            modele_option = st.selectbox('Mod', ['Code', 'Text'])
            if modele_option == 'Code':
                modele_a_charger = "davinci-codex-002"
            elif modele_option == 'Text':
                modele_a_charger = "davinci-002"
    
        st.session_state['vtemperature'] = st.slider('Temperature :', value=0.7, min_value=0., max_value=1., step=.1)
        st.session_state['vtoken'] = st.slider('Token :', value=190, min_value=0, max_value=2048, step=1)
        st.session_state['vtop'] = st.slider('Top_p :', value=1.0, min_value=0.0, max_value=1.0, step=.1)
        st.session_state['vfreq_penalty'] = st.slider('frequence penalty :', value=0.0, min_value=0.0, max_value=1.0, step=.1)
        st.session_state['vpres_penalty'] = st.slider('présence penalty :', value=0.0, min_value=0.0, max_value=1.0, step=.1)

if __name__ == '__main__':
    main()
