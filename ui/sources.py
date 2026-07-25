import streamlit as st


def show_sources(documents):
    """
    Display all research sources.
    Compatible with ResearchDocument objects.
    """

    st.subheader("🔗 Sources")

    if not documents:
        st.info("No sources found.")
        return

    for i, doc in enumerate(documents, start=1):

        title = getattr(doc, "title", f"Source {i}")
        url = getattr(doc, "url", "")
        summary = getattr(doc, "summary", "")
        snippet = getattr(doc, "snippet", "")
        content = getattr(doc, "content", "")

        with st.expander(f"{i}. {title}"):

            if url:
                st.markdown(f"**🌐 URL:** {url}")

            if summary:
                st.markdown("**Summary**")
                st.write(summary)

            elif snippet:
                st.markdown("**Snippet**")
                st.write(snippet)

            elif content:
                st.markdown("**Content Preview**")
                st.write(content[:700] + "...")

            else:
                st.info("No preview available.")