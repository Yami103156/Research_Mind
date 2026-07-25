from rich.console import Console

from tools.scraper import scrape_url

from utils.schemas import (

    SearchResult,

    ResearchDocument,

)

console = Console()

def read_search_results(

    search_results: list[SearchResult],

) -> list[ResearchDocument]:

    documents = []

    console.rule(

        "[bold cyan]READER AGENT[/bold cyan]"

    )

    visited_urls = set()

    for search in search_results:

        for item in search.results:

            if item.url in visited_urls:

                continue

            visited_urls.add(

                item.url

            )

            console.print(

                f"[yellow]Reading[/yellow]"

            )

            console.print(item.url)

            try:

                article = scrape_url.invoke(

                    {

                        "url": item.url

                    }

                )

                documents.append(

                    ResearchDocument(

                        title=item.title,

                        url=item.url,

                        content=article,

                    )

                )

                console.print(

                    "[green]✓ Scraped[/green]"

                )

            except Exception as e:

                console.print(

                    f"[red]{e}[/red]"

                )

    return documents