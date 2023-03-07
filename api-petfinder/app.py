from flask import Flask
import requests

app = Flask(__name__)

# Set up the Petfinder API credentials and search parameters
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

def get_access_token():
    # Get an access token from the Petfinder API
    response = requests.post(
        'https://api.petfinder.com/v2/oauth2/token',
        data={
            'grant_type': 'client_credentials',
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET
        }
    )
    # Return the access token
    return response.json()['access_token']

@app.route('/v2/oauth2/token')
def token():
    # Return an access token to the client
    response = get_access_token()
    return response

@app.route('/v2/animals')
def search():
    # Get an access token from the Petfinder API
    access_token = get_access_token()
    # Set up the API request URL and headers
    url = 'https://api.petfinder.com/v2/animals'
    headers = {'Authorization': f'Bearer {access_token}'}
    # Make a request to the API and return the JSON response
    response = requests.get(url, headers=headers, params=SEARCH_PARAMS)
    return response.json()

if __name__ == '__main__':
    # Start the Flask app on port 8000
    app.run(host='0.0.0.0', port=8000)

