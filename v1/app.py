import json
import streamlit as st
from main import run_agent

st.set_page_config(page_title="File Management Agent", page_icon="📂")

st.title("File Management Agent")
st.write("Ask me to manage files and directories.\n(Default location: current working directory)")


def save_chat(messages):
    with open("chat_history.json", "w") as f:
        json.dump(messages, f)

def load_chat():
    try:
        with open("chat_history.json") as f:
            return json.load(f)
    except:
        return []

# Session state chat history
if "messages" not in st.session_state:
    st.session_state.messages = load_chat()

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
prompt = st.chat_input("Ask something...")

if prompt:
    # Show user message
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    # Run agent
    with st.spinner("Agent thinking..."):
        response = run_agent(prompt, st.session_state.messages)

    # Show agent response
    with st.chat_message("assistant"):
        st.markdown(response)

    st.session_state.messages.append({"role": "assistant", "content": response})

    save_chat(st.session_state.messages)