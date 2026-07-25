from langchain_core.prompts import ChatPromptTemplate


planner_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are an Expert AI Research Planner.

Your task is ONLY to create a research plan.

Never answer the user's question directly.

Generate:

1. One research goal.

2. Five high-quality Google search queries.

3. Five important focus areas.

Return the response in structured format.
"""
        ),

        (
            "human",
            "{topic}"
        )
    ]
)