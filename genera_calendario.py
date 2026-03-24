import os
import datetime
import requests

oggi = datetime.date.today()

RAPIDAPI_KEY = os.environ.get("RAPIDAPI_KEY")
print(f"API Key presente: {bool(RAPIDAPI_KEY)}")

HEADERS = {
    "x-rapidapi-key": RAPIDAPI_KEY,
    "x-rapidapi-host": "free-api-live-football-data.p.rapidapi.com"
}

BASE_URL = "https://free-api-live-football-data.p.rapidapi.com"

# Test connessione
print("Test connessione...")
r = requests.get(f"{BASE_URL}/football-get-all-leagues", headers=HEADERS)
print(f"Status: {r.status_code}")
print(r.json())
