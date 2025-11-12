
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Set random seed for reproducibility
np.random.seed(42)

# Generate weather data for one year (365 days)
start_date = datetime(2024, 1, 1)
dates = [start_date + timedelta(days=i) for i in range(365)]

# Generate realistic weather data
def generate_weather_data(dates):
    data = []
    for i, date in enumerate(dates):
        # Create seasonal variations
        day_of_year = date.timetuple().tm_yday
        
        # Temperature varies with season (higher in summer, lower in winter)
        base_temp = 20 + 15 * np.sin(2 * np.pi * (day_of_year - 80) / 365)
        temperature = base_temp + np.random.normal(0, 3)
        
        # Humidity (percentage)
        humidity = np.random.uniform(40, 90)
        
        # Wind speed (km/h)
        wind_speed = np.random.uniform(5, 40)
        
        # Pressure (hPa)
        pressure = np.random.uniform(990, 1030)
        
        # Visibility (km)
        visibility = np.random.uniform(5, 15)
        
        # Rainfall (mm) - more in certain seasons
        rain_prob = 0.3 if 150 < day_of_year < 250 else 0.15
        rainfall = np.random.exponential(5) if np.random.random() < rain_prob else 0
        
        # Weather condition based on rainfall and temperature
        if rainfall > 10:
            condition = "Heavy Rain"
        elif rainfall > 0:
            condition = "Light Rain"
        elif temperature > 30:
            condition = "Hot"
        elif temperature < 10:
            condition = "Cold"
        elif humidity > 75:
            condition = "Cloudy"
        else:
            condition = "Clear"
        
        data.append({
            'Date': date.strftime('%Y-%m-%d'),
            'Temperature_C': round(temperature, 2),
            'Humidity_%': round(humidity, 2),
            'Wind_Speed_kmh': round(wind_speed, 2),
            'Pressure_hPa': round(pressure, 2),
            'Visibility_km': round(visibility, 2),
            'Rainfall_mm': round(rainfall, 2),
            'Weather_Condition': condition
        })
    
    return pd.DataFrame(data)

# Generate the dataset
weather_df = generate_weather_data(dates)

# Save to CSV
weather_df.to_csv('weather_data.csv', index=False)

print("Weather data CSV file created successfully!")
print(f"\nDataset shape: {weather_df.shape}")
print(f"\nFirst few rows:")
print(weather_df.head(10))
print(f"\nLast few rows:")
print(weather_df.tail(5))
print(f"\nBasic statistics:")
print(weather_df.describe())
