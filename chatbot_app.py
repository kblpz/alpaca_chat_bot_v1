import streamlit as st
from bot import chat_with_alpaca 

st.set_page_config(page_title="Alpaca Chatbot")
st.title("Chat with Alpaca")
#st.markdown("Ask anything about *Alpaca*.")

# Initialize session state
if "history" not in st.session_state:
    st.session_state.history = []

# User input
user_input = st.chat_input("Ask your question:")

# Handle user input
if user_input:
    with st.spinner("Thinking..."):
        reply = chat_with_alpaca(user_input)
        st.session_state.history.append(("user", user_input))
        st.session_state.history.append(("bot", reply))

# Display chat history
for speaker, message in st.session_state.history:
    if speaker == "user":
        with st.chat_message("user"):
            st.markdown(message)
    else:
        with st.chat_message("assistant"):
            st.markdown(message)