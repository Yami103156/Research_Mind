from agents.planner import generate_research_plan
from agents.search import execute_search_plan
from agents.reader import read_search_results
from agents.writer import generate_report
from agents.critic import review_report

topic = "Artificial Intelligence"

print("\nGenerating Plan...\n")

plan = generate_research_plan(topic)

search_results = execute_search_plan(plan)

documents = read_search_results(search_results)

report = generate_report(

    topic,

    documents

)

feedback = review_report(

    topic,

    report,

)

print()

print("=" * 80)

print("REPORT")

print("=" * 80)

print(report)

print()

print("=" * 80)

print("CRITIC")

print("=" * 80)

print(feedback)