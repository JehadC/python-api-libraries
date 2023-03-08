from flask import Flask
import requests
import json

# Define the URL of the Coin Desk API
COINDESK_API_URL = 'http://api.coindesk.com/'

# Create a Flask app instance
app = Flask(__name__)

# Define a route to fetch from the Coin Desk API
@app.route('/')
def index():
    # Construct the API endpoint
    endpoint = COINDESK_API_URL + 'v1/bpi/currentprice.json'
    # Make a request to the CoinDesk API
    response = requests.get(endpoint)
    # Load the response JSON data
    data = json.loads(response.text)
    # Return the data as the response to the HTTP GET request
    return data

# Start the Flask app if the script is run directly
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
