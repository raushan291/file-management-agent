import json
import asyncio
import streamlit as st
from google.genai import types

from main import create_runner, APP_NAME, USER_ID, SESSION_ID


st.set_page_config(page_title="File Management Agent", page_icon="📂")

st.title("File Management Agent")
st.write("Ask me to manage files and directories.\n(Default location: current working directory)")

# Chat persistence
def save_chat(messages):
    with open("chat_history.json", "w") as f:
        json.dump(messages, f)


def load_chat():
    try:
        with open("chat_history.json") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


# Initialize runner once
if "runner" not in st.session_state:
    st.session_state.runner = create_runner()
    
    # Define an internal function to handle the async creation
    async def init_session():
        await st.session_state.runner.session_service.create_session(
            app_name=APP_NAME,
            user_id=USER_ID,
            session_id=SESSION_ID
        )

    # Use a try/except or run_until_complete to avoid loop shutdown conflicts
    try:
        loop = asyncio.get_event_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
    
    loop.run_until_complete(init_session())
    st.session_state.session_created = True


# Load chat history
if "messages" not in st.session_state:
    st.session_state.messages = load_chat()


# Display chat
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# Chat input
prompt = st.chat_input("Ask something...")

if prompt:

    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.spinner("Agent thinking..."):

        content = types.Content(
            role="user",
            parts=[types.Part(text=prompt)]
        )

        events = st.session_state.runner.run(
            user_id=USER_ID,
            session_id=SESSION_ID,
            new_message=content
        )

        response = ""

        for event in events:
            if event.content and event.content.parts:
                for part in event.content.parts:
                    
                    # TOOL CALL
                    if hasattr(part, "function_call") and part.function_call:
                        print("\nTOOL CALLED")
                        print("Tool:", part.function_call.name)
                        print("Arguments:", part.function_call.args)

                    # TOOL RESULT
                    if hasattr(part, "function_response") and part.function_response:
                        print("\nTOOL RESULT")
                        print("Tool:", part.function_response.name)
                        print("Output:", part.function_response.response)
                    
                    if hasattr(part, "text") and part.text:
                        response += part.text

    with st.chat_message("assistant"):
        st.markdown(response)

    st.session_state.messages.append({"role": "assistant", "content": response})

    save_chat(st.session_state.messages)
