import data
import sender_stand_request

# Function to generate a user request body with a specific first name
def get_user_body(first_name):
    current_body = data.user_body.copy()
    current_body["firstName"] = first_name
    return current_body

# Function to retrieve an authentication token for a new user
def get_new_user_token(first_name):
    user_body = get_user_body(first_name)
    user_response = sender_stand_request.create_new_user(user_body)
    assert user_response.status_code == 201
    return user_response.json()["authToken"]

# Function to generate a kit request body with a specific name
def get_kit_body(name):
    current_body = data.kit_body.copy()
    current_body["name"] = name
    return current_body

# Positive test case
def positive_assert(kit_body):
    auth_token = get_new_user_token("Andrea")
    kit_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    assert kit_response.status_code == 201
    assert kit_response.json()["name"] == kit_body["name"]

# Negative test case: expecting status code 400
def negative_assert_code_400(kit_body):
    auth_token = get_new_user_token("Andrea")
    kit_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    assert kit_response.status_code == 400

# Function to generate a kit request body without the "name" field
def get_kit_body_without_name():
    current_body = data.kit_body.copy()
    # Remove the "name" field from the request body
    del current_body["name"]
    return current_body

# Function to generate a kit request body with a numeric "name" (invalid)
def get_kit_body_with_numeric_name():
    current_body = data.kit_body.copy()
    current_body["name"] = 123  # Numeric value (invalid type)
    return current_body

# 1. Test: Create a kit with a one-character name
def test_create_kit_with_one_character_name():
    kit_body = get_kit_body("a")
    auth_token = get_new_user_token("Andrea")
    kit_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    assert kit_response.status_code == 201, f"Error: Expected status code 201, got {kit_response.status_code}"
    assert kit_response.json()["name"] == kit_body["name"], f"Error: Name mismatch. Expected: {kit_body['name']}, Got: {kit_

