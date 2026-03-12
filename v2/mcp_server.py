import os
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP
from tool_registry import TOOLS

load_dotenv()

mcp = FastMCP(
    name="file-tools",
    host=os.getenv("MCP_HOST", "0.0.0.0"),
    port=int(os.getenv("MCP_PORT", 8000))
)

for name, spec in TOOLS.items():
    func = spec["function"]
    description = spec["description"]

    mcp.tool(
        name=name,
        description=description
    )(func)

if __name__ == "__main__":
    mcp.run(transport="streamable-http")