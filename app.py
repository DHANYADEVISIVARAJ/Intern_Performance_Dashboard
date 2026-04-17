import streamlit as st
import pandas as pd

df = pd.read_csv("final_dataset.csv")

st.title("Intern Dashboard")

# KPI
st.metric("Avg Marks", round(df["marks"].mean(),2))
st.metric("Attendance %", round(df["Attendance_Percentage"].mean(),2))
st.metric("Task %", round(df["Task_Completion_Rate"].mean(),2))

# Charts
st.bar_chart(df["marks"])
st.line_chart(df["marks"])

name = st.selectbox("Select Intern", df["name"])
st.write(df[df["name"] == name])