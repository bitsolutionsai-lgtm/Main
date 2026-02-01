import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf
import time
import smtplib
import requests
import xml.etree.ElementTree as ET
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

    # --- TAB 1: THE CLASSROOM (RESTORED TO EXPANDED VERSIONS) ---
    with tab_learn:
        st.header("Blockchain Fundamentals")
        
        # --- LESSON 1: EXPANDED ---
        with st.expander("Lesson 1: What is a Blockchain? (The Foundation)"):
            st.subheader("1. The Problem with 'Normal' Money")
            st.write("Right now, if I send you $50, we both trust the **Bank** to update the ledger. The Bank has the 'Master Book'.")
            st.error("❌ **The Risk:** What if the Bank makes a mistake? What if they freeze your account? You don't own your data.")
            st.divider()
            st.subheader("2. The Solution: The 'Stone Tablet' Analogy")
            st.write("Imagine a giant **Stone Tablet** in the middle of the Town Square.")
            c_concept1, c_concept2 = st.columns(2)
            with c_concept1:
                st.info("📢 **Public & Transparent**")
                st.write("""
                * Everyone in town can see the tablet.
                * If Alice sends Bob $5, a 'Miner' carves it into the stone.
                * **Everyone sees it happen.** No secrets.
                """)
            with c_concept2:
                st.success("🔒 **Immutable (Permanent)**")
                st.write("""
                * Once carved, it is there **forever**.
                * You cannot use an eraser.
                * You cannot tear out the page.
                * This creates **Total Trust** without a middleman.
                """)
            st.divider()
            st.subheader("3. How does it actually work?")
            st.write("It's not just one tablet. It is **Distributed**.")
            st.write("Imagine if **10,000 people** took a photo of that stone tablet instantly.")
            st.caption("If a hacker tries to change ONE photo, the other 9,999 people will say: 'Hey! That's fake!' and reject it. That is why Bitcoin has never been hacked.")
            st.divider()
            st.subheader("4. Real World Use Cases (Beyond Bitcoin)")
            c_use1, c_use2 = st.columns(2)
            with c_use1:
                st.warning("☕ **Supply Chain (Starbucks)**")
                st.write("**The Problem:** Is this coffee actually Fair Trade? Or did they just slap a sticker on it?")
                st.write("**Blockchain:** You scan the bag. You see the *exact date* the farmer picked the beans, recorded on the blockchain. It cannot be faked.")
            with c_use2:
                st.info("🏡 **Real Estate (The Deed)**")
                st.write("**The Problem:** Buying a house takes 30 days because lawyers have to verify the paper title history.")
                st.write("**Blockchain:** The 'Title' is a token. You send the money, the house token hits your wallet. Deal done in 10 seconds.")

        # --- LESSON 2: EXPANDED ---
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

        # --- LESSON 3: EXPANDED ---
        with st.expander("Lesson 3: Staking & Liquid Staking (How to Earn Interest)"):
            st.subheader("1. What is Staking?")
            st.write("Staking is basically a **High-Yield Savings Account** for the internet. You lock up your crypto to help secure the network, and the network pays you interest (usually 4-7%).")
            st.divider()
            st.subheader("2. The Problem: 'The Locked Vault'")
            st.write("In standard staking, your money is **LOCKED**. You cannot touch it. If an emergency happens, you have to wait days to get it out.")
            c_lock1, c_lock2 = st.columns(2)
            with c_lock1:
                st.error("🚫 Standard Staking (Bank CD)")
                st.write("""
                * **You give:** 1 ETH.
                * **Status:** Locked in a vault.
                * **Use:** None. It sits there.
                * **Exit:** Wait 5-7 days to withdraw.
                """)
            with c_lock2:
                st.success("💧 Liquid Staking (The Solution)")
                st.write("""
                * **You give:** 1 ETH.
                * **You get:** 1 'Receipt Token' (stETH).
                * **Status:** You hold the receipt in your wallet.
                * **Use:** You can sell the receipt instantly if you need cash.
                """)
            st.divider()
            st.subheader("3. The 'Casino Chip' Analogy (Best for Beginners)")
            st.info("Think of Liquid Staking like walking into a Casino.")
            st.write("""
            1.  You give the cashier **$100 Cash** (Your Crypto).
            2.  They give you a **$100 Chip** (The Liquid Token).
            3.  **The Magic:** While you hold that chip, it automatically grows in value. When you leave, you might cash out **$105**.
            4.  **The Freedom:** If you don't want to wait at the cashier, you can just give the chip to a friend (trade it) for cash instantly. You aren't stuck.
            """)
            st.write("**Top Examples:** Lido (stETH), Coinbase (cbETH), Rocket Pool (rETH).")

        # --- LESSON 4: EXPANDED ---
        with st.expander("Lesson 4: What actually IS a Wallet? (Deep Dive)"):
            st.subheader("1. The 'Glass Box' Analogy")
            st.write("Crypto is confusing because you can't 'see' the money. Here is the best way to visualize it:")
            st.info("Imagine the Blockchain is a giant wall of **Glass Lockboxes**.")
            st.write("""
            * **Anyone** can see inside Box #402. They can see it has 5 BTC.
            * **Only the person with the Key** can open Box #402 to move the money.
            * Your 'Wallet' is just a **Keychain** that holds the key to your box. It doesn't hold the money itself.
            """)
            st.divider()
            st.subheader("2. How does it work? (Email Analogy)")
            st.write("When you create a wallet, you generate two things:")
            c_key1, c_key2 = st.columns(2)
            with c_key1:
                st.success("🟢 Public Key (The Address)")
                st.write("**Think: Email Address**")
                st.write("You give this to people so they can send you money. It is perfectly safe to share.")
                st.code("0x71C...9A23")
            with c_key2:
                st.error("🔴 Private Key (The Seed Phrase)")
                st.write("**Think: Email Password**")
                st.write("This allows you to 'Login' and spend the money. If you give this away, you lose everything.")
                st.code("apple river galaxy...")
            st.divider()
            st.subheader("3. Hot vs. Cold (The Pocket vs. The Vault)")
            st.write("Not all wallets are the same. You need to choose the right one for your goals.")
            c_hot, c_cold = st.columns(2)
            with c_hot:
                st.warning("🔥 Hot Wallet (The Pocket)")
                st.write("""
                * **What:** An app on your phone (Metamask, Coinbase Wallet).
                * **Pros:** Fast, easy, connects to websites.
                * **Cons:** Connected to the internet (hackable).
                * **Use for:** Buying coffee, trading, carrying $100-$500.
                """)
            with c_cold:
                st.info("❄️ Cold Wallet (The Home Safe)")
                st.write("""
                * **What:** A physical USB stick (Ledger, Trezor).
                * **Pros:** Impossible to hack (offline).
                * **Cons:** Annoying to use (must plug in).
                * **Use for:** Your life savings, retirement, holding >$1,000.
                """)
            st.divider()
            st.write("**Which one should you get?**")
            col_rec1, col_rec2, col_rec3 = st.columns(3)
            with col_rec1:
                st.write("**Total Beginner**")
                st.link_button("Coinbase App ↗", "https://www.coinbase.com")
            with col_rec2:
                st.write("**Explorer**")
                st.link_button("Phantom Wallet ↗", "https://phantom.app")
            with col_rec3:
                st.write("**Investor**")
                st.link_button("Ledger Nano ↗", "https://www.ledger.com")

        # --- LESSON 5: EXPANDED (DEEP DIVE) ---
        with st.expander("Lesson 5: 🛡️ Security Masterclass (The Survival Guide)"):
            st.subheader("1. The Core Concept: 'Self-Custody'")
            st.write("In crypto, YOU are the bank. There is no customer support hotline. If you lose your keys, the money is gone. This responsibility requires new habits.")
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
            st.write("**The 'Fake Support' Scam:**")
            st.write("You ask a question on Twitter/Discord. Someone named 'MetaMask Support' DMs you. They are very helpful. They send you a link to 'sync your wallet'.")
            st.error("🚨 **REALITY:** Support will NEVER DM you first. That link steals your money.")
            st.divider()
            st.subheader("4. Advanced: Revoking Allowances")
            st.write("When you use a DeFi app (like Uniswap), you give it permission to spend your coins. If that app gets hacked later, your wallet is at risk.")
            st.info("🛠️ **The Fix:** Once a month, use a tool like **Revoke.cash** to disconnect your wallet from old apps you don't use anymore.")

    # --- TAB 2: THE SANDBOX ---
    with tab_sim:
        st.header("🧪 Interactive Lab")
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

    # --- TAB 3: REAL WORLD DATA ---
    with tab_data:
        st.header("Live Market Data (24h Change)")
        def get_data(t):
            try:
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

    # --- TAB 4: CRYPTO NEWS (RSS FEED) ---
    with tab_news:
        st.header("📰 Global Crypto News")
        st.write("Live feed from **Cointelegraph**. Always verify news from multiple sources.")
        col_news1, col_news2 = st.columns([2, 1])
        
        with col_news1:
            st.subheader("Latest Headlines")
            # Get news from the robust RSS fetcher
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

    # --- TAB 5: QUIZ ---
    with tab_quiz:
        st.header("🧠 Knowledge Check")
        score = 0
        q1 = st.radio("1. Where is your crypto actually stored?", ["In my Ledger USB stick", "On the Blockchain", "In the Coinbase App"])
        if q1 == "On the Blockchain": score += 1
        q2 = st.radio("2. What happens if you lose your Seed Phrase?", ["I can reset it via email", "I lose my money forever", "Support can recover it"])
        if q2 == "I lose my money forever": score += 1
        q3 = st.radio("3. Which wallet type is safer for long-term storage?", ["Hot Wallet", "Cold Wallet", "Exchange Wallet"])
        if q3 == "Cold Wallet": score += 1
        st.markdown("---")
        if st.button("Check Score"):
            if score == 3:
                st.balloons()
                st.success(f"🎉 Perfect Score! 3/3. You are ready for DeFi.")
            else:
                st.warning(f"You got {score}/3. Review the lessons and try again!")
