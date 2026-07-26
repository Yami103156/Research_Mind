import streamlit as st


def show_sources(documents):

    st.subheader("🔗 Research Sources")

    if not documents:
        st.warning("No sources found.")
        return

    st.success(f"Found {len(documents)} sources")

    for i, doc in enumerate(documents, start=1):

        with st.expander(f"📄 {i}. {doc.title}"):

            st.markdown(
                f"**🌐 URL:** [{doc.url}]({doc.url})"
            )

            st.markdown("---")

            preview = doc.content[:1000]

            st.write(preview)

            if len(doc.content) > 1000:
                st.caption("Showing first 1000 characters...")