import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from utils.data_loader import load_prices, load_price_adoption
from utils.navigation import show_navigation

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(page_title="Price Revolution", layout="wide",
                   initial_sidebar_state="collapsed")

st.markdown("""
    <style>
        [data-testid="stSidebar"] {display: none;}
        .metric-card {
            background: #FDF6EC;
            border: 1px solid #F0D9B5;
            border-radius: 8px;
            padding: 20px;
            margin: 4px;
        }
        .metric-value { font-size: 2.2rem; font-weight: 700; color: #E8721C; }
        .metric-label { font-size: 0.85rem; color: #666; }
        .metric-sub   { font-size: 0.8rem;  color: #999; margin-top: 4px; }
    </style>
""", unsafe_allow_html=True)

show_navigation(current=1, total=6)

# ── Header ───────────────────────────────────────────────────────────────────
st.markdown("### 1 &nbsp; THE PRICE REVOLUTION")
st.markdown("## Solar is now the cheapest electricity source on earth")
st.markdown(
    "PV module prices collapsed **99.8%** since 1975 — from \$128/W to \$0.26/W. "
    "The cost barrier is gone. Market expansion now depends on policy, infrastructure, and financing."
)

# ── Metric Cards ─────────────────────────────────────────────────────────────
c1, c2, c3, c4 = st.columns(4)
with c1:
    st.markdown("""<div class='metric-card'>
        <div class='metric-label'>Price decline</div>
        <div class='metric-value'>99.8%</div>
        <div class='metric-sub'>Since 1975</div>
    </div>""", unsafe_allow_html=True)
with c2:
    st.markdown("""<div class='metric-card'>
        <div class='metric-label'>Current price</div>
        <div class='metric-value' style='color:#1A1A1A'>$0.26/W</div>
        <div class='metric-sub'>2024 module cost</div>
    </div>""", unsafe_allow_html=True)
with c3:
    st.markdown("""<div class='metric-card'>
        <div class='metric-label'>Global generation</div>
        <div class='metric-value'>2,094 TWh</div>
        <div class='metric-sub'>2024, up 12× since 2015</div>
    </div>""", unsafe_allow_html=True)
with c4:
    st.markdown("""<div class='metric-card'>
        <div class='metric-label'>Annual additions</div>
        <div class='metric-value' style='color:#1A1A1A'>200+ GW</div>
        <div class='metric-sub'>Per year since 2022</div>
    </div>""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ── Chart 1: Price (log scale) ────────────────────────────────────────────────
prices = load_prices()
st.markdown("**Solar PV module price (log scale)**")
fig1 = go.Figure()
fig1.add_trace(go.Scatter(
    x=prices["year"], y=prices["pv_module_cost_usd_per_w"],
    mode="lines+markers",
    line=dict(color="#CC4400", width=2.5),
    marker=dict(size=6, color="#CC4400"),
    fill="tozeroy", fillcolor="rgba(232,114,28,0.1)",
    name="$/Watt"
))
fig1.update_layout(
    yaxis_type="log",
    yaxis=dict(
        tickvals=[0.3, 0.5, 1, 2, 5, 10, 30, 50, 100, 128],
        ticktext=["$0.3", "$0.5", "$1", "$2", "$5", "$10", "$30", "$50", "$100", "$128"],
        title="$/Watt (log scale)",
        gridcolor="#F0F0F0",),
    yaxis_title="$/Watt (log scale)",
    xaxis_title="",
    template="plotly_white",
    height=350,
    margin=dict(l=40, r=20, t=10, b=40),
    showlegend=False
)
fig1.add_vrect(
    x0=2008, x1=2024,
    fillcolor="rgba(232,114,28,0.06)",
    layer="below",
    line_width=0,
    annotation_text="Major cost decline era",
    annotation_position="top left",
    annotation_font=dict(color="#E8721C", size=10)
)
st.plotly_chart(fig1, use_container_width=True)

# ── Chart 2: Global generation ────────────────────────────────────────────────
adoption = load_price_adoption()
st.markdown("**Global solar electricity generation (TWh)**")
fig2 = go.Figure()
fig2.add_trace(go.Scatter(
    x=adoption["year"], y=adoption["solar_electricity"],
    mode="lines+markers",
    line=dict(color="#E8A020", width=2.5),
    marker=dict(size=7, color="#E8A020"),
    fill="tozeroy", fillcolor="rgba(232,160,32,0.12)",
    name="TWh"
))
fig2.update_layout(
    yaxis_title="TWh generated",
    xaxis_title="",
    template="plotly_white",
    height=350,
    margin=dict(l=40, r=20, t=10, b=40),
    showlegend=False
)
st.plotly_chart(fig2, use_container_width=True)