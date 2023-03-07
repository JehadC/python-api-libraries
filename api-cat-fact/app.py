from flask import Flask
import requests
import json

CAT_FACT_API_URL = 'https://cat-fact.herokuapp.com/facts'

# Create a Flask app instance
app = Flask(__name__)

# Define the app route for the homepage
@app.route('/')
def index():
    # Make a request to the Cat-Fact API
    response = requests.get(CAT_FACT_API_URL)
    # Load the response JSON data
    data = json.loads(response.text)
    # Return the data as the response to the HTTP GET request
    return data

# Start the Flask app if the script is run directly
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
