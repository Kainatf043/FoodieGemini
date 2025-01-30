from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure the Google Generative AI client
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Create a generative model instance
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

# Function to get response from the Gemini model
def get_gemini_response(question):
    response = chat.send_message(question, stream=True)
    return response

# Streamlit app configuration
st.set_page_config(page_title="Foodie Gemini")

# App header
st.header("🍲 Foodie Gemini")

# Initialize chat history in session state
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

# Input text box
input = st.text_input("hi", key="input")
submit = st.button("Ask the question")

# Handle the submission of a question
if submit and input:
    response = get_gemini_response(input)
    st.session_state['chat_history'].append(("You", input))
    st.subheader("The Response is")
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("Bot", chunk.text))

# Display the chat history
st.subheader("The Chat history is")
for role, text in st.session_state['chat_history']:
    st.write(f"{role}: {text}")

# Display a simple face image to match the given screenshot
st.markdown("<img src='https://via.placeholder.com/150' style='border-radius:50%;'>", unsafe_allow_html=True)
