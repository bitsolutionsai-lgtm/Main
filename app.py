import streamlit as st
import pandas as pd
import yfinance as yf

# --- PAGE SETUP ---
st.set_page_config(
    page_title="Prime Protocol",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- PROFESSIONAL STYLING ---
st.markdown("""
    <style>
    /* App Background */
    .stApp { background-color: #F4F6F9; }
    
    /* Remove default header/footer */
    #MainMenu, footer, header { visibility: hidden; }
    
    /* Tabs Styling - Making them look like buttons */
    .stTabs [data-baseweb="tab-list"] {
        gap: 20px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        background-color: #FFFFFF;
        border-radius: 5px;
        padding-left: 20px;
        padding-right: 20px;
        box-shadow: 0 1px 2px rgba(0,0,0,0.1);
    }
    .stTabs [aria-selected="true"] {
        background-color: #0d47a1; /* Bank Blue */
        color: #FFFFFF;
    }
    
    /* Card Styling */
    div[data-testid="stMetric"] {
        background-color: #FFFFFF;
        padding: 10px;
        border-radius: 8px;
        box-shadow: 0 1px 2px rgba(0,0,0,0.05);
    }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER ROW ---
col_logo, col_wallet = st.columns([3, 1])
with col_logo:
    st.title("PRIME PROTOCOL")
    st.caption("Decentralized Lending & Liquidity Market")

with col_wallet:
    st.write("") # Spacer
    st.write("") # Spacer
    # A simulated wallet button
    st.button("⚡ Connect Wallet")

st.markdown("---")

# --- MAIN TABS (This is the new layout) ---
tab_market, tab_stake, tab_borrow = st.tabs(["📊 Markets", "🔒 Staking", "💸 Borrow"])

# --- TAB 1: MARKETS (Live Data) ---
with tab_market:
    st.subheader("Asset Overview")
    
    # Helper for prices
    def get_price(t):
        try:
            d = yf.Ticker(t).history(period="1d")
            if not d.empty:
                return d["Close"].iloc[-1], d["Close"].iloc[-1]-d["Open"].iloc[-1]
            return 0.0, 0.0
        except:
            return 0.0, 0.0

    # Data Fetch
    btc_p, btc_d = get_price("BTC-USD")
    eth_p, eth_d = get_price("ETH-USD")
    sol_p, sol_d = get_price("SOL-USD")
    aave_p, aave_d = get_price("AAVE-USD")

    # Metrics Row
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Bitcoin", f"${btc_p:,.0f}", f"{btc_d:.2f}")
    m2.metric("Ethereum", f"${eth_p:,.0f}", f"{eth_d:.2f}")
    m3.metric("Solana", f"${sol_p:.2f}", f"{sol_d:.2f}")
    m4.metric("Aave", f"${aave_p:.2f}", f"{aave_d:.2f}")

    # A "Fake" Market Table to look like a pro dashboard
    st.write("### Total Value Locked (TVL)")
    market_data = pd.DataFrame({
        'Asset': ['USDC', 'ETH', 'WBTC', 'DAI'],
        'Total Supplied': ['$450M', '$210M', '$180M', '$95M'],
        'Supply APY': ['4.5%', '3.2%', '1.8%', '5.1%'],
        'Total Borrowed': ['$320M', '$150M', '$60M', '$70M'],
        'Borrow APY': ['6.1%', '4.5%', '2.5%', '7.2%']
    })
    st.dataframe(market_data, use_container_width=True)

# --- TAB 2: STAKING (Interactive) ---
with tab_stake:
    st.subheader("Earn Yield")
    
    c1, c2 = st.columns([1, 2])
    
    with c1:
        st.info("Choose a Pool to Stake")
        pool = st.selectbox("Select Asset", ["Prime ETH (4.5%)", "Stable USDC (8.2%)"])
        amount = st.number_input("Amount to Stake", value=10.0)
        st.button("Approve & Stake")
        
    with c2:
        st.success(f"**Projected Monthly Earnings:** ${(amount * 0.045 / 12) * 1000:,.2f} USD")
        st.write("Your funds are audited and secured by Prime Protocol smart contracts.")
        st.progress(65, text="Pool Capacity")

# --- TAB 3: BORROW (Lending Interface) ---
with tab_borrow:
    st.subheader("Instant Liquidity")
    st.write("Collateralize your assets to borrow stablecoins.")
    
    b1, b2 = st.columns(2)
    
    with b1:
        st.markdown("#### 1. Deposit Collateral")
        st.selectbox("Collateral Asset", ["ETH", "WBTC", "SOL"])
        st.text_input("Deposit Amount", "0.00")
    
    with b2:
        st.markdown("#### 2. Borrow Funds")
        st.selectbox("Borrow Asset", ["USDC", "USDT", "DAI"])
        st.text_input("Borrow Amount", "0.00")
        
    st.warning("Liquidation Threshold: 82.5%")
    st.button("Execute Borrow Transaction")
