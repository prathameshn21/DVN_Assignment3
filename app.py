import streamlit as st

from utils.data_loader import load_opportunity, load_price_adoption, load_prices


st.set_page_config(
    page_title="Chasing the Sun - Canadian Solar",
    page_icon="☀️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
        [data-testid="stSidebar"] {display: none;}
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        [data-testid="stAppViewContainer"] {
            background: linear-gradient(180deg, #FFF8F1 0%, #FFFDF9 100%);
        }
        .hero {
            background: linear-gradient(135deg, #0D1B2A 0%, #15385D 62%, #1F4C73 100%);
            border-radius: 24px;
            padding: 58px 56px;
            box-shadow: 0 18px 42px rgba(13, 27, 42, 0.14);
        }
        .eyebrow {
            color: #E8A020;
            font-size: 0.84rem;
            font-weight: 800;
            letter-spacing: 2.2px;
            text-transform: uppercase;
            margin-bottom: 14px;
        }
        .hero-title {
            color: white;
            font-size: 4rem;
            font-weight: 850;
            line-height: 0.95;
            margin: 0 0 14px 0;
        }
        .hero-question {
            color: #FFE2B0;
            font-size: 1.38rem;
            font-weight: 650;
            margin-bottom: 16px;
        }
        .hero-sub {
            color: #D9E3EE;
            font-size: 1.04rem;
            line-height: 1.75;
            max-width: 760px;
        }
        .hero-note {
            margin-top: 22px;
            display: inline-block;
            background: rgba(255, 255, 255, 0.10);
            border: 1px solid rgba(255, 255, 255, 0.14);
            color: #F4F7FA;
            border-radius: 999px;
            padding: 8px 14px;
            font-size: 0.86rem;
            font-weight: 600;
        }
        .section-kicker {
            color: #C9651B;
            font-size: 0.82rem;
            font-weight: 800;
            letter-spacing: 1.4px;
            text-transform: uppercase;
            margin-bottom: 4px;
        }
        .section-title {
            color: #14212E;
            font-size: 1.8rem;
            font-weight: 760;
            margin-bottom: 16px;
        }
        .evidence-card {
            background: white;
            border: 1px solid #F0E2CF;
            border-radius: 18px;
            padding: 24px 22px;
            min-height: 178px;
            box-shadow: 0 8px 22px rgba(20, 33, 46, 0.05);
        }
        .evidence-value {
            color: #E8721C;
            font-size: 2.3rem;
            font-weight: 850;
            line-height: 1.05;
            margin-bottom: 8px;
        }
        .evidence-label {
            color: #14212E;
            font-size: 1rem;
            font-weight: 760;
            margin-bottom: 8px;
        }
        .evidence-body {
            color: #5D636A;
            font-size: 0.92rem;
            line-height: 1.65;
        }
        .thesis-box {
            background: linear-gradient(135deg, #FFF1DE 0%, #FFF8EE 100%);
            border: 1px solid #F1D6AE;
            border-radius: 18px;
            padding: 24px 26px;
        }
        .thesis-label {
            color: #A85318;
            font-size: 0.82rem;
            font-weight: 800;
            letter-spacing: 1.2px;
            text-transform: uppercase;
            margin-bottom: 8px;
        }
        .thesis-text {
            color: #14212E;
            font-size: 1.08rem;
            font-weight: 640;
            line-height: 1.7;
        }
        .path-card {
            background: #FFFCF8;
            border: 1px solid #EEDBC2;
            border-radius: 18px;
            padding: 20px 18px;
            min-height: 148px;
        }
        .path-step {
            color: #E8721C;
            font-size: 0.83rem;
            font-weight: 800;
            letter-spacing: 1.2px;
            text-transform: uppercase;
            margin-bottom: 8px;
        }
        .path-title {
            color: #14212E;
            font-size: 1.04rem;
            font-weight: 760;
            margin-bottom: 8px;
        }
        .path-body {
            color: #5D636A;
            font-size: 0.91rem;
            line-height: 1.66;
        }
        .shortlist-box {
            background: white;
            border: 1px solid #F0E2CF;
            border-radius: 18px;
            padding: 22px 24px;
            box-shadow: 0 8px 22px rgba(20, 33, 46, 0.05);
        }
        .shortlist-title {
            color: #14212E;
            font-size: 1rem;
            font-weight: 760;
            margin-bottom: 12px;
        }
        .shortlist-copy {
            color: #5D636A;
            font-size: 0.92rem;
            line-height: 1.68;
            margin-bottom: 12px;
        }
        .pill {
            display: inline-block;
            background: #FDF1DF;
            color: #A85318;
            border: 1px solid #F0D6B5;
            border-radius: 999px;
            padding: 6px 12px;
            font-size: 0.84rem;
            font-weight: 700;
            margin: 0 8px 8px 0;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

prices = load_prices()
price_adoption = load_price_adoption()
opp = load_opportunity()

p_1975 = float(prices.loc[prices["year"] == 1975, "pv_module_cost_usd_per_w"].iloc[0])
p_2024 = float(prices.loc[prices["year"] == 2024, "pv_module_cost_usd_per_w"].iloc[0])
price_drop = (1 - p_2024 / p_1975) * 100

global_2015 = float(price_adoption.loc[price_adoption["year"] == 2015, "solar_electricity"].iloc[0])
global_2024 = float(price_adoption.loc[price_adoption["year"] == 2024, "solar_electricity"].iloc[0])
growth_multiple = global_2024 / global_2015

saudi_row = opp.loc[opp["country"] == "Saudi Arabia"].iloc[0]
chile_share = float(opp.loc[opp["country"] == "Chile", "solar_share_elec"].iloc[0])
saudi_share = float(saudi_row["solar_share_elec"])

st.markdown(
    """
    <div class='hero'>
        <div class='eyebrow'>Canadian Solar Strategic Brief</div>
        <div class='hero-title'>Chasing the Sun</div>
        <div class='hero-question'>A new economical Age of Solar. The next horizon to chase.</div>
        <div class='hero-sub'>
            This dashboard is built for the Vice President of Strategy & Innovation at Canadian Solar.
            It uses global solar cost, generation, adoption-gap, and market-opportunity data to narrow
            the next set of utility-scale expansion markets.
        </div>
    """,
    unsafe_allow_html=True,
)

st.markdown("<br>", unsafe_allow_html=True)

cta1, _ = st.columns([1.25, 5.75])
with cta1:
    if st.button("Start the story ->", type="primary"):
        st.switch_page("pages/1_price_revolution.py")

st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<div class='section-kicker'>Opening Evidence</div>", unsafe_allow_html=True)
st.markdown("<div class='section-title'>Three signals explain why this decision matters now.</div>", unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)
with c1:
    st.markdown(
        f"""
        <div class='evidence-card'>
            <div class='evidence-value'>{price_drop:.1f}%</div>
            <div class='evidence-label'>Photovoltaic Module Price Decline – Since 1975</div>
            <div class='evidence-body'>
                Hardware cost is no longer the reason for using solar at scale.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
with c2:
    st.markdown(
        f"""
        <div class='evidence-card'>
            <div class='evidence-value'>{global_2024:,.0f} TWh</div>
            <div class='evidence-label'>Global Solar Generation – 12x from 2015 to 2024</div>
            <div class='evidence-body'>
                The world is rapidly adopting solar at a system-wide scale.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
with c3:
    st.markdown(
        f"""
        <div class='evidence-card'>
            <div class='evidence-value'>22.3% Solar Share in Chile</div>
            <div class='evidence-label'>The precedent has been set in Chile</div>
            <div class='evidence-body'>
                Where potential and opportunities meet, is where the horizon is.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown("<br>", unsafe_allow_html=True)
st.markdown(
    """
    <div class='thesis-box'>
        <div class='thesis-label'>What Does This Mean?</div>
        <div class='thesis-text'>
            Module cost is no longer the bottleneck. The world is ready and asking for utility scale Solar. The question where next for Candian Solar?
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown("<br>", unsafe_allow_html=True)
