# FastMCP from mcp.server.mcp.server import FastMCP
#step 1: Import FastMCP from the correct module
from mcp.server.fastmcp import FastMCP
#step 2: Create an instance of FastMCP with name and stateless_http
mcp = FastMCP(name="hello-mcp", stateless_http=True)
#step 3: Transport the FastMCP instance with starlette instance streamable_http_app
mcp_app = mcp.streamable_http_app()