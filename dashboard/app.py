import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="Ethiopia FI Dashboard", layout="wide")

# --- DYNAMIC PATH HANDLING ---
# This finds the absolute path to the directory where app.py lives
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Joins that with the relative path to the data
DATA_PATH = os.path.join(BASE_DIR, "..", "data", "processed", "ethiopia_fi_enriched.csv")

# --- LOAD DATA ---
@st.cache_data
def load_data():
    if not os.path.exists(DATA_PATH):
        st.error(f"Data file not found at {DATA_PATH}. Please check your folder structure!")
        return pd.DataFrame()
    
    df = pd.read_csv(DATA_PATH)
    df['observation_date'] = pd.to_datetime(df['observation_date'], errors='coerce')
    df['year'] = df['observation_date'].dt.year
    return df

df = load_data()

# --- SIDEBAR NAVIGATION ---
st.sidebar.title("Selam Analytics")
page = st.sidebar.radio("Navigate", ["Overview", "Trends", "Event Impacts", "Inclusion Projections"])

# Stop execution if data failed to load
if df.empty:
    st.warning("Dashboard cannot render without data.")
    st.stop()

# --- PAGE 1: OVERVIEW ---
if page == "Overview":
    st.title("🇪🇹 Financial Inclusion Overview")
    
    # Key Metrics Cards
    col1, col2, col3 = st.columns(3)
    
    # Logic for Metrics
    p2p_val = df[df['indicator_code'] == 'USG_P2P_VALUE']['value_numeric'].max()
    atm_val = df[df['indicator_code'] == 'USG_ATM_VALUE']['value_numeric'].max()
    ratio = p2p_val / atm_val if atm_val > 0 else 0

    col1.metric("Account Ownership (2024)", "49.0%", "+3.0% (vs 2021)")
    col2.metric("Mobile Money Penetration", "9.45%", "+4.75% (vs 2021)")
    col3.metric("P2P/ATM Crossover Ratio", f"{ratio:.2f}x", "Digital > Physical")

    st.markdown("---")
    st.subheader("Progress Summary")
    st.write("Ethiopia is experiencing an **'Access-Usage Paradox'**. While traditional bank account growth (Access) is steady, digital transaction volumes and mobile money adoption (Usage) are exploding.")

# --- PAGE 2: TRENDS ---
elif page == "Trends":
    st.title("📈 Indicator Trends")
    
    indicators = st.multiselect("Select Indicators to Compare", 
                               options=df['indicator_code'].unique().tolist(),
                               default=['ACC_OWNERSHIP', 'ACC_MM_ACCOUNT'])
    
    trend_df = df[df['indicator_code'].isin(indicators)].sort_values('observation_date')
    
    if not trend_df.empty:
        fig = px.line(trend_df, x='observation_date', y='value_numeric', color='indicator_code',
                     title="Interactive Time Series Analysis", markers=True,
                     labels={"value_numeric": "Percentage / Value", "observation_date": "Date"})
        st.plotly_chart(fig, use_container_width=True)
        
        st.download_button("Download Trend Data", trend_df.to_csv(index=False), "ethiopia_trends.csv")
    else:
        st.info("Select indicators to view the trend.")

# --- PAGE 3: EVENT IMPACTS ---
elif page == "Event Impacts":
    st.title("⚡ Catalyst Event Analysis")
    
    # Filtering for actual events
    events = df[df['record_type'] == 'event'].copy()
    if not events.empty:
        st.write("The following market shocks were used to calibrate our forecasting models:")
        st.dataframe(events[['observation_date', 'indicator', 'category', 'notes']].dropna(how='all'))
    
    st.info("Our **Association Matrix** indicates that the Telebirr Launch and National ID (Fayda) rollout are the strongest structural drivers of inclusion.")

# --- PAGE 4: INCLUSION PROJECTIONS ---
elif page == "Inclusion Projections":
    st.title("🔮 2026-2027 Projections")
    
    scenario = st.selectbox("Select Scenario", ["Base", "Optimistic", "Pessimistic"])
    
    # Logic built from Task 4 Prophet output
    years = [2024, 2025, 2026, 2027]
    base_vals = [49.0, 54.5, 60.6, 64.3]
    
    if scenario == "Optimistic":
        # Using the 1.58 scaling factor for high ID adoption
        vals = [49.0, 56.0, 62.5, 66.2]
    elif scenario == "Pessimistic":
        # Accounting for infrastructure lag
        vals = [49.0, 52.0, 58.5, 62.3]
    else:
        vals = base_vals

    fig = go.Figure()
    # Shaded Area for Target
    fig.add_hrect(y0=60, y1=100, fillcolor="green", opacity=0.1, annotation_text="Target Zone (60%+)")
    
    fig.add_trace(go.Scatter(x=years, y=vals, mode='lines+markers', name=f"{scenario} Forecast",
                             line=dict(width=4, color='green' if scenario=="Optimistic" else 'blue')))
    
    # 60% Target Line
    fig.add_hline(y=60, line_dash="dash", line_color="red", annotation_text="Consortium Target (60%)")
    
    fig.update_layout(yaxis_title="Account Ownership (%)", xaxis_title="Year")
    st.plotly_chart(fig, use_container_width=True)
    
    # Final Interpretation Statement
    if vals[-1] >= 60:
        st.success(f"Under the **{scenario}** scenario, Ethiopia is projected to achieve the 60% inclusion target by **{2026 if vals[2] >= 60 else 2027}**.")
    else:
        st.warning(f"Under the **{scenario}** scenario, the 60% target may not be reached until after 2027.")