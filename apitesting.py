import requests

# Set the URL of the API endpoint
api_url = "http://example.com/api/endpoint"

# Set the API credentials
api_username = "your_api_username"
api_password = "your_api_password"

# Set the headers for the API request
headers = {
    "Content-Type": "application/json",
    "Authorization": "Basic " + b64encode(api_username + ":" + api_password)
}

# Set the payload for the API request
payload = {
    "key1": "value1",
    "key2": "value2"
}

# Send the API request
response = requests.post(api_url, headers=headers, json=payload)

# Print the response status code
print(response.status_code)

# Print the response body
print(response.text)
