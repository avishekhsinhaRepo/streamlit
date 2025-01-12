import streamlit as st

# Page Title
st.title("Page Title")

# Page Header
st.header("Page Header")

# divider
st.divider()

# Page Sub header

st.subheader("Page Sub header")

# Page Text
st.text("Hello Streamlit")

# Page Markdown
st.markdown("# Markdown Header 1")

st.markdown("## Markdown  Header 2")

st.markdown("### Markdown  Header 1")

# Page Error
st.error("Error Message")

# Page Warning
st.warning("Warning Message")

# Page Success

st.success("Success Message")

# Page Info
st.info("Info Message")


# latex

st.latex("f(x) = x^2")

# Display text
st.write("Hello, world!")

# Display a list
st.write(["apple", "banana", "cherry"])

# Display a dictionary
st.write({"name": "John", "age": 30})

