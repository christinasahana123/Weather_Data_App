import pandas as pd

# Load the CSV
df = pd.read_csv("testset.csv")

# Clean column names
df.columns = df.columns.str.strip().str.lstrip('_')

# Convert datetime
df['datetime_utc'] = pd.to_datetime(df['datetime_utc'])

# Drop rows where datetime or temperature is missing
df = df.dropna(subset=["datetime_utc", "tempm"])

# Optional: Fill other NaNs with 0
df.fillna(0, inplace=True)

# Save cleaned data
df.to_csv("cleaned_weather_data.csv", index=False)

print("🎉 Cleaned data saved as 'cleaned_weather_data.csv'")
