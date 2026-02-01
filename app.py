import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf
import time
import smtplib
import requests
import xml.etree.ElementTree as ET
import streamlit.components.v1 as components
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

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

# --- EMAIL FUNCTION ---
def send_email(user_email, user_message):
    try:
        sender_email = st.secrets["email"]["sender_email"]
        sender_password = st.secrets["email"]["sender_password"]
        receiver_email = st.secrets["email"]["receiver_email"]

        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = f"New Inquiry from {user_email}"

        body = f"User Email: {user_email}\n\nMessage:\n{user_message}"
        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        text = msg.as_string()
        server.sendmail(sender_email, receiver_email, text)
        server.quit()
        return True
    except Exception as e:
        return False

# --- NEWS FETCHING FUNCTION (RSS) ---
def get_crypto_news():
    url = "https://cointelegraph.com/rss"
    news_items = []
    try:
        response = requests.get(url, timeout=5)
        root = ET.fromstring(response.content)
        for item in root.findall('./channel/item')[:10]:
            news = {
                'title': item.find('title').text,
                'link': item.find('link').text,
                'pubDate': item.find('pubDate').text,
                'source': 'Cointelegraph'
            }
            news_items.append(news)
    except Exception as e:
        return []
    return news_items

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    .stApp {
        background-image: linear-gradient(rgba(0, 0, 0, 0.90), rgba(0, 0, 0, 0.90)), 
                          url('https://images.unsplash.com/photo-1550751827-4bd374c3f58b?q=80&w=2940&auto=format&fit=crop');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }
    h1, h2, h3 { color: #FFFFFF !important; text-shadow: 0px 2px 4px rgba(0,0,0,0.5); }
    p, li, label { color: #E0E0E0 !important; font-size: 1.1em; line-height: 1.6; }
    div[data-baseweb="notification"] {
        background-color: rgba(13, 71, 161, 0.8);
        color: white;
        border: 1px solid #1976D2;
        backdrop-filter: blur(5px);
    }
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
    section[data-testid="stSidebar"] {
        background-color: rgba(33, 37, 41, 0.95);
        border-right: 1px solid #343A40;
    }
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
    code {
        color: #e83e8c;
        background-color: #f1f3f5;
        padding: 2px 4px;
        border-radius: 4px;
    }
    </style>
    """, unsafe_allow_html=True)

# ==========================================
# SIDEBAR
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
    with st.form("contact_form"):
        contact_email = st.text_input("Your Email (for inquiry)")
        contact_msg = st.text_area("How can we help?")
        submit_button = st.form_submit_button("Send Inquiry")
    if submit_button:
        if contact_email and contact_msg:
            with st.spinner("Sending message..."):
                success = send_email(contact_email, contact_msg)
                if success:
                    st.success("✅ Message sent! We will contact you shortly.")
                else:
                    st.error("❌ Error sending. Check your Secrets configuration.")
        else:
            st.warning("Please fill out both fields.")

# ==========================================
# COVER PAGE
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
# MAIN ACADEMY
# ==========================================
else:
    col1, col2 = st.columns([3, 1])
    with col1:
        st.title("BIT SOLUTIONS ACADEMY")
        st.caption("Classroom Dashboard")
    with col2:
        if st.button("⬅ Exit to Cover"):
            st.session_state.page = 'cover'
            st.rerun()
    st.markdown("---")

    tab_learn, tab_sim, tab_data, tab_news, tab_quiz = st.tabs(["📖 Learn Concepts", "🧪 Lab Simulation", "📊 Live Market", "📰 Crypto News", "🧠 Knowledge Quiz"])

    # --- TAB 1: LEARN ---
    with tab_learn:
        st.header("Blockchain Fundamentals")
        
        # --- LESSON 1: EXPANDED (NEW) ---
        with st.expander("Lesson 1: What is a Blockchain? (The Deep Dive)"):
            st.subheader("1. The History: Origins of Bitcoin")
            st.write("To understand Blockchain, you must understand why it was built.")
            st.write("In **2008**, the global financial system collapsed. Banks gambled with user money, and governments printed trillions to bail them out. People lost trust in centralization.")
            st.info("👤 **Satoshi Nakamoto:** On Oct 31, 2008, an anonymous cryptographer published the **Bitcoin Whitepaper**. It proposed a system of money that required no banks, no governments, and no trust.")
            st.link_button("📜 Read the Bitcoin Whitepaper", "https://bitcoin.org/bitcoin.pdf")
            
            st.divider()
            
            st.subheader("2. What is it? (The Digital Ledger)")
            st.write("A blockchain is a **Distributed Digital Ledger**.")
            st.markdown("""
            * **Distributed:** No single computer runs it. It runs on thousands of computers (Nodes) globally.
            * **Ledger:** It is a list of transactions (Alice sent Bob 5 BTC).
            * **Blocks:** Transactions are bundled into groups called 'Blocks'.
            * **Chain:** Each block is cryptographically tied to the one before it.
            """)
            
            st.divider()

            st.subheader("3. Security: Why is it Unhackable?")
            st.write("Blockchain security relies on **Hashing (SHA-256)** and **Consensus**.")
            c_sec1, c_sec2 = st.columns(2)
            with c_sec1:
                st.warning("🔗 The Chain Effect")
                st.write("If a hacker tries to change a transaction in Block 50, it changes the 'Hash' (ID) of that block. Because Block 51 is connected to Block 50's ID, Block 51 also changes. This creates a domino effect where **every subsequent block breaks**.")
            with c_sec2:
                st.error("🛡️ The 51% Rule")
                st.write("To successfully hack Bitcoin, you would need to control **51% of all computing power in the world** simultaneously. This would cost billions of dollars per hour, making it economically impossible.")

            st.divider()

            st.subheader("4. Types of Blockchains")
            st.write("Not all blockchains are Bitcoin. There are three main types:")
            st.markdown("""
            1.  **Public (Permissionless):** Bitcoin, Ethereum, Solana. Anyone can join, read, or write. Total transparency.
            2.  **Private (Permissioned):** Hyperledger, Ripple (historically). Used by banks/enterprises. You need an invite to join.
            3.  **Hybrid:** A mix of both. Used for medical records or identity verification.
            """)

            st.divider()

            st.subheader("5. The Future of Crypto")
            st.write("Where are we going from here?")
            st.success("🚀 **The Phase of Utility**")
            st.write("We are moving from 'Speculation' (gambling) to 'Utility' (using).")
            st.write("**Key Trends:**")
            st.write("* **Tokenization of Assets:** Stocks, Real Estate, and Bonds moving onto the blockchain (BlackRock is doing this now).")
            st.write("* **Layer 2 Scaling:** Networks like Optimism and Base making crypto fast and cheap for daily coffee purchases.")
            st.write("* **DePIN:** Decentralized Physical Infrastructure (using crypto to build wifi networks and energy grids).")

        with st.expander("Lesson 2: Smart Contracts (The 'Robot Lawyer')"):
            st.subheader("1. What makes it 'Smart'?")
            st.write("A Smart Contract is just **Programmable Money**. It's code that holds money and releases it only when a condition is met.")
            st.info("💡 **Think:** 'If This Happens, Then Pay That.'")
            st.divider()
            st.subheader("2. The Vending Machine Analogy")
            st.write("The best way to understand it is to compare a **Human Barista** vs. a **Vending Machine**.")
            c_human, c_bot = st.columns(2)
            with c_human:
                st.error("☕ The Old Way")
                st.write("Slow, Expensive, Trust-Based.")
            with c_bot:
                st.success("🤖 The New Way")
                st.write("Instant, Cheap, Trustless.")
            st.divider()
            st.subheader("3. A Simple Example: The Sports Bet")
            st.write("Two friends bet on the Super Bowl. The code holds the money and automatically pays the winner based on the official score.")

        # --- LESSON 3: EXPANDED (STAKING & YIELD) ---
        with st.expander("Lesson 3: Staking, Liquid Staking & Yield (How to Earn)"):
            st.subheader("1. The Two Ways to Earn in DeFi")
            st.write("Just holding crypto is like stuffing cash under your mattress. In DeFi, you can make your assets work for you.")
            
            c_earn1, c_earn2 = st.columns(2)
            with c_earn1:
                st.success("🛡️ Protocol Staking")
                st.write("**What is it?** You lock your coins to help secure the blockchain network (like Ethereum or Solana).")
                st.write("**Risk:** Low.")
                st.write("**Reward:** ~3-7% APY (Paid in more coins).")
            with c_earn2:
                st.info("🏦 DeFi Lending")
                st.write("**What is it?** You lend your coins to other users (borrowers) through a smart contract.")
                st.write("**Risk:** Medium (Smart Contract Risk).")
                st.write("**Reward:** Variable (Based on demand).")
            
            st.divider()
            
            st.subheader("2. Deep Dive: Liquid Staking (Jito & Lido)")
            st.write("Standard staking has a flaw: your money is **locked**. You can't sell it if the market crashes.")
            st.write("**The Solution: Liquid Staking Tokens (LSTs).**")
            st.write("When you stake your SOL or ETH, the protocol gives you a 'Receipt Token' (like JitoSOL). This receipt creates three benefits:")
            st.write("1. **Liquidity:** You can swap JitoSOL back to SOL instantly (no waiting period).")
            st.write("2. **Yield:** The token value grows automatically.")
            st.write("3. **MEV Rewards:** (Specific to Jito) You earn extra money from 'Maximal Extractable Value'—basically tips paid by traders for speed.")
            
            col_jito1, col_jito2 = st.columns([3,1])
            with col_jito1:
                st.write("**Example:** You deposit **10 SOL** into Jito. You get **9.x JitoSOL**. A year later, that 9.x JitoSOL is worth **10.7 SOL**.")
            with col_jito2:
                st.link_button("Explore Jito ↗", "https://www.jito.network/")

            st.divider()

            st.subheader("3. Deep Dive: Decentralized Lending (Aave)")
            st.write("**Aave** is the biggest 'Bank' in DeFi, but it has no employees. It is run entirely by code.")
            st.markdown("""
            * **Depositors (You):** Deposit USDC or ETH to earn interest.
            * **Borrowers:** Deposit collateral (like BTC) to borrow USDC.
            """)
            st.warning("⚠️ **Safety Feature:** Aave is 'Over-Collateralized'. To borrow $100, you must deposit ~$120 worth of collateral. If the value drops, the robot liquidates the collateral to pay YOU (the depositor) back. This protects your deposit.")
            
            col_aave1, col_aave2 = st.columns([3,1])
            with col_aave1:
                st.write("**Strategy:** Many people deposit ETH into Aave to earn a small yield, while keeping the flexibility to withdraw instantly.")
            with col_aave2:
                st.link_button("Explore Aave ↗", "https://aave.com/")

        with st.expander("Lesson 4: What actually IS a Wallet? (The Ultimate Guide)"):
            st.subheader("1. The 'Glass Box' Analogy")
            st.write("Crypto is confusing because you can't 'see' the money. Here is the best way to visualize it:")
            st.info("Imagine the Blockchain is a giant wall of **Glass Lockboxes**.")
            st.write("""
            * **Anyone** can see inside Box #402. They can see it has 5 BTC.
            * **Only the person with the Key** can open Box #402 to move the money.
            * Your 'Wallet' is just a **Keychain** that holds the key to your box. It doesn't hold the money itself.
            """)
            
            st.divider()
            
            st.subheader("2. The Keys to the Kingdom")
            st.write("When you create a wallet, you aren't creating an account with a company. You are generating cryptography.")
            c_key1, c_key2 = st.columns(2)
            with c_key1:
                st.success("🟢 Public Key (The Address)")
                st.write("**Think: Email Address.**")
                st.write("This is what you give people so they can send you money. It is perfectly safe to share on social media.")
                st.code("0x71C...9A23")
            with c_key2:
                st.error("🔴 Private Key (Seed Phrase)")
                st.write("**Think: The Master Password.**")
                st.write("This is a list of 12-24 words. If anyone sees this, they can steal ALL your money from ANY device. Never type this into a website.")
                st.code("apple river galaxy...")

            st.divider()

            st.subheader("3. Hot vs. Cold Wallets (Which do you need?)")
            st.write("The difference comes down to one thing: **Is it connected to the internet?**")

            # Hot Wallets Section
            st.markdown("#### 🔥 Hot Wallets (Software)")
            st.write("**Best for:** Daily spending, trading on Uniswap, holding small amounts (< $1,000).")
            c_hot1, c_hot2 = st.columns([3, 1])
            with c_hot1:
                st.write("""
                * **Pros:** Free, easy to use, connects to websites instantly.
                * **Cons:** Vulnerable to malware and hacks because keys exist on your phone/laptop.
                * **Recommendation:** **Phantom** (Best UX) or **MetaMask** (Standard).
                """)
            with c_hot2:
                st.link_button("Download Phantom ↗", "https://phantom.app")

            # Cold Wallets Section
            st.markdown("#### ❄️ Cold Wallets (Hardware)")
            st.write("**Best for:** Long-term savings, retirement, holding large amounts (> $1,000).")
            c_cold1, c_cold2 = st.columns([3, 1])
            with c_cold1:
                st.write("""
                * **Pros:** Unhackable by online viruses. Keys NEVER leave the physical device.
                * **Cons:** Costs money ($70-$150), requires physical button pressing to sign transactions.
                * **Recommendation:** **Ledger Nano S Plus** or **Trezor Safe 3**.
                """)
            with c_cold2:
                st.link_button("Get a Ledger ↗", "https://shop.ledger.com")
            
            st.divider()
            
            st.subheader("4. Custodial vs. Self-Custody")
            st.warning("⚠️ **Important Distinction:**")
            st.write("""
            * **Custodial (Coinbase/Binance):** The exchange holds the keys. If they go bankrupt (like FTX), you lose your money.
            * **Self-Custody (Ledger/Phantom):** YOU hold the keys. You are the bank. No one can freeze your funds, but no one can reset your password.
            """)

        with st.expander("Lesson 5: 🛡️ Security Masterclass (The Survival Guide)"):
            st.subheader("1. The Core Concept: 'Self-Custody'")
            st.write("In crypto, YOU are the bank. If you lose your keys, the money is gone. This responsibility requires new habits.")
            st.divider()
            st.subheader("2. The Official 'Dos and Don'ts' Checklist")
            st.write("Memorize this list before you move a single dollar.")
            c_do, c_dont = st.columns(2)
            with c_do:
                st.success("✅ THE DOS (Safe Habits)")
                st.write("""
                * **DO** write your 12-word seed phrase on paper or steel.
                * **DO** store that paper in a fireproof safe.
                * **DO** use a 'burner wallet' for risky new websites.
                * **DO** double-check the first 4 and last 4 characters of every address you paste.
                """)
            with c_dont:
                st.error("❌ THE DON'TS (Ways to get Rekt)")
                st.write("""
                * **DON'T** take a screenshot of your seed phrase.
                * **DON'T** save your seed phrase in Google Drive, Notes, or Email.
                * **DON'T** click links sent to you in Discord or Twitter DMs.
                * **DON'T** type your seed phrase into ANY website, ever.
                """)
            st.divider()
            st.subheader("3. Understanding 'Social Engineering'")
            st.warning("⚠️ **Fact:** Most people don't get 'hacked' by code. They get 'tricked' by people.")
            st.write("**The 'Fake Support' Scam:** You ask a question on Twitter. Someone DMs you. They are very helpful. They send you a link to 'sync your wallet'. **It is a scam.**")
            st.divider()
            st.subheader("4. Advanced: Revoking Allowances")
            st.write("When you use a DeFi app (like Uniswap), you give it permission to spend your coins. If that app gets hacked later, your wallet is at risk.")
            st.info("🛠️ **The Fix:** Once a month, use a tool like **Revoke.cash** to disconnect your wallet from old apps.")

    # --- TAB 2: LAB ---
    with tab_sim:
        st.header("🧪 Interactive Lab")
        st.write("Experiment with the mechanics of DeFi in a safe, simulated environment.")

        # --- LAB 1: COMPOUND STAKING ---
        st.subheader("📈 1. Compound Interest Calculator")
        st.write("Visualize the power of **DCA (Dollar Cost Averaging)** + **Staking Yield**.")
        
        c_calc1, c_calc2 = st.columns([1, 2])
        with c_calc1:
            initial = st.number_input("Starting Balance ($)", value=1000)
            monthly = st.number_input("Monthly Contribution ($)", value=100)
            apy = st.slider("APY (%)", 1, 50, 8)
            years = st.slider("Years to Grow", 1, 20, 10)
        
        with c_calc2:
            # Calculation: Future Value of a Series
            months = years * 12
            monthly_rate = (apy / 100) / 12
            
            balance = []
            contributions = []
            
            current_bal = initial
            total_contributed = initial
            
            for i in range(months + 1):
                if i > 0:
                    current_bal = current_bal * (1 + monthly_rate) + monthly
                    total_contributed += monthly
                balance.append(current_bal)
                contributions.append(total_contributed)
                
            # Create Data for Chart
            chart_data = pd.DataFrame({
                "Total Value": balance,
                "Your Principal": contributions
            })
            
            st.line_chart(chart_data)
            
            profit = balance[-1] - contributions[-1]
            st.success(f"💰 **Final Balance:** ${balance[-1]:,.2f}")
            st.caption(f"You contributed: ${contributions[-1]:,.2f} | **Interest Earned: ${profit:,.2f}**")

        # --- LAB 2: PROFIT/ROI CALCULATOR ---
        st.markdown("---")
        st.subheader("💰 2. Trade Profit (ROI) Calculator")
        st.write("Calculate your exact Net Profit after exchange fees.")
        
        roi_c1, roi_c2 = st.columns(2)
        with roi_c1:
            buy_price = st.number_input("Buy Price per Coin ($)", value=50000.0)
            sell_price = st.number_input("Sell Price per Coin ($)", value=65000.0)
            amount_coin = st.number_input("Amount of Coins", value=0.1)
            fee_pct = st.number_input("Exchange Fee (%)", value=0.1)
            
        with roi_c2:
            cost_basis = buy_price * amount_coin
            gross_sale = sell_price * amount_coin
            
            # Calculate Fees (Buy + Sell side)
            buy_fee = cost_basis * (fee_pct/100)
            sell_fee = gross_sale * (fee_pct/100)
            total_fees = buy_fee + sell_fee
            
            net_profit = gross_sale - cost_basis - total_fees
            roi_pct = (net_profit / cost_basis) * 100
            
            st.write("### 📊 Results")
            if net_profit >= 0:
                st.success(f"**Net Profit:** ${net_profit:,.2f}")
                st.metric("ROI", f"{roi_pct:.2f}%", delta="Profit")
            else:
                st.error(f"**Net Loss:** ${net_profit:,.2f}")
                st.metric("ROI", f"{roi_pct:.2f}%", delta="Loss")
                
            st.caption(f"Total Fees Paid: ${total_fees:.2f}")

        # --- LAB 3: RISK/REWARD CALCULATOR ---
        st.markdown("---")
        st.subheader("⚖️ 3. Risk/Reward Ratio Calculator")
        st.write("Strategy Tool: Should you take this trade? (Target Ratio: 1:3 or higher)")
        
        risk_c1, risk_c2 = st.columns(2)
        with risk_c1:
            entry_p = st.number_input("Entry Price ($)", value=100.0)
            stop_loss = st.number_input("Stop Loss ($)", value=90.0)
            take_profit = st.number_input("Take Profit Target ($)", value=130.0)
            
        with risk_c2:
            risk_amt = entry_p - stop_loss
            reward_amt = take_profit - entry_p
            
            if risk_amt <= 0 or reward_amt <= 0:
                st.warning("Check your inputs. Stop Loss must be lower than Entry (for Longs).")
            else:
                ratio = reward_amt / risk_amt
                
                st.metric("Risk / Reward Ratio", f"1 : {ratio:.1f}")
                st.write(f"Risking **${risk_amt:.2f}** to make **${reward_amt:.2f}**")
                
                if ratio >= 3:
                    st.success("✅ **Excellent Trade.** (Ratio > 1:3)")
                elif ratio >= 2:
                    st.info("🆗 **Good Trade.** (Ratio > 1:2)")
                else:
                    st.error("❌ **Bad Trade.** Risk is too high for the reward.")

    # --- TAB 3: LIVE MARKET (UNCHANGED) ---
    with tab_data:
        st.header("📊 Market Dashboard")
        
        col_sel, col_empty = st.columns([3, 1])
        with col_sel:
            coin_opt = st.selectbox("Select Asset to Analyze:", 
                                    ["Bitcoin (BTC)", "Ethereum (ETH)", "Solana (SOL)", "Cardano (ADA)", "Ripple (XRP)", "Dogecoin (DOGE)"])
            
            asset_map = {
                "Bitcoin (BTC)": {"yf": "BTC-USD", "tv": "COINBASE:BTCUSD"},
                "Ethereum (ETH)": {"yf": "ETH-USD", "tv": "COINBASE:ETHUSD"},
                "Solana (SOL)": {"yf": "SOL-USD", "tv": "COINBASE:SOLUSD"},
                "Cardano (ADA)": {"yf": "ADA-USD", "tv": "BINANCE:ADAUSDT"},
                "Ripple (XRP)": {"yf": "XRP-USD", "tv": "BINANCE:XRPUSDT"},
                "Dogecoin (DOGE)": {"yf": "DOGE-USD", "tv": "BINANCE:DOGEUSDT"}
            }
            
            yf_symbol = asset_map[coin_opt]["yf"]
            tv_symbol = asset_map[coin_opt]["tv"]

        try:
            coin_data = yf.Ticker(yf_symbol)
            hist = coin_data.history(period="2d")
            
            if not hist.empty:
                current_price = hist["Close"].iloc[-1]
                prev_price = hist["Close"].iloc[0]
                delta = ((current_price - prev_price) / prev_price) * 100
                volume = hist["Volume"].iloc[-1]
                
                m1, m2, m3 = st.columns(3)
                m1.metric("Current Price", f"${current_price:,.2f}", f"{delta:.2f}%")
                m2.metric("24h Volume", f"${volume:,.0f}")
                m3.metric("Asset", coin_opt.split('(')[1][:-1]) 
            else:
                st.warning("Data loading...")
        except:
            st.error("Metric data unavailable. Chart below is live.")

        st.markdown("---")

        tv_widget_code = f"""
        <div class="tradingview-widget-container">
          <div id="tradingview_chart"></div>
          <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
          <script type="text/javascript">
          new TradingView.widget(
          {{
          "width": "100%",
          "height": 500,
          "symbol": "{tv_symbol}",
          "interval": "D",
          "timezone": "Etc/UTC",
          "theme": "dark",
          "style": "1",
          "locale": "en",
          "toolbar_bg": "#f1f3f6",
          "enable_publishing": false,
          "allow_symbol_change": true,
          "container_id": "tradingview_chart"
          }}
          );
          </script>
        </div>
        """
        components.html(tv_widget_code, height=510)

        st.markdown("---")
        st.subheader("🧮 Quick Converter")
        col_conv1, col_conv2 = st.columns(2)
        with col_conv1:
            amount = st.number_input(f"Amount of {coin_opt.split('(')[1][:-1]}", value=1.0)
        with col_conv2:
            try:
                st.metric("Value in USD", f"${(amount * current_price):,.2f}")
            except:
                st.write("Loading price...")

    # --- TAB 4: NEWS ---
    with tab_news:
        st.header("📰 Global Crypto News")
        st.write("Live feed from **Cointelegraph**. Always verify news from multiple sources.")
        col_news1, col_news2 = st.columns([2, 1])
        with col_news1:
            st.subheader("Latest Headlines")
            news_list = get_crypto_news()
            if news_list:
                for item in news_list:
                    with st.container():
                        st.markdown(f"#### [{item['title']}]({item['link']})")
                        st.caption(f"**{item['source']}** | 🕒 {item['pubDate']}")
                        st.markdown("---")
            else:
                st.info("Loading news... (If this takes too long, check connection)")
        with col_news2:
            st.subheader("Educational: How to Read News")
            with st.expander("🟢 Bullish vs 🔴 Bearish"):
                st.write("**Bullish:** Good news (Adoption, New Tech). Price often goes UP.")
                st.write("**Bearish:** Bad news (Hacks, Bans). Price often goes DOWN.")
            with st.expander("⚠️ FUD vs. FOMO"):
                st.write("**FUD:** Fake fear to make you sell.")
                st.write("**FOMO:** Fake hype to make you buy.")
            st.info("💡 **Pro Tip:** Never trade immediately on a headline. Wait 15 minutes.")

    # --- TAB 5: QUIZ (UNCHANGED) ---
    with tab_quiz:
        st.header("🧠 Knowledge Check")
        st.write("Test your mastery of the Academy material. Can you get a perfect 10/10?")
        
        with st.form("quiz_form"):
            score = 0
            
            st.subheader("Part 1: The Basics")
            q1 = st.radio("1. Where is your crypto actually stored?", 
                          ["On the Blockchain", "In my hardware wallet", "In the Coinbase app"], index=None)
            
            q2 = st.radio("2. Who controls the Blockchain ledger?", 
                          ["The Bank", "No one (Distributed Network)", "Google"], index=None)
            
            q3 = st.radio("3. What is a 'Smart Contract' best compared to?", 
                          ["A Lawyer", "A Vending Machine", "A Handshake"], index=None)

            st.markdown("---")
            st.subheader("Part 2: Wallets & Security")
            
            q4 = st.radio("4. Which wallet type is safest for long-term storage?", 
                          ["Hot Wallet", "Cold Wallet", "Exchange Account"], index=None)
            
            q5 = st.radio("5. What should you do with your Seed Phrase (Private Key)?", 
                          ["Save it in Google Drive", "Screenshot it", "Write it on paper/metal & hide it"], index=None)
            
            q6 = st.radio("6. Will legitimate Crypto Support ever DM you first?", 
                          ["Yes, to help me", "No, NEVER"], index=None)

            st.markdown("---")
            st.subheader("Part 3: Advanced Concepts")

            q7 = st.radio("7. What is 'Staking'?", 
                          ["Selling your coins", "Earning interest by securing the network", "Mining Bitcoin"], index=None)
            
            q8 = st.radio("8. What does 'Bullish' mean in market terms?", 
                          ["Prices going DOWN", "Prices going UP", "Market is flat"], index=None)
            
            q9 = st.radio("9. What pays for a transaction on the network?", 
                          ["Gas Fees", "Subscription Fees", "It is free"], index=None)
            
            q10 = st.radio("10. Can you reverse a blockchain transaction if you make a mistake?", 
                           ["Yes, call support", "No, it is immutable (permanent)"], index=None)
            
            st.markdown("---")
            submitted = st.form_submit_button("Submit Answers")
            
            if submitted:
                # Calculate Score
                if q1 == "On the Blockchain": score += 1
                if q2 == "No one (Distributed Network)": score += 1
                if q3 == "A Vending Machine": score += 1
                if q4 == "Cold Wallet": score += 1
                if q5 == "Write it on paper/metal & hide it": score += 1
                if q6 == "No, NEVER": score += 1
                if q7 == "Earning interest by securing the network": score += 1
                if q8 == "Prices going UP": score += 1
                if q9 == "Gas Fees": score += 1
                if q10 == "No, it is immutable (permanent)": score += 1
                
                # Feedback
                if score == 10:
                    st.balloons()
                    st.success(f"🏆 PERFECT SCORE! 10/10. You are a true Crypto Master.")
                elif score >= 7:
                    st.success(f"✅ Great Job! You got {score}/10. You are ready to start.")
                else:
                    st.error(f"⚠️ You got {score}/10. Please review the lessons and try again.")
