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
    
    /* Code Block Styling */
    code {
        color: #e83e8c;
        background-color: #f1f3f5;
        padding: 2px 4px;
        border-radius: 4px;
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

    # --- EXPANDED LESSON 2 ---
    with st.expander("Lesson 2: Smart Contracts (The 'Robot Lawyer')"):
        st.subheader("1. The Vending Machine Analogy")
        st.write("""
        Think of a traditional contract like a **Restaurant**: You order food, eat it, and then pay. If you refuse to pay, the restaurant has to call the police (a middleman).
        
        A Smart Contract is like a **Vending Machine**:
        * **You put money in.**
        * **The machine drops the snack.**
        * **No middleman required.** The machine *cannot* cheat you. If you don't put money in, it gives no snack. If you do, it *must* give the snack.
        """)
        
        st.subheader("2. Real World Example: Flight Insurance")
        st.write("""
        **Old Way:** Your flight is cancelled. You call insurance, wait on hold, fill out forms, and wait 3 weeks for a check.
        
        **Smart Contract Way:**
        1. You buy a policy on the blockchain.
        2. The contract is connected to Flight Data.
        3. **IF** `Flight #902` is `Cancelled` -> **THEN** `Send $500 to Your Wallet` instantly.
        """)
        
        st.subheader("3. The Logic (If-This-Then-That)")
        st.code("""
        # This is how the code actually thinks:
        
        function pay_insurance():
            if flight_status == "CANCELLED":
                send_money(customer_wallet, $500)
            else:
                keep_premium()
        """, language="python")
        st.success("Result: No lawyers, no waiting, no 'claim denied' by a human.")

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

    with st.expander("Lesson 5: 🛡️ Security & Scams (CRITICAL)"):
        st.error("⚠️ THE GOLDEN RULE: Never, ever share your Seed Phrase.")
        st.write("""
        **1. The Seed Phrase:** 12-24 random words. If you lose them, you lose your money. If someone else gets them, they steal your money.
        **2. Phishing:** Always check the URL (e.g., `Coinbaze.com` is a fake).
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
