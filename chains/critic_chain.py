from langchain_core.output_parsers import StrOutputParser

from config.model import llm

from prompts.critic_prompt import critic_prompt

critic_chain = (

    critic_prompt

    | llm

    | StrOutputParser()

)