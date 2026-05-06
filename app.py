import streamlit as st

st.set_page_config(
    page_title="Chasing the Sun — Canadian Solar",
    page_icon="☀️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Hide default sidebar & Streamlit branding
st.markdown("""
    <style>
        [data-testid="stSidebar"] {display: none;}
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

st.switch_page("pages/1_price_revolution.py")