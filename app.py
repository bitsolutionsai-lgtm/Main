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
# Added the "Quiz" Tab
tab_learn, tab_sim, tab_data, tab_quiz = st.tabs(["📖 Learn Concepts", "🧪 Lab Simulation", "📊 Live Market", "📝 Quiz & Cert"])

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

    with st.expander("Lesson 2: Smart Contracts (The 'Robot Lawyer')"):
        st.subheader("The Vending Machine Analogy")
        st.write("A Smart Contract is a vending machine: You put money in, the snack comes out. No employee needed.")
        st.code("""
        function pay_insurance():
            if flight_status == "CANCELLED":
                send_money(customer, $500)
        """, language="python")

    with st.expander("Lesson 3: Consensus & Staking"):
        st.write("How strangers agree on truth.")
        c1, c2 = st.columns(2)
        with c1:
            st.warning("Miners (Proof of Work): Solve puzzles.")
        with c2:
            st.success("Validators (Proof of Stake): Lock up money.")
        st.info("Liquid Staking = Valet Parking (Get a claim ticket for your parked car).")

    with st.expander("Lesson 4: What actually IS a Wallet?"):
        st.write("The wallet is the **Remote Control**, not the money vault.")
        c_mail_1, c_mail_2 = st.columns(2)
        with c_mail_1:
            st.success("🟢 Public Key (Email Address): Share with anyone.")
        with c_mail_2:
            st.error("🔴 Private Key (Password): NEVER share this.")
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

# --- TAB 4: QUIZ & CERTIFICATE (NEW) ---
with tab_quiz:
    st.header("📝 Final Exam")
    st.write("Answer 3 questions to earn your Bit Solutions Certificate.")
    
    with st.form("quiz_form"):
        # Question 1
        q1 = st.radio(
            "1. What is the 'Golden Rule' of Crypto Security?",
            ["Share your password with support", "Never share your Seed Phrase", "Use the same password everywhere"]
        )
        
        # Question 2
        q2 = st.radio(
            "2. Which blockchain is described as a 'Race Car' (Fast but less stable)?",
            ["Bitcoin", "Ethereum", "Solana"]
        )
        
        # Question 3
        q3 = st.radio(
            "3. If you lose your Cold Wallet (USB stick), is your money gone?",
            ["Yes, it's inside the stick", "No, you can recover it with your Seed Phrase"]
        )
        
        submit_quiz = st.form_submit_button("Submit Answers")
        
        if submit_quiz:
            # Check Answers
            if q1 == "Never share your Seed Phrase" and q2 == "Solana" and q3 == "No, you can recover it with your Seed Phrase":
                st.balloons()
                st.success("🎉 CONGRATULATIONS! You passed.")
                
                st.markdown("""
                <div style="background-color: #198754; padding: 20px; border-radius: 10px; border: 2px solid gold; text-align: center;">
                    <h2 style="color: white !important;">🏆 Certificate of Completion</h2>
                    <p style="color: white !important;">This certifies that the student has mastered the basics of Blockchain Technology.</p>
                    <p style="color: white !important;"><b>Issued by: Bit Solutions Academy</b></p>
                </div>
                """, unsafe_allow_html=True)
                
                st.divider()
                st.write("### 🚀 Ready for the next step?")
                st.write("Need help setting up your own mining rig, wallet, or business blockchain?")
                
                # Simple Contact Simulation
                with st.expander("Book a Private Consultation"):
                    st.text_input("Your Email")
                    st.text_area("What do you need help with?")
                    if st.button("Request Call"):
                        st.success("Request Sent! We will contact you shortly.")
                
            else:
                st.error("❌ One or more answers were incorrect. Review the lessons and try again!")
