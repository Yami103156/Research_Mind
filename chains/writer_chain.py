from langchain_core.output_parsers import StrOutputParser

from prompts.writer_prompt import writer_prompt

from config.model import llm


writer_chain = (

    writer_prompt

    | llm

    | StrOutputParser()

)