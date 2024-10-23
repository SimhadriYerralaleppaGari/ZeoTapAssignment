import sqlite3
from datetime import datetime
import os

class WeatherDatabase:
    def __init__(self):
        # Define the path to the database
        db_path = 'data/weather_data.db'
        
        # Ensure the data directory exists
        os.makedirs(os.path.dirname(db_path), exist_ok=True)
        
        # If the file exists but is not a valid database, remove it
        if os.path.exists(db_path):
            try:
                # Try to connect to the existing database
                conn = sqlite3.connect(db_path)
                conn.close()
            except sqlite3.DatabaseError:
                # If there's an error, remove the invalid file
                os.remove(db_path)
                print(f"Removed invalid database file: {db_path}")

        # Create a new database connection
        self.conn = sqlite3.connect(db_path)
        self.create_table()

    def create_table(self):
        """Create the weather_data table if it doesn't already exist."""
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS weather_data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                city TEXT,
                main TEXT,
                temp REAL,
                feels_like REAL,
                dt INTEGER
            )
        ''')
        self.conn.commit()

    def insert_weather_data(self, data):
        """Insert weather data into the database."""
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT INTO weather_data (city, main, temp, feels_like, dt)
            VALUES (?, ?, ?, ?, ?)
        ''', (data['city'], data['main'], data['temp'], data['feels_like'], data['dt']))
        self.conn.commit()

    def get_daily_data(self, city, date):
        """Retrieve daily weather data for a specific city and date."""
        cursor = self.conn.cursor()
        start_of_day = int(datetime.combine(date, datetime.min.time()).timestamp())
        end_of_day = int(datetime.combine(date, datetime.max.time()).timestamp())
        
        cursor.execute('''
            SELECT * FROM weather_data
            WHERE city = ? AND dt BETWEEN ? AND ?
        ''', (city, start_of_day, end_of_day))
        return cursor.fetchall()

    def get_recent_data(self, city, limit):
        """Retrieve recent weather data for a specific city."""
        cursor = self.conn.cursor()
        cursor.execute('''
            SELECT * FROM weather_data
            WHERE city = ?
            ORDER BY dt DESC
            LIMIT ?
        ''', (city, limit))
        return cursor.fetchall()

    def get_data_range(self, city, start_date, end_date):
        """Get weather data summary for a specific date range."""
        cursor = self.conn.cursor()
        start_timestamp = int(datetime.strptime(start_date, '%Y-%m-%d').timestamp())
        end_timestamp = int(datetime.strptime(end_date, '%Y-%m-%d').timestamp())
        
        cursor.execute('''
            SELECT 
                date(datetime(dt, 'unixepoch')) as date,
                AVG(temp) as avg_temp,
                MAX(temp) as max_temp,
                MIN(temp) as min_temp,
                GROUP_CONCAT(main) as conditions
            FROM weather_data
            WHERE city = ? AND dt BETWEEN ? AND ?
            GROUP BY date(datetime(dt, 'unixepoch'))
        ''', (city, start_timestamp, end_timestamp))
        
        return [
            {
                'date': row[0],
                'avg_temp': row[1],
                'max_temp': row[2],
                'min_temp': row[3],
                'dominant_condition': max(row[4].split(','), key=row[4].split(',').count)
            }
            for row in cursor.fetchall()
        ]

    def close(self):
        """Close the database connection."""
        self.conn.close()
