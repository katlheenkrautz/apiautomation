import requests
import configuration
import data

# Function to send a POST request to create a new user
def create_new_user(body):
    # Sends a POST request to the user creation endpoint with the provided request body and headers
    return requests.post(configuration.CREATE_USER_URL, json=body, headers=data.headers)

# Function to send a POST request to create a new kit for a user
def post_new_client_kit(kit_body, auth_token):
    # Copy the default headers and add the Authorization token
    headers_with_auth = data.headers.copy()
    headers_with_auth["Authorization"] = f"Bearer {auth_token}"

    # Sends a POST request to the kit creation endpoint with the provided kit body and auth headers
    return requests.post(configuration.CREATE_KIT_URL, json=kit_body, headers=headers_with_auth)
