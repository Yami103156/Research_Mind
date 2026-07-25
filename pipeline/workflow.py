from rich.console import Console

from agents.planner import generate_research_plan
from agents.search import execute_search_plan
from agents.reader import read_search_results
from agents.writer import generate_report
from agents.critic import review_report

from utils.parser import extract_score

console = Console()


def run_research_pipeline(topic: str):

    state = {
        "topic": topic
    }

    console.rule("[bold green]PLANNER[/bold green]")

    plan = generate_research_plan(topic)

    state["plan"] = plan

    console.rule("[bold green]SEARCH[/bold green]")

    search_results = execute_search_plan(plan)

    state["search_results"] = search_results

    console.rule("[bold green]READER[/bold green]")

    documents = read_search_results(search_results)

    state["documents"] = documents

    console.rule("[bold green]WRITER[/bold green]")

    report = generate_report(
        topic,
        documents,
    )

    state["report"] = report

    console.rule("[bold green]CRITIC[/bold green]")

    feedback = review_report(
        topic,
        report,
    )

    score = extract_score(feedback)

    state["feedback"] = feedback

    state["score"] = score

    if score < 8:

        console.rule(
            "[bold yellow]AUTO IMPROVEMENT[/bold yellow]"
        )

        report = generate_report(
            topic,
            documents,
            previous_feedback=feedback,
        )

        feedback = review_report(
            topic,
            report,
        )

        score = extract_score(
            feedback
        )

        state["report"] = report

        state["feedback"] = feedback

        state["score"] = score

    return state