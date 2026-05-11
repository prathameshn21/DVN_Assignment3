import streamlit as st
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from utils.navigation import show_navigation

st.set_page_config(page_title="Chasing The Sun", layout="wide",
                   initial_sidebar_state="collapsed")

st.markdown("""
    <style>
        [data-testid="stSidebar"] {display: none;}
        [data-testid="stAppViewContainer"] { background-color: #0D1B2A; }
        [data-testid="stHeader"]           { background-color: #0D1B2A; }
    </style>
""", unsafe_allow_html=True)

show_navigation(current=2, total=6)

# ── Hero Section ──────────────────────────────────────────────────────────────
st.markdown("""
    <div style='background: linear-gradient(135deg, #0D1B2A 0%, #1A3A5C 100%);
                border-radius: 16px; padding: 80px 60px; text-align: center; margin: 20px 0;'>
        <p style='color:#E8A020; font-size:1rem; letter-spacing:3px; margin-bottom:12px;'>
            CANADIAN SOLAR STRATEGIC BRIEF
        </p>
        <h1 style='color:white; font-size:3.5rem; font-weight:800; margin:0;'>
            Chasing the Sun
        </h1>
        <p style='color:#aaa; font-size:1.3rem; margin-top:20px; max-width:600px;
                  margin-left:auto; margin-right:auto;'>
            The hardware cost barrier has been eliminated. The time for utility
            scale solar is now. Where does Canadian Solar go from here?
        </p>
        <div style='margin-top:40px;'>
            <span style='background:#E8721C; color:white; padding:14px 36px;
                         border-radius:30px; font-weight:700; font-size:1.1rem;'>
                Chasing the Bright Future of Solar
            </span>
        </div>
    </div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ── Three Pillars ─────────────────────────────────────────────────────────────
# FIX — Use min-height instead of height:100% so all 3 cards are same height
CARD_STYLE = """
    background:#FDF6EC;
    border-radius:12px;
    padding:28px 32px;
    text-align:left;
    min-height:200px;
"""

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f"""
        <div style='{CARD_STYLE}'>
            <h4 style='color:#E8721C; margin-top:0; margin-bottom:12px;'>
                Price
            </h4>
            <p style='color:#555; font-size:1.05rem; line-height:1.6; margin:0;'>
                Solar is now the cheapest electricity source in 85% of the world
            </p>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
        <div style='{CARD_STYLE}'>
            <h4 style='color:#E8721C; margin-top:0; margin-bottom:12px;'>
                Opportunity
            </h4>
            <p style='color:#555; font-size:1.05rem; line-height:1.6; margin:0;'>
                MENA and Latin America have the sun and the appetite —
                the opportunity is there to take
            </p>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
        <div style='{CARD_STYLE}'>
            <h4 style='color:#E8721C; margin-top:0; margin-bottom:12px;'>
                Proven Track Record
            </h4>
            <p style='color:#555; font-size:1.05rem; line-height:1.6; margin:0;'>
                Canadian Solar has deployed utility-scale projects across 20+ countries
            </p>
        </div>
    """, unsafe_allow_html=True)