from rich.console import Console
from tenacity import retry, stop_after_attempt, wait_fixed

from tools.search_tool import web_search

from utils.schemas import (
    ResearchPlan,
    SearchResult,
    SearchItem,
)

console = Console()


@retry(
    stop=stop_after_attempt(3),
    wait=wait_fixed(2),
)
def search_query(query: str):
    """
    Execute one Tavily search.
    """
    return web_search.invoke(
        {
            "query": query
        }
    )


def execute_search_plan(
    plan: ResearchPlan,
) -> list[SearchResult]:

    outputs = []

    total = len(plan.queries)

    console.rule("[bold cyan]SEARCH AGENT[/bold cyan]")

    for index, query in enumerate(
        plan.queries,
        start=1,
    ):

        console.print(
            f"[yellow]{index}/{total}[/yellow] {query}"
        )

        try:

            response = search_query(query)

            items = []

            for result in response["results"]:

                items.append(

                    SearchItem(

                        title=result["title"],

                        url=result["url"],

                        snippet=result["content"]

                    )

                )

            outputs.append(

                SearchResult(

                    query=query,

                    results=items

                )

            )

            console.print(
                "[green]✓ Success[/green]"
            )

        except Exception as e:

            console.print(
                f"[red]Error:[/red] {e}"
            )

    return outputs