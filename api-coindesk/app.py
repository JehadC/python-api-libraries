from flask import Flask
import requests
import json

URL = 'http://api.coindesk.com/v1/bpi/currentprice.json'


app = Flask(__name__)


@app.route('/')
def index():
    response = requests.get(URL)
    data = json.loads(response.text)
    return data


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

