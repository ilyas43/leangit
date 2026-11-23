"""A small MCP server example.

Install the SDK with ``pip install "mcp[cli]"``, then run this file with
``python server.py``. Connect an MCP client to the Streamable HTTP endpoint
at ``http://127.0.0.1:8000/mcp``.
"""

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Example Server", host="127.0.0.1", port=8000)


@mcp.tool()
def add(a: float, b: float) -> float:
	"""Add two numbers."""
	return a + b


@mcp.tool()
def greet(name: str) -> str:
	"""Return a friendly greeting."""
	return f"Hello, {name}!"


@mcp.resource("greeting://welcome")
def welcome_resource() -> str:
	"""A simple example MCP resource."""
	return "Welcome to the example MCP server."


if __name__ == "__main__":
	mcp.run(transport="streamable-http")
