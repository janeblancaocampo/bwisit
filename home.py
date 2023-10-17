import streamlit as st
from datetime import datetime

# Set the page title and description
st.set_page_config(page_title="Weather Simulation", page_icon="⛅️")
st.title("Weather Simulation")
st.markdown("---")

# Simulated weather data
weather_data = {
    "Temperature": "22°C",
    "Humidity": "55%",
    "Conditions": "Partly Cloudy",
    "Wind Speed": "5 km/h",
}

# Simulated weather icons
st.image("path_to_weather_icon.png", caption="Weather Icon", use_column_width=True)

# CSS to set the background image
background_image_style = """
<style>
body {
    background-image: url('path_to_background_image.jpg');
    background-size: cover;
}
</style>
"""
st.markdown(background_image_style, unsafe_allow_html=True)

# Display current date and time
current_time = datetime.now()
st.subheader("Current Date and Time")
st.write(current_time.strftime('%Y-%m-%d %H:%M:%S'))
