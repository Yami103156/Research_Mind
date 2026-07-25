import streamlit as st


def timeline():

    st.markdown("## 🤖 Agent Workflow")

    c1, c2, c3, c4, c5 = st.columns(5)

    with c1:

        st.success(

            "🧠 Planner\n\nCompleted"

        )

    with c2:

        st.success(

            "🌐 Search\n\nCompleted"

        )

    with c3:

        st.success(

            "📖 Reader\n\nCompleted"

        )

    with c4:

        st.success(

            "✍ Writer\n\nCompleted"

        )

    with c5:

        st.success(

            "🧐 Critic\n\nCompleted"

        )

    st.divider()