from agents.planner import generate_research_plan

from agents.search import execute_search_plan

from agents.reader import read_search_results


topic = "Artificial Intelligence"

plan = generate_research_plan(topic)

search_results = execute_search_plan(plan)

documents = read_search_results(

    search_results

)

print()

print("=" * 80)

print("SCRAPED DOCUMENTS")

print("=" * 80)

for doc in documents:

    print()

    print(doc.title)

    print(doc.url)

    print()

    print(doc.content[:600])

    print()

    print("-" * 80)