import streamlit as st

from pipeline.workflow import run_research_pipeline

from ui.sidebar import sidebar
from ui.cards import info_cards
from ui.timeline import timeline
from ui.report import show_report
from ui.sources import show_sources
from ui.feedback import show_feedback
from ui.downloads import download_buttons
from ui.footer import footer

############################################################

st.set_page_config(
    page_title="ResearchMind AI",
    page_icon="🧠",
    layout="wide",
)

############################################################

with open("assets/style.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True,
    )

############################################################

sidebar()

############################################################

st.markdown(
    """
    <div class='main-title'>
        🧠 ResearchMind AI
    </div>

    <div class='subtitle'>
        Autonomous AI Research Assistant
    </div>
    """,
    unsafe_allow_html=True,
)

############################################################

topic = st.text_input(
    "Research Topic",
    placeholder="Example: Future of Quantum Computing",
    label_visibility="collapsed",
)

############################################################

############################################################

st.markdown("<br>", unsafe_allow_html=True)

generate = st.button(
    "🚀 Generate Research Report",
    use_container_width=True,
    type="primary",
)

if generate:

    if not topic.strip():
        st.warning("Please enter a research topic.")
        st.stop()

    with st.spinner("🤖 Research Agents are working..."):

        state = run_research_pipeline(topic)

    ########################################################

    info_cards(state)

    timeline()

    ########################################################

    tab1, tab2, tab3 = st.tabs(
        [
            "📄 Report",
            "🌐 Sources",
            "🧐 Critic",
        ]
    )

    ########################################################

    with tab1:
        show_report(
            state["report"]
        )

    ########################################################

    with tab2:
        # IMPORTANT: Pass search_results instead of documents
        show_sources(
            state["documents"]
        )

    ########################################################

    with tab3:
        show_feedback(
            state["feedback"],
            state["score"],
        )

    ########################################################

    download_buttons(
        state["report"],
        state["feedback"],
    )

############################################################

footer()