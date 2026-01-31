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

# --- CUSTOM CSS (New Cyber Background) ---
st.markdown("""
    <style>
    /* BACKGROUND IMAGE SETTINGS 
       New Image: A smooth, dark digital wave/circuit feel.
       Tint: Slightly darker (0.90) to ensure text pops perfectly.
    */
    .stApp {
        background-image: linear-gradient(rgba(0, 0, 0, 0.90), rgba(0, 0, 0, 0.90)), 
                          url('https://images.unsplash.com/photo-1550751827-4bd374c3f58b?q=80&w=2940&auto=format&fit=crop');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }
    
    /* Text Readability */
    h1, h2, h3 { color: #FFFFFF !important; text-shadow: 0px 2px 4px rgba(0,0,0,0.5); }
    p, li { color: #E0E0E0 !important; font-size: 1.1em; line-height: 1.6; }
    
    /* Info Boxes - made them slightly more transparent to blend with the cyber look */
    div[data-baseweb="notification"] {
        background-color: rgba(13, 71, 161, 0.8);
        color: white;
        border: 1px solid #1976D2;
        backdrop-filter: blur(5px); /* Glassmorphism effect */
    }
    
    /* Hide Menu */
    #MainMenu, footer, header {visibility: hidden;}
    
    /* Tabs */
    .stTabs [data-baseweb="tab-list"] { gap: 10px; }
    .stTabs [data-baseweb="tab"] {
        background-color: rgba(33, 37, 41, 0.9);
        color: #ADB5BD;
        border: 1px solid #343A40;
    }
    .stTabs [aria-selected="true"] {
        background-color: #00BFA5; /* Cyber Teal Highlight */
        color: #FFFFFF !important;
        border-color: #00BFA5;
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
        st.write("**The Flavors:** ETH (Truck), SOL (Race Car), AVAX (Fleet), BASE (Express Lane).")

    with st.expander("Lesson 2: Smart Contracts (The 'Robot Lawyer')"):
        st.subheader("1. The Vending Machine Analogy (Deep Dive)")
        st.write("The best way to understand a Smart Contract is to compare a **Barista** vs. a **Vending Machine**.")
        c_human, c_bot = st.columns(2)
        with c_human:
            st.error("☕ The Human Way")
            st.write("Subjective, biased, and requires trust.")
        with c_bot:
            st.success("🤖 The Smart Contract")
            st.write("Deterministic, unbiased, and trustless.")
            
        st.divider()
        st.subheader("2. Try it Real Life")
        c_app1, c_app2 = st.columns(2)
        with c_app1:
            st.info("🏦 **Aave (Lending)**")
            st.link_button("Visit Aave ↗", "https://aave.com")
        with c_app2:
            st.info("⚡ **Drift (Trading)**")
            st.link_button("Visit Drift ↗", "https://www.drift.trade")

        st.divider()
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

    with st.expander("Lesson 4: What actually IS a Wallet? (Keys explained)"):
        st.subheader("1. The Big Misconception: 'The Bag vs. The Browser'")
        st.write("The wallet is just a **Web Browser** that views your money on the blockchain.")
        
        st.divider()
        st.subheader("2. The Keys: Public vs. Private")
        c_key1, c_key2 = st.columns(2)
        with c_key1:
            st.success("🟢 Public Key (The 'Account Number')")
            st.write("Like your Email Address. Safe to share.")
        with c_key2:
            st.error("🔴 Private Key (The 'PIN Code')")
            st.write("Like your Password. NEVER share this.")
            
        st.divider()
        st.write("**Types of Wallets:**")
        st.write("* **Hot Wallet:** Online app (Coinbase). Good for spending.")
        st.write("* **Cold Wallet:** Offline USB (Ledger). Good for saving.")
        st.link_button("Download Coinbase App (Hot Wallet) ↗", "https://www.coinbase.com")

    with st.expander("Lesson 5: 🛡️ Security & Scams (HOW TO SURVIVE)"):
        st.error("⚠️ THE GOLDEN RULE: Never, ever share your Seed Phrase with anyone. Support will NEVER ask for it.")
        
        st.subheader("1. The 'Paper vs. Cloud' Rule")
        st.write("""
        * **✅ CORRECT:** Write seed phrase on paper. Store in safe.
        * **❌ WRONG:** Do not screenshot. Do not save in Cloud.
        """)
        
        st.divider()
        st.subheader("2. Common Attack Vectors")
        c_scam_1, c_scam_2 = st.columns(2)
        with c_scam_1:
            st.warning("🎣 **Phishing Sites**")
            st.write("Fake sites like `Coinbaze.com`. Bookmark the real one.")
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
