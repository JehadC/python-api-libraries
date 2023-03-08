from flask import Flask
import requests
import json

# Define the URL of the Cat Fact API
CAT_FACT_API_URL = 'https://cat-fact.herokuapp.com/'

# Create a Flask app instance
app = Flask(__name__)


# Define a route to fetch facts from the Cat Fact API
@app.route('/facts')
def facts():
    # Construct the API endpoint
    endpoint = CAT_FACT_API_URL + 'facts'
    # Make a request to the Cat-Fact API
    response = requests.get(endpoint)
    # Load the response JSON data
    data = json.loads(response.text)
    # Return the data as the response to the HTTP GET request
    return data


# Start the Flask app if the script is run directly
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
