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

# --- CUSTOM CSS (Readable Dark Mode) ---
st.markdown("""
    <style>
    /* Background */
    .stApp { background-color: #212529; }
    
    /* Text Readability */
    h1, h2, h3 { color: #F8F9FA !important; }
    p, li { color: #DDE2E6 !important; font-size: 1.1em; line-height: 1.6; }
    
    /* Info Boxes (Blue) */
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
        background-color: #198754; /* Green for Education */
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
    # A fun "Student Status" button
    st.button("🎓 Enroll Free")

st.markdown("---")

# --- NAVIGATION ---
tab_learn, tab_sim, tab_data = st.tabs(["📖 Learn Concepts", "🧪 Lab Simulation", "📊 Live Market"])

# --- TAB 1: THE CLASSROOM (Educational Content) ---
with tab_learn:
    st.header("Blockchain Fundamentals")
    
    # Accordions are great for teaching without overwhelming
    with st.expander("Lesson 1: What is a Blockchain?"):
        st.write("""
        Imagine a Google Doc that **nobody can delete or edit**, only add to.
        * **Decentralized:** No single bank owns it. It lives on thousands of computers.
        * **Immutable:** Once a transaction is written, it is carved in stone.
        * **Transparent:** Anyone can audit the ledger at any time.
        """)
        st.info("💡 Key Concept: 'Trustless' means you don't need to trust a stranger; you only need to trust the code.")

    with st.expander("Lesson 2: Smart Contracts"):
        st.write("""
        A Smart Contract is just **digital vending machine code**.
        * **Input:** You send 1 ETH.
        * **Code:** If 1 ETH is received -> Send 1 NFT.
        * **Output:** You get your NFT instantly, without a lawyer or middleman.
        """)
        
    with st.expander("Lesson 3: Proof of Work vs. Stake"):
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("#### ⛏️ Proof of Work (Bitcoin)")
            st.write("Miners use massive electricity to solve math puzzles. Secure, but slow and energy-heavy.")
        with c2:
            st.markdown("#### 🥩 Proof of Stake (Ethereum)")
            st.write("Validators 'lock up' their coins to secure the network. Faster, greener, and earns yield.")

# --- TAB 2: THE SANDBOX (Interactive Learning) ---
with tab_sim:
    st.header("Interactive Sandbox")
    st.write("Don't just read about it. **Try it.** (This is a simulation, no real money is used).")
    
    col_sim_1, col_sim_2 = st.columns(2)
    
    with col_sim_1:
        st.subheader("Try a Token Swap")
        st.caption("See how decentralized exchanges (DEXs) work.")
        
        # Simple Simulator
        sell = st.selectbox("Sell Asset", ["USDC (Stablecoin)", "ETH (Volatile)"])
        amount = st.number_input("Amount to Sell", value=100)
        
        if st.button("Simulate Swap"):
            with st.spinner("Finding Liquidity Route..."):
                time.sleep(1)
            st.success(f"✅ Swapped {amount} {sell} for {amount * 0.0003 if 'USDC' in sell else amount * 2800} Tokens!")
            st.write("Notice: No bank approved this. The code just executed it.")

    with col_sim_2:
        st.subheader("Understand Staking Yield")
        st.caption("How 'locking' money earns interest.")
        
        st.write("If you lock **10 ETH** for **1 Year** at **5% APY**...")
        if st.button("Calculate Reward"):
            st.balloons()
            st.metric("You Earn", "+0.5 ETH", "Passive Income")
            st.info("In traditional banking, you get 0.01%. In DeFi, you get the full value.")

# --- TAB 3: REAL WORLD DATA ---
with tab_data:
    st.header("Live Market Data")
    st.write("This is what the actual blockchain is doing right now.")
    
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
