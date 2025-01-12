import streamlit as st
import pandas as pd

# Sidebar
with st.sidebar:
    st.write("Text in the sidebar")

# Three column layout
col1, col2, col3 = st.columns(3)

# First column
with col1:
    st.write("First column")
    st.text_input("Text input")

# Second column
with col2:
    st.write("Second column")
    st.slider("Slider", min_value=0, max_value=10, step=1)

# Third column
with col3:
    st.write("Third column")
    st.button(type="primary", label="Button")

tab1, tab2 = st.tabs(["Tab 1", "Tab 2"])

with tab1:
    st.write("Content of Tab 1")
    st.checkbox("Are u in Tab1 ")

with tab2:
    st.write("Content of Tab 2")
    st.selectbox("Select box in Tab2", options=["Option 1", "Option 2", "Option 3"])

with st.expander("Click to expand"):
    st.write("Content inside the expander")

