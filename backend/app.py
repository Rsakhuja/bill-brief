from flask import Flask, request, jsonify
from flask_cors import CORS
import time
import os
from llm_implementation import rag
import json

app = Flask(__name__)
CORS(app, origins='http://localhost:3000')

def process_file(file):
    # Function to process the file
    file_name = file.filename
    print(f"\n Processing file: {file_name} \n")
    pdf_storage_directory = f"llm_implementation/data/{file_name}" # This where the PDF should be 
    
    # Ensuring that the directory exists
    if not os.path.exists(pdf_storage_directory): # If it doesn't, we create the directory
        print(f"\nCreating directory at :::{pdf_storage_directory}::: to store pdf \n")
        os.makedirs(pdf_storage_directory)

    file_path = os.path.join(pdf_storage_directory, file_name)

    if os.path.exists(file_path):
       print(f"\n {file_name} already exists at {file_path} \n")
    else:
        print(f"\nNew File ::: {file_name} being saved at {file_path} \n")
        file.save(file_path)
        rag.create_new_rag_model(file_name) # Creates a new RAG Index for the file uploaded in the rag-indexes directory

    # This will always be called 
    data = rag.analyze(file_name)
    print(f"\n\nTHIS WAS THE DATA RETURNED :::{data}\n\n")
    return data

@app.route('/analysis', methods=['POST'])
def analysis():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    if file:
        llm_response = process_file(file)
        try:
            json_object = json.loads(llm_response)
            json_object['paper_title'] = file.filename
            return json_object
        except ValueError:
            return jsonify({'error': 'Could not process PDF'}), 400

# BELOW FUNCTIONS ARE EXAMPLES TO TEST INTEGRATION


def returns_file_name(file):
    file_name = file.filename
    print(f"Processing file: {file_name}")
    return file_name

@app.route('/mock-response', methods=['POST'])
def mock_response():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    if file:
        file_name = returns_file_name(file)
        mock_data = {
            'paper_title': str(file_name),
            'summary': f'File {file_name} processed successfully. This is its summary',
            'benefits': "There are some benefits for the people",
            'concerns': 'This is what is concerning in the bill you uploaded'
        }
        response = jsonify(mock_data)
        return response

if __name__ == '__main__':
    app.run(debug=True)
