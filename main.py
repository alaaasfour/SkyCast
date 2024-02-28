import streamlit as st
import plotly.express as px
from backed import get_data

# Add title, text input, slider, select box, and subheader elements
st.title("🌤️🌦️☀️")
st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5, help="Select the number of forecasted days")
option = st.selectbox("Select data to view forecast for", ("Temperature", "Sky"))
st.subheader(f"{option} forecast for the next {days} days in {place}")

# Get the temperature/sky data
d, t = get_data(place, days, option)

# Create a temperature plot
figure = px.line(x=d, y=t, labels={"x": "Date", "y": "Temperature (C)"})
st.plotly_chart(figure)