import json
from flask import Flask, jsonify, request
from prediction import predict

app = Flask(__name__)


@app.route('/')
@app.route('/status')
def status():
    return jsonify({'status': 'ok'})


@app.route('/predictions', methods=['POST'])
def create_prediction():
    data = request.data or '{}'
    body = json.loads(data)
    return jsonify(predict(body))

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0') # Launch built-in we server and run this Flask webapp
