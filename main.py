import streamlit as st

st.title("🌤️🌦️☀️")
st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5, help="Select the number of forecasted days")
option = st.selectbox("Select data to view forecast for", ("Temperature", "Sky"))
st.subheader(f"{option} forecast for the next {days} days in {place}")

