from dotenv import load_dotenv
from llama_index.core import GPTVectorStoreIndex, SimpleDirectoryReader, StorageContext, load_index_from_storage
import os.path
from llm_implementation import prompt

rag_models = {}

persist_dir = "llm_implementation/storage"

def create_rag_model(file_name):
    documents = SimpleDirectoryReader(input_files=["llm_implementation/data/" + file_name]).load_data()
    index = GPTVectorStoreIndex.from_documents(documents)
    index.storage_context.persist(persist_dir=persist_dir)
    
    return index
            
def analyze(file_name):
    load_dotenv()
    print("FILE NAME::::" + file_name)
    index = create_rag_model(file_name=file_name)
    query_engine = index.as_query_engine()
    response = query_engine.query("Can you give me the summary, main findings, benefits, and concerns of the bill in json format?")
    result = prompt.bill_json_parser.parse(str(response))
    print(result)
    return response
