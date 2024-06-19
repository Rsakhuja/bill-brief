from flask import Flask, request, jsonify
from flask_cors import CORS
import time
import os
from llm_implementation import rag
import json

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
    file_path = os.path.join("llm_implementation/data", file_name)
    file.save(file_path)

    # Add your file processing logic here
    llm_response = rag.analyze()
    print(llm_response)
    return llm_response

@app.route('/analysis', methods=['POST'])
def analysis():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    if file:
        llm_response = str(process_file(file))

        try:
            json_object = json.loads(llm_response)
            return json_object
        except ValueError:
            return "Could not process pdf"


@app.route('/mock-response', methods=['POST'])
def mock_response():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    if file:
        file_name = process_file(file)
        time.sleep(2)  # Simulate processing time
        mock_data = {
            'paper_title': str(file_name),
            'summary': f'File {file_name} processed successfully. This is its summary',
            'main_findings': 'success',
            'benefits': "There are some benefits for the people",
            'concerns': 'This is what is concerning in the bill you uploaded'
        }
        response = jsonify(mock_data)
        return response

if __name__ == '__main__':
    app.run(debug=True)
