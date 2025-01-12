import streamlit as st

with st.form(key="form1"):
    st.write("What u like to order")
    appetizers = st.selectbox("Appetizers", index=0, options=["Fries", "Onion Rings", "Cheese Sticks"])
    main_course = st.selectbox("Main Course", index=0, options=["Pizza", "Burger", "Pasta"])
    deserts = st.selectbox("Deserts", index=0, options=["Ice Cream", "Cake", "Donuts"])
    checkbox = st.checkbox("Are you bringing a friend?")
    day = st.date_input("When you are coming")
    time = st.time_input("At what time you are coming")
    allergies = st.text_area("Any allergies we should know about?", height=100, placeholder="Write here")
    submit_button = st.form_submit_button("Submit")

st.write(f"Your order is {appetizers}")
st.write(f"Your order is {main_course}")
st.write(f"Your order is {deserts}")
st.write(f"Are you bringing a friend? {"Yes" if checkbox else "No"}")
st.write(f"You are coming on  {day}")
st.write(f"You are coming at  {time}")
if allergies:
    st.write(f"Your allergies are {allergies}")
