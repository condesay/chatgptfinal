import openai
import streamlit as st

# Set up OpenAI API key
openai.api_key = "YOUR_API_KEY_HERE"

# Define function to generate response from OpenAI GPT-3
def generate_response(prompt, engine, temperature, max_tokens, top_p, frequency_penalty, presence_penalty):
    completion = openai.Completion.create(
        engine=engine,
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

# Define function to display chat messages
def message(text, is_user=False):
    if is_user:
        st.write("You: " + text)
    else:
        st.write("Bot: " + text)


# Define Streamlit app
def main():
    # Set page title
    st.set_page_config(page_title="ChatGPT Web App by Sayon")

    # Set up sidebar options
    engine_options = {
        "Davinci": {
            "Text": "text-davinci-003",
            "Code": "davinci-codex"
        }
    }

    # Set up initial settings
    settings = {
        "engine": "Davinci",
        "mode": "Text",
        "temperature": 0.7,
        "max_tokens": 190,
        "top_p": 1.0,
        "frequency_penalty": 0.0,
        "presence_penalty": 0.0
    }

    # Create session state for chat history
    if "chat_history" not in st.session_state:
        st.session_state["chat_history"] = []

    # Display page title and API key input
    st.title("ChatGPT Web App par Sayon")
    api_key = st.text_input("Entrez votre clé OpenAI API Key:", type="password")

    # If API key is provided, display chat interface
    if api_key:
        # Update OpenAI API key
        openai.api_key = api_key

        # Display chat interface
        st.header("Chat")
        user_input = st.text_input("You:")
        if user_input:
            message(user_input, is_user=True)
            prompt = "\n".join([f"You: {msg}" for msg in st.session_state["chat_history"]] + [f"Bot: {user_input}"])
            engine = engine_options[settings["engine"]][settings["mode"]]
            response = generate_response(prompt, engine, settings["temperature"], settings["max_tokens"], settings["top_p"], settings["frequency_penalty"], settings["presence_penalty"])
            message(response)
            st.session_state["chat_history"].append(user_input)

        # Display chat settings sidebar
        st.sidebar.title("Paramètres")
        settings["engine"] = st.sidebar.selectbox("Engine", list(engine_options.keys()))
        settings["mode"] = st.sidebar.selectbox("Mode", list(engine_options[settings["engine"]].keys()))
        settings["temperature"] = st.sidebar.slider("Temperature", min_value=0.0, max_value=1.0, step=0.1, value=settings["temperature"])
        settings["max_tokens"] = st.sidebar.slider("Max Tokens", min_value=1, max_value=2048, step=1, value=settings["max_tokens"])
        settings["top_p"] = st.sidebar.slider("Top P", min_value=0.0, max_value=1.0, step=0.1, value=settings["top_p"])
        settings["frequency_penalty"] = st.sidebar.slider("Frequency Penalty", min_value=0.0, max_value=1.0, step=0.1, value=settings["frequency_penalty"])
        settings["presence_penalty"] = st.sidebar.slider("Presence Penalty", min_value=0.0, max_value=1.0, step=0.1, value=settings["presence_penalty"])
                                                              # Display current settings
        st.sidebar.markdown("### Paramètres Actuels")
        st.sidebar.write(f"Engine: {settings['engine']}")
        st.sidebar.write(f"Mode: {settings['mode']}")
        st.sidebar.write(f"Temperature: {settings['temperature']}")
        st.sidebar.write(f"Max Tokens: {settings['max_tokens']}")
        st.sidebar.write(f"Top P: {settings['top_p']}")
        st.sidebar.write(f"Frequency Penalty: {settings['frequency_penalty']}")
        st.sidebar.write(f"Presence Penalty: {settings['presence_penalty']}")
                
            
if __name__ == '__main__':
    main()                                                   
                                                          
