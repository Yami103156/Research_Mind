import streamlit as st


def hero():

    st.markdown(
        """
        <div style="text-align:center;padding:25px">

        <h1 style="
        font-size:48px;
        background:linear-gradient(90deg,#4F46E5,#06B6D4);
        -webkit-background-clip:text;
        -webkit-text-fill-color:transparent;
        ">

        🔬 ResearchMind AI

        </h1>

        <p style="font-size:20px;color:#9CA3AF">

        Autonomous Multi-Agent Research Assistant

        </p>

        </div>

        """,
        unsafe_allow_html=True,
    )