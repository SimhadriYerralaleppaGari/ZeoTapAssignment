import matplotlib.pyplot as plt
from src.database import WeatherDatabase

class WeatherVisualizer:
    def __init__(self):
        self.db = WeatherDatabase()

    def plot_daily_summary(self, city, start_date, end_date):
        data = self.db.get_data_range(city, start_date, end_date)
        dates = [d['date'] for d in data]
        avg_temps = [d['avg_temp'] for d in data]
        max_temps = [d['max_temp'] for d in data]
        min_temps = [d['min_temp'] for d in data]

        plt.figure(figsize=(12, 6))
        plt.plot(dates, avg_temps, label='Average')
        plt.plot(dates, max_temps, label='Max')
        plt.plot(dates, min_temps, label='Min')
        plt.title(f'Daily Temperature Summary for {city}')
        plt.xlabel('Date')
        plt.ylabel('Temperature (°C)')
        plt.legend()
        plt.savefig(f'{city}_temperature_summary.png')
        plt.close()

    def plot_weather_conditions(self, city, start_date, end_date):
        data = self.db.get_data_range(city, start_date, end_date)
        conditions = [d['dominant_condition'] for d in data]
        condition_counts = {c: conditions.count(c) for c in set(conditions)}

        plt.figure(figsize=(10, 6))
        plt.bar(condition_counts.keys(), condition_counts.values())
        plt.title(f'Weather Conditions Distribution for {city}')
        plt.xlabel('Weather Condition')
        plt.ylabel('Frequency')
        plt.savefig(f'{city}_weather_conditions.png')
        plt.close()