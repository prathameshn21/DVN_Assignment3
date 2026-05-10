import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from utils.data_loader import load_opportunity
from utils.navigation import show_navigation

st.set_page_config(page_title="The Anomaly", layout="wide",
                   initial_sidebar_state="collapsed")

st.markdown("""
    <style>
        [data-testid="stSidebar"] {display: none;}
        .comparison-card-green {
            background: #F0FAF4;
            border-left: 4px solid #2ECC71;
            border-radius: 0 8px 8px 0;
            padding: 24px 28px;
        }
        .comparison-card-red {
            background: #FFF3F0;
            border-left: 4px solid #E8721C;
            border-radius: 0 8px 8px 0;
            padding: 24px 28px;
        }
        .card-country-green { color: #27AE60; font-size: 1.45rem; font-weight: 800; margin-bottom: 14px; }
        .card-country-red   { color: #E8721C; font-size: 1.45rem; font-weight: 800; margin-bottom: 14px; }
        .card-big-number    { font-size: 2.8rem; font-weight: 800; color: #1A1A1A; line-height: 1; margin-bottom: 6px; }
        .card-sub           { font-size: 0.85rem; color: #777; }
        .insight-box {
            border-left: 4px solid #E8721C;
            background: #FFFAF5;
            padding: 20px 24px;
            border-radius: 0 8px 8px 0;
            margin-top: 24px;
            font-size: 0.95rem;
            color: #333;
            line-height: 1.7;
        }
        .section-label {
            display: inline-block;
            background: #FDF0E6;
            color: #E8721C;
            border-radius: 20px;
            padding: 10px 22px;
            font-size: 2.2rem;
            font-weight: 850;
            letter-spacing: 2px;
            margin-bottom: 18px;
        }
    </style>
""", unsafe_allow_html=True)

# ── Navigation ────────────────────────────────────────────────────────────────
show_navigation(current=3, total=6)

# ── Load Data ─────────────────────────────────────────────────────────────────
opp = load_opportunity()

chile_row = opp[opp["country"] == "Chile"].iloc[0] \
    if "Chile" in opp["country"].values else None
saudi_row = opp[opp["country"] == "Saudi Arabia"].iloc[0] \
    if "Saudi Arabia" in opp["country"].values else None

chile_share = f"{chile_row['solar_share_elec']:.1f}" if chile_row is not None else "22.3"
chile_pvout = f"{chile_row['pvout_kwh_kwp_day']:.2f}" if chile_row is not None else "5.36"
saudi_share = f"{saudi_row['solar_share_elec']:.1f}" if saudi_row is not None else "1.8"
saudi_pvout = f"{saudi_row['pvout_kwh_kwp_day']:.2f}" if saudi_row is not None else "5.16"

# ── Header ────────────────────────────────────────────────────────────────────
st.markdown("<div class='section-label'>THE ANOMALY</div>",
            unsafe_allow_html=True)

st.markdown("""
    <h2 style='font-size:2.2rem; font-weight:850; margin-bottom:10px; line-height:1.1;'>
        If the sun is the same, why is adoption different?
    </h2>
""", unsafe_allow_html=True)

st.markdown(
    f"Chile has **{chile_share}% solar share** at PVOUT {chile_pvout}. "
    f"Saudi Arabia has **{saudi_share}%** at PVOUT {saudi_pvout} "
    "— nearly identical sunlight. The gap isn't physics. "
    "It's policy, investment, and infrastructure — and those barriers are now falling."
)

st.markdown("<br>", unsafe_allow_html=True)

# ── Comparison Cards ──────────────────────────────────────────────────────────
col_chile, col_gap, col_saudi = st.columns([5, 1, 5])

with col_chile:
    st.markdown(f"""
        <div class='comparison-card-green'>
            <div class='card-country-green'>Chile (the proof)</div>
            <div class='card-big-number'>
                {chile_share}%
                <span style='font-size:1rem; font-weight:400; 
                             color:#999; margin-left:6px;'>solar share</span>
            </div>
            <div style='font-size:1.4rem; font-weight:700;
                        color:#27AE60; margin-top:8px;'>
                PVOUT {chile_pvout}
                <span style='font-size:1rem; font-weight:400;
                             color:#999; margin-left:6px;'>kWh/kWp/day</span>
            </div>
        </div>
    """, unsafe_allow_html=True)

with col_gap:
    st.markdown(
        "<div style='text-align:center; padding-top:36px; "
        "font-size:1.4rem; color:#ccc;'>vs</div>",
        unsafe_allow_html=True)

