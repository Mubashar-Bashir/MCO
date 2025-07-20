# FastMCP from mcp.server.mcp.server import FastMCP
#step 1: Import FastMCP from the correct module
from mcp.server.fastmcp import FastMCP
#step 2: Create an instance of FastMCP with name and stateless_http
mcp = FastMCP(name="hello-mcp", stateless_http=True)
#step 3: Transport the FastMCP instance with starlette instance streamable_http_app
mcp_app = mcp.streamable_http_app()

# create tools for the MCP tools
@mcp.tool("get_weather")
async def get_weather(city: str):
    """
    Example tool to get weather information for a given city.
    """
    # Simulate fetching weather data
    return {"city": city, "temperature": "20°C", "condition": "Sunny"}
@mcp.tool("get_time")
async def get_time():
    """
    Example tool to get the current time.
    """
    from datetime import datetime
    return {"current_time": datetime.now().isoformat()}
@mcp.tool("online_status")
async def online_status():
    """
    Example tool to check online status.
    """
    return {"status": "Online"}


# step 4: Run the FastMCP server with the specified host and port
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(mcp_app, host="localhost", port=8000, log_level="info")
# step 5: Print a message indicating the server is running
    print("FastMCP server is running at http://localhost:8000/mcp/")
# step 6: Add a comment to indicate the end of the main.py file
# End of main.py file