import streamlit as st


def info_cards(state):

    st.markdown("## 📊 Research Overview")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            label="📚 Documents",
            value=len(state["documents"])
        )

    with col2:
        st.metric(
            label="⭐ Critic Score",
            value=f"{state['score']:.1f}/10"
        )

    with col3:

        total_results = sum(
            len(search.results)
            for search in state["search_results"]
        )

        st.metric(
            label="🔎 Search Results",
            value=total_results
        )

    with col4:

        topic = state["topic"]

        if len(topic) > 18:
            topic = topic[:18] + "..."

        st.metric(
            label="📝 Topic",
            value=topic
        )

    st.divider()