import os
import datetime
import requests

oggi = datetime.date.today()
FOOTBALL_API_KEY = os.environ.get("FOOTBALL_API_KEY")

HEADERS = {
    "x-apisports-key": FOOTBALL_API_KEY
}

BASE_URL = "https://v3.football.api-sports.io"
INTER_ID = 505  # ID dell'Inter su API-Football
SEASON = 2025

def get_partite_inter():
    url = f"{BASE_URL}/fixtures"
    params = {
        "team": INTER_ID,
        "season": SEASON
    }
    response = requests.get(url, headers=HEADERS, params=params)
    data = response.json()
    return data.get("response", [])

def formato_data(date_str):
    dt = datetime.datetime.fromisoformat(date_str.replace("Z", "+00:00"))
    return dt.strftime("%Y%m%dT%H%M%SZ")

def get_competizione(league_name):
    if "Serie A" in league_name:
        return "Serie A"
    elif "Champions" in league_name:
        return "Champions League"
    elif "Coppa Italia" in league_name or "Italy Cup" in league_name:
        return "Coppa Italia"
    elif "Supercoppa" in league_name or "Super Cup" in league_name:
        return "Supercoppa"
    else:
        return league_name

def is_casa(fixture, home_id=INTER_ID):
    return fixture["teams"]["home"]["id"] == home_id

def crea_evento(uid, dtstart, dtend, summary, description, location, status):
    return f"""BEGIN:VEVENT
UID:{uid}
DTSTART:{dtstart}
DTEND:{dtend}
SUMMARY:{summary}
DESCRIPTION:{description}
LOCATION:{location}
STATUS:{status}
END:VEVENT"""

print("📡 Recupero partite Inter dalla API-Football...")
partite_raw = get_partite_inter()
print(f"✅ Trovate {len(partite_raw)} partite")

eventi = []

for p in partite_raw:
    fixture = p["fixture"]
    league = p["league"]
    teams = p["teams"]
    goals = p["goals"]
    
    league_name = get_competizione(league["name"])
    
    # Filtra solo le competizioni che ci interessano
    if league_name not in ["Serie A", "Champions League", "Coppa Italia", "Supercoppa"]:
        continue
    
    # Data e ora
    date_str = fixture["date"]
    dtstart = formato_data(date_str)
    dt = datetime.datetime.fromisoformat(date_str.replace("Z", "+00:00"))
    dtend = (dt + datetime.timedelta(hours=2)).strftime("%Y%m%dT%H%M%SZ")
    
    # Squadre
    home_team = teams["home"]["name"]
    away_team = teams["away"]["name"]
    
    # Casa o trasferta
    casa = is_casa(p)
    icona = "🏠" if casa else "✈️"
    
    # Derby
    derby = ""
    if "Milan" in home_team or "Milan" in away_team:
        if "Inter" in home_team or "Inter" in away_team:
            derby = " 🔥"
    if "Juventus" in home_team or "Juventus" in away_team:
        if "Inter" in home_team or "Inter" in away_team:
            derby = " 🔥"
    
    summary = f"{icona} [{league_name}] {home_team} vs {away_team}{derby}"
    
    # Stato e risultato
    status_fixture = fixture["status"]["short"]
    
    if status_fixture in ["FT", "AET", "PEN"]:
        score = f"{goals['home']} - {goals['away']}"
        description = f"🏆 {league_name}\\n{home_team} {score} {away_team}\\n✅ Risultato Finale"
        status = "CONFIRMED"
    elif status_fixture in ["NS", "TBD"]:
        if status_fixture == "TBD":
            summary = f"{icona} [{league_name}] {home_team} vs {away_team}{derby} - TBD"
        description = f"🏆 {league_name}\\n{home_team} vs {away_team}\\n📅 Partita in programma"
        status = "TENTATIVE"
    else:
        description = f"🏆 {league_name}\\n{home_team} vs {away_team}\\n📅 Partita in programma"
        status = "TENTATIVE"
    
    # Aggiungi DAI NOI
    description = f"⚫️🔵 DAI NOI!\\n\\n{description}"
    
    # Location
    venue = fixture.get("venue", {})
    location = f"{venue.get('name', 'San Siro')}, {venue.get('city', 'Milano')}"
    
    uid = f"inter-{fixture['id']}@inter-calendar"
    
    evento = crea_evento(uid, dtstart, dtend, summary, description, location, status)
    eventi.append((dt, evento))

# Ordina per data
eventi.sort(key=lambda x: x[0])
eventi_ics = [e[1] for e in eventi]

header = f"""BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//Inter Milano Calendario Completo//IT
CALNAME:⚽️ Inter Milano 2025/26
CALDESC:Calendario completo Inter Milano - Serie A, Champions League, Coppa Italia 2025/26
X-WR-CALNAME:⚽️ Inter Milano 2025/26
X-WR-CALDESC:Serie A | Champions League | Coppa Italia
X-WR-TIMEZONE:Europe/Rome
REFRESH-INTERVAL;VALUE=DURATION:PT12H
COLOR:0070B5
X-LAST-UPDATED:{oggi.strftime("%Y%m%d")}"""

footer = "END:VCALENDAR"

ics_content = header + "\n\n" + "\n\n".join(eventi_ics) + "\n\n" + footer

output_path = "Inter_Milano_Calendario_2526.ics"
with open(output_path, "w", encoding="utf-8") as f:
    f.write(ics_content)

print(f"✅ Calendario aggiornato salvato - {oggi.strftime('%d/%m/%Y')}")
print(f"📅 Totale partite: {len(eventi_ics)}")
print(f"🏠 Casa | ✈️ Trasferta | ⚫️🔵 DAI NOI!")
