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
    
    with st.expander("Lesson 1: The 'Flavors' of Blockchain (ETH, SOL, AVAX, BASE)"):
        st.write("""
        Not all blockchains are the same. Think of them like **vehicles**—some are built for heavy cargo, some for racing.
        """)
        c1, c2 = st.columns(2)
        with c1:
            st.info("**Ethereum (The Semi-Truck):** Secure, heavy duty, but can be slow.")
            st.info("**Solana (The Race Car):** Fast and cheap, but has had engine trouble.")
        with c2:
            st.info("**Avalanche (The Fleet):** Custom networks for specific businesses.")
            st.info("**Base (The Express Lane):** Built on top of Ethereum to save costs.")

    with st.expander("Lesson 2: Smart Contracts (The 'Robot Lawyer')"):
        st.subheader("The Vending Machine Analogy")
        st.write("A Smart Contract is a vending machine: You put money in, the snack comes out. No employee needed.")
        st.code("""
        function pay_insurance():
            if flight_status == "CANCELLED":
                send_money(customer, $500)
        """, language="python")

    # --- EXPANDED LESSON 3 ---
    with st.expander("Lesson 3: Consensus & Staking (How It Works)"):
        st.write("How do strangers agree on who owns what without a bank? They use a 'Consensus Mechanism'.")
        
        col_pow, col_pos = st.columns(2)
        
        with col_pow:
            st.subheader("⛏️ Proof of Work (Bitcoin)")
            st.info("**The 'Sudoku Puzzle' Method**")
            st.write("""
            * **How it works:** Computers (Miners) race to solve a super-hard math puzzle. The winner gets to write the next page of the ledger.
            * **Why it's secure:** To cheat, you would need more electricity than a small country.
            * **Downside:** Uses a lot of energy.
            """)
            
        with col_pos:
            st.subheader("🥩 Proof of Stake (Ethereum)")
            st.info("**The 'Security Deposit' Method**")
            st.write("""
            * **How it works:** Instead of burning energy, Validators lock up their own money (32 ETH) as a security deposit.
            * **Why it's secure:** If a Validator tries to cheat, the network confiscates their deposit (called "Slashing").
            * **Benefit:** 99.9% less energy usage.
            """)
            
        st.divider()
        
        st.subheader("💧 What is Liquid Staking?")
        st.warning("Advanced Concept: Solving the 'Locked Money' Problem")
        
        st.write("""
        **The Problem:** When you stake ETH, it is locked. You can't sell it or use it. It's stuck.
        
        **The Solution (Liquid Staking):** Imagine **Valet Parking**.
        1. You give your car (ETH) to the Valet (Lido or Rocket Pool).
        2. The Valet gives you a **Claim Ticket** (`stETH`).
        3. **The Magic:** This Claim Ticket has value! You can sell the ticket, lend the ticket, or use the ticket as collateral—all while your car is still parked safely.
        
        **Result:** You earn Staking Rewards (Parking Rewards) + You can still use your funds (The Ticket) in DeFi.
        """)

    with st.expander("Lesson 4: Digital Wallets"):
        st.write("Hot Wallets (Online Apps) vs Cold Wallets (Offline USB Sticks).")
        st.link_button("Download Coinbase App ↗", "https://www.coinbase.com")

    with st.expander("Lesson 5: 🛡️ Security & Scams"):
        st.error("⚠️ THE GOLDEN RULE: Never share your Seed Phrase.")

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
    sol = get_price("SOL-USD")
    
    m1, m2, m3 = st.columns(3)
    m1.metric("Bitcoin", f"${btc:,.0f}")
    m2.metric("Ethereum", f"${eth:,.0f}")
    m3.metric("Solana", f"${sol:.2f}")
    
    st.line_chart(yf.Ticker("BTC-USD").history(period="1mo")["Close"])
    st.caption("Bitcoin Price Trend")
