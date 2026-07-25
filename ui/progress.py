import streamlit as st
import time

def progress():

    status = st.status(
        "Research Running...",
        expanded=True
    )

    with status:

        st.write("🧠 Planner Agent")

        time.sleep(.5)

        st.write("🌍 Search Agent")

        time.sleep(.5)

        st.write("📖 Reader Agent")

        time.sleep(.5)

        st.write("✍ Writer Agent")

        time.sleep(.5)

        st.write("🧐 Critic Agent")

        time.sleep(.5)

    status.update(
        label="Completed",
        state="complete"
    )