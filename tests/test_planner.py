from agents.planner import generate_research_plan


def main():

    topic = "Artificial Intelligence"

    plan = generate_research_plan(topic)

    print()

    print("=" * 80)

    print("PLANNER OUTPUT")

    print("=" * 80)

    print()

    print(plan)

    print()

    print("=" * 80)

    print("Goal")

    print(plan.goal)

    print()

    print("=" * 80)

    print("Queries")

    for q in plan.queries:

        print("-", q)

    print()

    print("=" * 80)

    print("Focus Areas")

    for area in plan.focus_areas:

        print("-", area)


if __name__ == "__main__":

    main()