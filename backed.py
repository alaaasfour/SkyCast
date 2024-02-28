import requests

# API key for accessing the OpenWeatherMap API
API_KEY = "0fe9342a21fba27b9ee1554db99bb25d"


def get_data(place, forecast_days=None):
    """
        Function to fetch weather forecast data from the OpenWeatherMap API.
        Args:
            place (str): The location for which weather forecast data is requested.
            forecast_days (int, optional): The number of days for which forecast data is requested.
                Defaults to None, which returns the default forecast data provided by the API.
        Returns:
            list: A list of dictionaries containing weather forecast data for the specified location and days.
        """

    # Construct the URL for the API request
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"

    # Send a GET request to the API endpoint and retrieve the response
    response = requests.get(url)

    # Parse the JSON response into a Python dictionary
    data = response.json()

    # Extract the list of forecasted data from the response
    filtered_data = data["list"]

    # Calculate the number of values to filter based on the forecast days
    number_of_values = 8 * forecast_days

    # Filter the forecast data to include only the specified number of days
    filtered_data = filtered_data[:number_of_values]

    # Return the filtered forecast data
    return filtered_data


if __name__ == "__main__":
    print(get_data(place="Toronto", forecast_days=3))
