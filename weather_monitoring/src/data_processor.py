from collections import Counter
from src.database import WeatherDatabase

class WeatherDataProcessor:
    def __init__(self, db=None):
        """
        Initialize the WeatherDataProcessor.

        :param db: Optional database instance. If None, a new WeatherDatabase instance will be created.
        """
        self.db = db if db else WeatherDatabase()

    def process_weather_data(self, city, weather_data):
        """
        Process and store the weather data for a specific city.

        :param city: The name of the city for which the weather data is collected.
        :param weather_data: The raw weather data from the API response.
        """
        processed_data = {
            'city': city,
            'main': weather_data.get('weather', [{}])[0].get('main', 'Unknown'),
            'temp': weather_data.get('main', {}).get('temp', 0.0),
            'feels_like': weather_data.get('main', {}).get('feels_like', 0.0),
            'dt': weather_data.get('dt', 0)
        }
        self.db.insert_weather_data(processed_data)

    def calculate_daily_summary(self, city, date):
        """
        Calculate daily weather summary for a specific city and date.

        :param city: The name of the city.
        :param date: The date for which the summary is calculated.
        :return: A dictionary containing the average, maximum, and minimum temperature, and the dominant condition.
        """
        data = self.db.get_daily_data(city, date)
        if not data:
            return None

        temps = [d[2] for d in data]  # Assuming temp is the third column in the result
        weather_conditions = [d[1] for d in data]  # Assuming main is the second column

        return {
            'city': city,
            'date': date,
            'avg_temp': sum(temps) / len(temps),
            'max_temp': max(temps),
            'min_temp': min(temps),
            'dominant_condition': Counter(weather_conditions).most_common(1)[0][0]
        }

    def check_alert_threshold(self, city, threshold, consecutive_updates):
        """
        Check if the recent temperatures exceed the defined alert threshold.

        :param city: The name of the city to check.
        :param threshold: The temperature threshold for alerts.
        :param consecutive_updates: The number of consecutive updates that must exceed the threshold.
        :return: True if all recent updates exceed the threshold, otherwise False.
        """
        recent_data = self.db.get_recent_data(city, consecutive_updates)
        if len(recent_data) < consecutive_updates:
            return False

        return all(data[3] > threshold for data in recent_data)  # Assuming temp is the fourth column
