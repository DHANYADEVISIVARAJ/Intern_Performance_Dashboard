import streamlit as st
import pandas as pd

df = pd.read_csv("final_dataset.csv")

st.title("Intern Performance Dashboard")

# KPI Section
st.subheader("Key Metrics")

st.metric("Average Marks", round(df["marks"].mean(), 2))
st.metric("Attendance %", round(df["Attendance_Percentage"].mean(), 2))
st.metric("Task Completion %", round(df["Task_Completion_Rate"].mean(), 2))

# Bar Chart
st.subheader("Marks Comparison")
st.bar_chart(df["marks"])

# Line Chart
st.subheader("Marks Trend")
st.line_chart(df["marks"])

name = st.selectbox("Select Intern", df["name"])
st.write(df[df["name"] == name])