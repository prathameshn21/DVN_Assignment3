import streamlit as st
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from utils.navigation import show_navigation


st.set_page_config(page_title="Chasing The Sun", layout="wide",
                   initial_sidebar_state="collapsed")

st.markdown("""
    <style>
        [data-testid="stSidebar"] {display: none;}
        [data-testid="stAppViewContainer"] {
            background-color: #0D1B2A;
        }
        [data-testid="stHeader"] {
            background-color: #0D1B2A;
        }
    </style>
""", unsafe_allow_html=True)

show_navigation(current=2, total=6)

# Dark hero section
st.markdown("""
    <div style='background: linear-gradient(135deg, #0D1B2A 0%, #1A3A5C 100%);
                border-radius: 16px; padding: 80px 60px; text-align: center; margin: 20px 0;'>
        <p style='color:#E8A020; font-size:1rem; letter-spacing:3px; margin-bottom:12px;'>
            CANADIAN SOLAR STRATEGIC BRIEF — 2025
        </p>
        <h1 style='color:white; font-size:3.5rem; font-weight:800; margin:0;'>
            Chasing the Sun
        </h1>
        <p style='color:#aaa; font-size:1.3rem; margin-top:20px; max-width:600px; margin-left:auto; margin-right:auto;'>
            The cost barrier has been eliminated. The opportunity is now.
            Where should Canadian Solar expand next?
        </p>
        <div style='margin-top:40px;'>
            <span style='background:#E8721C; color:white; padding:14px 36px;
                         border-radius:30px; font-weight:700; font-size:1.1rem;'>
                ☀️ Chasing the Bright Future of Solar
            </span>
        </div>
    </div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Three pillars
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("""
        <div style='background:#FDF6EC; border-radius:12px; padding:28px; text-align:center;'>
            <div style='font-size:2rem;'>💰</div>
            <h4 style='color:#E8721C;'>Price</h4>
            <p style='color:#555; font-size:0.9rem;'>
                Solar is now the cheapest electricity source in 85% of the world
            </p>
        </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown("""
        <div style='background:#FDF6EC; border-radius:12px; padding:28px; text-align:center;'>
            <div style='font-size:2rem;'>🌍</div>
            <h4 style='color:#E8721C;'>Opportunity</h4>
            <p style='color:#555; font-size:0.9rem;'>
                MENA and Latin America have the sun but not the solar — the gap is the opportunity
            </p>
        </div>
    """, unsafe_allow_html=True)
with col3:
    st.markdown("""
        <div style='background:#FDF6EC; border-radius:12px; padding:28px; text-align:center;'>
            <div style='font-size:2rem;'>🏗️</div>
            <h4 style='color:#E8721C;'>Proven Track Record</h4>
            <p style='color:#555; font-size:0.9rem;'>
                Canadian Solar has deployed utility-scale projects across 20+ countries
            </p>
        </div>
    """, unsafe_allow_html=True)