# Headers used in HTTP requests to specify that the content type is JSON
headers = {
    "Content-Type": "application/json"
}

# Default request body for creating a new user
user_body = {
    "firstName": "Andrea",  # User's first name
    "phone": "+11234567890",  # User's phone number
    "address": "123 Elm Street, Hilltop"  # User's address
}

# Default request body for creating a new kit
kit_body = {
    "name": "a"  # Kit name (can be modified during testing)
}
