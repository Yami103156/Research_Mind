import streamlit as st


def show_report(report):

    st.markdown("## 📄 AI Research Report")

    st.markdown(
        """
<div class="report-card">
""",
        unsafe_allow_html=True,
    )

    st.markdown(report)

    st.markdown(
        """
</div>
""",
        unsafe_allow_html=True,
    )