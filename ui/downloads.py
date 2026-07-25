import streamlit as st

def download_buttons(report, feedback):

    col1, col2 = st.columns(2)

    with col1:

        st.download_button(

            "Download Report",

            report,

            "report.md"

        )

    with col2:

        st.download_button(

            "Download Feedback",

            feedback,

            "feedback.txt"

        )