import streamlit as st
import yfinance as yf

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="DeFi Labs",
    page_icon="🔹",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    .stApp { background-color: #D8DCE3; }
    #MainMenu, footer, header { visibility: hidden; }
    div[data-testid="stMetric"] {
        background-color: #F0F2F6;
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #C4C9D0;
        box-shadow: 0 1px 3px rgba(0,0,0,0.08);
    }
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
            c = data["Close"].iloc[-1]
            o = data["Open"].iloc[-1]
            return c, c - o
        return 0.0, 0.0
    except:
        return 0.0, 0.0

# Fetch Data
uni_p, uni_d = get_price("UNI-USD")
aave_p, aave_d = get_price("AAVE-USD")
mkr_p, mkr_d = get_price("MKR-USD")
crv_p, crv_d = get_price("CRV-USD")

# Metrics - Shorter lines to prevent errors
with col1:
    st.metric(label="Uniswap (UNI)", value=f"${uni_p:.2f}", delta=f"{uni_d:.2f}")
with col2:
    st.metric(label="Aave (AAVE)", value=f"${aave_p:.2f}", delta=f"{aave_d:.2f}")
with col3:
    st.metric(label="Maker (MKR)", value=f"${mkr_p:,.2f}", delta=f"{mkr_d:.2f}")
with col4:
    st.metric(label="Curve (CRV)", value=f"${crv_p:.3f}", delta=f"{crv_d:.3f}")

st.markdown("---")

# --- SERVICES SECTION ---
st.header("Protocol Services")

c1, c2, c3 = st.columns(3)

with c1:
    st.subheader("🌾 Yield Farming")
    st.info("**Strategy Optimization**")
    st.write("We design automated strategies to maximize APY across multiple lending protocols while hedging against impermanent loss.")

with c2:
    st.subheader("💧 Liquidity Mining")
    st.info("**Market Making**")
    st.write("Provide deep liquidity to DEXs (Decentralized Exchanges). We manage the pools to ensure capital efficiency and token stability.")

with c3:
    st.subheader("🏛️ DAO Governance")
    st.info("**Voting & Proposals**")
    st.write("Technical implementation of on-chain voting systems. We help you transition your project into a fully decentralized autonomous organization.")

st.markdown("---")

# --- CONTACT ---
c_left, c_right = st.columns([2,1])

with c_left:
    st.markdown("### Join the Liquidity Pool")
    with st.form("defi_form"):
        email = st.text_input("Email / ENS Domain")
        interest = st.multiselect("Interests", ["Staking", "Lending", "Flash Loans"])
        submitted = st.form_submit_button("Connect Wallet (Simulation)")
        if submitted:
            st.success("Details captured. We will air-drop our whitepaper to your inbox.")
            
with c_right:
    st.image("https://cryptologos.cc/logos/ethereum-eth-logo.png?v=026", width=80)
    st.write("**Built on Ethereum.**")
    st.caption("Audited by DeFi Labs Security.")
