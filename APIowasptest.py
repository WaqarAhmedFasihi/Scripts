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

# A1:2017 - Injection
# Try sending a payload with an SQL injection attack
payload_with_injection = {
    "key1": "value1'; DROP TABLE users; --",
    "key2": "value2"
}
response = requests.post(api_url, headers=headers, json=payload_with_injection)
print(response.status_code)
print(response.text)

# A2:2017 - Broken Authentication
# Try sending a request with an incorrect API username and password
incorrect_api_username = "incorrect_username"
incorrect_api_password = "incorrect_password"
headers_with_incorrect_credentials = {
    "Content-Type": "application/json",
    "Authorization": "Basic " + b64encode(incorrect_api_username + ":" + incorrect_api_password)
}
response = requests.post(api_url, headers=headers_with_incorrect_credentials, json=payload)
print(response.status_code)
print(response.text)

# A3:2017 - Broken Access Control
# Try sending a request with an unauthorized user's API credentials
unauthorized_api_username = "unauthorized_user"
unauthorized_api_password = "unauthorized_password"
headers_with_unauthorized_credentials = {
    "Content-Type": "application/json",
    "Authorization": "Basic " + b64encode(unauthorized_api_username + ":" + unauthorized_api_password)
}
response = requests.post(api_url, headers=headers_with_unauthorized_credentials, json=payload)
print(response.status_code)
print(response.text)
