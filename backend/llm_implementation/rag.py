from dotenv import load_dotenv
from llama_index.core import get_response_synthesizer, GPTVectorStoreIndex, SimpleDirectoryReader, StorageContext, load_index_from_storage
from llama_index.core.retrievers import VectorIndexRetriever
from llama_index.core.query_engine import RetrieverQueryEngine
import os.path
from llm_implementation.prompt import rag_prompt_dict
import time



def create_new_rag_model(file_name):

    documents = SimpleDirectoryReader(f"llm_implementation/data/{file_name}/").load_data()
    index = GPTVectorStoreIndex.from_documents(documents)
    persist_dir = f"llm_implementation/rag-indexes/{file_name}/"
    if not os.path.exists(persist_dir):
        print(f"\n::: CREATING RAG INDEX FOR {file_name} in the DIR {persist_dir} ::: \n")
        os.makedirs(persist_dir)
    index.storage_context.persist(persist_dir=persist_dir)
    return True




def analyze_from_rag(file_name):
    load_dotenv()
    INDEX_DIRECTORY = f"llm_implementation/rag-indexes/{file_name}/"

    storage_context = StorageContext.from_defaults(persist_dir=INDEX_DIRECTORY)
    index = load_index_from_storage(storage_context)
    retriever = VectorIndexRetriever(index=index,similarity_top_k=3,)
    response_synthesizer = get_response_synthesizer(response_mode="tree_summarize",)

    query_engine = RetrieverQueryEngine(
            retriever=retriever,
            response_synthesizer=response_synthesizer,
        )
    
    json_dict = {"paper_title":file_name}

    for key, prompt in rag_prompt_dict.items():
        response = query_engine.query(prompt)
        print(f"\n\n QUERY RESPONSE FROM THE LLM for {key} and {prompt}  ::: {response}")
        response = str(response)
        json_dict[key] = response
        time.sleep(1)

    return json_dict
