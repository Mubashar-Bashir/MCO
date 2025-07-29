from datetime import datetime
from pydantic import Field
import uvicorn
# FastMCP from mcp.server.mcp.server import FastMCP
#step 1: Import FastMCP from the correct module
from mcp.server.fastmcp import FastMCP
#step 2: Create an instance of FastMCP with name and stateless_http
mcp = FastMCP(name="hello-mcp", stateless_http=True)
#step 3: Transport the FastMCP instance with starlette instance streamable_http_app
mcp_app = mcp.streamable_http_app()

# create tools for the MCP tools
@mcp.tool("get_weather", description="Get weather information for a city")
async def get_weather(
    city: str = Field(..., description="The name of the city to get weather for")
    ):
    """
    Example tool to get weather information for a given city.
    """
    # Simulate fetching weather data
    return {"city": city, "temperature": "20°C", "condition": "Sunny"}
@mcp.tool("get_time", description="Get the current time")
async def get_time():
    """
    Example tool to get the current time.
    """
    return {"current_time": datetime.now().isoformat()}
@mcp.tool(name="online_status", description="Check online status")
async def online_status():
    """
    Example tool to check online status.
    """
    return {"status": "Online"}
@mcp.tool("Search_Online")
async def Search_Online(
    query: str = Field(description="The search query")
    ):
    """
    Example tool to search online for a query.
    """
    # Simulate an online search
    return {"query": query, "results": ["Result 1", "Result 2", "Result 3"]}
@mcp.tool(name= "add_numbers", description="Add two numbers")
async def add_numbers(
    a: int = Field(..., description="The first number"), 
    b: int = Field(..., description="The second number")):
    """
    Example tool to add two numbers.
    """
    
    return {"result": a + b}

docs = {
    "deposition.md": "This deposition covers the testimony of Angela Smith, P.E.",
    "report.pdf": "The report details the state of a 20m condenser tower.",
    "financials.docx": "These financials outline the project's budget and expenditures.",
    "outlook.pdf": "This document presents the projected future performance of the system.",
    "plan.md": "The plan outlines the steps for the project's implementation.",
    "spec.txt": "These specifications define the technical requirements for the equipment.",
}

#TODO: Add a tool to retrieve documents
@mcp.tool(name="read_document", description="Retrieve a document by name")
async def read_document(
    name: str =Field(..., description="The name of the document")):
    """
    Example tool to retrieve a document by name.
    """
    if name in docs:
        return {"Document name": name, "content": docs[name]}
    else:
        raise ValueError(f"Document '{name}' not found.")

# step 4: Run the FastMCP server with the specified host and port
if __name__ == "__main__":
   
    uvicorn.run(mcp_app, host="localhost", port=8000, log_level="info")
# step 5: Print a message indicating the server is running
    print("FastMCP server is running at http://localhost:8000/mcp/")
# step 6: Add a comment to indicate the end of the main.py file
# End of main.py file