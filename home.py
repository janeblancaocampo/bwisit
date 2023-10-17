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

# Display current date and time
current_time = datetime.now()
st.subheader("Current Date and Time")
st.write(current_time.strftime('%Y-%m-%d %H:%M:%S'))

# Weather UI
st.subheader("Current Weather Conditions")
st.write("Location: [Your Location]")

# Display simulated weather data
for key, value in weather_data.items():
    st.write(f"{key}: {value}")

# Simulated weather icons
st.image("path_to_weather_icon.png", caption="Weather Icon", use_column_width=True)

# Additional weather information
st.subheader("Additional Weather Information")
st.write("Today's Forecast: [Your forecast here]")

# Weather radar or map (replace with an actual map component)
st.subheader("Weather Radar")
st.image("path_to_weather_radar.png", caption="Weather Radar", use_column_width=True)
