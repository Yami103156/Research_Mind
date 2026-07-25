from langchain.tools import tool
from tavily import TavilyClient
import os
from dotenv import load_dotenv

load_dotenv()

client = TavilyClient(
    api_key=os.getenv("TAVILY_API_KEY")
)


@tool
def web_search(query: str):
    """Search the web using Tavily."""

    return client.search(
        query=query,
        max_results=5,
    )