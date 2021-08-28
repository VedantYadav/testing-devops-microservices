from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def print_world():
    secret = "Triton Server"
    return jsonify({"message":" Python World v1", "secret": secret})

if __name__=='__main__':
    app.run(host='0.0.0.0', port=5001)