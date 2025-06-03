# Urban Grocers Project – API Test Automation
## Description
This project automates API testing for creating personalized product kits in the Urban Grocers application using Python and the pytest framework. The workflow includes:
- Creating a new user
- Retrieving an authentication token
- Creating a custom product kit

The tests cover both positive and negative cases, verifying the server's response to different formats and sizes of the name field.

## Project Structure
- configuration.py: Stores base URLs and API routes.
- data.py: Contains request payloads for POST methods.
- sender_stand_request.py: Functions for sending HTTP requests.
- create_kit_name_kit_test.py: Automated test cases.
- README.md: Project documentation.
- .gitignore: Specifies files and folders to exclude from version control.

## How to Clone This Repository
Open your terminal and run:
- gh repo clone katlheenkrautz/apiautomation
Make sure you have GitHub CLI installed to use the gh repo clone command. You can also use git clone if you prefer.

## Running the Tests
1. Clone the repository (see instructions above).
2. Install the dependencies: pip install -r requirements.txt
3. Run the tests: pytest create_kit_name_kit_test.py -v

## Technologies Used
- **Python**: Main programming language.
- **Pytest**: Test Framework.
- **Requests**: Library for sending HTTP requests.

