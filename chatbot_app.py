import streamlit as st
from bot import chat_with_alpaca 

st.set_page_config(page_title="Alpaca Chatbot")
st.title("Chat with Alpaca")
#st.markdown("Ask anything about *Alpaca*.")
# hide_streamlit_style = """
#                 <style>
#                 div[data-testid="stToolbar"] {
#                 visibility: hidden;
#                 height: 0%;
#                 position: fixed;
#                 }
#                 div[data-testid="stDecoration"] {
#                 visibility: hidden;
#                 height: 0%;
#                 position: fixed;
#                 }
#                 div[data-testid="stStatusWidget"] {
#                 visibility: hidden;
#                 height: 0%;
#                 position: fixed;
#                 }
#                 #MainMenu {
#                 visibility: hidden;
#                 height: 0%;
#                 }
#                 header {
#                 visibility: hidden;
#                 height: 0%;
#                 }
#                 footer {
#                 visibility: hidden;
#                 height: 0%;
#                 }
#                 </style>
#                 """
# st.markdown(hide_streamlit_style, unsafe_allow_html=True)
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
        with st.chat_message("user", avatar='./user.png'):
            st.markdown(message)
    else:
        with st.chat_message("assistant", avatar='./alpaca.png'):
            st.markdown(message)