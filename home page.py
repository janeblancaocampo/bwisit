import streamlit as st
from datetime import datetime

# Set the page title and description
st.set_page_config(page_title="Weather Classification", page_icon="⛅️")
st.title("Weather Classification")
st.markdown("---")

# Display the current date and time
current_time = datetime.now()
st.write(f"Current Date and Time: {current_time.strftime('%Y-%m-%d %H:%M:%S')}")
