import streamlit as st

from pipeline import state

def show_sources(documents):

    st.subheader("Sources")

    for doc in documents:

        with st.expander(doc.query):

            for result in doc.results:

                st.markdown(
                    f"### {result.title}"
                )

                st.write(result.snippet)

                st.link_button(
                    "Open",
                    result.url
                )
    show_sources(state["documents"])