import os
from fastmcp import FastMCP
from fastmcp.server.auth import JWTVerifier
from ..tools.f1_tools import register_f1_tools

def create_mcp_server() -> FastMCP:
    """Create and configure the MCP server"""

    auth = JWTVerifier(
        public_key=os.getenv("PUBLIC_KEY"),
        algorithm=os.getenv("ALGORITHM")
    )

    mcp = FastMCP(
        "mcp-f1analisys",
        auth=auth
    )

    # Register all F1 tools
    register_f1_tools(mcp)
    return mcp

def main():
    """Main function for local development"""
    mcp = create_mcp_server()
    mcp.run()