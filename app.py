import streamlit as st
import yfinance as yf
import pandas as pd

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Baez Blockchain",
    page_icon="⛓️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- CUSTOM CSS (Clean, Modern, Edgy) ---
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# --- HERO SECTION ---
st.title("BAEZ BLOCKCHAIN SOLUTIONS")
st.markdown("### *Immutable Infrastructure • Smart Contract Audits • Enterprise Web3 Integration*")
st.markdown("We bridge the gap between traditional IT and the Decentralized Future.")
st.markdown("---")

# --- LIVE CRYPTO METRICS ---
st.subheader("⛓️ On-Chain Market Pulse")
col1, col2, col3, col4 = st.columns(4)

def get_price(ticker):
    try:
        data = yf.Ticker(ticker).history(period="1d")
        if not data.empty:
            return data["Close"].iloc[-1], data["Close"].iloc[-1] - data["Open"].iloc[-1]
        return 0.0, 0.0
    except:
        return 0.0, 0.0

# Fetch Data
btc_price, btc_delta = get_price("BTC-USD")
eth_price, eth_delta = get_price("ETH-USD")
sol_price, sol_delta = get_price("SOL-USD")
matic_price, matic_delta = get_price("MATIC-USD") # Added Polygon as it is usage-heavy

with col1:
    st.metric(label="Bitcoin (Store of Value)", value=f"${btc_price:,.0f}", delta=f"{btc_delta:.2f}")
with col2:
    st.metric(label="Ethereum (Smart Contracts)", value=f"${eth_price:,.0f}", delta=f"{eth_delta:.2f}")
with col3:
    st.metric(label="Solana (High Speed)", value=f"${sol_price:.2f}", delta=f"{sol_delta:.2f}")
with col4:
    st.metric(label="Polygon (Scaling)", value=f"${matic_price:.4f}", delta=f"{matic_delta:.4f}")

st.markdown("---")

# --- BLOCKCHAIN SERVICES SECTION ---
st.header("Decentralized Services")

col_left, col_mid, col_right = st.columns(3)

with col_left:
    st.subheader("📝 Smart Contracts")
    st.write("""
    Secure, audited smart contract development for Ethereum and Solana.
    * **Automated Escrows**
    * **NFT Minting Engines**
    * **DAO Governance Systems**
    """)

with col_mid:
    st.subheader("🏦 DeFi Integration")
    st.write("""
    Launch your own financial protocols or integrate existing ones.
    * **Staking Mechanisms**
    * **Liquidity Pools**
    * **Tokenomics Strategy**
    """)

with col_right:
    st.subheader("🌐 Enterprise Web3")
    st.write("""
    Moving real-world assets (RWA) onto the blockchain.
    * **Supply Chain Tracking**
    * **Asset Tokenization**
    * **Private Permissioned Chains**
    """)

st.markdown("---")

# --- CONTACT SECTION ---
col_contact_left, col_contact_right = st.columns([2, 1])

with col_contact_left:
    st.header("Build on Chain")
    st.write("Ready to deploy? Tell us about your protocol or project.")
    
    contact_form = st.form(key='contact_form')
    email = contact_form.text_input("Wallet Address or Email")
    message = contact_form.text_area("Project Scope (e.g., 'I need a staking token')")
    submit = contact_form.form_submit_button("Initialize Project")
    
    if submit:
        st.success("Transmission Received. We will contact you shortly.")

with col_contact_right:
    st.info("📍 **Base:** New York, NY")
    st.info("🔐 **Security:** Audited & Verified")
    st.info("⛓️ **Focus:** ETH, SOL, POLYGON")
