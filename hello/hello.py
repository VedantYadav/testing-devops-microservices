from flask import Flask, jsonify
import requests
import os

# os.environ['URL'] = "http://127.0.0.1:5001/"

app = Flask(__name__)

@app.route("/")
def print_world():
    url = os.environ.get('URL')
    port = os.environ.get('PORT')
    print("----------- URL -------------")
    print(f'{url}:{port}/')
    print("-----------------------------")
    data = requests.get(f'{url}:{port}/')
    secret = data.json()
    return jsonify({"message":" Python Hello v1", "secret": secret})

if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000)