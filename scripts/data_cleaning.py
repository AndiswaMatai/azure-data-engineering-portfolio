import pandas as pd

# Load raw data
df = pd.read_csv('../data/raw/sample_sql_server_table.csv')

# Calculate trip duration in minutes
df['StartTime'] = pd.to_datetime(df['TripDate'] + ' ' + df['StartTime'])
df['EndTime'] = pd.to_datetime(df['TripDate'] + ' ' + df['EndTime'])
df['TripDurationMinutes'] = (df['EndTime'] - df['StartTime']).dt.total_seconds() / 60

# Calculate revenue per hour
df['RevenuePerHour'] = df['FareCollected'] / (df['TripDurationMinutes'] / 60)

# Reorder columns for clean dataset
df_clean = df[['DriverID', 'RouteID', 'TripDate', 'TripDurationMinutes', 'FareCollected', 'RevenuePerHour']]

# Save clean CSV
df_clean.to_csv('../data/clean/sample_clean_table.csv', index=False)

print("Data cleaning complete!")
