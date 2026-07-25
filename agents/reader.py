from langchain.agents import create_agent

from config.model import llm

from tools.scraper import scrape_url

def build_reader_agent():

    return create_agent(

        model=llm,

        tools=[

            scrape_url

        ]

    )