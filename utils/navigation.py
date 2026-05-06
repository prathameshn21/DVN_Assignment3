# utils/navigation.py
import streamlit as st

def show_navigation(current: int, total: int):
    page_files = [
        "pages/1_price_revolution.py",
        "pages/2_chasing_the_sun.py",
        "pages/3_anomaly.py",
        "pages/4_opportunity_map.py",
        "pages/5_country_deep_dive.py",
        "pages/6_recommendation.py",
    ]
    titles = [
        "Price Revolution", "Chasing The Sun", "The Anomaly",
        "Opportunity Map", "Country Deep Dive", "Recommendation"
    ]

    col1, col2, col3 = st.columns([1, 4, 1])
    with col1:
        if current > 1:
            if st.button("← Prev"):
                st.switch_page(page_files[current - 2])
    with col2:
        st.markdown(
            f"<p style='text-align:center; color:#888; margin-top:8px'>"
            f"{current} / {total} · {titles[current-1]}</p>",
            unsafe_allow_html=True
        )
    with col3:
        if current < total:
            if st.button("Next →"):
                st.switch_page(page_files[current])
    st.markdown("---")