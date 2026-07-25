from langchain.agents import create_agent

from config.model import llm

from tools.search_tool import web_search


def build_search_agent():

    agent = create_agent(

        model=llm,

        tools=[web_search],

    )

    return agent