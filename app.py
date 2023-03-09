import openai
import streamlit as st

model_engine = "davinci"

def is_api_key_valid(api_key):
    try:
        openai.api_key = api_key
        response = openai.Completion.create(
            engine=model_engine,
            prompt="Hello, World!",
            max_tokens=2,
            n=1,
            stop=None,
            temperature=1.0,
        )
        return True
    except Exception as e:
        return False

def generate_text(prompt):
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = response.choices[0].text
    return message.strip()

def main():
    st.title("OpenAI Chatbot Demo")
    api_key_valid = False

    while not api_key_valid:
        api_key = st.text_input("Enter your OpenAI API key:")
        if is_api_key_valid(api_key):
            openai.api_key = api_key
            api_key_valid = True
            st.empty()

    user_input = st.text_input("You:", "")
    if st.button("Send"):
        bot_response = generate_text(user_input)
        st.text_area("Bot:", value=bot_response, height=200, max_chars=None, key=None)

if __name__ == "__main__":
    main()
