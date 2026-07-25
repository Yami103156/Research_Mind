from rich.console import Console

from chains.writer_chain import writer_chain

from utils.schemas import ResearchDocument

console = Console()


def build_context(
    documents: list[ResearchDocument],
) -> str:
    """
    Convert ResearchDocument objects into
    one prompt context.
    """

    context = ""

    for document in documents:

        context += f"""
====================================================

Title:
{document.title}

URL:
{document.url}

Content:
{document.content}

"""

    return context


def generate_report(
    topic: str,
    documents: list[ResearchDocument],
    previous_feedback: str = "",
) -> str:
    """
    Generate research report.

    previous_feedback is optional.

    First generation:
        previous_feedback=""

    Regeneration:
        previous_feedback=<critic feedback>
    """

    console.rule("[bold cyan]WRITER AGENT[/bold cyan]")

    if previous_feedback.strip():

        console.print(
            "[yellow]Improving report using critic feedback...[/yellow]"
        )

    else:

        console.print(
            "[yellow]Generating first report...[/yellow]"
        )

    context = build_context(documents)

    report = writer_chain.invoke(
        {
            "topic": topic,
            "documents": context,
            "feedback": previous_feedback,
        }
    )

    console.print(
        "[green]✓ Report Generated[/green]"
    )

    return report