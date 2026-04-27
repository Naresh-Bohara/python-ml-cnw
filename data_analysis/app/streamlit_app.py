import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("data/processed/clean_sales_data.csv")
st.title("Sales Data Analysis")

# Filtering
dept = st.selectbox("Select Department", df["Dept"].unique())
filtered = df[df["Dept"] == dept]

# KPI
st.metric("Total Sales", f"${filtered['Sales'].sum():,.2f}")

# Bar Chart
st.subheader("Employee Performance")
fig, ax = plt.subplots()
sns.barplot(x="Name", y="Sales", data=filtered, ax=ax)
st.pyplot(fig)

# Trend
st.subheader("Monthly Sales Trends")
fig2, ax2 = plt.subplots()
sns.lineplot(x="Month", y="Sales", data=filtered,markers="o", ax=ax2)
st.pyplot(fig2)

# Data
st.subheader("Data")
st.dataframe(filtered)