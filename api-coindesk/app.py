from flask import Flask
import requests
import json

COINDESK_API_URL = 'http://api.coindesk.com/v1/bpi/currentprice.json'

# Create a Flask app instance
app = Flask(__name__)

# Define the app route for the homepage
@app.route('/')
def index():
    # Make a request to the CoinDesk API
    response = requests.get(COINDESK_API_URL)
    # Load the response JSON data
    data = json.loads(response.text)
    # Return the data as the response to the HTTP GET request
    return data

# Start the Flask app if the script is run directly
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
