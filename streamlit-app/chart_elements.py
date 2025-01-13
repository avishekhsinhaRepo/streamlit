import streamlit as st
import pandas as pd

df = pd.read_csv("data/sample.csv", dtype=int)

# line chart
st.line_chart(df, x="year", y=["col1", "col2", "col3"])

# area chart
st.area_chart(df, x="year", y=["col1", "col2", "col3"])


# Create an area chart
data = {'x': [1, 2, 3, 4, 5],
        'y': [10, 15, 7, 12, 9]}
df1 = pd.DataFrame(data)
st.area_chart(df1)


st.bar_chart(df, x="year", y=["col1", "col2", "col3"])

# Streamlit map
geo_df = pd.read_csv("data/sample_map.csv")

st.map(geo_df)