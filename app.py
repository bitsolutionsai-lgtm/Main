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

    # --- TAB 1: LEARN (UNCHANGED) ---
    with tab_learn:
        st.header("Blockchain Fundamentals")
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
            st.write("It's not just one tablet. It is **Distributed**. Imagine if **10,000 people** took a photo of that stone tablet instantly.")
            st.caption("If a hacker tries to change ONE photo, the other 9,999 people will say: 'Hey! That's fake!'")
            st.divider()
            st.subheader("4. Real World Use Cases")
            c_use1, c_use2 = st.columns(2)
            with c_use1:
                st.warning("☕ **Supply Chain**")
                st.write("You scan a coffee bag and see the *exact date* the farmer picked the beans. It cannot be faked.")
            with c_use2:
                st.info("🏡 **Real Estate**")
                st.write("The 'Title' is a token. You send money, the house token hits your wallet. Deal done in 10 seconds.")

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

        with st.expander("Lesson 3: Staking & Liquid Staking (How to Earn Interest)"):
            st.subheader("1. What is Staking?")
            st.write("Staking is basically a **High-Yield Savings Account** for the internet.")
            st.divider()
            st.subheader("2. The Problem: 'The Locked Vault'")
            c_lock1, c_lock2 = st.columns(2)
            with c_lock1:
                st.error("🚫 Standard Staking")
                st.write("Your money is locked in a vault. You cannot touch it for days.")
            with c_lock2:
                st.success("💧 Liquid Staking")
                st.write("You get a 'Receipt Token' (stETH) that represents your deposit. You can trade this receipt instantly.")
            st.divider()
            st.subheader("3. The 'Casino Chip' Analogy")
            st.write("You trade $100 Cash for a $100 Chip. The chip earns value while you hold it. You can cash out the chip anytime.")

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
            c_key1, c_key2 = st.columns(2)
            with c_key1:
                st.success("🟢 Public Key (Address)")
                st.write("**Think: Email Address.** Safe to share.")
                st.code("0x71C...9A23")
            with c_key2:
                st.error("🔴 Private Key (Seed Phrase)")
                st.write("**Think: Email Password.** NEVER SHARE THIS.")
                st.code("apple river galaxy...")
            st.divider()
            st.subheader("3. Hot vs. Cold")
            c_hot, c_cold = st.columns(2)
            with c_hot:
                st.warning("🔥 Hot Wallet (App)")
                st.write("Convenient but online. Good for spending ($100-$500).")
            with c_cold:
                st.info("❄️ Cold Wallet (USB)")
                st.write("Offline and secure. Good for savings (>$1000).")

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

    # --- TAB 2: LAB (ENHANCED) ---
    with tab_sim:
        st.header("🧪 Interactive Lab")
        st.write("Experiment with the mechanics of DeFi in a safe, simulated environment.")

        # --- LAB 1: GAS STATION ---
        st.markdown("---")
        st.subheader("⛽ 1. Gas Fee Visualizer")
        st.write("See how network congestion affects the cost of moving money.")
        
        col_traffic, col_chart = st.columns([1, 2])
        with col_traffic:
            traffic = st.select_slider("Select Network Traffic Level:", options=["Low", "Medium", "High", "Extreme"])
            if traffic == "Low": fees = [2.50, 0.05, 0.001]
            elif traffic == "Medium": fees = [8.00, 0.15, 0.002]
            elif traffic == "High": fees = [25.00, 0.60, 0.005]
            else: fees = [120.00, 2.50, 0.01] # Extreme
            
            st.caption("**Estimated Cost to Send $100:**")
            st.metric("Ethereum (L1)", f"${fees[0]:.2f}")
            st.metric("Base (L2)", f"${fees[1]:.2f}")
            st.metric("Solana", f"${fees[2]:.4f}")
            
        with col_chart:
            # Bar Chart Comparison
            fee_df = pd.DataFrame({
                "Network": ["Ethereum", "Base (L2)", "Solana"],
                "Fee ($)": fees
            })
            st.bar_chart(fee_df, x="Network", y="Fee ($)", color="#00BFA5")

        # --- LAB 2: COMPOUND STAKING ---
        st.markdown("---")
        st.subheader("📈 2. Compound Interest Calculator")
        st.write("Visualize the power of **DCA (Dollar Cost Averaging)** + **Staking Yield**.")
        
        c_calc1, c_calc2 = st.columns([1, 2])
        with c_calc1:
            initial = st.number_input("Starting Balance ($)", value=1000)
            monthly = st.number_input("Monthly Contribution ($)", value=100)
            apy = st.slider("APY (%)", 1, 50, 8)
            years = st.slider("Years to Grow", 1, 20, 10)
        
        with c_calc2:
            # Calculation: Future Value of a Series
            # Formula: FV = P * (1+r)^t + PMT * [ ((1+r)^t - 1) / r ]
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

        # --- LAB 3: IMPERMANENT LOSS ---
        st.markdown("---")
        st.subheader("⚖️ 3. Impermanent Loss Visualizer")
        st.write("What happens if you provide liquidity (Uniswap) and one coin price crashes (or pumps)?")
        st.info("💡 **Concept:** When prices diverge, LPs lose money compared to just HODLing.")
        
        il_col1, il_col2 = st.columns(2)
        with il_col1:
            price_change = st.slider("Price Change of Token A (%)", -90, 500, 0, format="%d%%")
        
        with il_col2:
            # IL Formula: 2 * sqrt(ratio) / (1 + ratio) - 1
            ratio = (1 + price_change / 100)
            if ratio < 0.01: ratio = 0.01 # Prevent zero division error
            
            il_pct = (2 * np.sqrt(ratio) / (1 + ratio)) - 1
            il_pct = abs(il_pct) * 100 # Make positive for display
            
            st.metric("Impermanent Loss", f"-{il_pct:.2f}%", delta_color="inverse")
            
            if price_change == 0:
                st.write("✅ No loss. Prices are stable.")
            elif il_pct < 5:
                st.warning("⚠️ Small loss. Trading fees might cover this.")
            else:
                st.error("🚨 **High Risk!** You are losing significant value compared to holding.")

        # --- LAB 4: DEX SIMULATOR ---
        st.markdown("---")
        st.subheader("🔄 4. DEX Swap Simulator")
        st.write("Try a simulated swap.")
        
        dex_c1, dex_c2 = st.columns(2)
        with dex_c1:
            swap_from = st.selectbox("From", ["ETH", "USDC", "SOL"])
            swap_amt = st.number_input("Amount", value=1.0)
        with dex_c2:
            swap_to = st.selectbox("To", ["USDC", "ETH", "SOL"], index=1)
            
            # Simulated Prices
            prices = {"ETH": 3200, "USDC": 1, "SOL": 145}
            
            if swap_from == swap_to:
                st.warning("Select different tokens.")
            else:
                rate = prices[swap_from] / prices[swap_to]
                receive_amt = swap_amt * rate
                st.metric("You Receive (Estimated)", f"{receive_amt:,.4f} {swap_to}")
                
                if st.button("Confirm Swap"):
                    with st.spinner("Broadcasting to network..."):
                        time.sleep(1.5)
                    st.success(f"✅ Swapped {swap_amt} {swap_from} for {receive_amt:.4f} {swap_to}!")
                    st.caption("Gas Fee Paid: $4.50 (Simulated)")

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

    # --- TAB 4: NEWS (UNCHANGED) ---
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
