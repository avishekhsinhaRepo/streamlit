import streamlit as st
import pandas as pd

primary_btn = st.button(type="primary", label="Primary Button")

secondary_btn = st.button(type="secondary", label="Secondary Button")

if primary_btn:
    st.write("Hello from primary")

if secondary_btn:
    st.write("Hello from secondary")

checkbox = st.checkbox("Remember me")

if checkbox:
    st.write("I will remember you")
else:
    st.write("I will forget you")

radio = st.radio("What's your favorite color?", options=["Red", "Green", "Blue"], index=2, horizontal=True)
st.write(f"Your favorite color is {radio}")

df = pd.read_csv("data/sample.csv")

radio_btn_csv_col_drop_down = st.radio("Choose a column", options=df.columns[1:], index=0)


select_box = st.selectbox("Choose a column", options=df.columns[1:], index=0)
st.write(select_box)

multiselect = st.multiselect("Choose as many columns as you want", options=df.columns[1:], default=["col2"],
                             max_selections=2)
st.write(multiselect)

slider = st.slider("Pick a number", min_value=0, max_value=10, value=0, step=1)
st.write(slider)

text_input = st.text_input("What's your name?", placeholder="John Doe")
st.write(f"Your name is {text_input}")

num_input = st.number_input("Pick a number", min_value=0, max_value=10, value=0, step=1)
st.write(f"You picked {num_input}")

txt_area = st.text_area("What do you want to tell me?", height=500, placeholder="Write your message here")
st.write(txt_area)


