import streamlit as st

# Set the page title and description
st.set_page_config(page_title="Weather Classification", page_icon="⛅️")
st.title("Weather Classification")
st.markdown("---")

# Define weather conditions and their descriptions
weather_conditions = {
    "Sunny": "Clear skies, bright sun, and no clouds.",
    "Cloudy": "Partly or mostly cloudy sky with no precipitation.",
    "Rainy": "Rainfall, with varying intensities from drizzle to heavy rain.",
    "Snowy": "Snowfall, with varying intensities from light snow to heavy snowfall.",
}

# Sidebar widget for user input
selected_condition = st.selectbox("Select Weather Condition", list(weather_conditions.keys()))

# Display the selected weather condition and its description
st.write(f"Selected Weather Condition: {selected_condition}")
st.write("Description:", weather_conditions[selected_condition])
