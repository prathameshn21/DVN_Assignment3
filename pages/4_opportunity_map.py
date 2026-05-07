import streamlit as st
import plotly.express as px
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from utils.data_loader import load_opportunity
from utils.navigation import show_navigation

st.set_page_config(page_title="Opportunity Map", layout="wide",
                   initial_sidebar_state="collapsed")
st.markdown("<style>[data-testid='stSidebar']{display:none;}</style>",
            unsafe_allow_html=True)

show_navigation(current=4, total=6)

st.markdown("### 4 &nbsp; THE OPPORTUNITY")
st.markdown("## Where should Canadian Solar expand next?")

opp = load_opportunity()

# ── ADVANCED FEATURE 1: Context-Aware Filtering ───────────────────────────────
st.markdown("**Filter by metric to recolour the map:**")
metric = st.selectbox(
    "Colour map by:",
    options={
        "opportunity_score":    "Overall Opportunity Score",
        "pvout_kwh_kwp_day":    "Solar Resource (PVOUT)",
        "solar_share_elec":     "Current Solar Share (%)",
        "solar_cagr_5yr":       "5-Year Growth Rate (CAGR)",
        "electricity_demand":   "Electricity Demand (TWh)",
    }.keys(),
    format_func=lambda x: {
        "opportunity_score":    "Overall Opportunity Score",
        "pvout_kwh_kwp_day":    "Solar Resource (PVOUT)",
        "solar_share_elec":     "Current Solar Share (%)",
        "solar_cagr_5yr":       "5-Year Growth Rate (CAGR)",
        "electricity_demand":   "Electricity Demand (TWh)",
    }[x]
)
with st.expander("ℹ️ What do these metrics mean?"):
    st.markdown("""
    | Metric | What it means |
    |--------|--------------|
    | **PVOUT** | Practical solar output — kWh a 1kWp system produces per day. Higher = better natural conditions |
    | **Solar Share (%)** | % of a country's electricity that comes from solar. Low = more room to grow |
    | **5yr CAGR** | Compound annual growth rate of solar generation 2019–2024. High = strong momentum |
    | **Opportunity Score** | Composite score combining all above metrics + demand + GDP |
    """)

# Choropleth map — hover shows full stats (ADVANCED FEATURE 2: Tooltips)
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
    color_continuous_scale=[
    [0.0,  "#A8DADC"],   # light aqua — low score
    [0.3,  "#70C1B3"],   # teal
    [0.5,  "#F4D35E"],   # yellow
    [0.7,  "#F28C28"],   # orange
    [1.0,  "#E8351C"],   # strong red-orange — high score
],

    projection="natural earth",
)
fig_map.update_layout(
    template="plotly_white",
    height=480,
    margin=dict(l=0, r=0, t=10, b=0),
    coloraxis_colorbar=dict(title=metric.replace("_", " ").title())
)
st.plotly_chart(fig_map, use_container_width=True)

# Top 15 bar chart — updates based on same metric filter
st.markdown(f"**Top 15 countries by {metric.replace('_',' ').title()}**")
TARGET = ["Saudi Arabia", "Egypt", "Colombia", "Pakistan"]
top15 = opp.nlargest(15, metric)
top15["is_target"] = top15["country"].isin(TARGET)
fig_bar = px.bar(
    top15.sort_values(metric),
    x=metric, y="country",
    orientation="h",
    color=metric,
    color_continuous_scale=[
    [0.0,  "#A8DADC"],
    [0.3,  "#70C1B3"],
    [0.5,  "#F4D35E"],
    [0.7,  "#F28C28"],
    [1.0,  "#E8351C"],
],
    hover_data=["solar_share_elec", "pvout_kwh_kwp_day", "solar_cagr_5yr"],
)
fig_bar.update_layout(
    template="plotly_white",
    height=340,
    showlegend=False,
    margin=dict(l=120, r=20, t=10, b=40),
    coloraxis_showscale=False
)
st.plotly_chart(fig_bar, use_container_width=True)
st.markdown("""
    <div style='font-size:0.78rem; color:#999; margin-top:-16px; 
                margin-bottom:24px; padding-left:4px;'>
        ℹ️ &nbsp; <strong>Opportunity Score</strong> is a weighted composite: 
        Solar Resource PVOUT (25%) · Untapped Market Share (25%) · 
        Electricity Demand (20%) · 5-yr Growth Rate CAGR (20%) · 
        GDP per Capita (10%)
    </div>
""", unsafe_allow_html=True)