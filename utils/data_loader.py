import pandas as pd
import streamlit as st
import os

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")

@st.cache_data
def load_merged():
    return pd.read_csv(os.path.join(DATA_DIR, "solar_merged_dataset.csv"))

@st.cache_data
def load_opportunity():
    return pd.read_csv(os.path.join(DATA_DIR, "solar_market_opportunity.csv"))

@st.cache_data
def load_top20():
    return pd.read_csv(os.path.join(DATA_DIR, "solar_top20_opportunity_markets.csv"))

@st.cache_data
def load_capacity():
    return pd.read_csv(os.path.join(DATA_DIR, "solar_capacity_utilization.csv"))

@st.cache_data
def load_prices():
    return pd.read_csv(os.path.join(DATA_DIR, "solar_pv_prices_clean.csv"))

@st.cache_data
def load_price_adoption():
    return pd.read_csv(os.path.join(DATA_DIR, "solar_price_vs_adoption.csv"))