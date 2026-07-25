from pipeline.workflow import run_research_pipeline

topic = "Artificial Intelligence"

state = run_research_pipeline(topic)

print("\n")

print("=" * 80)

print("FINAL SCORE")

print("=" * 80)

print(state["score"])

print("\n")

print("=" * 80)

print("FINAL REPORT")

print("=" * 80)

print(state["report"])

print("\n")

print("=" * 80)

print("CRITIC")

print("=" * 80)

print(state["feedback"])