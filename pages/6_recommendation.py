import streamlit as st
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from utils.navigation import show_navigation

st.set_page_config(page_title="Recommendation", layout="wide",
                   initial_sidebar_state="collapsed")

st.markdown("""
    <style>
        [data-testid="stSidebar"] {display: none;}
        .section-label {
            display: inline-block;
            background: #FDF0E6;
            color: #E8721C;
            border-radius: 20px;
            padding: 6px 18px;
            font-size: 2.2rem;
            font-weight: 800;
            letter-spacing: 1.5px;
            margin-bottom: 12px;
        }
    </style>
""", unsafe_allow_html=True)

show_navigation(current=6, total=6)

st.markdown("<div class='section-label'>THE DECISION</div>",
            unsafe_allow_html=True)
st.markdown("""
    <h2 style='font-size:2.2rem; font-weight:800; margin-bottom:8px;'>
        The time to act is now
    </h2>
""", unsafe_allow_html=True)

st.markdown(
    "Solar is the cheapest electricity source in history. The markets are opening. "
    "Canadian Solar has the track record. The only question is: **which markets to pursue?**"
)

st.markdown("<br>", unsafe_allow_html=True)

countries = [
    {
        "iso":   "SA",
        "name":  "Saudi Arabia",
        "rank":  "1",
        "why":   "Highest PVOUT in the world, +108% CAGR, Vision 2030 government backing",
        "score": "0.672"
    },
    {
        "iso":   "EG",
        "name":  "Egypt",
        "rank":  "2",
        "why":   "Massive demand base, low current share, World Bank investment pipeline",
        "score": "0.528"
    },
    {
        "iso":   "CO",
        "name":  "Colombia",
        "rank":  "3",
        "why":   "Strong momentum +90% CAGR, stable governance, growing energy demand",
        "score": "0.515"
    },
    {
        "iso":   "OM",
        "name":  "Oman",
        "rank":  "4",
        "why":   "PVOUT 5.17, +102% CAGR, government-backed renewable expansion",
        "score": "0.632"
    },
    {
        "iso":   "PK",
        "name":  "Pakistan",
        "rank":  "5",
        "why":   "10% solar share but +81% CAGR — scale-up phase, high demand growth",
        "score": "0.493"
    },
]

cols = st.columns(5)
for col, c in zip(cols, countries):
    with col:
        st.markdown(f"""
            <div style='background:#FDF6EC; border:2px solid #F0D9B5;
                        border-radius:12px; padding:24px; text-align:center;
                        min-height:220px;'>
                <div style='font-size:1.6rem; font-weight:800; color:#1A1A1A;
                            letter-spacing:1px; margin-bottom:8px;'>
                    {c['name']}
                </div>
                <div style='background:#E8721C; color:white; border-radius:20px;
                            padding:2px 14px; display:inline-block; font-size:0.8rem;
                            font-weight:700; margin:8px 0;'>
                    #{c['rank']} Priority
                </div>
                <p style='color:#666; font-size:0.82rem; line-height:1.5; margin-top:12px;'>
                    {c['why']}
                </p>
                <div style='margin-top:12px; font-size:0.85rem; color:#999;'>
                    Opportunity Score:
                    <strong style='color:#E8721C;'>{c['score']}</strong>
                </div>
            </div>
        """, unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# ── Closing Hook ──────────────────────────────────────────────────────────────
st.markdown(f"""
    <div style='background:linear-gradient(135deg,#0D1B2A,#1A3A5C);
                border-radius:16px; padding:48px; text-align:center;'>
        <h2 style='color:white; font-size:2rem; margin-bottom:16px;'>
            "The sun is not the constraint.<br>
            The gap is investment, policy, and infrastructure."
        </h2>
        <p style='color:#E8A020; font-size:1.1rem; margin-bottom:24px;'>
            Canadian Solar fills exactly that gap. The time to act is now.
        </p>
        <div style='background:rgba(232,114,28,0.15); border:1px solid #E8721C;
                    border-radius:10px; padding:16px 24px;
                    display:inline-block; margin-top:8px;'>
            <span style='color:#E8A020; font-size:1.05rem; font-weight:700;'>
                Every day we wait is opportunity for competitors.<br>
                <span style='font-size:0.9rem; font-weight:400; color:#ddd;'>
                    Saudi Arabia's CAGR is +108%.
                    Every quarter of inaction is market share conceded.
                </span>
            </span>
        </div>
    </div>
""", unsafe_allow_html=True)