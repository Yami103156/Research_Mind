import streamlit as st

def info_cards(state):

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric(
            "Sources",
            len(state["documents"])
        )

    with c2:
        st.metric(
            "Critic Score",
            state["score"]
        )

    with c3:
        st.metric(
            "Topic",
            state["topic"]
        )