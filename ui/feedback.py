import streamlit as st


def show_feedback(feedback, score):

    st.markdown("## 🧐 Critic Review")

    if score >= 9:

        st.success(f"Excellent Report • Score: {score:.1f}/10")

    elif score >= 8:

        st.info(f"Good Report • Score: {score:.1f}/10")

    elif score >= 6:

        st.warning(f"Needs Improvement • Score: {score:.1f}/10")

    else:

        st.error(f"Poor Report • Score: {score:.1f}/10")

    st.markdown(feedback)