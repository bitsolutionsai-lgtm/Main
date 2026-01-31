import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf
import time

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Bit Solutions Academy",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- SESSION STATE ---
if 'page' not in st.session_state:
    st.session_state.page = 'cover'

def enter_site():
    st.session_state.page = 'main'

# --- CUSTOM CSS ---
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
    p, li, label { color: #E0E0E0 !important; font-size: 1.1em; line-height: 1.6; }
    
    /* Info Boxes */
    div[data-baseweb="notification"] {
        background-color: rgba(13, 71, 161, 0.8);
        color: white;
        border: 1px solid #1976D2;
        backdrop-filter: blur(5px);
    }
    
    /* Buttons */
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
    
    /* Sidebar */
    section[data-testid="stSidebar"] {
        background-color: rgba(33, 37, 41, 0.95);
        border-right: 1px solid #343A40;
    }
    
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
    
    /* Code Block */
    code {
        color: #e83e8c;
        background-color: #f1f3f5;
        padding: 2px 4px;
        border-radius: 4px;
    }
    </style>
    """, unsafe_allow_html=True)

# ==========================================
# SIDEBAR: BUSINESS CONTACT
# ==========================================
with st.sidebar:
    st.header("Baez IT Solutions")
    st.write("Expert Crypto & IT Consulting.")
    st.markdown("---")
    st.subheader("Services")
    st.write("🔒 **Wallet Security Audits**")
    st.write("⚙️ **Node Setup & Maintenance**")
    st.write("📈 **DeFi Strategy Planning**")
    
    st.markdown("---")
    st.write("**Need Help?**")
    contact_email = st.text_input("Your Email (for inquiry)")
    contact_msg = st.text_area("How can we help?")
    if st.button("Send Inquiry"):
        st.success("Message sent! We will contact you shortly.")

# ==========================================
# PAGE 1: THE COVER PAGE
# ==========================================
if st.session_state.page == 'cover':
    c1, c2, c3 = st.columns([1, 2, 1])
    with c2:
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.title("BIT SOLUTIONS ACADEMY")
        st.markdown("<h3 style='text-align: left; color: #00BFA5 !important;'>Master the Future of Finance.</h3>", unsafe_allow_html=True)
        st.write("Welcome to the next generation of financial education. Learn how Blockchain, Smart Contracts, and DeFi are rewriting the rules of money.")
        st.write("")
        st.write("---")
        st.write("")
        if st.button("🚀 Enter Academy"):
            enter_site()
            st.rerun()

# ==========================================
# PAGE 2: THE MAIN ACADEMY
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
    tab_learn, tab_sim, tab_data, tab_quiz = st.tabs(["📖 Learn Concepts", "🧪 Lab Simulation", "📊 Live Market", "🧠 Knowledge Quiz"])

    # --- TAB 1: THE CLASSROOM ---
    with tab_learn:
        st.header("Blockchain Fundamentals")
        
        # --- EXPANDED & SIMPLIFIED LESSON 1 ---
        with st.expander("Lesson 1: Blockchain Basics (For Total Beginners)"):
            
            st.subheader("1. The Simple Analogy: 'The Group Chat'")
            st.write("Imagine a **WhatsApp Group Chat** with your friends, but it has 2 special rules:")
            
            c_chat1, c_chat2 = st.columns(2)
            with c_chat1:
                st.info("👁️ Rule 1: Everyone Sees Everything")
                st.write("If you say *'I owe Bob $5'*, everyone in the group sees it. You cannot lie later and say you didn't say it.")
            with c_chat2:
                st.info("🔒 Rule 2: No Deleting")
                st.write("Once a message is sent, it is carved in stone. You cannot delete it. You cannot edit it.")
                
            st.write("**That is a Blockchain.** It is just a record of events that everyone has a copy of, and no one can erase.")

            st.divider()

            st.subheader("2. Why do we need this? (The 'Trust' Problem)")
            st.write("In the normal world, we need **Middlemen** to build trust.")
            
            st.warning("🏦 **The Old Way (Bank):** If I send you $50, the Bank has to verify I have the money. We trust the Bank.")
            st.success("⛓️ **The New Way (Blockchain):** The 'Group Chat' verifies I have the money because everyone has the history. We don't need the Bank.")

            st.divider()
            
            st.subheader("3. Real Life Examples (Not just money!)")
            st.write("Since we can prove who owns what without a middleman, we can fix annoying real-world problems.")
            
            c_ex1, c_ex2 = st.columns(2)
            with c_ex1:
                st.info("👟 **Nike Sneakers (Authenticity)**")
                st.write("""
                **Problem:** You buy Jordans on eBay. Are they fake?
                **Solution:** The shoe comes with a 'Digital Token' on the blockchain. You scan it, and the blockchain confirms it came from the Nike factory.
                """)
            with c_ex2:
                st.info("🎟️ **Concert Tickets (Ticketmaster)**")
                st.write("""
                **Problem:** You buy a Taylor Swift ticket from a scalper. It's a photocopy. You get denied at the gate.
                **Solution:** Blockchain tickets cannot be photocopied. You can check on your phone if the ticket is real instantly.
                """)
            
            

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
            st.divider()
            st.subheader("4. Real World Apps")
            c_app1, c_app2 = st.columns(2)
            with c_app1:
                st.info("🏦 **Aave (Lending)**")
                st.link_button("Visit Aave ↗", "https://aave.com")
            with c_app2:
                st.info("⚡ **Drift (Trading)**")
                st.link_button("Visit Drift ↗", "https://www.drift.trade")

        with st.expander("Lesson 3: The 3 Types of Staking (Detailed Breakdown)"):
            st.write("In crypto, there is no CEO. The network runs itself. But how do we stop people from cheating? We use **Consensus Mechanisms**.")
            c_pow, c_pos = st.columns(2)
            with c_pow:
                st.subheader("⛏️ 1. Proof of Work (Bitcoin)")
                st.info("**The 'Hardware Race'**")
                st.write("Miners race to solve math puzzles. Secure, but high energy.")
            with c_pos:
                st.subheader("🥩 2. Proof of Stake (Ethereum)")
                st.info("**The 'Financial Bond'**")
                st.write("Validators lock up money. If they cheat, they lose the money.")
            st.divider()
            st.subheader("💧 3. Liquid Staking")
            st.write("Regular staking locks your money. **Liquid Staking** gives you a 'Receipt Token' (stETH) that you can still use/sell.")

        with st.expander("Lesson 4: What actually IS a Wallet? (A Beginner's Guide)"):
            st.subheader("1. The Big Misconception")
            st.write("""
            **Stop thinking of it as a 'Leather Wallet'.**
            Your crypto is **NOT** inside the app. It is **NOT** inside the USB stick.
            * **The Blockchain:** Is the cloud (like Google Drive) where the money lives.
            * **Your Wallet:** Is just the **Password (Key)** that lets you move that money.
            """)
            st.divider()
            st.subheader("2. The Email Analogy (Public vs. Private Keys)")
            st.write("Every wallet comes with a Key Pair. It works exactly like Email.")
            c_key1, c_key2 = st.columns(2)
            with c_key1:
                st.success("🟢 Public Key (The Address)")
                st.write("Like your Email Address. Safe to share.")
            with c_key2:
                st.error("🔴 Private Key (The Seed Phrase)")
                st.write("Like your Password. NEVER SHARE THIS.")
            st.divider()
            st.subheader("3. Hot vs. Cold Wallets (Which do I need?)")
            c_hot, c_cold = st.columns(2)
            with c_hot:
                st.warning("🔥 Hot Wallet (Software)")
                st.write("App on phone. Convenient but less secure.")
            with c_cold:
                st.info("❄️ Cold Wallet (Hardware)")
                st.write("USB stick. Offline and very secure.")
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
            st.subheader("1. Storage Security")
            st.write("* **✅ CORRECT:** Write it on paper. Store in physical safe.\n* **❌ WRONG:** Screenshot, Google Drive, Email.")
            st.divider()
            st.subheader("2. Advanced Threats")
            c_scam_1, c_scam_2 = st.columns(2)
            with c_scam_1:
                st.warning("📋 **Clipboard Hijacking**")
                st.write("Malware that swaps copied addresses. Always check the first 4 and last 4 digits.")
            with c_scam_2:
                st.warning("🔓 **The 'Unlimited Approval' Trap**")
                st.write("Fake sites ask for unlimited permission. Read the popup before clicking Approve.")
            st.divider()
            st.subheader("3. Daily Habits")
            st.write("1. **The $1 Test**\n2. **No SMS 2FA**\n3. **Bookmark Everything**")

    # --- TAB 2: THE SANDBOX ---
    with tab_sim:
        st.header("🧪 Interactive Lab")
        st.write("Experiment with the mechanics of DeFi in a safe, simulated environment.")
        
        # --- SECTION 1: GAS STATION ---
        st.subheader("1. Gas Fee Simulator")
        traffic = st.select_slider("Select Network Traffic Level:", options=["Low", "Medium", "High", "Extreme"])
        if traffic == "Low": eth_fee, l2_fee, sol_fee = 2.50, 0.05, 0.0001
        elif traffic == "Medium": eth_fee, l2_fee, sol_fee = 8.00, 0.12, 0.0001
        elif traffic == "High": eth_fee, l2_fee, sol_fee = 25.00, 0.40, 0.0005
        else: eth_fee, l2_fee, sol_fee = 120.00, 1.50, 0.002
        c_gas1, c_gas2, c_gas3 = st.columns(3)
        with c_gas1: st.metric("Ethereum (L1)", f"${eth_fee:.2f}")
        with c_gas2: st.metric("Base (L2)", f"${l2_fee:.2f}", delta="-98%")
        with c_gas3: st.metric("Solana", f"${sol_fee:.4f}", delta="Cheap")
        st.markdown("---")

        # --- SECTION 2: COMPOUND INTEREST ---
        st.subheader("2. Staking Calculator")
        c_calc1, c_calc2 = st.columns([1, 2])
        with c_calc1:
            initial = st.number_input("Initial Investment ($)", value=1000)
            apy = st.slider("APY (%)", 1, 100, 8)
            years = st.slider("Years to Hold", 1, 20, 5)
        with c_calc2:
            data = [initial * ((1 + (apy/100)) ** i) for i in range(years + 1)]
            chart_data = pd.DataFrame(data, columns=["Portfolio Value"])
            st.line_chart(chart_data)
            st.success(f"💰 In {years} years: **${data[-1]:,.2f}**")
        st.markdown("---")

        # --- SECTION 3: DEX SIMULATOR ---
        st.subheader("3. DEX Simulator (Swap)")
        c_dex1, c_dex2 = st.columns(2)
        with c_dex1:
            sell_amt = st.number_input("Amount to Swap (USDC)", value=1000)
            slippage = 5.0 if sell_amt > 100000 else (1.0 if sell_amt > 10000 else 0)
            if slippage > 0: st.warning(f"⚠️ High Volume: {slippage}% Slippage")
        with c_dex2:
            if st.button("Execute Swap"):
                with st.spinner("Routing..."):
                    time.sleep(1)
                st.success(f"✅ Received ${(sell_amt * (1 - slippage/100)):,.2f} ETH")

    # --- TAB 3: REAL WORLD DATA (ENHANCED) ---
    with tab_data:
        st.header("Live Market Data (24h Change)")
        
        def get_data(t):
            try:
                # Get 2 days of data to calculate change
                d = yf.Ticker(t).history(period="5d") 
                current = d["Close"].iloc[-1]
                prev = d["Close"].iloc[-2]
                change = ((current - prev) / prev) * 100
                return current, change, d["Close"]
            except: return 0.0, 0.0, []

        btc_p, btc_c, btc_h = get_data("BTC-USD")
        eth_p, eth_c, eth_h = get_data("ETH-USD")
        sol_p, sol_c, sol_h = get_data("SOL-USD")
        
        m1, m2, m3 = st.columns(3)
        m1.metric("Bitcoin", f"${btc_p:,.0f}", f"{btc_c:.2f}%")
        m2.metric("Ethereum", f"${eth_p:,.0f}", f"{eth_c:.2f}%")
        m3.metric("Solana", f"${sol_p:.2f}", f"{sol_c:.2f}%")
        
        st.area_chart(btc_h)
        st.caption("Bitcoin Price Trend (Last 5 Days)")

    # --- TAB 4: QUIZ (NEW) ---
    with tab_quiz:
        st.header("🧠 Knowledge Check")
        st.write("Test your understanding of the Academy lessons.")
        
        score = 0
        
        q1 = st.radio("1. Where is your crypto actually stored?", 
                      ["In my Ledger USB stick", "On the Blockchain", "In the Coinbase App"])
        if q1 == "On the Blockchain": score += 1
        
        q2 = st.radio("2. What happens if you lose your Seed Phrase?", 
                      ["I can reset it via email", "I lose my money forever", "Support can recover it"])
        if q2 == "I lose my money forever": score += 1
        
        q3 = st.radio("3. Which wallet type is safer for long-term storage?", 
                      ["Hot Wallet", "Cold Wallet", "Exchange Wallet"])
        if q3 == "Cold Wallet": score += 1
        
        st.markdown("---")
        if st.button("Check Score"):
            if score == 3:
                st.balloons()
                st.success(f"🎉 Perfect Score! 3/3. You are ready for DeFi.")
            else:
                st.warning(f"You got {score}/3. Review the lessons and try again!")
