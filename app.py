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

# --- SESSION STATE (Track if user is on Cover or Main) ---
if 'page' not in st.session_state:
    st.session_state.page = 'cover'

def enter_site():
    st.session_state.page = 'main'

# --- CUSTOM CSS (Cyber Blue Theme) ---
st.markdown("""
    <style>
    /* BACKGROUND IMAGE SETTINGS */
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
    
    /* Info Boxes */
    div[data-baseweb="notification"] {
        background-color: rgba(13, 71, 161, 0.8);
        color: white;
        border: 1px solid #1976D2;
        backdrop-filter: blur(5px);
    }
    
    /* Buttons (Make them pop) */
    div.stButton > button {
        background-color: #00BFA5;
        color: white;
        border: none;
        padding: 10px 24px;
        font-size: 1.2em;
        border-radius: 8px;
        transition: all 0.3s;
    }
    div.stButton > button:hover {
        background-color: #009688;
        box-shadow: 0px 0px 10px #00BFA5;
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
        background-color: #00BFA5;
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

# ==========================================
# PAGE 1: THE COVER PAGE (SPLASH SCREEN)
# ==========================================
if st.session_state.page == 'cover':
    # Centering mechanism using columns
    c1, c2, c3 = st.columns([1, 2, 1])
    
    with c2:
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.title("BIT SOLUTIONS ACADEMY")
        st.markdown("<h3 style='text-align: left; color: #00BFA5 !important;'>Master the Future of Finance.</h3>", unsafe_allow_html=True)
        st.write("""
        Welcome to the next generation of financial education. 
        Learn how Blockchain, Smart Contracts, and DeFi are rewriting the rules of money.
        """)
        
        st.write("")
        st.write("---")
        st.write("")
        
        # Big Start Button
        if st.button("🚀 Enter Academy"):
            enter_site()
            st.rerun()

# ==========================================
# PAGE 2: THE MAIN ACADEMY (FULL CONTENT)
# ==========================================
else:
    # --- HEADER ---
    col1, col2 = st.columns([3, 1])
    with col1:
        st.title("BIT SOLUTIONS ACADEMY")
        st.caption("Classroom Dashboard")
    with col2:
        if st.button("⬅ Exit to Cover"):
            st.session_state.page = 'cover'
            st.rerun()

    st.markdown("---")

    # --- NAVIGATION ---
    tab_learn, tab_sim, tab_data = st.tabs(["📖 Learn Concepts", "🧪 Lab Simulation", "📊 Live Market"])

    # --- TAB 1: THE CLASSROOM ---
    with tab_learn:
        st.header("Blockchain Fundamentals")
        
        with st.expander("Lesson 1: Blockchain Basics & Real World Use"):
            st.subheader("1. What IS a Blockchain?")
            st.write("Think of a Blockchain like a **shared Google Sheet** that everyone can read, but NO ONE can delete.")
            
            c_concept1, c_concept2 = st.columns(2)
            with c_concept1:
                st.info("🧱 **The 'Block' (The Page)**")
                st.write("Imagine a notebook page filled with transactions. Once full, it gets sealed.")
            with c_concept2:
                st.info("🔗 **The 'Chain' (The Glue)**")
                st.write("Each page is mathematically glued to the previous one. You cannot rip out old pages.")
            
            st.divider()
            
            st.subheader("2. Beyond Money: Real World Use Cases")
            c_use1, c_use2 = st.columns(2)
            with c_use1:
                st.success("🚚 **Supply Chain (Walmart)**")
                st.write("Walmart traces mangoes to the farm in 2.2 seconds.")
            with c_use2:
                st.success("🏠 **Real Estate (Tokenization)**")
                st.write("Buy 1/100th of a house instantly.")
                
            st.divider()
            st.subheader("3. The Origin")
            st.write("It all started in 2008 with a whitepaper by **Satoshi Nakamoto**.")
            st.link_button("📄 Read the Bitcoin Whitepaper (PDF)", "https://bitcoin.org/bitcoin.pdf")

        with st.expander("Lesson 2: Smart Contracts (The 'Robot Lawyer')"):
            st.subheader("1. What makes it 'Smart'?")
            st.write("A Smart Contract is just **Programmable Money**. It's code that holds money and releases it only when a condition is met.")
            st.info("💡 **Think:** 'If This Happens, Then Pay That.'")

            st.divider()

            st.subheader("2. The Vending Machine Analogy")
            st.write("The best way to understand it is to compare a **Human Barista** vs. a **Vending Machine**.")
            
            c_human, c_bot = st.columns(2)
            with c_human:
                st.error("☕ The Old Way (Human Contract)")
                st.write("Slow, Expensive, Trust-Based.")
            with c_bot:
                st.success("🤖 The New Way (Smart Contract)")
                st.write("Instant, Cheap, Trustless.")
            
            st.divider()
            st.subheader("3. A Simple Example: The Sports Bet")
            st.write("Two friends bet on the Super Bowl. The code holds the money and automatically pays the winner based on the official score. No fighting.")

        # --- REVERTED LESSON 3 (Simple Version) ---
        with st.expander("Lesson 3: The 3 Types of Staking (Detailed Breakdown)"):
            st.write("In crypto, there is no CEO. The network runs itself. But how do we stop people from cheating? We use **Consensus Mechanisms**.")
            
            c_pow, c_pos = st.columns(2)
            with c_pow:
                st.subheader("⛏️ 1. Proof of Work (Bitcoin)")
                st.info("**The 'Hardware Race'**")
                st.write("""
                * **Who runs it:** "Miners" with powerful computers.
                * **How it works:** They race to solve a math puzzle.
                * **Security:** Extremely high.
                * **Downside:** High energy use.
                """)
            with c_pos:
                st.subheader("🥩 2. Proof of Stake (Ethereum)")
                st.info("**The 'Financial Bond'**")
                st.write("""
                * **Who runs it:** "Validators" who lock up money.
                * **How it works:** Random selection based on deposit size.
                * **Security (Slashing):** If they cheat, the network takes their money.
                * **Downside:** Rich get richer.
                """)
            
            st.divider()
            st.subheader("💧 3. Liquid Staking")
            st.write("Regular staking locks your money. **Liquid Staking** gives you a 'Receipt Token' (stETH) that you can still use/sell.")
            st.success("Result: Earn interest + Keep liquidity.")

        # --- EXPANDED LESSON 4 (Beginner's Guide) ---
        with st.expander("Lesson 4: What actually IS a Wallet? (A Beginner's Guide)"):
            st.subheader("1. The Big Misconception")
            st.write("""
            **Stop thinking of it as a 'Leather Wallet'.**
            Your crypto is **NOT** inside the app. It is **NOT** inside the USB stick.
            
            * **The Blockchain:** Is the cloud (like Google Drive) where the money lives.
            * **Your Wallet:** Is just the **Password (Key)** that lets you move that money.
            
            *If you lose your phone, your money is still safe on the cloud... IF you have your Key.*
            """)
            
            st.divider()

            st.subheader("2. The Email Analogy (Public vs. Private Keys)")
            st.write("Every wallet comes with a Key Pair. It works exactly like Email.")
            
            c_key1, c_key2 = st.columns(2)
            with c_key1:
                st.success("🟢 Public Key (The Address)")
                st.write("""
                * **Like your:** Email Address.
                * **Function:** You give this to people so they can send you money.
                * **Safety:** 100% Safe to share on Instagram/Twitter.
                * **Looks like:** `0x71C...9A23`
                """)
            with c_key2:
                st.error("🔴 Private Key (The Seed Phrase)")
                st.write("""
                * **Like your:** Email Password.
                * **Function:** This signs the check to move the money out.
                * **Safety:** NEVER SHARE THIS. Anyone who sees it owns your money.
                * **Looks like:** 12 random words (`apple river galaxy...`).
                """)

            st.divider()

            st.subheader("3. Hot vs. Cold Wallets (Which do I need?)")
            
            c_hot, c_cold = st.columns(2)
            with c_hot:
                st.warning("🔥 Hot Wallet (Software)")
                st.write("""
                * **What is it?** An app on your phone (like Coinbase Wallet).
                * **Best for:** Spending, trading, small amounts.
                * **Risk:** It's connected to the internet, so hackers *could* reach it.
                """)
            with c_cold:
                st.info("❄️ Cold Wallet (Hardware)")
                st.write("""
                * **What is it?** A USB stick (like Ledger) that stays offline.
                * **Best for:** Life savings, long-term holding.
                * **Security:** Unhackable unless you physically give it away.
                """)

            st.divider()
            st.write("**Top Recommendations:**")
            
            btn1, btn2, btn3 = st.columns(3)
            with btn1:
                st.link_button("Coinbase (Hot Wallet) ↗", "https://www.coinbase.com")
            with btn2:
                st.link_button("Ledger (Cold Wallet) ↗", "https://www.ledger.com")
            with btn3:
                st.link_button("Tangem (Card Wallet) ↗", "https://tangem.com")

        with st.expander("Lesson 5: 🛡️ Security & Scams (THE SURVIVAL GUIDE)"):
            st.error("⚠️ THE GOLDEN RULE: Never, ever share your Seed Phrase with anyone. Support will NEVER ask for it.")
            
            st.subheader("1. Storage Security (Paper vs. Cloud)")
            st.write("""
            * **✅ CORRECT:** Write it on paper. Store in physical safe.
            * **❌ WRONG:** Screenshot, Google Drive, Email.
            """)
            
            st.divider()
            
            st.subheader("2. Advanced Threats (Know Your Enemy)")
            c_scam_1, c_scam_2 = st.columns(2)
            with c_scam_1:
                st.warning("📋 **Clipboard Hijacking**")
                st.write("Malware that swaps copied addresses. Always check the first 4 and last 4 digits.")
            with c_scam_2:
                st.warning("🔓 **The 'Unlimited Approval' Trap**")
                st.write("Fake sites ask for unlimited permission. Read the popup before clicking Approve.")

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
