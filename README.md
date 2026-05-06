# DVN_Assignment3

# ☀️ Chasing the Sun — Canadian Solar Market Opportunity Dashboard

> **AT3 – 36104 Data Visualisation and Narratives | UTS | 2026**  
> An interactive Streamlit dashboard identifying global solar expansion 
> opportunities for Canadian Solar Inc.

---

## 📋 Project Overview

This dashboard presents a data-driven strategic narrative for the 
**Vice President of Strategy & Innovation at Canadian Solar Inc.**

The story answers one question:
> *"Where in the world should Canadian Solar expand next — and why now?"*

Starting with the global solar price revolution, uncovering the Chile 
anomaly, and ending with a ranked opportunity matrix across key markets.

---

## 👥 Team

| Name | Role |
|------|------|
| Benjamin | Project Co-ordinator / Narrative & Story Designer / Presenter |
| Supreechaya | Data Analyst / Engineer |
| Ricki | Data Analyst / Engineer |
| Victor | Dashboard / Streamlit Designer |
| Prathamesh | Dashboard / Streamlit Designer |
| Yunkwang | Dashboard / Streamlit Designer |
| Lin | Dashboard / Streamlit Designer / Project Administration |

---

## 🗂️ Project Structure
DVN_Assignment3/
│
├── app.py                        # Entry point — launches dashboard
├── requirements.txt              # Python dependencies
│
├── .streamlit/
│   └── config.toml               # Theme and colour configuration
│
├── data/                         # Processed datasets (see Data Dictionary)
│   ├── solar_merged_dataset.csv
│   ├── solar_market_opportunity.csv
│   ├── solar_top20_opportunity_markets.csv
│   ├── solar_capacity_utilization.csv
│   ├── solar_price_vs_adoption.csv
│   └── solar_pv_prices_clean.csv
│
├── utils/
│   ├── data_loader.py            # Cached data loading functions
│   └── navigation.py             # Shared prev/next navigation component
│
└── pages/
├── 1_price_revolution.py     # Page 1 — Solar price collapse & growth
├── 2_chasing_the_sun.py      # Page 2 — Title & narrative intro
├── 3_anomaly.py              # Page 3 — The Chile anomaly
├── 4_opportunity_map.py      # Page 4 — Global opportunity choropleth
├── 5_country_deep_dive.py    # Page 5 — Country selector & what-if
└── 6_recommendation.py       # Page 6 — Final recommendation

---

## 🚀 How to Run Locally

**1. Clone the repository**
```bash
git clone https://github.com/prathameshn21/DVN_Assignment3.git
cd DVN_Assignment3
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Run the dashboard**
```bash
streamlit run app.py
```

**4. Open in browser**
http://localhost:8501

---

## ⚙️ Advanced Features Implemented

| Feature | Where | Description |
|---------|-------|-------------|
| Context-Aware Filtering | Page 4 | Dropdown recolours the world map and updates the bar chart dynamically |
| Visual Tooltips | Page 4 | Hover over any country on the choropleth to see solar share, PVOUT, CAGR and opportunity score |
| What-If Parameterization | Page 5 | Slider lets user set a target solar share % — dashboard calculates required new GW capacity |

---

## 📊 Data Dictionary

| File | Source | Description | Key Columns |
|------|--------|-------------|-------------|
| `solar_merged_dataset.csv` | OWID + IRENA + World Bank | Main dataset — country level energy data 2000–2024 joined across 4 sources | `country`, `iso_code`, `year`, `solar_electricity`, `solar_share_elec`, `installed_capacity_gw`, `pvout_kwh_kwp_day` |
| `solar_market_opportunity.csv` | Derived | 2024 snapshot with composite opportunity score for 119 countries | `opportunity_score`, `solar_cagr_5yr`, `pvout_kwh_kwp_day`, `solar_share_elec` |
| `solar_top20_opportunity_markets.csv` | Derived | Top 20 countries by opportunity score | Same as above, filtered |
| `solar_capacity_utilization.csv` | Derived | Capacity utilisation factor 2010–2024 for 10 key countries | `capacity_util_factor`, `installed_capacity_gw`, `solar_electricity` |
| `solar_price_vs_adoption.csv` | OWID + IRENA | Global PV price vs solar generation 2000–2024 | `pv_module_cost_usd_per_w`, `solar_electricity`, `solar_share_elec` |
| `solar_pv_prices_clean.csv` | IRENA via OWID | Annual PV module price 1975–2024 | `year`, `pv_module_cost_usd_per_w` |

**Opportunity Score Formula:**
score = 0.25 × PVOUT_normalised
+ 0.25 × untapped_share_normalised
+ 0.20 × electricity_demand_normalised
+ 0.20 × 5yr_CAGR_normalised
+ 0.10 × GDP_per_capita_normalised

---

## 📦 Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| streamlit | ≥1.32.0 | Dashboard framework |
| plotly | latest | All charts and maps |
| pandas | latest | Data manipulation |
| numpy | latest | Numerical calculations |
| openpyxl | latest | Reading Excel source files |

---

## 🌿 Branch Strategy

| Branch | Purpose |
|--------|---------|
| `main` | Final submitted version only |
| `dev` | Integration branch — all pages merged here first |
| `feature/*` | Individual feature/page branches |

---

## 📚 Data Sources & Credits

| Dataset | Provider | Link |
|---------|----------|------|
| OWID Energy Data | Our World in Data / Ember / Energy Institute | [ourworldindata.org/energy](https://ourworldindata.org/energy) |
| IRENA Installed Solar Capacity | IRENA via Our World in Data | [ourworldindata.org](https://ourworldindata.org) |
| Solar PV Module Prices | IRENA / Nemet / Farmer & Lafond via OWID | [ourworldindata.org](https://ourworldindata.org) |
| World Bank PV Potential | Solargis / World Bank (2020) | [World Bank ESMAP](https://esmap.org) |

Data analysis and processing by **Supreechaya** and **Ricki**.  
Dashboard design and development by **Victor**, **Prathamesh**, **Yunkwang**, and **Lin**.  
Narrative, strategy, and presentation by **Benjamin**.

---
