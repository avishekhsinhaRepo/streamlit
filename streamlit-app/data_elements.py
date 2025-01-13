import streamlit as st
import pandas as pd

df = pd.read_csv("data/sample.csv", dtype=int)

st.dataframe(df)

st.table(df)

st.metric("Revenue", "$1,000,000")

st.metric("Total Sales", "$1,000,000", delta=10, delta_color="normal")

st.metric("Total Sales", "$1,000,000", delta=-10, delta_color="normal")


st.metric("Total Expenses", "$6,000", delta=-10, delta_color="inverse")

st.metric("Total Expenses", "$6,000", delta=10, delta_color="inverse")


