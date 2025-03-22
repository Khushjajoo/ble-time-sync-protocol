

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

# Function to convert string timestamp to datetime object including milliseconds
def parse_timestamp(timestamp_str):
    return datetime.strptime(timestamp_str, '%H:%M:%S.%f')

# Read the CSV file
df = pd.read_csv('data.csv')

# Convert timestamp strings to datetime objects
df['ServerTimestamp'] = df['server_timestamp'].apply(parse_timestamp)
df['ClientTimestamp'] = df['client_timestamp'].apply(parse_timestamp)

# Calculate drift (in seconds)
df['DriftInSeconds'] = (df['ServerTimestamp'] - df['ClientTimestamp']).dt.total_seconds()

# Adjust client timestamp by drift
df['AdjustedClientTimestamp'] = df['ClientTimestamp'] + pd.to_timedelta(df['DriftInSeconds'], unit='s')

# Save the adjusted data to a new Excel sheet
with pd.ExcelWriter('adjusted_data.xlsx') as writer:
    df.to_excel(writer, sheet_name='Adjusted Timestamps', index=False)

# Plotting the data
plt.figure(figsize=(10, 6))

# Plotting sensor values against adjusted client timestamp
plt.plot(df['AdjustedClientTimestamp'], df['sensor_values'], label='Sensor Data')

plt.title('Sensor Data Over Time')
plt.xlabel('Adjusted Timestamp')
plt.ylabel('Sensor Values')
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
plt.gca().xaxis.set_major_locator(mdates.HourLocator())
plt.gcf().autofmt_xdate()  # Rotate date labels
plt.legend()
plt.show()

print("complete")

