import os
import time
import asyncio
from collections import deque
from dotenv import load_dotenv
from google import genai
from google.genai import types
from mcp.client.streamable_http import streamable_http_client
from mcp import ClientSession
from prompts import SYSTEM_PROMPT


load_dotenv()

# client
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

# conversation memory
MAX_HISTORY = 20
conversation_history = deque(maxlen=MAX_HISTORY)

def get_mcp_url():
    host = os.getenv("MCP_HOST", "localhost")
    port = os.getenv("MCP_PORT", "8000")
    return f"http://{host}:{port}/mcp"

def safe_generate(**kwargs):
    retries = 3

    for attempt in range(retries):
        try:
            return client.models.generate_content(**kwargs)

        except Exception as e:
            if "503" in str(e) and attempt < retries - 1:
                print("LLM overloaded. Retrying...")
                time.sleep(2)
            else:
                raise


def convert_mcp_tools_to_llm_format(tools):
    tool_schemas = []

    for tool in tools.tools:
        tool_schemas.append(
            types.Tool(
                function_declarations=[
                    types.FunctionDeclaration(
                        name=tool.name,
                        description=tool.description,
                        parameters=tool.inputSchema,
                    )
                ]
            )
        )

    return tool_schemas

def load_agent_memory(data):
    try:
        conversation_history.clear()

        for msg in data[-MAX_HISTORY:]:
            role = "model" if msg["role"] == "assistant" else "user"

            conversation_history.append(
                {
                    "role": role,
                    "parts": [{"text": msg["content"]}],
                }
            )
    except:
        pass

def clean_history(history):

    cleaned = []

    for msg in history:

        # Handle LLM Content object
        if isinstance(msg, types.Content):

            parts = []

            for p in msg.parts:

                if getattr(p, "text", None):
                    parts.append({"text": p.text})

                elif getattr(p, "function_call", None):
                    parts.append({"function_call": p.function_call})

                elif getattr(p, "function_response", None):
                    parts.append({"function_response": p.function_response})

            if parts:
                cleaned.append({
                    "role": msg.role,
                    "parts": parts
                })

        # Handle dict messages
        elif isinstance(msg, dict):

            parts = []

            for p in msg.get("parts", []):

                if p.get("text"):
                    parts.append({"text": p["text"]})

                elif p.get("function_call"):
                    parts.append({"function_call": p["function_call"]})

                elif p.get("function_response"):
                    parts.append({"function_response": p["function_response"]})

            if parts:
                cleaned.append({
                    "role": msg["role"],
                    "parts": parts
                })

    return cleaned


async def run_agent(user_input: str, session: ClientSession, tool_schemas:list, history: list):
    load_agent_memory(history)

    # ignore meaningless inputs
    if user_input.strip().lower() in ["", ".", "ok", "okay", "sure", "no"]:
        return "Alright."

    # add user message
    conversation_history.append(
        {
            "role": "user",
            "parts": [{"text": user_input}],
        }
    )

    response = safe_generate(
        model="gemini-2.5-flash",
        contents=clean_history(conversation_history),
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_PROMPT,
            tools=tool_schemas,
        ),
    )

    candidate = response.candidates[0]
    conversation_history.append(candidate.content)

    # check if tool was called
    if candidate.content.parts:

        for part in candidate.content.parts:

            if part.function_call:

                function_name = part.function_call.name
                arguments = dict(part.function_call.args)

                print("\nTOOL CALLED")
                print("Tool:", function_name)
                print("Arguments:", arguments)

                # call MCP tool
                result = await session.call_tool(
                    function_name,
                    arguments
                )

                print("Result:", result)
                print("-" * 50)

                # add tool response to conversation
                conversation_history.append(
                    {
                        "role": "tool",
                        "parts": [
                            {
                                "function_response": {
                                    "name": function_name,
                                    "response": {
                                        "result": str(result)
                                    },
                                }
                            }
                        ],
                    }
                )

                # send tool result back to model
                followup = safe_generate(
                    model="gemini-2.5-flash",
                    contents=clean_history(conversation_history),
                    config=types.GenerateContentConfig(
                        system_instruction=SYSTEM_PROMPT,
                        tools=tool_schemas,
                    ),
                )

                conversation_history.append(
                    followup.candidates[0].content
                )

                text_parts = []

                for part in followup.candidates[0].content.parts:
                    if hasattr(part, "text") and part.text:
                        text_parts.append(part.text)

                if text_parts:
                    return "\n".join(text_parts)

                return "Task completed."

    # if no tool call
    conversation_history.append(candidate.content)

    return response.text


async def main():

    print("\nFile Management Agent (MCP + LLM)")
    print("Type 'exit' or 'quit' to stop.\n")

    async with streamable_http_client(get_mcp_url()) as (read, write):

        async with ClientSession(read, write) as session:

            # initialize MCP
            await session.initialize()

            # discover tools
            tools = await session.list_tools()

            print("Loaded MCP tools:")

            for tool in tools.tools:
                print(" -", tool.name)

            # convert tools to LLM format
            tool_schemas = convert_mcp_tools_to_llm_format(tools)

            while True:

                user_input = input("\nUser: ")

                if user_input.lower() in ["exit", "quit"]:
                    print("Goodbye!")
                    break

                output = await run_agent(
                    user_input,
                    session,
                    tool_schemas,
                    history=[]
                )

                print("\nAgent:", output)


if __name__ == "__main__":
    asyncio.run(main())
