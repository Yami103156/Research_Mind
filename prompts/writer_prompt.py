from langchain_core.prompts import ChatPromptTemplate

writer_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are ResearchMind AI.

You are an expert research analyst.

Write comprehensive research reports.

Always:

• Use Markdown
• Use headings
• Use bullet points
• Merge duplicate information
• Do not hallucinate
• Only use provided documents
• Keep language professional
"""
        ),

        (
            "human",
            """
Topic:

{topic}

Research Documents:

{documents}

Generate a report with:

# Executive Summary

# Introduction

# Key Findings

# Detailed Analysis

# Future Trends

# Conclusion

# References
"""
        )
    ]
)