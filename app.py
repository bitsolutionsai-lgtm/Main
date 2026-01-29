import streamlit as st
import pandas as pd
import yfinance as yf

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="DeFi Labs",
    page_icon="🔹",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- CUSTOM CSS (The Charcoal Terminal Look) ---
st.markdown("""
    <style>
    /* Main Background - Dark Charcoal */
    .stApp {
        background-color: #212529;
    }
    
    /* Hide default menu */
    #MainMenu, footer, header {visibility: hidden;}
    
    /* TEXT COLORS - Make everything light grey/white */
    h1, h2, h3, h4, h5, p, span, div {
        color: #E9ECEF !important;
    }
    
    /* CARDS / METRICS - Slightly lighter charcoal to pop */
    div[data-testid="stMetric"] {
        background-color: #2C3035;
        padding: 15px;
        border-radius: 8px;
        border: 1px solid #343A40;
    }
    /* Metric Value Color (The numbers) */
    div[data-testid="stMetricValue"] {
        color: #FFFFFF !important;
    }
    
    /* TABS - Customizing the tab bar */
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
        background-color: transparent;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: #2C3035;
        border-radius: 5px;
        color: #ADB5BD;
        border: 1px solid #343A40;
    }
    .stTabs [aria-selected="true"] {
        background-color: #0d6efd; /* Electric Blue Highlight */
        color: #FFFFFF !important;
        border-color: #0d6efd;
    }
    
    /* DATAFRAME / TABLE styling */
    div[data-testid="stDataFrame"] {
        background-color: #2C3035;
        padding: 10px;
        border-radius: 8px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER ---
col_head, col_btn = st.columns([3, 1])
with col_head:
    st.title("DEFI LABS")
    st.caption("Institutional Liquidity Protocol")

with col_btn:
    st.write("")
    st.write("")
    st.button("⚡ Connect Wallet")

st.markdown("---")

# --- TABS NAVIGATION ---
tab1, tab2, tab3 = st.tabs(["📊 Markets", "💎 Staking Vault", "🔄 Swap"])

# --- TAB 1: MARKET DATA ---
with tab1:
    st.subheader("Live Market Data")
    
    # Helper for prices
    def get_price(t):
        try:
            d = yf.Ticker(t).history(period="1d")
            if not d.empty:
                c = d["Close"].iloc[-1]
                o = d["Open"].iloc[-1]
                return c, c-o
            return 0.0, 0.0
        except:
            return 0.0, 0.0

    # Fetch Data
    b_p, b_d = get_price("BTC-USD")
    e_p, e_d = get_price("ETH-USD")
    s_p, s_d = get_price("SOL-USD")
    l_p, l_d = get_price("LINK-USD")

    # Metrics
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Bitcoin", f"${b_p:,.0f}", f"{b_d:.2f}")
    c2.metric("Ethereum", f"${e_p:,.0f}", f"{e_d:.2f}")
    c3.metric("Solana", f"${s_p:.2f}", f"{s_d:.2f}")
    c4.metric("Chainlink", f"${l_p:.2f}", f"{l_d:.2f}")

    st.write("### Top Liquidity Pools")
    # Clean table data
    df = pd.DataFrame({
        'Pool Name': ['USDC-ETH', 'WBTC-DAI', 'SOL-USDC', 'LINK-ETH'],
        'TVL (Millions)': ['$450M', '$210M', '$180M', '$95M'],
        '24h Volume': ['$32M', '$15M', '$45M', '$8M'],
        'APY': ['12.5%', '8.2%', '18.4%', '15.1%']
    })
    st.dataframe(df, use_container_width=True, hide_index=True)

# --- TAB 2: STAKING VAULT ---
with tab2:
    st.subheader("Yield Generation")
    
    col_stake_left, col_stake_right = st.columns([1, 2])
    
    # Safe list for selectbox
    pool_options = ["USDC Vault (8.5%)", "ETH Staking (4.2%)", "SOL Validator (7.1%)"]
    
    with col_stake_left:
        with st.container():
            st.info("Select a Vault Strategy")
            pool = st.selectbox("Strategy", pool_options)
            amt = st.number_input("Amount", value=1000)
            st.button("Deposit Funds")
            
    with col_stake_right:
        # Simple Math for display
        daily = (amt * 0.085) / 365
        monthly = daily * 30
        st.success(f"**Estimated Monthly Yield:** ${monthly:.2f}")
        st.write("Funds are secured by Multi-Sig Treasury.")
        st.progress(75, text="Vault Fill Rate")

# --- TAB 3: SWAP INTERFACE ---
with tab3:
    st.subheader("Token Swap")
    
    c_swap_1, c_swap_2 = st.columns(2)
    
    assets = ["ETH", "USDC", "DAI", "WBTC"]
    
    with c_swap_1:
        st.selectbox("From", assets, key="s1")
        st.text_input("Amount In", "1.0")
        
    with c_swap_2:
        st.selectbox("To", assets, index=1, key="s2")
        st.text_input("Amount Out (Est.)", "2850.45")
        
    st.button("Execute Swap")
