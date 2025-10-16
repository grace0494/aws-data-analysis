"""
AWS Data Analysis
-----------------
This script analyzes automatic weather station (AWS) data to compute
basic weather statistics like average temperature, humidity, and extremes.

Author: Grace Nulud
Date: October 16, 2025
"""

import numpy as np

# 1. Load dataset
# Example CSV columns: datetime, temperature, humidity, rainfall, wind_speed
# Skip the header row and read numeric data only
data = np.genfromtxt('5147_Davao City AWS-03-10-2025-13_26_30.csv', delimiter=',', skip_header=1, dtype=float, usecols=(1,2,3,4))

# 2. Replace missing or invalid values (-999, -99) with NaN
data[data < -90] = np.nan

# 3. Extract each column for clarity
temperature = data[:, 0]
humidity = data[:, 1]

# 4. Compute summary statistics using NumPy
avg_temp = np.nanmean(temperature)
max_temp = np.nanmax(temperature)
min_temp = np.nanmin(temperature)
avg_hum = np.nanmean(humidity)

# 5. Print summary
print("=== WEATHER SUMMARY REPORT (NumPy) ===")
print(f"Average Temperature (°C): {avg_temp:.2f}")
print(f"Max Temperature (°C): {max_temp:.2f}")
print(f"Min Temperature (°C): {min_temp:.2f}")
print(f"Average Humidity (%): {avg_hum:.2f}")

