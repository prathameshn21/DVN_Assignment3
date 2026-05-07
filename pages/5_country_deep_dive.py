import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from utils.data_loader import load_opportunity, load_merged
from utils.navigation import show_navigation

st.set_page_config(page_title="Country Deep Dive", layout="wide",
                   initial_sidebar_state="collapsed")
st.markdown("<style>[data-testid='stSidebar']{display:none;}</style>",
            unsafe_allow_html=True)

show_navigation(current=5, total=6)

st.markdown("### 5 &nbsp; TARGET MARKETS")
st.markdown("## Deep Dive — Each Opportunity Country")

TARGET = ["Saudi Arabia", "Egypt", "Colombia", "Pakistan"]
RISKS  = {
    "Saudi Arabia": "Policy dependency on Vision 2030; grid infrastructure still developing",
    "Egypt":        "Currency risk and subsidy reform uncertainty; strong World Bank backing offsets",
    "Colombia":     "Political transition risk; stable regulatory framework and growing PPAs",
    "Pakistan":     "Grid stability and payment risk; high demand growth makes it hard to ignore",
}

opp    = load_opportunity()
merged = load_merged()

# ADVANCED FEATURE 1: Country selector — updates all visuals below
selected = st.selectbox("Select a target country:", TARGET)
row = opp[opp["country"] == selected].iloc[0]
opp_sorted = opp.sort_values("opportunity_score", ascending=False).reset_index()
rank = opp_sorted[opp_sorted["country"] == selected].index[0] + 1
total_countries = len(opp_sorted)
# Metric row
m1, m2, m3, m4 = st.columns(4)
m1.metric("Solar Share",  f"{row['solar_share_elec']:.1f}%",
          f"Rank #{rank} of {total_countries}")
m2.metric("PVOUT",        f"{row['pvout_kwh_kwp_day']:.2f}",
          "kWh/kWp/day")
m3.metric("5yr CAGR",     f"{row['solar_cagr_5yr']*100:.0f}%",
          "2019–2024")
m4.metric("Installed GW", f"{row['installed_capacity_gw']:.1f} GW",
          "2024")
st.markdown("<br>", unsafe_allow_html=True)
st.info(
    "💡 **Why these 4 countries?** Higher-scoring markets like Oman, Kuwait, "
    "and China were excluded from target recommendations due to market access "
    "constraints — Canadian Solar already has significant China exposure, while "
    "Oman and Kuwait have smaller addressable market sizes relative to "
    "deployment risk."
)

col_left, col_right = st.columns(2)

# YoY trend chart
with col_left:
    ts = merged[merged["country"] == selected].sort_values("year")
    fig_ts = go.Figure()
    fig_ts.add_trace(go.Scatter(
        x=ts["year"], y=ts["solar_electricity"],
        mode="lines+markers",
        line=dict(color="#E8721C", width=2.5),
        marker=dict(size=6),
        fill="tozeroy", fillcolor="rgba(232,114,28,0.1)",
        name="Solar TWh"
    ))
    fig_ts.update_layout(
        title=f"Solar Generation — {selected} (TWh)",
        template="plotly_white", height=320,
        margin=dict(l=40, r=20, t=40, b=40)
    )
    st.plotly_chart(fig_ts, use_container_width=True)

# Solar share trend
with col_right:
    fig_share = go.Figure()
    fig_share.add_trace(go.Bar(
        x=ts[ts["year"] >= 2015]["year"],
        y=ts[ts["year"] >= 2015]["solar_share_elec"],
        marker_color="#E8A020",
        name="Solar Share %"
    ))
    fig_share.update_layout(
        title=f"Solar Share of Electricity — {selected} (%)",
        template="plotly_white", height=320,
        margin=dict(l=40, r=20, t=40, b=40)
    )
    st.plotly_chart(fig_share, use_container_width=True)

# ADVANCED FEATURE 2: What-If Slider
st.markdown("---")
st.markdown("### 📐 What-If Scenario")
st.markdown("How much capacity does Canadian Solar need to deploy to hit a target?")

target_share = st.slider(
    f"If solar reaches X% of electricity in {selected}...",
    min_value=int(row["solar_share_elec"]) + 1,
    max_value=50,
    value=min(20, 50)
)

demand         = row["electricity_demand"] if row["electricity_demand"] > 0 else 100
current_solar  = row["solar_electricity"]
target_twh     = (target_share / 100) * demand
additional_twh = max(target_twh - current_solar, 0)
pvout          = row["pvout_kwh_kwp_day"] if row["pvout_kwh_kwp_day"] > 0 else 4.5
required_gw    = (additional_twh * 1000) / (pvout * 365)

r1, r2, r3 = st.columns(3)
r1.metric("Additional Generation Needed", f"{additional_twh:.1f} TWh")
r2.metric("New Capacity Required",        f"{required_gw:.1f} GW")
r3.metric("Target Solar Share",           f"{target_share}%")

st.success(
    f"To reach **{target_share}% solar share** in {selected}, Canadian Solar would need to deploy "
    f"approximately **{required_gw:.1f} GW** of new capacity — generating an additional "
    f"**{additional_twh:.1f} TWh** per year."
)

# Risk flag
st.markdown("---")
st.markdown("**⚠️ Key Risks & Considerations**")
st.warning(RISKS[selected])