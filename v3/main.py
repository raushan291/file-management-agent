import os
import asyncio
from dotenv import load_dotenv

from google.adk.agents import Agent
from google.adk.runners import Runner
from google.adk.tools.mcp_tool import MCPToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StreamableHTTPServerParams
from google.adk.sessions import InMemorySessionService

from prompts import SYSTEM_PROMPT

APP_NAME = "file_management_agent"
USER_ID = "streamlit_user"
SESSION_ID = "file_management_chat"

load_dotenv()

def get_mcp_url():
    host = os.getenv("MCP_HOST", "localhost")
    port = os.getenv("MCP_PORT", "8000")
    return f"http://{host}:{port}/mcp"


def create_runner():
    """Create ADK agent runner"""

    # load MCP tools
    mcp_tools = MCPToolset(
        connection_params=StreamableHTTPServerParams(
            url=get_mcp_url()
        )
    )

    # create agent
    agent = Agent(
        name="file_agent",
        model="gemini-2.5-flash",
        instruction=SYSTEM_PROMPT,
        tools=[mcp_tools],
    )

    # session memory for conversations
    session_service = InMemorySessionService()

    return Runner(agent=agent, app_name=APP_NAME, session_service=session_service)


async def main():
    print("\nFile Management Agent (ADK + MCP)")
    print("Type 'exit' to quit\n")

    runner = create_runner()

    while True:

        user_input = input("\nUser: ")

        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break

        response = await runner.run(user_input)

        print("\nAgent:", response)


if __name__ == "__main__":
    asyncio.run(main())
