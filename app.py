
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("company_financials_clean.csv")

# Title
st.title("Financial Dashboard: Company")

# KPI Cards
c1, c2, c3 = st.columns(3)

c1.metric("Latest Sales", f"{df['Sales'].iloc[-1]:,.0f}")
c2.metric("Latest Net Profit", f"{df['Net_Profit'].iloc[-1]:,.0f}")
c3.metric("Latest OPM %", f"{df['OPM_Percent'].iloc[-1]:.2f}%")

# Chart 1: Sales Trend
st.subheader("Sales Trend")
fig, ax = plt.subplots()
ax.plot(df["Sales"], marker="o")
ax.set_xlabel("Period")
ax.set_ylabel("Sales")
st.pyplot(fig)

# Chart 2: Net Profit Trend
st.subheader("Net Profit Trend")
fig, ax = plt.subplots()
ax.plot(df["Net_Profit"], marker="o")
ax.set_xlabel("Period")
ax.set_ylabel("Net Profit")
st.pyplot(fig)
