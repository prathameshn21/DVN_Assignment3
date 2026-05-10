import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from utils.data_loader import load_prices, load_price_adoption
from utils.navigation import show_navigation

# ── Page config ───────────────────────────────────────────────────────────────
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

        .section-label {
            display: inline-block;
            background: #FDF0E6;
            color: #E8721C;
            border-radius: 20px;
            padding: 8px 22px;
            font-size: 2.2rem;
            font-weight: 800;
            letter-spacing: 0px;
            margin-bottom: 12px;
        }
    </style>
""", unsafe_allow_html=True)

show_navigation(current=1, total=6)

# ── Header ────────────────────────────────────────────────────────────────────
# CHANGE 1 — Remove "1", rename, increase size, match page 3 format
# Replace the two heading lines with this:
st.markdown("<div class='section-label'>THE SOLAR PRICE REVOLUTION</div>",
            unsafe_allow_html=True)
st.markdown("""
    <h2 style='font-size:2.2rem; font-weight:800; margin-bottom:10px; line-height:1.1;'>
        Solar is now the cheapest electricity source on earth
    </h2>
""", unsafe_allow_html=True)
st.markdown(
    "PV module prices collapsed **99.8%** since 1975 — from \$128/W to \$0.26/W. "
    "The cost barrier is gone. Market expansion now depends on policy, "
    "infrastructure, and financing."
)

# ── Metric Cards ──────────────────────────────────────────────────────────────
# CHANGE 2 — "Global generation" label should say TWh
c1, c2, c3, c4 = st.columns(4)
with c1:
    st.markdown("""<div class='metric-card'>
        <div class='metric-label'>Price decline</div>
        <div class='metric-value'>99.8%</div>
        <div class='metric-sub'>Since 1975</div>
    </div>""", unsafe_allow_html=True)
with c2:
    # CHANGE 3 — Round to 3 decimal points and add $ sign
    st.markdown("""<div class='metric-card'>
        <div class='metric-label'>Current price</div>
        <div class='metric-value' style='color:#1A1A1A'>$0.258/W</div>
        <div class='metric-sub'>2024 module cost</div>
    </div>""", unsafe_allow_html=True)
with c3:
    # CHANGE 2 — Add TWh label clearly
    st.markdown("""<div class='metric-card'>
        <div class='metric-label'>Global generation</div>
        <div class='metric-value'>2,094 TWh</div>
        <div class='metric-sub'>2024, up 12× since 2015</div>
    </div>""", unsafe_allow_html=True)
with c4:
    st.markdown("""<div class='metric-card'>
        <div class='metric-label'>Annual additions</div>
        <div class='metric-value' style='color:#1A1A1A'>200+ TWh</div>
        <div class='metric-sub'>Per year since 2022</div>
    </div>""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ── Chart 1: Price (log scale) ────────────────────────────────────────────────
prices = load_prices()

# CHANGE 4 — Title without "log scale", Y axis title horizontal as "$ / Watt"
st.markdown("**Solar PV module price**")
fig1 = go.Figure()
fig1.add_trace(go.Scatter(
    x=prices["year"],
    y=prices["pv_module_cost_usd_per_w"],
    mode="lines+markers",
    line=dict(color="#CC4400", width=2.5),
    marker=dict(size=6, color="#CC4400"),
    fill="tozeroy",
    fillcolor="rgba(232,114,28,0.1)",
    name="$/Watt",
    # CHANGE 3 — Tooltip shows $X.XXX format with 3 decimal points
    hovertemplate="<b>%{x}</b><br>Price: $%{y:.3f}/W<extra></extra>"
))
fig1.update_layout(
    yaxis_type="log",
    yaxis=dict(
        # CHANGE 4 — Horizontal title, remove "(log scale)", rename to "$ / Watt"
        title=dict(
            text="$ / Watt",
            standoff=15,
        ),
        tickvals=[0.3, 0.5, 1, 2, 5, 10, 30, 50, 100, 128],
        ticktext=["$0.3", "$0.5", "$1", "$2", "$5", "$10", "$30", "$50", "$100", "$128"],
        gridcolor="#F0F0F0",
    ),
    xaxis_title="",
    template="plotly_white",
    height=350,
    margin=dict(l=60, r=20, t=10, b=40),
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

# ── Chart 2: Global generation + YoY % ───────────────────────────────────────
adoption = load_price_adoption()

# CHANGE 5 — Calculate YoY % change
adoption = adoption.sort_values("year").copy()
adoption["yoy_pct"] = adoption["solar_electricity"].pct_change() * 100

st.markdown("**Global solar electricity generation (TWh)**")

fig2 = go.Figure()

# Primary line — solar generation TWh
fig2.add_trace(go.Scatter(
    x=adoption["year"],
    y=adoption["solar_electricity"],
    mode="lines+markers",
    line=dict(color="#E8A020", width=2.5),
    marker=dict(size=7, color="#E8A020"),
    fill="tozeroy",
    fillcolor="rgba(232,160,32,0.12)",
    name="TWh generated",
    yaxis="y1",
    # CHANGE 5 — Add YoY % to tooltip instead of second axis if cluttered
    hovertemplate=(
        "<b>%{x}</b><br>"
        "Generation: %{y:.0f} TWh<br>"
        "YoY Change: %{customdata:.1f}%<extra></extra>"
    ),
    customdata=adoption["yoy_pct"]
))

# CHANGE 5 — Add YoY % as second line on right axis
fig2.add_trace(go.Scatter(
    x=adoption["year"],
    y=adoption["yoy_pct"],
    mode="lines",
    line=dict(color="#2E86AB", width=1.5, dash="dot"),
    name="YoY Growth %",
    yaxis="y2",
    hovertemplate="<b>%{x}</b><br>YoY Growth: %{y:.1f}%<extra></extra>"
))

fig2.update_layout(
    yaxis=dict(
        title=dict(text="TWh generated", standoff=15),
        gridcolor="#F0F0F0",
    ),
    # Second Y axis on right for YoY %
    yaxis2=dict(
        title=dict(text="YoY Growth %", standoff=15),
        overlaying="y",
        side="right",
        showgrid=False,
        ticksuffix="%",
        range=[-50, 150],
    ),
    xaxis_title="",
    template="plotly_white",
    height=380,
    margin=dict(l=60, r=60, t=10, b=40),
    showlegend=True,
    legend=dict(
        orientation="h",
        yanchor="bottom", y=1.02,
        xanchor="left", x=0
    )
)
st.plotly_chart(fig2, use_container_width=True)