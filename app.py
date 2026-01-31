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
        st.write("Not all blockchains are the same. Some are heavy trucks (ETH), some are race cars (SOL).")
        c1, c2 = st.columns(2)
        with c1:
            st.info("**Ethereum:** Secure, but expensive.")
            st.info("**Solana:** Fast, but less stable.")
        with c2:
            st.info("**Avalanche:** Custom networks.")
            st.info("**Base:** Cheap transactions on Ethereum.")

    # --- EXPANDED LESSON 2 ---
    with st.expander("Lesson 2: Smart Contracts (The 'Robot Lawyer')"):
        st.subheader("1. The Vending Machine Analogy")
        st.write("""
        A traditional contract (like buying a house) requires lawyers, notaries, and banks to verify it.
        
        A **Smart Contract** is like a **Vending Machine**:
        * **Input:** You insert $2.00.
        * **Logic:** You press 'A1'.
        * **Output:** The machine *must* drop the soda. 
        * **No Employee Needed:** The machine doesn't get tired, doesn't need a bribe, and can't change its mind.
        """)
        
        st.divider()
        
        st.subheader("2. Real World Examples")
        c_ex1, c_ex2 = st.columns(2)
        with c_ex1:
            st.info("🏦 **DeFi Lending (Aave)**")
            st.write("You want to borrow money. Instead of a bank credit check, the code says: *'If user deposits 1 Bitcoin collateral, let them borrow $50,000. If Bitcoin drops 20%, sell it to pay back the loan.'*")
        with c_ex2:
            st.info("🎨 **NFTs & Gaming**")
            st.write("In a video game: *'If player defeats the Boss Level, automatically generate the Golden Sword NFT and send it to their wallet.'* No game master needed.")

        st.divider()
        
        st.subheader("3. See the Logic (Kickstarter Example)")
        st.write("Imagine a fundraising site where the money is *only* released if the goal is met.")
        st.code("""
        # This code lives on the blockchain forever
        function fund_project():
            if total_donations >= $10,000:
                send_money_to_creator()
            else:
                refund_all_donors()
        """, language="python")
        
        st.warning("⚠️ **Note:** Once deployed, this code cannot be changed. If there is a bug, it stays there. This is why 'Audits' are so important in crypto.")

    with st.expander("Lesson 3: Consensus & Staking"):
        st.write("How strangers agree on truth.")
        c1, c2 = st.columns(2)
        with c1:
            st.warning("Miners (Proof of Work): Solve puzzles.")
        with c2:
            st.success("Validators (Proof of Stake): Lock up money.")
        st.info("Liquid Staking = Valet Parking (Get a claim ticket for your parked car).")

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
