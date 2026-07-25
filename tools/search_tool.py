from langchain.tools import tool
from tavily import TavilyClient

from config.settings import TAVILY_API_KEY

client = TavilyClient(api_key=TAVILY_API_KEY)


@tool
def web_search(query: str) -> str:
    """
    Search the web for recent and reliable information.
    Returns titles, urls and snippets.
    """

    try:

        results = client.search(
            query=query,
            max_results=5,
            search_depth="advanced",
        )

        output = []

        for item in results["results"]:

            output.append(

                f"""
Title : {item["title"]}

URL : {item["url"]}

Snippet :
{item["content"]}

-------------------------------------
"""
            )

        return "\n".join(output)

    except Exception as e:

        return f"Search Error : {e}"