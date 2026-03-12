import json
import asyncio
import streamlit as st
from mcp import ClientSession
from mcp.client.streamable_http import streamable_http_client
from main import run_agent, convert_mcp_tools_to_llm_format, get_mcp_url


st.set_page_config(page_title="File Management Agent", page_icon="📂")

st.title("File Management Agent")
st.write("Ask me to manage files and directories.\n(Default location: current working directory)")

if "loop" not in st.session_state:
    st.session_state.loop = asyncio.new_event_loop()
    asyncio.set_event_loop(st.session_state.loop)

# Chat persistence
def save_chat(messages):
    with open("chat_history.json", "w") as f:
        json.dump(messages, f)


def load_chat():
    try:
        with open("chat_history.json") as f:
            return json.load(f)
    except:
        return []


# MCP initialization
async def init_mcp():

    client = streamable_http_client(get_mcp_url())

    read, write, _ = await client.__aenter__()

    session = ClientSession(read, write)
    await session.__aenter__()

    await session.initialize()

    tools = await session.list_tools()

    tool_schemas = convert_mcp_tools_to_llm_format(tools)

    return client, session, tool_schemas


# Initialize MCP once
if "mcp_initialized" not in st.session_state:
    client, session, tool_schemas = st.session_state.loop.run_until_complete(init_mcp())
    st.session_state.mcp_client = client
    st.session_state.mcp_session = session
    st.session_state.tool_schemas = tool_schemas
    st.session_state.mcp_initialized = True


# Session state messages
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

        response = st.session_state.loop.run_until_complete(
            run_agent(
                prompt,
                st.session_state.mcp_session,
                st.session_state.tool_schemas,
                st.session_state.messages,
            )
        )

    with st.chat_message("assistant"):
        st.markdown(response)

    st.session_state.messages.append({"role": "assistant", "content": response})

    save_chat(st.session_state.messages)
