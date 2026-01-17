import pandas as pd

# Load raw data
df = pd.read_csv('../data/raw/sample_sql_server_table.csv')

# Transform
df['TripDurationMinutes'] = pd.to_datetime(df['EndTime']) - pd.to_datetime(df['StartTime'])
df['TripDurationMinutes'] = df['TripDurationMinutes'].dt.total_seconds() / 60
df['RevenuePerHour'] = df['FareCollected'] / (df['TripDurationMinutes'] / 60)

# Save clean data
df.to_csv('../data/clean/sample_clean_table.csv', index=False)

print("Data cleaning complete!")
