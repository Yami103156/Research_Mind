from agents.planner import generate_research_plan

from agents.search import execute_search_plan


topic = "Artificial Intelligence"

plan = generate_research_plan(topic)

results = execute_search_plan(plan)

print()

print("=" * 80)

print("SEARCH OUTPUT")

print("=" * 80)

for search in results:

    print()

    print(search.query)

    print()

    for item in search.results:

        print(item.title)

        print(item.url)

        print(item.snippet[:200])

        print()