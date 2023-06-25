import requests
import datetime

def getWeather():

# Get the current date
    current_date = datetime.date.today().isoformat()

    # Replace the start_date and end_date in the URL
    url = "https://api.open-meteo.com/v1/forecast?latitude=34.05&longitude=-118.24&hourly=temperature_2m,relativehumidity_2m,rain&current_weather=true&temperature_unit=fahrenheit&windspeed_unit=mph&precipitation_unit=inch&forecast_days=1&start_date={}&end_date={}&timezone=America%2FLos_Angeles".format(current_date, current_date)
    response = requests.get(url)
    data = response.json()

    # Extracting the values
    temperature_2m_selected = data['hourly']['temperature_2m'][8:21]
    relative_humidity_2m_selected = data['hourly']['relativehumidity_2m'][8:21]
    rain_selected = data['hourly']['rain'][8:21]

    # Calculating the average
    temperature_avg = sum(temperature_2m_selected) / len(temperature_2m_selected)
    humidity_avg = sum(relative_humidity_2m_selected) / len(relative_humidity_2m_selected)
    rain_avg = sum(rain_selected) / len(rain_selected)

    weather_forecast_8_20 = f'Average Temperature: 120 Farenheit, Average Relative Humidity (2m): {humidity_avg} Percent, Average Rain: {rain_avg} Inch'
    return weather_forecast_8_20