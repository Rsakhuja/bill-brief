from langchain_core.output_parsers import JsonOutputParser
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_core.prompts import PromptTemplate

class BillAnalysis(BaseModel):
    summary: str = Field(description="what does this bill aim to acheive?")
    benefits: str = Field(description="what are the positive impacts of the bill?")
    concerns: str = Field(description="what are the potential consequences and points of concern this bill brings about?")
    main_findings: str = Field(description="what are the main points of this bill in detail?")

bill_json_parser = JsonOutputParser(pydantic_object=BillAnalysis)

bill_analysis_prompt_template = PromptTemplate(
    template="Answer the query. \n{format_instructions}\n{query}\n",
    input_variables=["query"],
    partial_variables={"format_instructions": bill_json_parser.get_format_instructions()}
)

