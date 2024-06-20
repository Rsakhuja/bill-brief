from dotenv import load_dotenv
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, StorageContext, load_index_from_storage
import os.path
from llm_implementation import prompt

rag_models = {}

def create_rag_model(file_name):
    if file_name in rag_models:
        print("DOES RAG ALREADY EXISTS?")
        return rag_models[file_name]
    
    PERSIST_DIR = f"./storage/{file_name}"
    if not os.path.exists(PERSIST_DIR):
        documents = SimpleDirectoryReader("llm_implementation/data").load_data()
        index = VectorStoreIndex.from_documents(documents)
        index.storage_context.persist(persist_dir=PERSIST_DIR)
    else:
        storage_context = StorageContext.from_defaults(persist_dir=PERSIST_DIR)
        index = load_index_from_storage(storage_context)
    rag_models[file_name] = index
    print("**** RAG MODELS *****")
    print(rag_models)
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
