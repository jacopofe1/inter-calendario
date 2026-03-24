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
    "anthropic-version": "2023-06-01"
}

prompt = f"""Oggi è {oggi}. Genera un file ICS completo per le partite dell'Inter Milano stagione 2025/26.

REGOLE FONDAMENTALI:
- Includi Serie A, Champions League, Coppa Italia
- Partite giocate: metti risultato reale e STATUS:CONFIRMED
- Partite future confermate: metti STATUS:TENTATIVE
- NON includere partite non ancora qualificate (es finale coppa italia se non qualificati)
- Casa = 🏠, Trasferta = ✈️
- Derby (Milan, Juventus) = aggiungi 🔥
- DESCRIPTION inizia sempre con: ⚫️🔵 DAI NOI!\\n\\n

FORMATO ESATTO DA RISPETTARE - NON aggiungere nulla prima di BEGIN:VCALENDAR:
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

BEGIN:VEVENT
UID:inter-sa-20250825@inter-calendar
DTSTART:20250825T184500Z
DTEND:20250825T204500Z
SUMMARY:🏠 [Serie A] Inter vs Torino
DESCRIPTION:⚫️🔵 DAI NOI!\\n\\n🏆 Serie A - Giornata 1\\nInter Milano 5 - 0 Torino FC\\n✅ Risultato Finale
LOCATION:San Siro, Milano
STATUS:CONFIRMED
END:VEVENT

[CONTINUA CON TUTTE LE ALTRE PARTITE NELLO STESSO FORMATO]

END:VCALENDAR

Partite già giocate con risultati certi da includere:
- Serie A G1: Inter 5-0 Torino (25/08/2025)
- Serie A G2: Inter 1-2 Udinese (31/08/2025)
- Serie A G3: Juventus 4-3 Inter (13/09/2025) TRASFERTA DERBY
- CL: Ajax 0-2 Inter (17/09/2025) TRASFERTA
- Serie A G4: Inter 2-1 Sassuolo (21/09/2025)
- Serie A G5: Cagliari 0-2 Inter (27/09/2025) TRASFERTA
- CL: Inter 3-0 Slavia Praga (30/09/2025)
- Serie A G6: Inter 4-1 Cremonese (04/10/2025)
- Serie A G7: Roma 0-1 Inter (18/10/2025) TRASFERTA
- CL: Union SG 0-4 Inter (21/10/2025) TRASFERTA
- Serie A G8: Napoli 3-1 Inter (25/10/2025) TRASFERTA
- Serie A G9: Inter 3-0 Fiorentina (29/10/2025)
- Serie A G10: Verona 1-2 Inter (02/11/2025) TRASFERTA
- CL: Inter 2-1 Kairat (05/11/2025)
- Serie A G11: Inter 2-0 Lazio (09/11/2025)
- Serie A G12: Inter 0-1 Milan (23/11/2025) DERBY
- CL: Atletico Madrid 2-1 Inter (26/11/2025) TRASFERTA
- Serie A G13: Pisa 0-2 Inter (30/11/2025) TRASFERTA
- Coppa Italia Ottavi: Inter 5-1 Venezia (03/12/2025)
- Serie A G14: Inter 4-0 Como (06/12/2025)
- CL: Inter 0-1 Liverpool (09/12/2025)
- Serie A G15: Genoa 1-2 Inter (14/12/2025) TRASFERTA
- Serie A G17: Atalanta 0-1 Inter (28/12/2025) TRASFERTA
- Serie A G18: Inter 3-1 Bologna (04/01/2026)
- Serie A G21: Inter 1-0 Lecce (14/01/2026)
- CL: Inter 1-3 Arsenal (20/01/2026)
- CL: Borussia Dortmund 0-2 Inter (28/01/2026) TRASFERTA
- Serie A G22: Udinese 0-1 Inter (17/01/2026) TRASFERTA
- Serie A G23: Inter 6-2 Pisa (23/01/2026)
- Serie A G24: Cremonese 0-2 Inter (01/02/2026) TRASFERTA
- Serie A G25: Sassuolo 0-5 Inter (08/02/2026) TRASFERTA
- CL Playoff Andata: Bodo/Glimt 3-1 Inter (18/02/2026) TRASFERTA
- Serie A G26: Inter 3-2 Juventus (14/02/2026) DERBY
- CL Playoff Ritorno: Inter 1-2 Bodo/Glimt - ELIMINATI (24/02/2026)
- Serie A G27: Lecce 0-2 Inter (21/02/2026) TRASFERTA
- Serie A G28: Inter 2-0 Genoa (28/02/2026)
- Serie A G29: Milan 1-0 Inter (08/03/2026) TRASFERTA DERBY
- Serie A G30: Inter 1-1 Atalanta (14/03/2026)
- Serie A G31: Fiorentina 1-1 Inter (22/03/2026) TRASFERTA

Partite future confermate:
- Serie A G32: Inter vs Roma domenica 05/04/2026 ore 20:45
- Serie A G33: Como vs Inter domenica 12/04/2026 ore 20:45 TRASFERTA
- Serie A G34: Inter vs Cagliari venerdi 17/04/2026 ore 20:45
- Coppa Italia Semifinale Ritorno: Inter vs Como martedi 21/04/2026 ore 21:00
- Serie A G35: Torino vs Inter domenica 26/04/2026 ore 18:00 TRASFERTA
- Serie A G36: Inter vs Parma domenica 03/05/2026 ore 15:00
- Serie A G37: Lazio vs Inter domenica 10/05/2026 ore 15:00 TRASFERTA
- Serie A G38: Inter vs Verona domenica 17/05/2026 ore 15:00
- Serie A G38: Bologna vs Inter domenica 24/05/2026 ore 15:00 TRASFERTA

Genera SOLO il file ICS completo, nessun testo prima o dopo, nessun markdown."""

print("📡 Chiamo Claude per generare il calendario...")

response = requests.post(
    "https://api.anthropic.com/v1/messages",
    headers=headers,
    json={
        "model": "claude-haiku-4-5-20251001",
        "max_tokens": 8096,
        "messages": [{"role": "user", "content": prompt}]
    }
)

print(f"Status risposta: {response.status_code}")
data = response.json()

if response.status_code == 200:
    ics_content = data["content"][0]["text"]
    
    # Pulizia
    if "```" in ics_content:
        lines = ics_content.split("\n")
        lines = [l for l in lines if not l.startswith("```")]
        ics_content = "\n".join(lines)
    
    if "BEGIN:VCALENDAR" in ics_content:
        ics_content = ics_content[ics_content.index("BEGIN:VCALENDAR"):]
    
    with open("Inter_Milano_Calendario_2526.ics", "w", encoding="utf-8") as f:
        f.write(ics_content)
    
    print(f"✅ Calendario salvato!")
    print(f"📅 Righe generate: {len(ics_content.splitlines())}")
else:
    print(f"❌ Errore: {data}")
