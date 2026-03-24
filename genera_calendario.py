import os
import requests

RAPIDAPI_KEY = os.environ.get("RAPIDAPI_KEY")

HEADERS = {
    "x-rapidapi-key": RAPIDAPI_KEY,
    "x-rapidapi-host": "free-api-live-football-data.p.rapidapi.com"
}

BASE_URL = "https://free-api-live-football-data.p.rapidapi.com"

print("Cerco leghe italiane...")
r = requests.get(f"{BASE_URL}/football-get-all-leagues", headers=HEADERS)
data = r.json()
leghe = data.get("response", {}).get("leagues", [])
for lega in leghe:
    nome = lega.get("name", "")
    ccode = lega.get("ccode", "")
    if ccode == "ITA" or "ital" in nome.lower():
        print(f"ID: {lega.get('id')} - Nome: {nome} - Paese: {ccode}")
