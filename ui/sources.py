import streamlit as st


def show_sources(documents):

    st.markdown("## 🌐 Research Sources")

    for document in documents:

        with st.expander(f"🔎 {document.query}"):

            for result in document.results:

                st.markdown(
                    f"""
### {result.title}

{result.snippet}

🔗 {result.url}

---
"""
                )