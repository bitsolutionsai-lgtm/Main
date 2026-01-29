import streamlit as st
import yfinance as yf

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="DeFi Labs",
    page_icon="🔹",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- CUSTOM CSS (The "Slate-Blue" Look) ---
st.markdown("""
    <style>
    /* Main Background - Cool Gray-Blue */
    .stApp {
        background-color: #D8DCE3;
    }
    
    /* Hide default menu elements */
    #MainMenu, footer, header {visibility: hidden;}
    
    /* Styling the metrics/cards */
    div[data-testid="stMetric"] {
        background-color: #F0F2F6;
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #C4C9D0;
        box-shadow: 0 1px 3px rgba(0,0,0,0.08);
    }
    
    /* Typography */
    h1 { color: #2C3E50; font-family: 'Arial', sans-serif; letter-spacing: 1px; }
    h2, h3 { color: #34495E; }
    p, li { color: #445566; }
    
    </style>
    """, unsafe_allow_html=True)

# --- HERO SECTION ---
st.title("DEFI LABS")
st.markdown("### *Institutional-Grade Decentralized Finance Strategies*")
st.write("We architect high-yield liquidity pools and automated market making strategies for the next generation of finance.")
st.markdown("---")

# --- DEFI MARKET WATCH ---
st.subheader("🔵 DeFi Blue Chips")

col1, col2, col3, col4 = st.columns(4)

def get_price(ticker):
    try:
        data = yf.Ticker(ticker).history(period="1d")
        if not data.empty:
            return data["Close"].iloc[-1], data["Close"].iloc[-1] - data["Open"].iloc[-1]
        return 0.0, 0.0
    except:
        return 0.0, 0.0

# Fetching specific DeFi tokens
uni_price, uni_delta = get_price("UNI-USD")   # Uniswap
aave_price, aave_delta = get_price("AAVE-USD") # Aave
mkr_price, mkr_delta = get_price("MKR-USD")   # MakerDAO
crv_price, crv_delta = get_price("CRV-USD")   # Curve

with col1:
    st.metric(label="Uniswap (UNI)", value=f"${uni_price:.2f}", delta=f"{uni_delta:.2f}")
with col2:
    st.metric(label="Aave (AAVE)", value=f"${aave_price:.
