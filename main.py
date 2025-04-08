from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd

app = FastAPI()

# ✅ Allow CORS for all origins (you can restrict later)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For dev, allow everything
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load cleaned CSV
df = pd.read_csv("cleaned_weather_data.csv")
df['datetime_utc'] = pd.to_datetime(df['datetime_utc'])

@app.get("/weather/{date}")
def get_weather_by_date(date: str):
    try:
        date_parsed = pd.to_datetime(date).date()
        row = df[df['datetime_utc'].dt.date == date_parsed]
        if row.empty:
            return {"message": "No data found for this date"}
        return row.to_dict(orient="records")[0]
    except Exception as e:
        return {"error": str(e)}
