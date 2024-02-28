import streamlit as st
import plotly.express as px
from backed import get_data

# Add title, text input, slider, select box, and subheader elements
st.title("☀️ SkyCast Weather Forecast 🌤️🌦️☔️")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5, help="Select the number of forecasted days")
option = st.selectbox("Select data to view forecast for", ("Temperature", "Sky"))
st.subheader(f"{option} forecast for the next {days} days in {place}")


if place:
    # Get the temperature/sky data
    filtered_data = get_data(place, days)

    if option == "Temperature":
        temperatures_k = [dict["main"]["temp"] for dict in filtered_data]
        # Convert the degree from Kelvin to Celsius
        temperatures_c = [temp - 273.15 for temp in temperatures_k]
        dates = [dict["dt_txt"] for dict in filtered_data]
        # Create a temperature plot
        figure = px.line(x=dates, y=temperatures_c, labels={"x": "Date", "y": "Temperature (C)"})
        st.plotly_chart(figure)

    if option == "Sky":
        images = {"Clear": "images/clear.png", "Snow": "images/snow.png", "Clouds": "images/cloud.png", "Rain": "images/rain.png"}
        sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
        image_paths = [images[condition] for condition in sky_conditions]
        st.image(image_paths, width=115)
