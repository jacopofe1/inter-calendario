import os
import requests

RAPIDAPI_KEY = os.environ.get("RAPIDAPI_KEY")

HEADERS = {
    "x-rapidapi-key": RAPIDAPI_KEY,
    "x-rapidapi-host": "free-api-live-football-data.p.rapidapi.com"
}

BASE_URL = "https://free-api-live-football-data.p.rapidapi.com"

print("Cerco partite Inter con leagueid Serie A (135)...")
r = requests.get(f"{BASE_URL}/football-get-all-matches-by-league", headers=HEADERS, params={"leagueid": "135"})
print(f"Status: {r.status_code}")
data = r.json()
partite = data.get("response", {}).get("events", [])
print(f"Totale partite trovate: {len(partite)}")
for p in partite[:5]:
    home = p.get("homeTeam", {}).get("name", "")
    away = p.get("awayTeam", {}).get("name", "")
    print(f"{home} vs {away}")
