from dotenv import load_dotenv
from llama_index.core import GPTVectorStoreIndex, SimpleDirectoryReader, StorageContext, load_index_from_storage
import os.path
from llm_implementation import prompt

rag_models = {}

def create_new_rag_model(file_name):

    documents = SimpleDirectoryReader(f"llm_implementation/data/{file_name}/").load_data()

    print(f":::THIS IS DOCUMENTS::: {documents}")
    index = GPTVectorStoreIndex.from_documents(documents)
    persist_dir = f"llm_implementation/rag-indexes/{file_name}/"

    if not os.path.exists(persist_dir):
        print(f"\n::: CREATING RAG INDEX FOR {file_name} in the DIR {persist_dir} ::: \n")
        os.makedirs(persist_dir)
    index.storage_context.persist(persist_dir=persist_dir)
    
    return "RAG Index successfully created"
            
def analyze(file_name):
    load_dotenv()
    INDEX_DIRECTORY = f"llm_implementation/rag-indexes/{file_name}/"

    storage_context = StorageContext.from_defaults(persist_dir=INDEX_DIRECTORY)
    index = load_index_from_storage(storage_context)
    query_engine = index.as_query_engine()

    index_query = "You will be given a Congressional Bill. Analyse the Bill and give me the summary, concerns and benefits."
    print("THIS IS THE PROMPT :::", prompt.bill_analysis_prompt_template.format(query=index_query))
    index_prompt = prompt.bill_analysis_prompt_template.format(query=index_query)

    response = query_engine.query(index_prompt)
    print("\n\n QUERY RESPONSE FROM THE LLM  :::", response)
    print("THIS IS THE TYPE OF THE RESPONSE", type(response))

    response = str(response)

    print("THIS IS THE TYPE OF THE RESPONSE", type(response))

    return response
