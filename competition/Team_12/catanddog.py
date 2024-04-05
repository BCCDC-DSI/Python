import streamlit as st

# Set the layout to wide
st.set_page_config(layout="wide")

# Create two columns
col1, col2 = st.columns(2)

# Display "cat" in the left column and "dog" in the right column
with col1:
    st.write("cat")

with col2:
    st.write("dog")

