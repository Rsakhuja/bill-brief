from flask import Flask, request, jsonify
from flask_cors import CORS
import time
import os
from utils.utils import directory_exist
from llm_implementation import rag
import json
from twitter_post import x

app = Flask(__name__)
CORS(app, origins='http://localhost:3000')

def process_file_from_frontend(file):
    file_name = file.filename 
    if not directory_exist(file):  
        rag.create_new_rag_model(file_name) # Creates a new RAG Index for the file uploaded in the rag-indexes directory

    data = rag.analyze_from_rag(file_name)
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
        llm_response = process_file_from_frontend(file)
        post_to_twitter = input("Do you want to post to Twitter? (yes/no): ").strip().lower()

        if post_to_twitter == 'yes':
            tweet_id = x.post_to_twitter(file_name=file.filename, llm_response=llm_response)
            print(f"\n\nPosted to Twitter with tweet id {tweet_id}.\n\n")
        else:
            print("\n\nNot posted to Twitter. Simply will show to frontend \n\n")

        try:
            json_object = json.dumps(llm_response)
            return json_object
        except ValueError:
            return jsonify({'error': 'Could not process PDF'}), 400

if __name__ == '__main__':
    app.run(debug=True)
