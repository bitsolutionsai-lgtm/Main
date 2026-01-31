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
        st.subheader("The Vending Machine Analogy
