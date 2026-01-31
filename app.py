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
    
    # --- EXPANDED LESSON 1 ---
    with st.expander("Lesson 1: The 'Flavors' of Blockchain (ETH, SOL, AVAX, BASE)"):
        st.write("""
        Not all blockchains are the same. Think of them like **vehicles**—some are built for heavy cargo, some for racing, and some for cheap commuting.
        """)
        
        c1, c2 = st.columns(2)
        
        with c1:
            st.markdown("### 🔵 Ethereum (The World Computer)")
            st.info("**Role: The Heavy Duty Semi-Truck**")
            st.write("""
            * **What is it?** The first blockchain to introduce Smart Contracts.
            * **Pros:** Extremely secure, massive ecosystem, most money is here.
            * **Cons:** Can be slow and expensive ("Gas Fees") during busy times.
            """)
            
            st.markdown("### 🟣 Solana (The Speedster)")
            st.info("**Role: The F1 Race Car**")
            st.write("""
            * **What is it?** Built purely for speed and low cost.
            * **Pros:** Transactions cost $0.0001 and settle in milliseconds.
            * **Cons:** Has had network outages in the past (sacrifices some stability for speed).
            """)

        with c2:
            st.markdown("### 🔺 Avalanche (The Network of Networks)")
            st.info("**Role: The Fleet of Custom Vans**")
            st.write("""
            * **What is it?** Allows companies to build their *own* custom blockchains ("Subnets").
            * **Pros:** Highly scalable; gaming companies love it.
            * **Cons:** More complex to understand than a single chain.
            """)
            
            st.markdown("### 🔵 Base (The Layer 2 Helper)")
            st.info("**Role: The Express Lane**")
            st.write("""
            * **What is it?** Base is built *on top* of Ethereum (by Coinbase).
            * **How it works:** It bundles 1,000 transactions into one package and sends it to Ethereum.
            * **Result:** You get Ethereum's security but with 90% lower fees.
            """)

    with st.expander("Lesson 2: Smart Contracts (The 'Robot Lawyer')"):
        st.subheader("1. The Vending Machine Analogy")
        st.write("""
        A Smart Contract is like a **Vending Machine**:
        * **You put money in.**
        * **The machine drops the snack.**
        * **No middleman required.** The machine *cannot* cheat you.
        """)
        
        st.subheader("2. Real World Example: Flight Insurance")
        st.write("""
        **Old Way:** Call insurance, wait on hold, fill forms, wait weeks.
        **Smart Contract Way:** IF `Flight #902` is `Cancelled` -> THEN `Send $500` instantly.
        """)
        
        st.code("""
        function pay_insurance():
            if flight_status == "CANCELLED":
                send_money(customer, $500)
        """, language="python")

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
        * **🔥 Hot Wallet:** App on your phone (e.g., Coinbase). Good for spending.
        * **❄️ Cold Wallet:** USB stick (e.g., Ledger). Good for saving.
        """)
        st.link_button("Download Coinbase App ↗", "https://www.coinbase.com")

    with st.expander("Lesson 5: 🛡️ Security & Scams (CRITICAL)"):
        st.error("⚠️ THE GOLDEN RULE: Never share your Seed Phrase.")
        st.write("If you lose your 12-word phrase, you lose your money forever. No bank can help you.")

# --- TAB 2: THE SANDBOX ---
with tab_sim:
    st.header("Interactive Sandbox")
    st.write("Don't just read about it. **Try it.**")
    
    col_sim_1, col_sim_2 = st.columns(2)
    
    with col_sim_1:
        st.subheader("Try a Token Swap")
        sell = st.selectbox("Sell Asset", ["USDC", "ETH"])
        amount = st.number_input("Amount", value=100)
        
        if st.button("Simulate Swap"):
            with st.spinner("Finding Route..."):
                time.sleep(1)
            st.success(f"✅ Swapped {amount} {sell} successfully!")

    with col_sim_2:
        st.subheader("Staking Calculator")
        st.write("Locking **10 ETH** for **1 Year** at **5% APY**...")
        if st.button("Calculate Reward"):
            st.balloons()
            st.metric("You Earn", "+0.5 ETH")

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
    sol = get_price("SOL-USD") # Added Solana Price
    
    m1, m2, m3 = st.columns(3)
    m1.metric("Bitcoin", f"${btc:,.0f}")
    m2.metric("Ethereum", f"${eth:,.0f}")
    m3.metric("Solana", f"${sol:.2f}")
    
    st.line_chart(yf.Ticker("BTC-USD").history(period="1mo")["Close"])
    st.caption("Bitcoin Price Trend")
