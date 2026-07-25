import streamlit as st

def load_css():
    st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');

html, body, [class*="css"]{
    font-family:Inter,sans-serif;
}

.stApp{
    background:#0B1120;
}

.block-container{
    max-width:1200px;
    padding-top:2rem;
}

.main-title{
    font-size:50px;
    font-weight:700;
    color:white;
}

.subtitle{
    color:#9CA3AF;
    font-size:20px;
}

.metric-card{
    background:#111827;
    padding:18px;
    border-radius:18px;
    border:1px solid #1F2937;
}

.report-card{
    background:#101827;
    border-radius:18px;
    padding:25px;
    margin-top:15px;
}

.gradient-btn button{
    background:linear-gradient(90deg,#2563EB,#7C3AED);
    color:white;
    border-radius:12px;
    height:48px;
    border:none;
}

div[data-testid="stExpander"]{
    border-radius:15px;
    border:1px solid #1F2937;
}

</style>
""", unsafe_allow_html=True)