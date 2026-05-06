import streamlit as st
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from utils.navigation import show_navigation

st.set_page_config(page_title="Recommendation", layout="wide",
                   initial_sidebar_state="collapsed")
st.markdown("<style>[data-testid='stSidebar']{display:none;}</style>",
            unsafe_allow_html=True)

show_navigation(current=6, total=6)

st.markdown("### 6 &nbsp; THE DECISION")
st.markdown("## The time to act is now")
st.markdown(
    "Solar is the cheapest electricity source in history. The markets are opening. "
    "Canadian Solar has the track record. The only question is: **which markets first?**"
)

st.markdown("<br>", unsafe_allow_html=True)

# Recommendation cards
countries = [
    {"flag": "🇸🇦", "name": "Saudi Arabia", "rank": "1",
     "why": "Highest PVOUT in the world, +108% CAGR, Vision 2030 government backing",
     "score": "0.672"},
    {"flag": "🇪🇬", "name": "Egypt",         "rank": "2",
     "why": "Massive demand base, low current share, World Bank investment pipeline",
     "score": "0.528"},
    {"flag": "🇨🇴", "name": "Colombia",      "rank": "3",
     "why": "Strong momentum +90% CAGR, stable governance, growing energy demand",
     "score": "0.515"},
    {"flag": "🇵🇰", "name": "Pakistan",      "rank": "4",
     "why": "10% solar share but +81% CAGR — scale-up phase, high demand growth",
     "score": "0.493"},
]

cols = st.columns(4)
for col, c in zip(cols, countries):
    with col:
        st.markdown(f"""
            <div style='background:#FDF6EC; border:2px solid #F0D9B5;
                        border-radius:12px; padding:24px; text-align:center;'>
                <div style='font-size:3rem;'>{c['flag']}</div>
                <div style='background:#E8721C; color:white; border-radius:20px;
                            padding:2px 14px; display:inline-block; font-size:0.8rem;
                            font-weight:700; margin:8px 0;'>#{c['rank']} Priority</div>
                <h3 style='margin:8px 0; color:#1A1A1A;'>{c['name']}</h3>
                <p style='color:#666; font-size:0.85rem;'>{c['why']}</p>
                <div style='margin-top:12px; font-size:0.8rem; color:#999;'>
                    Opportunity Score: <strong style='color:#E8721C;'>{c['score']}</strong>
                </div>
            </div>
        """, unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# Closing hook
st.markdown("""
    <div style='background:linear-gradient(135deg,#0D1B2A,#1A3A5C);
                border-radius:16px; padding:48px; text-align:center;'>
        <h2 style='color:white; font-size:2rem; margin-bottom:16px;'>
            "The sun is not the constraint.<br>The gap is investment, policy, and infrastructure."
        </h2>
        <p style='color:#E8A020; font-size:1.1rem;'>
            Canadian Solar fills exactly that gap. The time to act is now.
        </p>
    </div>
""", unsafe_allow_html=True)