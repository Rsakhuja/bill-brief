from langchain_core.output_parsers import JsonOutputParser
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_core.prompts import PromptTemplate


rag_prompt_dict = {
    'summary':"Return the summary of the congressional bill provided. Return an objective summary of the bill. Answer in less than 60 words. Explain it in simple terms",
    'concerns':"Return the main concerns of the congressional bill provided. What are the potential implications and down sides of it. Answer in less than 60 words. Explain it in simple terms",
    'benefits':"Return the benefits of the congressional bill provided. Explain the positive impact it will have. Answer in less than 60 words. Explain it in simple terms"
    }

# Will not be using these any more. Will be querying for individual context items from the RAG

class BillAnalysis(BaseModel):
    summary: str = Field(description="what does this bill aim to acheive?")
    benefits: str = Field(description="what are the positive impacts of the bill?")
    concerns: str = Field(description="what are the potential consequences and points of concern this bill brings about?")
    main_findings: str = Field(description="what are the main points of this bill in detail?")

bill_json_parser = JsonOutputParser(pydantic_object=BillAnalysis)

bill_analysis_prompt_template = PromptTemplate(
    template="Answer the query \n{query} \n\n These are the format instruction \n\n {format_instructions} \n",
    input_variables=["query"],
    partial_variables={"format_instructions": bill_json_parser.get_format_instructions()}
)

