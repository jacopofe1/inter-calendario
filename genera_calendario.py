import os
import requests

RAPIDAPI_KEY = os.environ.get("RAPIDAPI_KEY")
print(f"API Key presente: {bool(RAPIDAPI_KEY)}")

HEADERS = {
    "x-rapidapi-key": RAPIDAPI_KEY,
    "x-rapidapi-host": "free-api-live-football-data.p.rapidapi.com"
}

BASE_URL = "https://free-api-live-football-data.p.rapidapi.com"

print("Cerco tutte le leghe...")
r = requests.get(f"{BASE_URL}/football-get-all-leagues", headers=HEADERS)
print(f"Status: {r.status_code}")
data = r.json()
leghe = data.get("response", {}).get("leagues", [])
for lega in leghe:
    nome = lega.get("name", "")
    if "serie" in nome.lower() or "italy" in nome.lower() or "italia" in nome.lower() or "coppa" in nome.lower() or "champion" in nome.lower() or "super" in nome.lower():
        print(f"ID: {lega.get('id')} - Nome: {nome}")
