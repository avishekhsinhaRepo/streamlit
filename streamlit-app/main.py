import streamlit as st
import pandas as pd
import numpy as np


st.title("Population of Canada")

st.markdown("Source can be found [here](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1710000901)")

with st.expander("See the full table"):
    st.write("This is the full table")

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
        st.selectbox("Quarter", options=['Q1', 'Q2', 'Q3', 'Q4'], index=3, key="location")

    st.form_submit_button("Analyze", type="primary")


tab1, tab2 = st.tabs(['Population Change', 'Compare'])

with tab1:
    st.subheader("Population Change")
    col1, col2 = st.columns(2)

    with col1:
        st.write(f"Population Change from {start_quarter} {start_year} to {end_quarter} {end_year}")
        st.write(f"{start_quarter} {start_year}")
        st.write("Q3 1991")
        st.write(f"{end_quarter} {end_year}")
        st.write("Q3 1991")
    with col2:
        st.write("Population Change col2")


with tab2:
    st.subheader("Compare with other locations")
    st.multiselect("Choose other locations", options=['USA', 'India', 'China'], key="compare_location")