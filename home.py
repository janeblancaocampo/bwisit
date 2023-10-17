import streamlit as st
from datetime import datetime

# Set the page title and description
st.set_page_config(page_title="Weather Simulation", page_icon="⛅️")
st.title("Weather Simulation")
st.markdown("---")


# CSS to set the teal gradient background
teal_gradient_style = """
<style>
body {
    background: linear-gradient(135deg, #2E8B57, #20B2AA);
}
</style>
"""
st.markdown(teal_gradient_style, unsafe_allow_html=True)

# Display current date and time
current_time = datetime.now()
st.subheader("Current Date and Time")
st.write(current_time.strftime('%Y-%m-%d %H:%M:%S'))
