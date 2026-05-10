import streamlit as st
import plotly.express as px
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from utils.data_loader import load_opportunity
from utils.navigation import show_navigation

st.set_page_config(page_title="Opportunity Map", layout="wide",
                   initial_sidebar_state="collapsed")

st.markdown("""
    <style>
        [data-testid="stSidebar"] {display: none;}
        /* CHANGE 1 — Match page 3 section label style */
        .section-label {
            display: inline-block;
            background: #FDF0E6;
            color: #E8721C;
            border-radius: 20px;
            padding: 6px 18px;
            font-size: 2.2rem;
            font-weight: 700;
            letter-spacing: 1.5px;
            margin-bottom: 12px;
        }
    </style>
""", unsafe_allow_html=True)

show_navigation(current=4, total=6)

st.markdown("<div class='section-label'>THE OPPORTUNITY</div>",
            unsafe_allow_html=True)
st.markdown("""
    <h2 style='font-size:2.2rem; font-weight:800; margin-bottom:16px;'>
        Where should Canadian Solar expand next?
    </h2>
""", unsafe_allow_html=True)

opp = load_opportunity()

# ── ADVANCED FEATURE 1: Context-Aware Filtering ───────────────────────────────
st.markdown("**Filter by metric to recolour the map:**")

METRIC_LABELS = {
    "opportunity_score":  "Overall Opportunity Score",
    "pvout_kwh_kwp_day":  "Solar Resource (PVOUT)",
    "solar_share_elec":   "Current Solar Share (%)",
    "solar_cagr_5yr":     "5-Year Growth Rate (CAGR)",
    "electricity_demand": "Electricity Demand (TWh)",
}

METRIC_AXIS_LABELS = {
    "opportunity_score":  "Opportunity Score",
    "pvout_kwh_kwp_day":  "PVOUT",
    "solar_share_elec":   "Solar Share (%)",
    "solar_cagr_5yr":     "5-Year CAGR",
    "electricity_demand": "Electricity Demand (TWh)",
}

metric = st.selectbox(
    "Colour map by:",
    options=METRIC_LABELS.keys(),
    format_func=lambda x: METRIC_LABELS[x]
)

with st.expander("ℹ️ What do these metrics mean?"):
    st.markdown("""
| Metric | What it means |
|--------|--------------|
| **PVOUT** | Practical solar output — Kilowatt Hours a 1 Kilowatt Peak system produces per day. Higher = better natural conditions |
| **Solar Share (%)** | % of a country's electricity that comes from solar. Low = more room to grow |
| **5yr CAGR** | Compound annual growth rate of solar generation 2019–2024. High = strong momentum & demand |
| **Opportunity Score** | Composite score combining all above metrics + demand + GDP |
""")
    st.markdown("""
---
**Opportunity Score** is a weighted composite:
Solar Resource PVOUT (25%) · Untapped Market Share (25%) ·
Electricity Demand (20%) · 5-yr Growth Rate CAGR (20%) ·
GDP per Capita (10%)
""")

# ── Choropleth Map ────────────────────────────────────────────────────────────
fig_map = px.choropleth(
    opp,
    locations="iso_code",
    color=metric,
    hover_name="country",
    hover_data={
        "solar_share_elec":   ":.1f",
        "pvout_kwh_kwp_day":  ":.2f",
        "solar_cagr_5yr":     ":.1%",
        "opportunity_score":  ":.3f",
        "iso_code":           False,
    },
    labels={
        "solar_share_elec":   "Solar Share %",
        "pvout_kwh_kwp_day":  "PVOUT",
        "solar_cagr_5yr":     "5yr CAGR",
        "opportunity_score":  "Opportunity Score",
        "electricity_demand": "Electricity Demand (TWh)",
    },
    color_continuous_scale=[
        [0.0, "#A8DADC"],
        [0.3, "#70C1B3"],
        [0.5, "#F4D35E"],
        [0.7, "#F28C28"],
        [1.0, "#E8351C"],
    ],
    projection="natural earth",
)
fig_map.update_layout(
    template="plotly_white",
    height=480,
    margin=dict(l=0, r=0, t=10, b=0),
    coloraxis_colorbar=dict(
        title=dict(
            text=METRIC_AXIS_LABELS[metric],
            side="right"
        ),
        tickformat=".2f"
    ),
    geo=dict(
        showframe=False,
        showcoastlines=True,
        coastlinecolor="#DDDDDD",
        showland=True,
        landcolor="#F9F9F9",
        showocean=True,
        oceancolor="#EEF6FF",
    )
)
st.plotly_chart(fig_map, use_container_width=True)

# ── Bar Chart ─────────────────────────────────────────────────────────────────
st.markdown(f"**Top 15 countries by {METRIC_AXIS_LABELS[metric]}**")

top15 = opp.nlargest(15, metric)

fig_bar = px.bar(
    top15.sort_values(metric),
    x=metric,
    y="country",
    orientation="h",
    color=metric,
    color_continuous_scale=[
        [0.0, "#A8DADC"],
        [0.3, "#70C1B3"],
        [0.5, "#F4D35E"],
        [0.7, "#F28C28"],
        [1.0, "#E8351C"],
    ],
    hover_data={
        "solar_share_elec":  ":.1f",
        "pvout_kwh_kwp_day": ":.2f",
        "solar_cagr_5yr":    ":.1%",
    },
    labels={
        metric:              METRIC_AXIS_LABELS[metric],
        "country":           "Country",
        "solar_share_elec":  "Solar Share %",
        "pvout_kwh_kwp_day": "PVOUT",
        "solar_cagr_5yr":    "5yr CAGR",
    },
)
fig_bar.update_layout(
    template="plotly_white",
    height=340,
    showlegend=False,
    # CHANGE 8 — Make axis titles horizontal, capitalise Country
    xaxis=dict(
        title=dict(
            text=METRIC_AXIS_LABELS[metric],
            standoff=10
        ),
        showgrid=True,
        gridcolor="#F5F5F5"
    ),
    yaxis=dict(
        title=dict(
            text="Country",
            standoff=10
        ),
    ),
    margin=dict(l=140, r=20, t=10, b=50),
    coloraxis_showscale=False
)
st.plotly_chart(fig_bar, use_container_width=True)