from agents.planner import generate_research_plan


def main():

    topic = "Large Language Models"

    plan = generate_research_plan(topic)

    print("=" * 60)
    print("RESEARCH GOAL")
    print("=" * 60)

    print(plan.goal)

    print()

    print("=" * 60)
    print("SEARCH QUERIES")
    print("=" * 60)

    for i, query in enumerate(plan.queries, start=1):

        print(f"{i}. {query}")

    print()

    print("=" * 60)
    print("FOCUS AREAS")
    print("=" * 60)

    for area in plan.focus_areas:

        print("-", area)


if __name__ == "__main__":
    main()