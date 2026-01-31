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
        
        # --- EXPANDED LESSON 1 ---
        with st.expander("Lesson 1: Blockchain Basics & Real World Use"):
            st.subheader("1. What IS a Blockchain?")
            st.write("Think of a Blockchain like a **shared Google Sheet** that everyone can read, but NO ONE can delete.")
            
            c_concept1, c_concept2 = st.columns(2)
            
            with c_concept1:
                st.info("🧱 **The 'Block' (The Page)**")
                st.write("""
                Imagine a notebook page filled with transactions (Alice sent Bob $5). 
                Once the page is full, it gets sealed.
                """)
                
            with c_concept2:
                st.info("🔗 **The 'Chain' (The Glue)**")
                st.write("""
                Each new page is mathematically glued to the previous one. 
                If you try to rip out an old page (to erase a debt), the whole notebook falls apart. This makes it **Immutable** (Unchangeable).
                """)
            
            st.divider()
            
            st.subheader("2. Beyond Money: Real World Use Cases")
            st.write("Because we can trust the data without a middleman, we can use it for huge industries:")
            
            c_use1, c_use2 = st.columns(2)
            with c_use1:
                st.success("🚚 **Supply Chain (Walmart)**")
                st.write("Walmart puts mangoes on the blockchain. If there is E. coli, they trace it to the exact farm in 2.2 seconds (used to take 7 days).")
            with c_use2:
                st.success("🏠 **Real Estate (Tokenization)**")
                st.write("Instead of buying a whole house, you can buy 1/100th of a house token instantly. It proves your ownership without a lawyer.")
                
            c_use3, c_use4 = st.columns(2)
            with c_use3:
                st.success("🗳️ **Voting Systems**")
                st.write("A blockchain vote cannot be deleted or faked. You can verify your vote was counted from your phone.")
            with c_use4:
                st.success("🏥 **Medical Records**")
                st.write("You own your X-rays in your wallet. When you switch doctors, you grant them access instantly. No fax machines needed.")

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
                st.write("""
                * **Slow:** Need a lawyer/bank to verify.
                * **Expensive:** You pay fees to the middleman.
                * **Trust-Based:** You hope they don't cheat you.
                """)
            with c_bot:
                st.success("🤖 The New Way (Smart Contract)")
                st.write("""
                * **Instant:** Runs 24/7 on the blockchain.
                * **Cheap:** No middleman fees.
                * **Trustless:** The machine *cannot* cheat. If you put $2 in, the soda *must* drop.
                """)
            
            st.divider()

            st.subheader("3. A Simple Example: The Sports Bet")
            st.write("""
            Two friends, **Alice** and **Bob**, want to bet $100 on the Super Bowl.
            
            * **Without Crypto:** Alice bets on Team A. Bob bets on Team B. Team A wins. Bob refuses to pay. Alice loses her money.
            * **With a Smart Contract:**
                1. Alice and Bob both send $100 to a **Digital Vault** (the contract).
                2. The Vault locks the funds ($200 total).
                3. The Vault checks the official score online (via an 'Oracle').
                4. **IF** Team A wins -> **THEN** The Vault automatically sends $200 to Alice.
            
            **Result:** Bob cannot refuse to pay. The code forces the payment.
            """)

            st.divider()
            
            st.subheader("4. Real World Apps")
            c_app1, c_app2 = st.columns(2)
            with c_app1:
                st.info("🏦 **Aave (Lending)**")
                st.write("A bank run by code. Depositors earn interest, borrowers pay interest. No CEO involved.")
                st.link_button("Visit Aave ↗", "https://aave.com")
            with c_app2:
                st.info("⚡ **Drift (Trading)**")
                st.write("A stock exchange run by code. Trades settle instantly on Solana.")
                st.link_button("Visit Drift ↗", "https://www.drift.trade")

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

        with st.expander("Lesson 4: What actually IS a Wallet? (Keys explained)"):
            st.subheader("1. The Big Misconception: 'The Bag vs. The Browser'")
            st.write("The wallet is just a **Web Browser** that views your money on the blockchain. It does not store the money inside.")
            
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
            
            btn1, btn2, btn3 = st.columns(3)
            with btn1:
                st.link_button("Coinbase (App) ↗", "https://www.coinbase.com")
            with btn2:
                st.link_button("Ledger (USB) ↗", "https://www.ledger.com")
            with btn3:
                st.link_button("Tangem (Card) ↗", "https://tangem.com")

        with st.expander("Lesson 5: 🛡️ Security & Scams (THE SURVIVAL GUIDE)"):
            st.error("⚠️ THE GOLDEN RULE: Never, ever share your Seed Phrase with anyone. Support will NEVER ask for it.")
            
            st.subheader("1. Storage Security (Paper vs. Cloud)")
            st.write("""
            The most common way people get hacked is by saving their 12 words in a password manager, email, or photo album.
            * **✅ CORRECT:** Write it on paper (or steel). Store it in a physical safe.
            * **❌ WRONG:** Taking a screenshot, saving to Google Drive, emailing it to yourself.
            """)
            
            st.divider()
            
            st.subheader("2. Advanced Threats (Know Your Enemy)")
            
            c_scam_1, c_scam_2 = st.columns(2)
            
            with c_scam_1:
                st.warning("📋 **Clipboard Hijacking**")
                st.write("""
                **The Attack:** Malware on your computer watches for crypto addresses. When you copy an address and paste it, the virus **swaps** the address for the hacker's address.
                
                **The Fix:** Always read the **First 4** and **Last 4** characters of the address AFTER pasting.
                """)
                
            with c_scam_2:
                st.warning("🔓 **The 'Unlimited Approval' Trap**")
                st.write("""
                **The Attack:** A scam website asks you to "Connect Wallet" and "Approve" access. You think you are signing a login, but you are actually giving them permission to **drain all your USDC**.
                
                **The Fix:** Read the popup carefully! If it says "Set Approval for All" or "Unlimited," REJECT it unless you trust the site 100%.
                """)

            st.divider()
            st.subheader("3. Daily Habits for Survival")
            st.write("""
            1.  **The $1 Test:** Before sending $10,000, send $1.00 first. If it arrives, send the rest.
            2.  **No SMS 2FA:** Hackers can steal your phone number (SIM Swap). Use an Authenticator App (Google/Authy) or a YubiKey.
            3.  **Bookmark Everything:** Never search "Coinbase" on Google. You might click a fake ad. Bookmark the real URL and only use that.
            """)

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
