import streamlit as st

def metrics(state):

    c1,c2,c3,c4 = st.columns(4)

    c1.metric(
        "Sources",
        len(state.documents)
    )

    c2.metric(
        "Quality",
        f"{state.score:.1f}/10"
    )

    c3.metric(
        "Sections",
        6
    )

    c4.metric(
        "Status",
        "Completed"
    )