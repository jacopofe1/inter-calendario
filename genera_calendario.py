import os
import requests

FOOTBALL_API_KEY = os.environ.get("FOOTBALL_API_KEY")

HEADERS = {
    "x-apisports-key": FOOTBALL_API_KEY
}

BASE_URL = "https://v3.football.api-sports.io"

# Test 1: verifica credenziali
print("Test 1: Verifica credenziali...")
r = requests.get(f"{BASE_URL}/status", headers=HEADERS)
print(r.json())

# Test 2: cerca l'ID dell'Inter
print("\nTest 2: Cerca Inter...")
r = requests.get(f"{BASE_URL}/teams", headers=HEADERS, params={"name": "Inter", "country": "Italy"})
print(r.json())
