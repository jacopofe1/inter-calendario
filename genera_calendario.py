import os
import requests

RAPIDAPI_KEY = os.environ.get("RAPIDAPI_KEY")

HEADERS = {
    "x-rapidapi-key": RAPIDAPI_KEY,
    "x-rapidapi-host": "free-api-live-football-data.p.rapidapi.com"
}

BASE_URL = "https://free-api-live-football-data.p.rapidapi.com"

# Serie A ha ID 87 su questa API - proviamo a cercare le squadre
print("Cerco squadre Serie A...")
r = requests.get(f"{BASE_URL}/football-get-all-teams-by-leagueid-and-season", headers=HEADERS, params={"leagueid": "87", "season": "2025"})
print(f"Status: {r.status_code}")
data = r.json()
print(data)
