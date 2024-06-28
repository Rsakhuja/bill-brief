from langchain_core.output_parsers import JsonOutputParser
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_core.prompts import PromptTemplate


rag_prompt_dict = {
    'summary':"Return the summary of the congressional bill provided. Return an objective summary of the bill. Answer in less than 60 words. Explain it in simple terms",
    'concerns':"Return the main concerns of the congressional bill provided. What are the potential implications and down sides of it. Answer in less than 60 words. Explain it in simple terms",
    'benefits':"Return the benefits of the congressional bill provided. Explain the positive impact it will have. Answer in less than 60 words. Explain it in simple terms"
    }
