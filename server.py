from mcp_f1analisys.server.mcp_server import create_mcp_server

mcp = create_mcp_server()

app = mcp.http_app()

if __name__ == "__main__":
    import os
    port = int(os.getenv("PORT", 8000))
    mcp.run(transport="streamable-http", host="0.0.0.0", port=port)