import streamlit as st
import pandas as pd
import yfinance as yf
import time

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Bit Solutions Academy",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    .stApp { background-color: #212529; }
    h1, h2, h3 { color: #F8F9FA !important; }
    p, li { color: #DDE2E6 !important; font-size: 1.1em; line-height: 1.6; }
    
    /* Info Boxes */
    div[data-baseweb="notification"] {
        background-color: #0D47A1;
        color: white;
    }
    
    /* Hide Menu */
    #MainMenu, footer, header {visibility: hidden;}
    
    /* Tabs */
    .stTabs [data-baseweb="tab-list"] { gap: 10px; }
    .stTabs [data-baseweb="tab"] {
        background-color: #2C3035;
        color: #ADB5BD;
        border: 1px solid #343A40;
    }
    .stTabs [aria-selected="true"] {
        background-color: #198754;
        color: #FFFFFF !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER ---
col1, col2 = st.columns([3, 1])
with col1:
    st.title("BIT SOLUTIONS ACADEMY")
    st.caption("Master the Future of Decentralized Finance")
with col2:
    st.button("🎓 Enroll Free")

st.markdown("---")

# --- NAVIGATION ---
tab_learn, tab_sim, tab_data = st.tabs(["📖 Learn Concepts", "🧪 Lab Simulation", "📊 Live Market"])

# --- TAB 1: THE CLASSROOM ---
with tab_learn:
    st.header("Blockchain Fundamentals")
    
    with st.expander("Lesson 1: What is a Blockchain?"):
        st.write("""
        Imagine a Google Doc that **nobody can delete or edit**, only add to.
        * **Decentralized:** No single bank owns it. It lives on thousands of computers.
        * **Immutable:** Once a transaction is written, it is carved in stone.
        """)
        st.info("💡 Key Concept: 'Trustless' means you don't need to trust a stranger; you only need to trust the code.")

    with st.expander("Lesson 2: Smart Contracts"):
        st.write("""
        A Smart Contract is just **digital vending machine code**.
        * **Input:** You send 1 ETH.
        * **Code:** If 1 ETH is received -> Send 1 NFT.
        * **Output:** You get your NFT instantly.
        """)
        
    with st.expander("Lesson 3: Proof of Work vs. Stake"):
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("#### ⛏️ Proof of Work (Bitcoin)")
            st.write("Miners use massive electricity to solve math puzzles.")
        with c2:
            st.markdown("#### 🥩 Proof of Stake (Ethereum)")
            st.write("Validators 'lock up' their coins to secure the network.")
            
    with st.expander("Lesson 4: Digital Wallets (Your Bank Account)"):
        st.write("""
        * **🔥 Hot Wallet (Software):** An app on your phone. Convenient but online. (Example: Coinbase).
        * **❄️ Cold Wallet (Hardware):** A USB stick that stays offline. Extremely secure. (Example: Ledger).
        """)
        st.link_button("Download Coinbase App ↗", "https://www.coinbase.com")

    # --- NEW LESSON 5: SECURITY ---
    with st.expander("Lesson 5: 🛡️ Security & Scams (CRITICAL)"):
        st.error("⚠️ THE GOLDEN RULE: Never, ever share your Seed Phrase.")
        
        st.write("""
        **1. The Seed Phrase (Recovery Phase)**
        When you create a wallet, you get 12-24 random words. 
        * **If you lose these words:** You lose your money forever.
        * **If someone else gets them:** They steal your money instantly.
        * **Support will NEVER ask for this.**
        
        **2. Phishing Scams**
        Hackers create fake websites that look like the real thing (e.g., `Coinbaze.com` instead of `Coinbase.com`).
        * **Always check the URL.**
        * **Bookmark your favorite sites.**
        
        **3. Two-Factor Authentication (2FA)**
        Turn this on everywhere! Use an app like **Google Authenticator**, not SMS text messages (which can be hacked).
        """)

# --- TAB 2: THE SANDBOX ---
with tab_sim:
    st.header("Interactive Sandbox")
    st.write("Don't just read about it. **Try it.** (Simulation only).")
    
    col_sim_1, col_sim_2 = st.columns(2)
    
    with col_sim_1:
        st.subheader("Try a Token Swap")
        sell = st.selectbox("Sell Asset", ["USDC (Stablecoin)", "ETH (Volatile)"])
        amount = st.number_input("Amount to Sell", value=100)
        
        if st.button("Simulate Swap"):
            with st.spinner("Finding Liquidity Route..."):
                time.sleep(1)
            st.success(f"✅ Swapped {amount} {sell} successfully!")

    with col_sim_2:
        st.subheader("Understand Staking Yield")
        st.write("If you lock **10 ETH** for **1 Year** at **5% APY**...")
        if st.button("Calculate Reward"):
            st.balloons()
            st.metric("You Earn", "+0.5 ETH", "Passive Income")

# --- TAB 3: REAL WORLD DATA ---
with tab_data:
    st.header("Live Market Data")
    
    def get_price(t):
        try:
            d = yf.Ticker(t).history(period="1d")
            return d["Close"].iloc[-1]
        except: return 0.0

    btc = get_price("BTC-USD")
    eth = get_price("ETH-USD")
    
    m1, m2, m3 = st.columns(3)
    m1.metric("Bitcoin Price", f"${btc:,.0f}")
    m2.metric("Ethereum Price", f"${eth:,.0f}")
    m3.metric("Gas Fee (Est)", "12 Gwei", "Low Cost")
    
    st.line_chart(yf.Ticker("BTC-USD").history(period="1mo")["Close"])
    st.caption("1-Month Bitcoin Trend")
