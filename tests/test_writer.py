from agents.planner import generate_research_plan

from agents.search import execute_search_plan

from agents.reader import read_search_results

from agents.writer import generate_report


topic = "Artificial Intelligence"

plan = generate_research_plan(topic)

search_results = execute_search_plan(plan)

documents = read_search_results(search_results)

report = generate_report(

    topic,

    documents

)

print()

print("=" * 80)

print(report)