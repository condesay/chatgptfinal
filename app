import openai
import streamlit as st

model_engine = "gpt-3.5-turbo"

def generate_text(prompt, api_key):
    openai.api_key = api_key
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
    api_key = st.text_input("Enter your OpenAI API key:")
    user_input = st.text_input("You:", "")

    if st.button("Send"):
        bot_response = generate_text(user_input, api_key)
        st.text_area("Bot:", value=bot_response, height=200, max_chars=None, key=None)

if __name__ == "__main__":
    main()
