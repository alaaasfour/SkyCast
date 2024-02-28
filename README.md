# Weather Forecast App 🌤️🌦️☔️

This is a simple weather forecast application built with Streamlit and Plotly Express. 
It allows users to input a location and select the number of days to forecast the weather. 
Users can choose to view either temperature or sky conditions for the selected location and 
forecast days.

## Features ✨

### 1. Dynamic Interface
Users can input a location and select the number of forecast days using text input, slider, and select box elements.

### 2. Temperature Forecast
Users can view the temperature forecast for the selected location and days in either Celsius.

### 3. Sky Condition Forecast
Users can view the sky conditions forecast for the selected location and days, represented by images (clear, snow, clouds, rain).

## Getting Started 🚀
### 1. Clone the repository:
`git clone https://github.com/alaaasfour/SkyCast.git`

### 2. Usage:
Run the `main.py` script tto launch the Streamlit application:
`streamlit run main.py`

You can then access the application through your web browser at http://localhost:8501.

### 3. File Structure
`main.py`: Contains the main Streamlit application code for the user interface and visualization.
`backend.py`: Contains the backend code for fetching weather data from the OpenWeatherMap API.

## Dependencies 🔧
* Streamlit: for the Streamlit web version
* Plotly: Python library for creating interactive plots and visualizations.
* Requests: Python library for making HTTP requests to APIs.

## Configuration ⚙️
To use the application, you need to obtain an API key from OpenWeatherMap. 
Replace the value of `API_KEY` in `backend.py` with your own API key:
`API_KEY = "your_api_key_here"`

## Screenshots 🖼️

### 1. Temperature View
![Temperature.png](images%2FTemperature.png)

### 2. Sky View
![Sky.png](images%2FSky.png)