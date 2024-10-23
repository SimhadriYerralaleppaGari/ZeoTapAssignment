import time
import configparser
from src.api_client import WeatherAPI
from src.data_processor import WeatherDataProcessor
from src.alerting import AlertSystem
from src.visualization import WeatherVisualizer
from src.database import WeatherDatabase

def main():
    # Load configuration
    config = configparser.ConfigParser()
    config.read('config/config.ini')

    #api_client = WeatherAPI(api_key=config['API']['api_key'], base_url=config['API']['base_url'])
    api_client = WeatherAPI()

    data_processor = WeatherDataProcessor(config)
    alert_system = AlertSystem('your_email@gmail.com', 'your_password')
    visualizer = WeatherVisualizer()

    # Initialize the MySQL database connection without password
    db = WeatherDatabase(config)

    cities = config['LOCATIONS']['cities'].split(',')
    update_interval = int(config['SETTINGS']['update_interval'])
    max_temp_threshold = float(config['ALERTS']['max_temperature'])
    consecutive_updates = int(config['ALERTS']['consecutive_updates'])

    print("Weather Monitoring System Started")
    print(f"Monitoring cities: {', '.join(cities)}")
    print(f"Update interval: {update_interval} seconds")

    while True:
        for city in cities:
            try:
                # Fetch weather data
                weather_data = api_client.get_weather(city)
                if weather_data:
                    data_processor.process_weather_data(city, weather_data)
                    db.insert_weather_data({
                        'city': city,
                        'main': weather_data['weather'][0]['main'],
                        'temp': weather_data['main']['temp'],
                        'feels_like': weather_data['main']['feels_like'],
                        'dt': weather_data['dt']
                    })

                    print(f"Updated weather data for {city}: {weather_data['main']['temp']}°C, {weather_data['weather'][0]['main']}")

                    # Check if an alert needs to be triggered
                    if data_processor.check_alert_threshold(city, max_temp_threshold, consecutive_updates):
                        alert_system.temperature_alert(city, weather_data['main']['temp'])
                        print(f"Alert triggered for {city}! Temperature: {weather_data['main']['temp']}°C")
                else:
                    print(f"Failed to fetch weather data for {city}")
            except Exception as e:
                print(f"Error processing weather data for {city}: {str(e)}")

        # Generate visualizations (daily or weekly, etc.)
        try:
            visualizer.plot_daily_summary(cities[0], '2024-03-01', '2024-03-07')
            visualizer.plot_weather_conditions(cities[0], '2024-03-01', '2024-03-07')
            print("Generated daily visualizations")
        except Exception as e:
            print(f"Error generating visualizations: {str(e)}")

        # Wait for the specified interval before fetching data again
        print(f"Waiting for {update_interval} seconds before the next update...")
        time.sleep(update_interval)

if __name__ == "__main__":
    main()
