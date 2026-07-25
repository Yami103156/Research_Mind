import streamlit as st


def footer():

    st.divider()

    st.markdown(
        """
<div style="text-align:center;padding:25px;color:#999;font-size:14px;">

Built with ❤️ using

LangChain • Gemini  • Streamlit

<br><br>

ResearchMind AI © 2026

</div>
""",
        unsafe_allow_html=True
    )