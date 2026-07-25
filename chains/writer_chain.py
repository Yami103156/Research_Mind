from langchain_core.output_parsers import StrOutputParser

from config.model import llm

from prompts.writer_prompt import writer_prompt


writer_chain = (

    writer_prompt

    | llm

    | StrOutputParser()

)