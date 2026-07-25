import streamlit as st


def info_cards(state):

    st.markdown("## 📊 Research Overview")

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(

            label="📚 Sources",

            value=len(state["documents"])

        )

    with col2:

        st.metric(

            label="⭐ Critic Score",

            value=f'{state["score"]:.1f}/10'

        )

    with col3:

        total_results = sum(

            len(doc.results)

            for doc in state["documents"]

        )

        st.metric(

            label="🔎 Search Results",

            value=total_results

        )

    with col4:

        st.metric(

            label="📝 Topic",

            value=state["topic"][:18] + "..."

            if len(state["topic"]) > 18

            else state["topic"]

        )

    st.divider()