with col_saudi:
    st.markdown(f"""
        <div class='comparison-card-red'>
            <div class='card-country-red'>Saudi Arabia (the gap)</div>
            <div class='card-big-number'>
                {saudi_share}%
                <span style='font-size:1rem; font-weight:400;
                             color:#999; margin-left:6px;'>solar share</span>
            </div>
            <div style='font-size:1.4rem; font-weight:700;
                        color:#E74C3C; margin-top:8px;'>
                PVOUT {saudi_pvout}
                <span style='font-size:1rem; font-weight:400;
                             color:#999; margin-left:6px;'>kWh/kWp/day</span>
            </div>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ── Scatter Plot ──────────────────────────────────────────────────────────────
st.markdown("**PVOUT vs solar share — the structural gap**")

st.markdown("""
    <div style='display:flex; gap:24px; margin-bottom:4px; font-size:0.85rem;'>
        <span><span style='color:#27AE60; font-size:1.1rem;'>●</span>&nbsp; Developed markets</span>
        <span><span style='color:#E74C3C; font-size:1.1rem;'>●</span>&nbsp; High Growth Markets</span>
        <span><span style='color:#E8A020; font-size:1.1rem;'>●</span>&nbsp; Growth markets</span>
        <span><span style='color:#95A5A6; font-size:1.1rem;'>●</span>&nbsp; Mature / low resource</span>
    </div>
""", unsafe_allow_html=True)

# Bubble size legend — moved above chart
st.markdown("""
    <div style='font-size:0.82rem; color:#888; margin-bottom:12px;'>
        ⬤ &nbsp; Bubble size represents
        <strong>electricity demand (TWh)</strong> —
        larger bubble = larger energy market
    </div>
""", unsafe_allow_html=True)

# Category assignment
DEVELOPED = ["Chile", "USA", "Spain", "Australia", "Italy", "Greece"]
MENA      = ["Saudi Arabia", "Egypt", "Oman", "Kuwait", "Libya",
             "Morocco", "Tunisia", "UAE", "Jordan", "Iraq", "Yemen"]
MATURE    = ["Germany", "Japan", "United Kingdom", "France", "Belgium"]

def assign_category(country):
    if country in DEVELOPED: return ("Developed",          "#27AE60")
    if country in MENA:      return ("High Growth Markets", "#E74C3C")
    if country in MATURE:    return ("Mature",              "#95A5A6")
    return                          ("Growth",              "#E8A020")

plot_df = opp.dropna(subset=["pvout_kwh_kwp_day", "solar_share_elec"]).copy()
plot_df[["category", "color"]] = plot_df["country"].apply(
    lambda c: pd.Series(assign_category(c))
)

max_demand = plot_df["electricity_demand"].max()
plot_df["bubble_size"] = (
    plot_df["electricity_demand"].fillna(plot_df["electricity_demand"].median())
    / max_demand * 50 + 8
).clip(8, 55)

LABEL_COUNTRIES = {
    "Chile", "Saudi Arabia", "Egypt", "Oman", "Colombia",
    "Pakistan", "Germany", "USA", "Spain", "Australia",
    "Japan", "Morocco", "Kuwait", "Tunisia"
}

HIGH_CAGR_THRESHOLD = 0.60

fig = go.Figure()

for _, row in plot_df.iterrows():
    show_label  = row["country"] in LABEL_COUNTRIES
    cagr_val    = row.get("solar_cagr_5yr", 0) or 0
    is_high_cagr = cagr_val >= HIGH_CAGR_THRESHOLD

    fig.add_trace(go.Scatter(
        x=[row["pvout_kwh_kwp_day"]],
        y=[row["solar_share_elec"]],
        mode="markers+text" if show_label else "markers",
        marker=dict(
            size=row["bubble_size"],
            color=row["color"],
            opacity=0.90 if (show_label or is_high_cagr) else 0.35,
            # CHANGE 5 — Gold border for 60%+ CAGR, white for others
            line=dict(
                width=3   if is_high_cagr else (1.5 if show_label else 0.5),
                color="#FFD700" if is_high_cagr else "white"
            )
        ),
        text=[row["country"]] if show_label else [""],
        textposition="top center",
        # CHANGE 2 — Slightly larger label font
        textfont=dict(size=11, color="#333"),
        hovertemplate=(
            f"<b>{row['country']}</b><br>"
            f"PVOUT: {row['pvout_kwh_kwp_day']:.2f} kWh/kWp/day<br>"
            f"Solar Share: {row['solar_share_elec']:.1f}%<br>"
            f"5yr CAGR: {cagr_val*100:.0f}%<br>"
            f"Category: {row['category']}<extra></extra>"
        ),
        showlegend=False,
        name=row["country"]
    ))

# Vertical reference line
fig.add_vline(
    x=5.0, line_dash="dash",
    line_color="#DDDDDD", line_width=1.5,
    annotation_text="MENA solar resource threshold",
    annotation_position="top right",
    annotation_font=dict(color="#AAAAAA", size=10)
)

# Chile annotation
if chile_row is not None:
    fig.add_annotation(
        x=float(chile_row["pvout_kwh_kwp_day"]),
        y=float(chile_row["solar_share_elec"]),
        text=f"<b>Chile</b> — {chile_share}%<br>Same sun as MENA",
        showarrow=True, arrowhead=2,
        arrowcolor="#27AE60",
        ax=-130, ay=-50,
        font=dict(color="#27AE60", size=11),
        bgcolor="white",
        bordercolor="#27AE60",
        borderwidth=1, borderpad=6
    )

fig.update_layout(
    template="plotly_white",
    height=500,
    xaxis=dict(
        # CHANGE 6 — Horizontal axis title
        title=dict(text="PVOUT (kWh/kWp/day)", standoff=15),
        showgrid=True, gridcolor="#F5F5F5",
        zeroline=False,
    ),
    yaxis=dict(
        # CHANGE 6 — Horizontal Y axis title, remove arrow prefix
        title=dict(text="Solar share of electricity (%)", standoff=15),
        showgrid=True, gridcolor="#F5F5F5",
        zeroline=True, zerolinecolor="#EEEEEE"
    ),
    margin=dict(l=60, r=40, t=20, b=60),
    plot_bgcolor="white",
    paper_bgcolor="white",
    hovermode="closest"
)

st.plotly_chart(fig, use_container_width=True)

# ── Insight Box ───────────────────────────────────────────────────────────────
st.markdown("""
    <div class='insight-box'>
        <div style='font-size:1.2rem; font-weight:800; color:#1A1A1A;
                    margin-bottom:10px; line-height:1.5;'>
            Countries with fast growing demand for solar, high sun,
            low adoption — is where opportunity lives.
        </div>
        These countries can replicate Chile's trajectory now that
        module prices are universal at <strong>$0.26/W</strong>.
        The gap is investment, policy, and grid infrastructure —
        exactly what <strong>Canadian Solar</strong> provides.
    </div>
""", unsafe_allow_html=True)