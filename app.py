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
    st.title("ChatGPT Sayon Web App")
    
    # Ask the user for their OpenAI API key
    api_key = st.text_input("Enter your OpenAI API key:")
    openai.api_key = api_key
    
    # Storing the chat
    if 'generated' not in st.session_state:
        st.session_state['generated'] = []
    if 'past' not in st.session_state:
        st.session_state['past'] = []
    
    user_input = st.text_input("You:", key='input')
    
    if user_input:
        output = generate_response(user_input)
        # Store the output
        st.session_state['past'].append(user_input)
        st.session_state['generated'].append(output)
    
    if st.session_state['generated']:
        for i in range(len(st.session_state['generated'])-1, -1, -1):
            st.write(st.session_state["generated"][i])
            st.write(st.session_state['past'][i])

if __name__ == "__main__":
    main()
