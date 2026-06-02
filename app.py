import streamlit as st
import pandas as pd

st.set_page_config(page_title="AI Trading Platform", layout="wide")

st.title("🤖 FULL AI TRADING PLATFORM")

# SESSION STORAGE
if "journal" not in st.session_state:
    st.session_state["journal"] = []

# INPUTS
st.header("📊 Market Analysis Input")

trend = st.selectbox("Market Trend", ["Uptrend", "Downtrend", "Range"])
structure = st.selectbox("Market Structure", ["Strong", "Weak"])
liquidity = st.selectbox("Liquidity Sweep", ["Yes", "No"])
candle = st.selectbox("Candle Strength", ["Strong", "Weak"])
session = st.selectbox("Session", ["London", "New York", "Asian", "Off"])

rr = st.slider("Risk Reward Ratio", 0.5, 5.0, 2.0)

# SCORE ENGINE
score = 0

if trend != "Range":
    score += 25

if structure == "Strong":
    score += 25

if liquidity == "Yes":
    score += 30

if candle == "Strong":
    score += 20
else:
    score += 10

if rr >= 2:
    score += 15
elif rr >= 1.5:
    score += 8

if session in ["London", "New York"]:
    score += 10
else:
    score -= 10

if score > 100:
    score = 100

# OUTPUT
st.header("🤖 AI Market Bias")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("BUY Probability", f"{score}%")

with col2:
    st.metric("SELL Probability", f"{100 - score}%")

with col3:
    st.metric("NO TRADE Risk", f"{max(0, 100 - score - 20)}%")

# DECISION
st.subheader("📌 AI Decision")

if score >= 80:
    st.success("🟢 HIGH PROBABILITY BUY SETUP")
elif score >= 60:
    st.warning("🟡 WAIT FOR CONFIRMATION")
else:
    st.error("🔴 NO TRADE ZONE")

# JOURNAL SYSTEM
st.header("📒 Trade Journal")

note = st.text_input("Trade Note (optional)")

if st.button("Save Trade"):
    st.session_state["journal"].append({
        "trend": trend,
        "structure": structure,
        "liquidity": liquidity,
        "candle": candle,
        "session": session,
        "rr": rr,
        "score": score,
        "note": note
    })
    st.success("Trade Saved!")

if st.session_state["journal"]:
    df = pd.DataFrame(st.session_state["journal"])
    st.dataframe(df)
