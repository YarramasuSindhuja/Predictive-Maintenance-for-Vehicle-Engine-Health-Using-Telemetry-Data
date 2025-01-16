import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Set the number of rows of data
num_rows = 1000

# Generate random telemetry data
vehicle_ids = np.random.choice(['V001', 'V002', 'V003', 'V004', 'V005'], size=num_rows)
speed = np.random.uniform(30, 120, size=num_rows)  # Speed between 30 and 120 km/h
engine_temperature = np.random.uniform(70, 120, size=num_rows)  # Engine temperature in Celsius
fuel_level = np.random.uniform(10, 100, size=num_rows)  # Fuel level percentage
timestamp = pd.date_range(start='2025-01-01', periods=num_rows, freq='H')

# Create a DataFrame
data = pd.DataFrame({
    'VehicleID': vehicle_ids,
    'Speed': speed,
    'EngineTemperature': engine_temperature,
    'FuelLevel': fuel_level,
    'Timestamp': timestamp
})

# Save the data to a CSV file
data.to_csv('vehicle_telemetry_data.csv', index=False)

# Show the first few rows of the data
print(data.head())

# Plot Speed vs Engine Temperature for visualization
plt.figure(figsize=(10, 6))
plt.scatter(data['Speed'], data['EngineTemperature'], alpha=0.5)
plt.title('Speed vs Engine Temperature')
plt.xlabel('Speed (km/h)')
plt.ylabel('Engine Temperature (°C)')
plt.show()
#end
