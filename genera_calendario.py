import os
import requests

FOOTBALL_API_KEY = os.environ.get("FOOTBALL_API_KEY")
print(f"API Key presente: {bool(FOOTBALL_API_KEY)}")
print(f"API Key inizio: {FOOTBALL_API_KEY[:8] if FOOTBALL_API_KEY else 'VUOTA'}")

BASE_URL = "https://v3.football.api-sports.io"

print("\nTest con x-apisports-key...")
r = requests.get(f"{BASE_URL}/status", headers={"x-apisports-key": FOOTBALL_API_KEY})
print(r.json())
