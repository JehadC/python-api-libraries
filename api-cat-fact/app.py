from flask import Flask, request
import requests
import json

CAT_FACT_API_URL = 'https://cat-fact.herokuapp.com/'

# Create a Flask app instance
app = Flask(__name__)


# Define the app route for the facts
@app.route('/facts')
def facts():
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
