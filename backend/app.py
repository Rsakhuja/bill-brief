from flask import Flask, request, jsonify
from flask_cors import CORS
import time

app = Flask(__name__)
CORS(app, origins=['http://localhost:3000'])

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

def process_file(file):
    # Function to process the file
    file_name = file.filename
    print(f"Processing file: {file_name}")
    # Add your file processing logic here
    return file_name

@app.route('/mock-response', methods=['POST'])
def mock_response():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    if file:
        file_name = process_file(file)
        time.sleep(5)  # Simulate processing time
        mock_data = {
            'message': f'File {file_name} processed successfully',
            'status': 'success'
        }
        response = jsonify(mock_data)
        return response

if __name__ == '__main__':
    app.run(debug=True)
