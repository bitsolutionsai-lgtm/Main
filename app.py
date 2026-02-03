import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf
import time
import smtplib
import requests
import xml.etree.ElementTree as ET
import streamlit.components.v1 as components
import google.generativeai as genai 
import plotly.graph_objects as go 
from plotly.subplots import make_subplots 
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

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

def enter_site():
    st.session_state.page = 'main'

# --- API CONFIGURATION (SILENT LOAD) ---
api_configured = False
if "gemini" in st.secrets and "api_key" in st.secrets["gemini"]:
    try:
        genai.configure(api_key=st.secrets["gemini"]["api_key"])
        api_configured = True
    except Exception as e:
        pass

# --- EMAIL FUNCTION ---
def send_email(user_email, user_message):
    if "email" not in st.secrets:
        return False
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

# --- HELPER: CALCULATE RSI ---
def calculate_rsi(data, window=14):
    delta = data['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
    rs = gain / loss
    return 100 - (100 / (1 + rs))

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    /* BACKGROUND IMAGE SETTINGS */
    .stApp {
        background-image: linear-gradient(rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.9)), 
                          url('https://images.unsplash.com/photo-1639322537228-f710d846310a?auto=format&fit=crop&q=80');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }
    
    /* Text Readability */
    h1, h2, h3 { 
        color: #FFFFFF !important; 
        text-shadow: 0px 4px 4px rgba(0,0,0,0.8);
        font-weight: 700 !important;
    }
    p, li, label, div { 
        color: #E6E6E6 !important; 
        font-weight: 500 !important; 
        line-height: 1.6; 
    }
    
    /* --- CRITICAL FIX: SELECT BOX & DROPDOWN MENU VISIBILITY --- */
    
    /* 1. The Closed Box (Input Field) */
    div[data-baseweb="select"] > div {
        background-color: #1a1a1d !important; /* Dark Grey Background */
        color: white !important;               /* White Text */
        border-color: #444 !important;         /* Dark Border */
    }
    
    /* 2. The Text Inside the Closed Box */
    div[data-baseweb="select"] span {
        color: white !important;
    }
    
    /* 3. The Dropdown Menu (The List that Pops Open) */
    div[data-baseweb="menu"] {
        background-color: #1a1a1d !important; /* Dark Background for the list */
    }
    
    /* 4. The Options Inside the Menu */
    div[data-baseweb="menu"] div, 
    div[data-baseweb="menu"] span, 
    div[data-baseweb="menu"] li {
        color: white !important; /* Force all list text to white */
    }
    
    /* 5. Hover State (When you mouse over an option) */
    div[data-baseweb="menu"] li:hover {
        background-color: #00BFA5 !important; /* Teal Highlight */
        color: white !important;
    }
    
    /* 6. Icon Colors (The arrow) */
    div[data-baseweb="select"] svg {
        fill: white !important;
    }
    /* ----------------------------------------------------------- */

    /* Buttons */
    div.stButton > button {
        background-color: #00BFA5;
        color: white;
        border: none;
        padding: 10px 24px;
        font-size: 1.2em;
        font-weight: 600;
        border-radius: 8px;
        transition: all 0.3s;
        box-shadow: 0px 4px 10px rgba(0, 191, 165, 0.3);
    }
    div.stButton > button:hover {
        background-color: #00E5C0;
        box-shadow: 0px 0px 15px #00BFA5;
        transform: translateY(-2px);
    }
    
    /* Sidebar */
    section[data-testid="stSidebar"] {
        background-color: rgba(20, 20, 25, 0.95);
        border-right: 1px solid #343A40;
    }
    
    /* Tabs */
    .stTabs [data-baseweb="tab-list"] { gap: 10px; }
    .stTabs [data-baseweb="tab"] {
        background-color: rgba(255, 255, 255, 0.05);
        color: #ADB5BD;
        border-radius: 5px;
        border: 1px solid rgba(255,255,255,0.1);
    }
    .stTabs [aria-selected="true"] {
        background-color: #00BFA5;
        color: #FFFFFF !important;
        font-weight: bold;
        border-color: #00BFA5;
    }
    
    /* Metric Cards */
    div[data-testid="stMetric"] {
        background-color: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 15px;
        border-radius: 10px;
    }
    
    /* AI Agent Modal - Dark Background Fix */
    div[role="dialog"] {
        background-color: #1a1a1d !important;
        color: white !important;
        border: 1px solid #333;
    }
    
    /* Code Block */
    code {
        color: #e83e8c;
        background-color: #212529;
        padding: 2px 4px;
        border-radius: 4px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- ☁️ FLOATING CHAT DIALOG ---
@st.dialog("☁️ Cloud Agent")
def show_chat_dialog():
    st.caption("I am your floating assistant. Ask me anything!")
    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    if prompt := st.chat_input("Ask a question..."):
        st.session_state.chat_history.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        if not api_configured:
            st.error("⚠️ AI Offline. Check Secrets.")
        else:
            with st.chat_message("assistant"):
                message_placeholder = st.empty()
                try:
                    model = genai.GenerativeModel('gemini-2.5-flash')
                    context_prompt = f"You are a crypto expert. Answer concise: {prompt}"
                    full_response = ""
                    response = model.generate_content(context_prompt, stream=True)
                    for chunk in response:
                        if chunk.text:
                            full_response += chunk.text
                            message_placeholder.markdown(full_response + "▌")
                    message_placeholder.markdown(full_response)
                    st.session_state.chat_history.append({"role": "assistant", "content": full_response})
                    st.rerun()
                except Exception as e:
                    st.error(f"Error: {str(e)}")

# ==========================================
# SIDEBAR
# ==========================================
with st.sidebar:
    st.header("Baez IT Solutions")
    st.write("Expert Crypto & IT Consulting.")
    st.markdown("---")
    st.write("Need help?")
    if st.button("☁️ OPEN CLOUD AGENT", type="primary", use_container_width=True, key="sidebar_agent"):
        show_chat_dialog()
    st.markdown("---")
    st.subheader("Services")
    st.write("🔒 **Wallet Security Audits**")
    st.write("⚙️ **Node Setup & Maintenance**")
    st.write("📈 **DeFi Strategy Planning**")
    st.markdown("---")
    st.subheader("Community")
    st.link_button("💬 Join Discord Server", "https://discord.gg/YOUR_INVITE_CODE")
    st.markdown("---")
    with st.form("contact_form"):
        contact_email = st.text_input("Your Email")
        contact_msg = st.text_area("How can we help?")
        submit_button = st.form_submit_button("Send")
    if submit_button:
        if contact_email and contact_msg:
            with st.spinner("Sending..."):
                time.sleep(1)
                success = send_email(contact_email, contact_msg)
                if success: st.success("✅ Sent!")
                elif "email" not in st.secrets: st.success("✅ Simulated!")
                else: st.error("❌ Error.")

# ==========================================
# PAGE 1: COVER
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
# PAGE 2: MAIN
# ==========================================
else:
    col1, col2 = st.columns([3, 1])
    with col1:
        st.title("BIT SOLUTIONS ACADEMY")
        st.caption("Classroom Dashboard")
    with col2:
        if st.button("☁️ Launch AI Agent", type="primary", use_container_width=True, key="dashboard_agent"):
            show_chat_dialog()
        if st.button("⬅ Exit to Cover", use_container_width=True):
            st.session_state.page = 'cover'
            st.rerun()

    st.markdown("---")

    # --- NAVIGATION ---
    tab_news, tab_data, tab_learn, tab_quiz = st.tabs(["⚡ Crypto News", "💎 Live Market", "🎓 Learn Concepts", "🧩 Knowledge Quiz"])

    # --- TAB 1: NEWS ---
    with tab_news:
        st.header("⚡ Global Crypto News")
        st.write("Live feed from **Cointelegraph**.")
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

    # --- TAB 2: LIVE MARKET (REVAMPED) ---
    with tab_data:
        st.header("💎 Professional Market Terminal")
        
        # 1. Top Controls
        c_sel, c_time, c_type = st.columns([2, 1, 1])
        with c_sel:
            coin_opt = st.selectbox("Select Asset Pair:", 
                                    ["Bitcoin (BTC-USD)", "Ethereum (ETH-USD)", "Solana (SOL-USD)", "Cardano (ADA-USD)", "Ripple (XRP-USD)", "Dogecoin (DOGE-USD)"])
            ticker_symbol = coin_opt.split('(')[1][:-1] # Extracts "BTC-USD"
        with c_time:
            timeframe = st.selectbox("Timeframe", ["1mo", "3mo", "6mo", "1y", "ytd"], index=1)
        with c_type:
            chart_type = st.selectbox("Chart Type", ["Candlestick", "Line"])

        # 2. Data Fetching
        try:
            ticker_data = yf.Ticker(ticker_symbol)
            df = ticker_data.history(period=timeframe)
            
            if not df.empty:
                # Calculate Indicators
                df['SMA_20'] = df['Close'].rolling(window=20).mean()
                df['RSI'] = calculate_rsi(df)
                
                # Current Metrics
                curr_price = df['Close'].iloc[-1]
                prev_price = df['Close'].iloc[-2]
                day_high = df['High'].iloc[-1]
                day_low = df['Low'].iloc[-1]
                price_change = curr_price - prev_price
                pct_change = (price_change / prev_price) * 100
                current_rsi = df['RSI'].iloc[-1]

                # 3. KPI Row
                kpi1, kpi2, kpi3, kpi4 = st.columns(4)
                kpi1.metric("Current Price", f"${curr_price:,.2f}", f"{pct_change:.2f}%")
                kpi2.metric("24h High", f"${day_high:,.2f}")
                kpi3.metric("24h Low", f"${day_low:,.2f}")
                
                # RSI Logic Badge
                rsi_state = "Neutral 😐"
                if current_rsi > 70: rsi_state = "Overbought (Sell Risk) 🔴"
                elif current_rsi < 30: rsi_state = "Oversold (Buy Opp) 🟢"
                kpi4.metric("RSI (14)", f"{current_rsi:.1f}", rsi_state, delta_color="off")

                st.markdown("---")

                # 4. Professional Charting (Plotly)
                fig = make_subplots(rows=2, cols=1, shared_xaxes=True, 
                                    vertical_spacing=0.05, row_heights=[0.7, 0.3])

                # Main Chart (Candles)
                if chart_type == "Candlestick":
                    fig.add_trace(go.Candlestick(x=df.index,
                                    open=df['Open'], high=df['High'],
                                    low=df['Low'], close=df['Close'], name='OHLC'), row=1, col=1)
                else:
                    fig.add_trace(go.Scatter(x=df.index, y=df['Close'], 
                                             mode='lines', name='Price', line=dict(color='#00BFA5')), row=1, col=1)
                
                # Add SMA
                fig.add_trace(go.Scatter(x=df.index, y=df['SMA_20'], 
                                         mode='lines', name='SMA 20', line=dict(color='orange', width=1)), row=1, col=1)

                # RSI Sub-chart
                fig.add_trace(go.Scatter(x=df.index, y=df['RSI'], 
                                         name='RSI', line=dict(color='#A020F0')), row=2, col=1)
                
                # RSI Lines
                fig.add_hline(y=70, line_dash="dash", line_color="red", row=2, col=1)
                fig.add_hline(y=30, line_dash="dash", line_color="green", row=2, col=1)

                # Layout styling
                fig.update_layout(
                    height=600,
                    margin=dict(l=20, r=20, t=30, b=20),
                    paper_bgcolor='rgba(0,0,0,0)',
                    plot_bgcolor='rgba(0,0,0,0.1)',
                    font=dict(color="white"),
                    xaxis_rangeslider_visible=False
                )
                fig.update_xaxes(showgrid=False)
                fig.update_yaxes(showgrid=True, gridcolor='rgba(255,255,255,0.1)')
                
                st.plotly_chart(fig, use_container_width=True)

            else:
                st.warning("Loading data...")
        except Exception as e:
            st.error(f"Error loading market data: {e}")

        # 5. TradingView Widget (Bottom for Quick Reference)
        with st.expander("🌍 View Global TradingView Chart"):
            tv_sym = ticker_symbol.replace("-", "") # Convert BTC-USD to BTCUSD
            components.html(f"""
            <div class="tradingview-widget-container">
              <div id="tradingview_chart"></div>
              <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
              <script type="text/javascript">
              new TradingView.widget(
              {{ "width": "100%", "height": 500, "symbol": "COINBASE:{tv_sym}", "interval": "D", "timezone": "Etc/UTC", "theme": "dark", "style": "1", "locale": "en", "toolbar_bg": "#f1f3f6", "enable_publishing": false, "allow_symbol_change": true, "container_id": "tradingview_chart" }}
              );
              </script>
            </div>
            """, height=510)

    # --- TAB 3: LEARN CONCEPTS ---
    with tab_learn:
        st.header("Blockchain Fundamentals")
        # --- LESSON 1 ---
        with st.expander("Lesson 1: What is a Blockchain? (The Deep Dive)"):
            st.subheader("1. The History: Origins of Bitcoin")
            st.write("To understand Blockchain, you must understand why it was built. In **2008**, the global financial system collapsed.")
            st.info("👤 **Satoshi Nakamoto:** On Oct 31, 2008, an anonymous cryptographer published the **Bitcoin Whitepaper**.")
            st.link_button("📜 Read the Bitcoin Whitepaper", "https://bitcoin.org/bitcoin.pdf")
            st.divider()
            st.subheader("2. What is it?")
            st.write("A blockchain is a **Distributed Digital Ledger**. No single computer runs it.")
            st.divider()
            st.subheader("3. Security")
            st.write("Blockchain security relies on **Hashing (SHA-256)** and **Consensus**.")
            st.divider()
            st.subheader("4. The Future")
            st.success("🚀 **The Phase of Utility:** Tokenization, L2 Scaling, DePIN.")

        # --- LESSON 2 ---
        with st.expander("Lesson 2: Smart Contracts (The 'Robot Lawyer')"):
            st.subheader("1. What exactly is a Smart Contract?")
            st.write("It is **self-executing code**. 'If This, Then That'.")
            st.info("💡 **Analogy:** A Vending Machine. You pay, you get item. No clerk needed.")
            st.code("""
            // Pseudo-code
            contract SimplePayment {
                function sendMoney() public payable {
                    if (msg.value >= 10 ETH) { transferOwnership(msg.sender); }
                }
            }""", language="solidity")

        # --- LESSON 3 ---
        with st.expander("Lesson 3: Staking & Yield"):
            st.subheader("1. Ways to Earn")
            st.write("**Staking:** Secure the network (Low Risk). **Lending:** Loan to others (Med Risk).")
            st.success("Liquid Staking: Get a receipt token (JitoSOL) so you stay liquid while earning.")

        # --- LESSON 4 ---
        with st.expander("Lesson 4: Wallets (Hot vs Cold)"):
            st.subheader("Hot vs. Cold")
            st.write("**Hot (Phantom):** Connected to internet. Good for spending.")
            st.write("**Cold (Ledger):** Offline. Good for savings.")
            st.error("🔴 **Private Key:** Never share this. It is your master password.")

        # --- LESSON 5 ---
        with st.expander("Lesson 5: Security Masterclass"):
            st.success("✅ **DO:** Write seed phrase on paper. Check URLs.")
            st.error("❌ **DON'T:** Store seed phrase in cloud. Click DM links.")

    # --- TAB 4: QUIZ ---
    with tab_quiz:
        st.header("🧠 Knowledge Check")
        st.write("Test your mastery of the Academy material. Can you get a perfect 10/10?")
        with st.form("quiz_form"):
            score = 0
            st.subheader("Part 1: The Basics")
            q1 = st.radio("1. Where is your crypto actually stored?", ["On the Blockchain", "In my hardware wallet", "In the Coinbase app"], index=None)
            q2 = st.radio("2. Who controls the Blockchain ledger?", ["The Bank", "No one (Distributed Network)", "Google"], index=None)
            q3 = st.radio("3. What is a 'Smart Contract' best compared to?", ["A Lawyer", "A Vending Machine", "A Handshake"], index=None)
            st.markdown("---")
            st.subheader("Part 2: Wallets & Security")
            q4 = st.radio("4. Which wallet type is safest for long-term storage?", ["Hot Wallet", "Cold Wallet", "Exchange Account"], index=None)
            q5 = st.radio("5. What should you do with your Seed Phrase?", ["Save it in Google Drive", "Screenshot it", "Write it on paper/metal & hide it"], index=None)
            q6 = st.radio("6. Will legitimate Crypto Support ever DM you first?", ["Yes, to help me", "No, NEVER"], index=None)
            st.markdown("---")
            st.subheader("Part 3: Advanced Concepts")
            q7 = st.radio("7. What is 'Staking'?", ["Selling your coins", "Earning interest by securing the network", "Mining Bitcoin"], index=None)
            q8 = st.radio("8. What does 'Bullish' mean in market terms?", ["Prices going DOWN", "Prices going UP", "Market is flat"], index=None)
            q9 = st.radio("9. What pays for a transaction on the network?", ["Gas Fees", "Subscription Fees", "It is free"], index=None)
            q10 = st.radio("10. Can you reverse a blockchain transaction?", ["Yes, call support", "No, it is immutable (permanent)"], index=None)
            st.markdown("---")
            submitted = st.form_submit_button("Submit Answers")
            if submitted:
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
                if score == 10:
                    st.balloons()
                    st.success(f"🏆 PERFECT SCORE! 10/10. You are a true Crypto Master.")
                elif score >= 7:
                    st.success(f"✅ Great Job! You got {score}/10. You are ready to start.")
                else:
                    st.error(f"⚠️ You got {score}/10. Please review the lessons and try again.")
