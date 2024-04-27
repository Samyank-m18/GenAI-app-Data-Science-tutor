import streamlit as st
import google.generativeai as genai

st.title("🤖AI Data Science Tutor🗨️")

f = open("keys/.open-ai-key.txt")
key = f.read()
genai.configure(api_key=key)

model = genai.GenerativeModel(model_name='gemini-1.5-pro-latest',
                              
                              system_instruction="""You are an AI Data Science Tutor,If a data science
                              topic is given as input help the user to understand it and if input query is not related to data science say you cannot answer in a humble way"""
                             )


# if there is no chat_history in session, init one
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

#Init the chat object
chat = model.start_chat(history=st.session_state["chat_history"])

for msg in chat.history:
    st.chat_message(msg.role).write(msg.parts[0].text)

user_prompt = st.chat_input()

if user_prompt:
    st.chat_message("user").write(user_prompt)
    response = chat.send_message(user_prompt)
    st.chat_message("ai").write(response.text)
    st.session_state["chat_history"] = chat.history