from flask import Flask
import requests

# Define the URL of the Pet Finder API
PETFINDER_API_URL = 'https://api.petfinder.com/'

# Set up the Pet Finder API credentials and search parameters
CLIENT_ID = 'YOUR-CLIENT-ID'
CLIENT_SECRET = 'YOUR-CLIENT-SECRET'
SEARCH_PARAMS = {
    'type': 'dog',           # The type of animal to search for
    'location': '94117',     # The ZIP code to search in
    'distance': '50',        # The distance from the ZIP code to search in
    'sort': 'distance',      # Sort the results by distance
    'limit': '10',           # The maximum number of results to return
    'status': 'adoptable'    # Only show adoptable animals
}

# Create a Flask app instance
app = Flask(__name__)

# Get an access token from the Pet Finder API
def get_access_token():
    # Construct the API endpoint
    endpoint = PETFINDER_API_URL + 'v2/oauth2/token'
    response = requests.post(
        endpoint,
        data={
            'grant_type': 'client_credentials',
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET
        }
    )
    # Return the access token
    return response.json()['access_token']


# Define a route to fetch token from the Pet Finder API
@app.route('/v2/oauth2/token')
def token():
    # Return an access token to the client
    response = get_access_token()
    return response


# Define a route to fetch animals from the Pet Finder API
@app.route('/v2/animals')
def search():
    # Construct the API endpoint
    endpoint = PETFINDER_API_URL + 'v2/animals'
    # Get an access token from the Pet Finder API
    access_token = get_access_token()
    # Set up the API request headers
    headers = {'Authorization': f'Bearer {access_token}'}
    # Make a request to the API and return the JSON response
    response = requests.get(endpoint, headers=headers, params=SEARCH_PARAMS)
    # Return the data as the response to the HTTP GET request
    return response.json()


# Start the Flask app if the script is run directly
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
