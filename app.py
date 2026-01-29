import streamlit as st
import pandas as pd
import yfinance as yf

# 1. Page Configuration
st.set_page_config(
    page_title="Baez IT Solutions",
    page_icon="💻",
    layout="wide"
)

# 2. Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Services", "Market Data", "Contact Us"])

# --- PAGE: HOME ---
if page == "Home":
    st.title("Baez IT Solutions 🚀")
    st.subheader("Empowering Business with IT Excellence & Financial Intelligence")
    st.image("https://images.unsplash.com/photo-1518770660439-4636190af475", use_container_width=True)
    st.write("---")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.header("💡 Innovation")
        st.write("Cutting-edge technology strategies tailored for modern businesses.")
    with col2:
        st.header("🔒 Security")
        st.write("Enterprise-grade cybersecurity to protect your most valuable assets.")
    with col3:
        st.header("📈 Growth")
        st.write("Data-driven insights and crypto-consulting to expand your portfolio.")

# --- PAGE: SERVICES ---
elif page == "Services":
    st.title("Our Services")
    st.write("We bridge the gap between traditional IT and the future of finance.")
    with st.container():
        st.write("---")
        st.header("🖥️ Managed IT Services")
        st.write("• 24/7 Network Monitoring\n• Cloud Migration (AWS/Azure)\n• Hardware & Software Support")
    with st.container():
        st.write("---")
        st.header("🛡️ Cybersecurity")
        st.write("• Threat Detection & Prevention\n• Data Backup & Recovery\n• Compliance Audits")
    with st.container():
        st.write("---")
        st.header("💰 Crypto & Blockchain Consulting")
        st.write("• Wallet Setup & Security\n• Mining Rig Configuration\n• Portfolio Tracking Tools")

# --- PAGE: MARKET DATA (LIVE) ---
elif page == "Market Data":
    st.title("Live Crypto Intelligence 📊")
    st.write("Real-time market data sourced directly from the blockchain.")

    # A function to get the data safely
    def get_live_data(ticker):
        data = yf.Ticker(ticker).history(period="5d")
        current_price = data['Close'].iloc[-1]
        prev_price = data['Close'].iloc[-2]
        delta_percent = ((current_price - prev_price) / prev_price) * 100
        return current_price, delta_percent, data['Close']

    # Create 3 columns for the metrics
    col1, col2, col3 = st.columns(3)

    # Fetch and display Bitcoin
    with col1:
        price, delta, history = get_live_data("BTC-USD")
        st.metric(label="Bitcoin (BTC)", value=f"${price:,.2f}", delta=f"{delta:.2f}%")
        
    # Fetch and display Ethereum
    with col2:
        price, delta, history = get_live_data("ETH-USD")
        st.metric(label="Ethereum (ETH)", value=f"${price:,.2f}", delta=f"{delta:.2f}%")

    # Fetch and display Solana
    with col3:
        price, delta, history = get_live_data("SOL-USD")
        st.metric(label="Solana (SOL)", value=f"${price:,.2f}", delta=f"{delta:.2f}%")

    st.write("---")
    st.subheader("7-Day Price Trend (BTC)")
    # Show a real chart of Bitcoin's recent history
    st.line_chart(history)

# --- PAGE: CONTACT ---
elif page == "Contact":
    st.title("Get In Touch")
    st.write("Ready to upgrade your IT infrastructure?")
    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Email Address")
        message = st.text_area("How can we help?")
        submitted = st.form_submit_button("Send Message")
        if submitted:
            st.success(f"Thank you {name}! We have received your message.")

# Footer
st.sidebar.markdown("---")
st.sidebar.write("© 2026 Baez IT Solutions")
