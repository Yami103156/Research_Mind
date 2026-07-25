from rich.console import Console

from chains.critic_chain import critic_chain

console = Console()

def review_report(

    topic: str,

    report: str,

):

    console.rule(

        "[bold cyan]CRITIC AGENT[/bold cyan]"

    )

    console.print(

        "[yellow]Reviewing Report...[/yellow]"

    )

    feedback = critic_chain.invoke(

        {

            "topic": topic,

            "report": report,

        }

    )

    console.print(

        "[green]✓ Review Complete[/green]"

    )

    return feedback