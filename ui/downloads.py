import streamlit as st


def download_buttons(report, feedback):

    st.markdown("---")

    st.markdown(
        """
        ## 📥 Export Results

        Download your generated research report and AI critic review.
        """
    )

    col1, col2 = st.columns(2)

    with col1:
        st.download_button(
            label="📄 Download Research Report",
            data=report,
            file_name="Research_Report.md",
            mime="text/markdown",
            use_container_width=True,
            type="primary",
        )

    with col2:
        st.download_button(
            label="🧐 Download Critic Review",
            data=feedback,
            file_name="Critic_Review.txt",
            mime="text/plain",
            use_container_width=True,
        )