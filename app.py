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
    
    with st.expander("Lesson 1: Blockchain Basics & Real World Use"):
        st.subheader("1. The Origin")
        st.write("In 2008, Satoshi Nakamoto released the Bitcoin Whitepaper.")
        st.link_button("📄 Read the Bitcoin Whitepaper (PDF)", "https://bitcoin.org/bitcoin.pdf")
        
        st.divider()
        st.subheader("2. Real World Use")
        c_use1, c_use2 = st.columns(2)
        with c_use1:
            st.info("🚚 **Supply Chain (Walmart)**")
            st.write("Tracking food from farm to store to prevent disease.")
        with c_use2:
            st.info("🏥 **Healthcare Records**")
            st.write("Patient data controlled by the patient, not the hospital.")
            
        st.divider()
        st.write("**The Flavors:** ETH (Truck), SOL (Race Car), AVAX (Fleet), BASE (Express Lane).")

    # --- EXPANDED LESSON 2 ---
    with st.expander("Lesson 2: Smart Contracts (The 'Robot Lawyer')"):
        st.subheader("1. The Vending Machine Analogy (Deep Dive)")
        st.write("""
        The best way to understand a Smart Contract is to compare a **Barista** vs. a **Vending Machine**.
        """)
        
        c_human, c_bot = st.columns(2)
        
        with c_human:
            st.error("☕ The Human Way (The Barista)")
            st.write("""
            * **Subjective:** They might be tired, grumpy, or mishear your order.
            * **Bias:** They might serve their friend before you.
            * **Trust Required:** You have to trust that they won't steal your change.
            """)
            
        with c_bot:
            st.success("🤖 The Smart Contract (The Vending Machine)")
            st.write("""
            * **Deterministic:** If you put in $2.00, the soda drops. Every single time.
            * **Unbiased:** It doesn't care who you are (rich, poor, famous).
            * **Trustless:** You don't trust the machine; you trust the **mechanism**. If the money goes in, the product comes out.
            """)
            
        st.write("""
        **Why this matters for Crypto:** A Smart Contract locks the money inside the "machine." Nobody—not even the person who built the machine—can steal the funds once the code is running.
        """)
        
        st.divider()
        
        st.subheader("2. Try it Real Life (Live Apps)")
        st.write("These are not websites run by companies. They are **Smart Contracts** that run themselves.")
        
        c_app1, c_app2 = st.columns(2)
        
        with c_app1:
            st.info("🏦 **Aave (on Ethereum)**")
            st.write("Replaces the Bank. The code holds the money and pays interest automatically.")
            st.link_button("Visit Aave Protocol ↗", "https://aave.com")
            
        with c_app2:
            st.info("⚡ **Drift (on Solana)**")
            st.write("Replaces the Stock Broker. The code executes trades instantly.")
            st.link_button("Visit Drift Protocol ↗", "https://www.drift.trade")

        st.divider()
        
        st.subheader("3. Code Example")
        st.code("""
        function fund_project():
            if total_donations >= $10,000:
                send_money_to_creator()
            else:
                refund_all_donors()
        """, language="python")

    with st.expander("Lesson 3: Consensus & Liquid Staking (The 'Valet' Analogy)"):
        st.write("In crypto, there is no CEO. So how do we agree on the truth? We use **Consensus**.")
        c_pow, c_pos = st.columns(2)
        with c_pow:
            st.subheader("⛏️ Proof of Work (Bitcoin)")
            st.info("**The 'Sudoku Puzzle'**")
            st.write("Miners race to solve hard math puzzles. Secure, but high energy.")
        with c_pos:
            st.subheader("🥩 Proof of Stake (Ethereum)")
            st.info("**The 'Security Deposit'**")
            st.write("Validators lock up money as a bond. Efficient, but strict rules.")
            
        st.divider()
        st.subheader("💧 Liquid Staking (The 'Valet' Analogy)")
        st.warning("Regular staking locks your car. Liquid staking gives you a claim ticket you can still use.")

    with st.expander("Lesson 4: What actually IS a Wallet?"):
        st.subheader("1. The Big Misconception")
        st.write("The wallet is the **Remote Control**, not the money vault.")
        
        st.subheader("2. The Email Analogy")
        c_mail_1, c_mail_2 = st.columns(2)
        with c_mail_1:
            st.success("🟢 Public Key (Email Address)")
            st.write("Share this with anyone to receive money.")
        with c_mail_2:
            st.error("🔴 Private Key (Password)")
            st.write("NEVER share this. It allows spending.")
            
        st.divider()
        st.write("**Types of Wallets:**")
        st.write("* **Hot Wallet:** Online app (Coinbase). Good for spending.")
        st.write("* **Cold Wallet:** Offline USB (Ledger). Good for saving.")
        st.link_button("Download Coinbase App (Hot Wallet) ↗", "https://www.coinbase.com")

    with st.expander("Lesson 5: 🛡️ Security & Scams (HOW TO SURVIVE)"):
        st.error("⚠️ THE GOLDEN RULE: Never, ever share your Seed Phrase with anyone. Support will NEVER ask for it.")
        
        st.subheader("1. The 'Paper vs. Cloud' Rule")
        st.write("""
        When you create a wallet, you get 12-24 words.
        * **✅ CORRECT:** Write them on paper. Store it in a fireproof safe.
        * **❌ WRONG:** Do not take a screenshot. Do not save in Google Drive.
        """)
        
        st.divider()
        st.subheader("2. Common Attack Vectors")
        c_scam_1, c_scam_2 = st.columns(2)
        with c_scam_1:
            st.warning("🎣 **Phishing Sites**")
            st.write("Fake sites like `Coinbaze.com`. Always bookmark the real one.")
        with c_scam_2:
            st.warning("📱 **SIM Swapping (2FA)**")
            st.write("Never use SMS for 2FA. Use Google Authenticator.")

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
