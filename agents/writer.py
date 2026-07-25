from rich.console import Console

from chains.writer_chain import writer_chain

from utils.schemas import ResearchDocument

console = Console()

def build_context(

    documents: list[ResearchDocument]

):

    context = ""

    for doc in documents:

        context += f"""

Title:
{doc.title}

URL:
{doc.url}

Content:
{doc.content}

=========================================
"""

    return context

def generate_report(

    topic: str,

    documents: list[ResearchDocument]

):

    console.rule("[bold cyan]WRITER AGENT[/bold cyan]")

    console.print(

        "[yellow]Generating Report...[/yellow]"

    )

    context = build_context(

        documents

    )

    report = writer_chain.invoke(

        {

            "topic": topic,

            "documents": context

        }

    )

    console.print(

        "[green]✓ Report Generated[/green]"

    )

    return report