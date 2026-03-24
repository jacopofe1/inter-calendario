import os
import datetime
import requests

oggi = datetime.date.today().strftime("%d/%m/%Y")
ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY")

print(f"API Key presente: {bool(ANTHROPIC_API_KEY)}")
print(f"Data oggi: {oggi}")

headers = {
    "Content-Type": "application/json",
    "x-api-key": ANTHROPIC_API_KEY,
    "anthropic-version": "2023-06-01",
    "anthropic-beta": "web-search-2025-03-05"
}

prompt = f"""Oggi è {oggi}.

Il tuo compito è generare un file ICS aggiornato con TUTTE le partite dell'Inter Milano stagione 2025/26.

PRIMA usa il web search per cercare:
1. "Inter Milano risultati Serie A 2025-26"
2. "Inter Milano prossime partite calendario 2026"
3. "Inter Coppa Italia 2025-26 calendario"

POI genera il file ICS con i dati aggiornati che hai trovato.

REGOLE:
- Includi Serie A, Champions League, Coppa Italia
- Partite giocate: STATUS:CONFIRMED con risultato reale
- Partite future: STATUS:TENTATIVE
- NON includere partite non confermate
- Casa = 🏠, Trasferta = ✈️
- Derby (Milan, Juventus) = aggiungi 🔥
- DESCRIPTION inizia sempre con: ⚫️🔵 DAI NOI!\\n\\n
- Ogni SUMMARY inizia con icona casa/trasferta seguita da [Competizione]

FORMATO OBBLIGATORIO - inizia ESATTAMENTE così:
BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//Inter Milano Calendario Completo//IT
CALNAME:⚽️ Inter Milano 2025/26
CALDESC:Calendario completo Inter Milano - Serie A, Champions League, Coppa Italia 2025/26
X-WR-CALNAME:⚽️ Inter Milano 2025/26
X-WR-CALDESC:Serie A | Champions League | Coppa Italia
X-WR-TIMEZONE:Europe/Rome
REFRESH-INTERVAL;VALUE=DURATION:PT12H
COLOR:0070B5
X-LAST-UPDATED:{oggi}

Genera SOLO il file ICS completo. Nessun testo prima o dopo. Nessun markdown. Nessun backtick."""

print("📡 Chiamo Claude con web search...")

response = requests.post(
    "https://api.anthropic.com/v1/messages",
    headers=headers,
    json={
        "model": "claude-haiku-4-5-20251001",
        "max_tokens": 8096,
        "tools": [
            {
                "type": "web_search_20250305",
                "name": "web_search"
            }
        ],
        "messages": [{"role": "user", "content": prompt}]
    }
)

print(f"Status risposta: {response.status_code}")
data = response.json()

if response.status_code == 200:
    ics_content = ""
    for block in data.get("content", []):
        if block.get("type") == "text":
            ics_content += block.get("text", "")
    
    if "```" in ics_content:
        lines = ics_content.split("\n")
        lines = [l for l in lines if not l.startswith("```")]
        ics_content = "\n".join(lines)
    
    if "BEGIN:VCALENDAR" in ics_content:
        ics_content = ics_content[ics_content.index("BEGIN:VCALENDAR"):]
    
    if ics_content:
        with open("Inter_Milano_Calendario_2526.ics", "w", encoding="utf-8") as f:
            f.write(ics_content)
        print(f"✅ Calendario salvato!")
        print(f"📅 Righe generate: {len(ics_content.splitlines())}")
    else:
        print("❌ Nessun contenuto ICS trovato!")
        print(data)
else:
    print(f"❌ Errore: {data}")
