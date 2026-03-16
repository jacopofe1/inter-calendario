import anthropic
import os
import datetime

client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

oggi = datetime.date.today().strftime("%d/%m/%Y")

prompt = f"""Oggi è {oggi}.

Sei un assistente specializzato nel calendario dell'Inter Milano.
Il tuo compito è generare un file ICS aggiornato con TUTTE le partite dell'Inter Milano per la stagione 2025/26.

Regole importanti:
1. Includi Serie A, Champions League e Coppa Italia
2. Per le partite già giocate includi il risultato nella DESCRIPTION con ✅
3. Per le partite future confermate usa 📅 nella DESCRIPTION
4. NON includere partite il cui svolgimento non è ancora confermato (es. finali non ancora qualificate)
5. Se orario non è definito usa TBD nel summary
6. Ogni partita deve avere ⚽️ nel SUMMARY
7. Il formato del SUMMARY deve essere: ⚽️ [Competizione] Squadra vs Squadra
8. Per i derby (Inter-Milan, Inter-Juventus) aggiungi 🔥 nel summary
9. Usa STATUS:CONFIRMED per partite giocate, STATUS:TENTATIVE per future

Genera SOLO il contenuto del file ICS completo, senza spiegazioni, senza markdown, senza backtick.
Inizia direttamente con BEGIN:VCALENDAR e finisci con END:VCALENDAR.

Il file deve iniziare così:
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
"""

print("📡 Chiamo Claude per aggiornare il calendario...")

message = client.messages.create(
    model="claude-opus-4-6",
    max_tokens=8096,
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)

ics_content = message.content[0].text

# Pulizia nel caso ci siano backtick o markdown
if "```" in ics_content:
    lines = ics_content.split("\n")
    lines = [l for l in lines if not l.startswith("```")]
    ics_content = "\n".join(lines)

# Assicuriamoci che inizi con BEGIN:VCALENDAR
if "BEGIN:VCALENDAR" in ics_content:
    ics_content = ics_content[ics_content.index("BEGIN:VCALENDAR"):]

output_path = "Inter_Milano_Calendario_2526.ics"
with open(output_path, "w", encoding="utf-8") as f:
    f.write(ics_content)

print(f"✅ Calendario aggiornato salvato in {output_path}")
print(f"📅 Data aggiornamento: {oggi}")
