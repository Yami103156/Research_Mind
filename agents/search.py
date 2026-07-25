from tenacity import retry, stop_after_attempt, wait_fixed
from rich.console import Console

from tools.search_tool import web_search
from utils.schemas import ResearchPlan, SearchResult

console = Console()


@retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
def search_query(query: str) -> str:
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

    results = []

    total = len(plan.queries)

    console.rule("[bold cyan]SEARCH AGENT[/bold cyan]")

    for index, query in enumerate(plan.queries, start=1):

        console.print(
            f"[yellow]({index}/{total})[/yellow] {query}"
        )

        try:

            result = search_query(query)

            results.append(

                SearchResult(

                    query=query,

                    result=result

                )

            )

            console.print(
                "[green]✓ Success[/green]"
            )

        except Exception as e:

            console.print(
                f"[red]✗ Failed[/red] {e}"
            )

    console.rule("[bold green]SEARCH COMPLETED[/bold green]")

    return results