import streamlit as st


def sidebar():

    with st.sidebar:

        st.image(
            "https://img.icons8.com/fluency/96/artificial-intelligence.png",
            width=80,
        )

        st.title("ResearchMind AI")

        st.write(
            """
AI Research Assistant

Planner

Search

Reader

Writer

Critic
"""
        )

        st.divider()

        st.success(
            "Powered by Gemini + LangChain"
        )

        st.markdown(
            """
### Tips

• Use detailed topics

• Be specific

• Reports improve automatically
"""
        )

        st.divider()

        st.caption(
            "Version 1.0"
        )