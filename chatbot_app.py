import streamlit as st
from streamlit.components.v1 import html
from bot import chat_with_alpaca


my_js = """
function resize() { var height = document.getElementsByTagName("html")[0].scrollHeight; window.parent.postMessage(["setHeight", height], "*"); }
document.addEventListener('DOMContentLoaded', function() {
      resize();
      setInterval(resize, 1000);
    })
"""
my_html = f"<script>{my_js}</script>"
st.markdown(my_html, unsafe_allow_html=True)

# html(f'<script src="https://cdn.jsdelivr.net/npm/@iframe-resizer/child@5.4.6"></script>')
# html(my_html)
st.set_page_config(page_title="Alpaca Chatbot")
with open("./style.css") as css:
    st.markdown(f'<style>{css.read()}</style>', unsafe_allow_html=True)
st.title("Alpaca AI")
st.subheader("Ask about the system, the site — or how Alpaca can boost your clinic")

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
