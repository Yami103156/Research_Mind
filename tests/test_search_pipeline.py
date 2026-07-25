from agents.planner import generate_research_plan
from agents.search import execute_search_plan


def main():

    topic = "Artificial Intelligence"

    plan = generate_research_plan(topic)

    print("\n")
    print("=" * 80)
    print("PLANNER OUTPUT")
    print("=" * 80)

    print(plan)

    print("\n")

    results = execute_search_plan(plan)

    print("\n")
    print("=" * 80)
    print("SEARCH RESULTS")
    print("=" * 80)

    for item in results:

        print()

        print("-" * 80)

        print("QUERY")

        print(item.query)

        print()

        print("RESULT")

        print(item.result)

        print()

        print("-" * 80)


if __name__ == "__main__":
    main()