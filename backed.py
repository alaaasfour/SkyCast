import requests

API_KEY = "0fe9342a21fba27b9ee1554db99bb25d"


def get_data(place, forecast_days=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    number_of_values = 8 * forecast_days
    filtered_data = filtered_data[:number_of_values]
    return filtered_data


if __name__ == "__main__":
    print(get_data(place="Toronto", forecast_days=3))
