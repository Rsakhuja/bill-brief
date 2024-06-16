from flask import Flask, jsonify
from flask_cors import CORS
import time

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Hello World!"

@app.route('/api/data', methods=['GET'])
def get_data():
    sample_data = {
        'message': 'Hello, this is your data!',
        'status': 'success'
    }
    return jsonify(sample_data)

@app.route('/mock-response', methods=['POST'])
def mock_response():
    time.sleep(5)  # Wait for 5 seconds
    mock_data = {
        'message': 'This is a mock response after 5 seconds',
        'status': 'success'
    }
    response = jsonify(mock_data)
    response.headers.add('Access-Control-Allow-Origin', 'http://localhost:3000')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    return response

if __name__ == '__main__':
    app.run(debug=True)