import streamlit as st
import yfinance as yf

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="DeFi Labs",
    page_icon="🔹",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- CUSTOM CSS (Executive Standard) ---
st.markdown("""
    <style>
    .stApp { background-color: #F9FAFB; }
    #MainMenu, footer, header { visibility: hidden; }
    div[data-testid="stMetric"] {
        background-color: #FFFFFF;
        padding: 15px;
        border-radius: 8px;
        border: 1px solid #E5E7EB;
        box-shadow: 0 1px 2px rgba(0,0,0,0.05);
    }
    h1 { color: #111827; font-family: 'Arial', sans-serif; }
    h2, h3 { color: #374151; }
    p, li { color: #4B5563; }
    </style>
    """, unsafe_allow_html=True)

# --- HERO SECTION ---
st.title("DEFI LABS")
st.markdown("### *Institutional-Grade Decentralized Finance Strategies*")
st.write("We architect high-yield liquidity pools and automated market making strategies.")
st.markdown("---")

# --- DEFI MARKET WATCH ---
st.subheader("🔵 DeFi Blue Chips")

col1, col2, col3, col4 = st.columns(4)

def get_price(ticker):
    try:
        data = yf.Ticker(ticker).history(period="1d")
        if not data.empty:
            c = data["Close"].iloc[-1]
            o = data["Open"].iloc[-1]
            return c, c - o
        return 0.0, 0.0
    except:
        return 0.0, 0.0

# Fetch Data
uni_p, uni_d = get_price("UNI-USD")
aave_p, aave_d = get_price("AAVE-USD")
mkr_p, mkr_d = get_price("MKR-USD")
crv_p, crv_d = get_price("CRV-USD")

# Metrics
with col1:
    st.metric(label="Uniswap", value=f"${uni_p:.2f}", delta=f"{uni_d:.2f}")
with col2:
    st.metric(label="Aave", value=f"${aave_p:.2f}", delta=f"{aave_d:.2f}")
with col3:
    st.metric(label="Maker", value=f"${mkr_p:,.2f}", delta=f"{mkr_d:.2f}")
with col4:
    st.metric(label="Curve", value=f"${crv_p:.3f}", delta=f"{crv_d:.3f}")

st.markdown("---")

# --- SERVICES SECTION ---
st.header("Protocol Services")

c1, c2, c3 = st.columns(3)

with c1:
    st.subheader("🌾 Yield Farming")
    st.info("**Strategy Optimization**")
    st.write("Automated strategies to maximize APY across lending protocols.")

with c2:
    st.subheader("💧 Liquidity Mining")
    st.info("**Market Making**")
    st.write("Provide deep liquidity to DEXs to ensure capital efficiency.")

with c3:
    st.subheader("🏛️ DAO Governance")
    st.info("**Voting & Proposals**")
    st.write("Technical implementation of on-chain voting systems.")

st.markdown("---")

# --- CONTACT ---
c_left, c_right = st.columns([2,1])

# Defined options separately to prevent line-break errors
options = ["Staking", "Lending", "Flash Loans"]

with c_left:
    st.markdown("### Join the Liquidity Pool")
    with st.form("defi_form"):
        email = st.text_input("Email / ENS Domain")
        # Passing the variable instead of the list
        interest = st.multiselect("Interests", options)
        submitted = st.form_submit_button("Connect Wallet")
        if submitted:
            st.success("Details captured.")
            
with c_right:
    # Short link to prevent breaking
    img_url = "https://cryptologos.cc/logos/ethereum-eth-logo.png?v=026"
    st.image(img_url, width=80)
    st.write("**Built on Ethereum.**")
    st.caption("Audited by DeFi Labs Security.")
