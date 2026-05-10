import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from utils.data_loader import load_opportunity, load_merged
from utils.navigation import show_navigation

st.set_page_config(page_title="Country Deep Dive", layout="wide",
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
        .strengths-box {
            background: #F0FAF4;
            border-left: 4px solid #27AE60;
            border-radius: 0 8px 8px 0;
            padding: 16px 20px;
        }
        .risks-box {
            background: #FFF3F0;
            border-left: 4px solid #E74C3C;
            border-radius: 0 8px 8px 0;
            padding: 16px 20px;
        }
        .considerations-box {
            background: #FDF6EC;
            border-left: 4px solid #E8A020;
            border-radius: 0 8px 8px 0;
            padding: 16px 20px;
        }
        .section-title {
            font-size: 0.78rem;
            font-weight: 700;
            letter-spacing: 1.5px;
            margin-bottom: 10px;
        }
        .bullet-item {
            font-size: 0.9rem;
            color: #444;
            margin-bottom: 4px;
            line-height: 1.5;
        }
    </style>
""", unsafe_allow_html=True)

show_navigation(current=5, total=6)

st.markdown("<div class='section-label'>TARGET MARKETS</div>",
            unsafe_allow_html=True)
st.markdown("""
    <h2 style='font-size:2.2rem; font-weight:800; margin-bottom:16px;'>
        Deep Dive — Each Opportunity Country
    </h2>
""", unsafe_allow_html=True)

TARGET = ["Saudi Arabia", "Egypt", "Colombia", "Pakistan", "Oman"]

COUNTRY_DETAILS = {
    "Saudi Arabia": {
        "strengths": [
            "Vision 2030 policy tailwind",
            "Aramco-certified suppliers",
            "Structured procurement via ACWA Power",
            "Exceptional solar irradiance",
        ],
        "risks": [
            "40% local content requirement",
            "Government-controlled market access",
            "Competition from Chinese JVs",
        ],
        "considerations": (
            "Canadian Solar is already a certified Aramco supplier. "
            "First solar panels for KAPSARC project. Active bidder on new tenders."
        ),
    },
    "Egypt": {
        "strengths": [
            "Large addressable electricity demand",
            "World Bank & IFC investment pipeline",
            "Strong solar irradiance (PVOUT 5.25)",
            "Government renewable energy targets",
        ],
        "risks": [
            "Currency risk and FX repatriation",
            "Subsidy reform uncertainty",
            "Grid infrastructure gaps",
        ],
        "considerations": (
            "Egypt's Benban Solar Park is one of the world's largest. "
            "Canadian Solar has prior regional presence via North Africa projects."
        ),
    },
    "Colombia": {
        "strengths": [
            "Stable regulatory framework",
            "Growing PPAs from private sector",
            "Strong 5yr CAGR momentum (+90%)",
            "Open to foreign investment",
        ],
        "risks": [
            "Political transition risk",
            "Grid integration challenges in rural areas",
            "Smaller market than MENA peers",
        ],
        "considerations": (
            "Colombia is a scale-up market. "
            "Early movers can lock in long-term PPA agreements at favourable rates."
        ),
    },
    "Pakistan": {
        "strengths": [
            "Massive and fast-growing electricity demand",
            "High PVOUT (4.71 kWh/kWp/day)",
            "Strong CAGR momentum (+81%)",
            "Large rural electrification opportunity",
        ],
        "risks": [
            "Grid stability and circular debt issues",
            "Payment risk from state utilities",
            "Political and regulatory uncertainty",
        ],
        "considerations": (
            "Pakistan's energy crisis creates urgent demand. "
            "Canadian Solar has existing regional supply chain via India operations."
        ),
    },
    "Oman": {
        "strengths": [
            "PVOUT 5.17 — exceptional solar resource",
            "Government-backed expansion targets",
            "+102% 5yr CAGR — fastest growing in region",
            "Stable political environment",
        ],
        "risks": [
            "Smaller addressable market than Saudi/Egypt",
            "Heavy government control of energy sector",
            "Limited private sector participation to date",
        ],
        "considerations": (
            "Oman's Vision 2040 includes aggressive renewable targets. "
            "Early entry now establishes track record for larger regional deals."
        ),
    },
}

opp    = load_opportunity()
merged = load_merged()

# ADVANCED FEATURE 1: Country selector
selected = st.selectbox("Select a target country:", TARGET)
row = opp[opp["country"] == selected].iloc[0]

opp_sorted = opp.sort_values("opportunity_score", ascending=False).reset_index(drop=True)
rank = opp_sorted[opp_sorted["country"] == selected].index[0] + 1
total_countries = len(opp_sorted)

# ── Metric Tiles ──────────────────────────────────────────────────────────────
m1, m2, m3, m4 = st.columns(4)

m1.metric(
    "Solar Share",
    f"{row['solar_share_elec']:.1f}%",
    f"Rank #{rank} of {total_countries}"
)
m2.metric(
    "PVOUT",
    f"{row['pvout_kwh_kwp_day']:.2f} kWh/kWp/day",
    f"Rank #{opp_sorted[opp_sorted['country']==selected].index[0]+1} of {total_countries}"
)
m3.metric(
    "5yr CAGR",
    f"{row['solar_cagr_5yr']*100:.0f}% · 2019–2024",
    "Growth rate"
)
m4.metric(
    "Installed GW",
    f"{row['installed_capacity_gw']:.1f} GW · 2024",
    "Installed capacity"
)

st.markdown("<br>", unsafe_allow_html=True)

st.info(
    "**Why these 5 countries?** Higher-scoring markets like Kuwait and China were "
    "excluded from target recommendations due to market access constraints — "
    "Canadian Solar already has significant China exposure, while Kuwait has a "
    "smaller addressable market size relative to deployment risk."
)

# ── Charts ────────────────────────────────────────────────────────────────────
col_left, col_right = st.columns(2)

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

# ── What-If Slider ────────────────────────────────────────────────────────────
st.markdown("---")
st.markdown("### What-If Scenario")
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

avg_cost_per_gw_usd = 800
market_value_usd    = required_gw * avg_cost_per_gw_usd

r1, r2, r3, r4 = st.columns(4)
r1.metric("Additional Generation Needed", f"{additional_twh:.1f} TWh")
r2.metric("New Capacity Required",        f"{required_gw:.1f} GW")
r3.metric("Target Solar Share",           f"{target_share}%")
# CHANGE 6 — New $ market size tile
r4.metric("Est. Market Opportunity",      f"${market_value_usd:,.0f}M USD")

st.success(
    f"To reach **{target_share}% solar share** in {selected}, Canadian Solar would need to deploy "
    f"approximately **{required_gw:.1f} GW** of new capacity — generating an additional "
    f"**{additional_twh:.1f} TWh** per year, representing an estimated market opportunity of "
    f"**${market_value_usd:,.0f}M USD**."
)

# ── Strengths / Risks / Considerations ───────────────────────────────────────
st.markdown("---")
st.markdown("### Strengths, Risks and Opportunity Considerations")

details = COUNTRY_DETAILS.get(selected, {})
c_str, c_risk, c_cons = st.columns(3)

with c_str:
    bullets = "".join(
        f"<div class='bullet-item'>+ {s}</div>"
        for s in details.get("strengths", [])
    )
    st.markdown(f"""
        <div class='strengths-box'>
            <div class='section-title' style='color:#27AE60;'>STRENGTHS</div>
            {bullets}
        </div>
    """, unsafe_allow_html=True)

with c_risk:
    bullets = "".join(
        f"<div class='bullet-item'>- {r}</div>"
        for r in details.get("risks", [])
    )
    st.markdown(f"""
        <div class='risks-box'>
            <div class='section-title' style='color:#E74C3C;'>RISKS</div>
            {bullets}
        </div>
    """, unsafe_allow_html=True)

with c_cons:
    st.markdown(f"""
        <div class='considerations-box'>
            <div class='section-title' style='color:#E8A020;'>
                CANADIAN SOLAR FIT
            </div>
            <div class='bullet-item'>
                {details.get('considerations', '')}
            </div>
        </div>
    """, unsafe_allow_html=True)