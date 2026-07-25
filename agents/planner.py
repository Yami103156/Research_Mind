from config.model import llm

from prompts.planner_prompt import planner_prompt

from utils.schemas import ResearchPlan


planner_llm = llm.with_structured_output(
    ResearchPlan
)

planner_chain = (
    planner_prompt
    |
    planner_llm
)


def generate_research_plan(
    topic: str
) -> ResearchPlan:
    """
    Generate a structured research plan
    from the user's topic.
    """

    return planner_chain.invoke(
        {
            "topic": topic
        }
    )