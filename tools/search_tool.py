import os

from dotenv import load_dotenv
from tavily import TavilyClient
from langchain.tools import tool

load_dotenv()

client = TavilyClient(
    api_key=os.getenv("TAVILY_API_KEY")
)


@tool
def web_search(query: str):
    """
    Search the web using Tavily.
    """

    return client.search(
        query=query,
        max_results=5,
    )