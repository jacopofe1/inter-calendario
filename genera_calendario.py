import os
import requests

RAPIDAPI_KEY = os.environ.get("RAPIDAPI_KEY")
print(f"API Key presente: {bool(RAPIDAPI_KEY)}")

HEADERS = {
    "x-rapidapi-key": RAPIDAPI_KEY,
    "x-rapidapi-host": "free-api-live-football-data.p.rapidapi.com"
}

BASE_URL = "https://free-api-live-football-data.p.rapidapi.com"

# Cerca Inter Milano
print("Cerco Inter Milano...")
r = requests.get(f"{BASE_URL}/football-search-all-teams", headers=HEADERS, params={"term": "Inter"})
print(f"Status: {r.status_code}")
data = r.json()
for team in data.get("response", {}).get("teams", []):
    print(f"ID: {team.get('id')} - Nome: {team.get('name')} - Paese: {team.get('country')}")
