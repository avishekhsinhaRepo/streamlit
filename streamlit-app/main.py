import streamlit as st
import pandas as pd
import numpy as np

df = pd.read_csv("data/quarterly_canada_population.csv",dtype=str)

st.title("Population of Canada")

st.markdown("Source can be found [here](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1710000901)")

with st.expander("See the full table"):
    st.dataframe(df)

with st.form("population_form"):
    col1, col2, col3 = st.columns(3)

    with col1:
        st.write("Choose the Start Date")
        start_quarter = st.selectbox("Quarter", options=['Q1', 'Q2', 'Q3', 'Q4'], index=3, key="start_quarter")
        start_year = st.slider("Year", min_value=1991, max_value=2023, value=1991, step=1, key="start_year")

    with col2:
        st.write("Choose the End Date")
        end_quarter = st.selectbox("Quarter", options=['Q1', 'Q2', 'Q3', 'Q4'], index=3, key="end_quarter")
        end_year = st.slider("Year", min_value=1991, max_value=2023, value=1991, step=1, key="end_year")

    with col3:
        st.write("Choose the Location")
        st.selectbox("Choose the Location", options=['Q1', 'Q2', 'Q3', 'Q4'], index=3, key="location")

    st.form_submit_button("Analyze", type="primary")

tab1, tab2 = st.tabs(['Population Change', 'Compare'])

with tab1:
    st.subheader(f"Population Change from {start_quarter} {start_year} to {end_quarter} {end_year}")
    col1, col2 = st.columns(2)

    with col1:
        st.metric(f"{start_quarter} {start_year}", "10,000")
        st.metric(f"{end_quarter} {end_year}", "10,000", delta=10, delta_color="normal")
    with col2:
        st.write("Population Change col2")

with tab2:
    st.subheader("Compare with other locations")
    st.multiselect("Choose other locations", options=['USA', 'India', 'China'], key="compare_location")
