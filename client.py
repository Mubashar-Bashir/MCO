#client for MCP server at main.py
#http/rest --> package --> request --> response, httpx
import requests

# http request needed 4 steps:
# url, headers, body, response
# step 1: Define the URL of the MCP server
url = "http://localhost:8000/mcp/"
# step 2: Define the headers for the request json, event-stream
headers = {"Accept": "application/json, text/event-stream"}
# step 3: Define the body of the request with the jsonrpc, method,id and parameters {}
body = {
    "jsonrpc": "2.0",
    "method": "tools/list",
    "id": 1,
    "params": {},
}
# step 4: Make the request using requests.post with url, headers and body
response = requests.post(url, headers=headers, json=body)
# step 5: Print the response from the server
# print("Response json >>> :",response.json())
print("Response Status_code >>> :",response.status_code)
# print("Response Header >>> :",response.headers)
print("Response Text >>> :",response.text)
