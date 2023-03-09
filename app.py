import openai
import streamlit as st

def generate_response(prompt):
    completion = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.6,
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
    
    user_input = st.text_input("You:", key='input')
    
    if user_input:
        output = generate_response(user_input)
        # Store the message in the chat history
        st.session_state['chat_history'].append({'user_input': user_input, 'bot_output': output})
    
    if st.session_state['chat_history']:
        for i in range(len(st.session_state['chat_history'])):
            chat = st.session_state['chat_history'][i]
            st.write("You: " + chat['user_input'])
            st.write("Bot: " + chat['bot_output'])

if __name__ == "__main__":
    main()
