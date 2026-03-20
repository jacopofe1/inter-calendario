import os
import datetime

oggi = datetime.date.today()

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

partite = [
    # PASSATE - Serie A
    ("inter-sa-20250825", "20250825T184500Z", "20250825T204500Z", "🏠 [Serie A] Inter vs Torino", "🏆 Serie A - Giornata 1\\nInter Milano 5 - 0 Torino FC\\n✅ Risultato Finale", "San Siro, Milano", "CONFIRMED"),
    ("inter-sa-20250831", "20250831T184500Z", "20250831T204500Z", "🏠 [Serie A] Inter vs Udinese", "🏆 Serie A - Giornata 2\\nInter Milano 1 - 2 Udinese Calcio\\n✅ Risultato Finale", "San Siro, Milano", "CONFIRMED"),
    ("inter-sa-20250913", "20250913T160000Z", "20250913T180000Z", "✈️ [Serie A] Juventus vs Inter 🔥", "🏆 Serie A - Giornata 3\\nJuventus Turin 4 - 3 Inter Milano\\n✅ Risultato Finale", "Allianz Stadium, Torino", "CONFIRMED"),
    ("inter-cl-20250917", "20250917T190000Z", "20250917T210000Z", "✈️ [Champions League] Ajax vs Inter", "🏆 UEFA Champions League\\nAjax Amsterdam 0 - 2 Inter Milano\\n✅ Risultato Finale", "Johan Cruyff Arena, Amsterdam", "CONFIRMED"),
    ("inter-sa-20250921", "20250921T184500Z", "20250921T204500Z", "🏠 [Serie A] Inter vs Sassuolo", "🏆 Serie A - Giornata 4\\nInter Milano 2 - 1 Sassuolo Calcio\\n✅ Risultato Finale", "San Siro, Milano", "CONFIRMED"),
    ("inter-sa-20250927", "20250927T184500Z", "20250927T204500Z", "✈️ [Serie A] Cagliari vs Inter", "🏆 Serie A - Giornata 5\\nCagliari Calcio 0 - 2 Inter Milano\\n✅ Risultato Finale", "Unipol Domus, Cagliari", "CONFIRMED"),
    ("inter-cl-20250930", "20250930T190000Z", "20250930T210000Z", "🏠 [Champions League] Inter vs Slavia Praga", "🏆 UEFA Champions League\\nInter Milano 3 - 0 Slavia Prague\\n✅ Risultato Finale", "San Siro, Milano", "CONFIRMED"),
    ("inter-sa-20251004", "20251004T160000Z", "20251004T180000Z", "🏠 [Serie A] Inter vs Cremonese", "🏆 Serie A - Giornata 6\\nInter Milano 4 - 1 US Cremonese\\n✅ Risultato Finale", "San Siro, Milano", "CONFIRMED"),
    ("inter-sa-20251018", "20251018T184500Z", "20251018T204500Z", "✈️ [Serie A] Roma vs Inter", "🏆 Serie A - Giornata 7\\nAS Roma 0 - 1 Inter Milano\\n✅ Risultato Finale", "Stadio Olimpico, Roma", "CONFIRMED"),
    ("inter-cl-20251021", "20251021T190000Z", "20251021T210000Z", "✈️ [Champions League] Union SG vs Inter", "🏆 UEFA Champions League\\nUnion Saint-Gilloise 0 - 4 Inter Milano\\n✅ Risultato Finale", "Lotto Park, Bruxelles", "CONFIRMED"),
    ("inter-sa-20251025", "20251025T160000Z", "20251025T180000Z", "✈️ [Serie A] Napoli vs Inter", "🏆 Serie A - Giornata 8\\nNapoli 3 - 1 Inter Milano\\n✅ Risultato Finale", "Stadio Maradona, Napoli", "CONFIRMED"),
    ("inter-sa-20251029", "20251029T194500Z", "20251029T214500Z", "🏠 [Serie A] Inter vs Fiorentina", "🏆 Serie A - Giornata 9\\nInter Milano 3 - 0 ACF Fiorentina\\n✅ Risultato Finale", "San Siro, Milano", "CONFIRMED"),
    ("inter-sa-20251102", "20251102T113000Z", "20251102T131500Z", "✈️ [Serie A] Verona vs Inter", "🏆 Serie A - Giornata 10\\nHellas Verona 1 - 2 Inter Milano\\n✅ Risultato Finale", "Stadio Bentegodi, Verona", "CONFIRMED"),
    ("inter-cl-20251105", "20251105T200000Z", "20251105T220000Z", "🏠 [Champions League] Inter vs Kairat", "🏆 UEFA Champions League\\nInter Milano 2 - 1 FC Kairat Almaty\\n✅ Risultato Finale", "San Siro, Milano", "CONFIRMED"),
    ("inter-sa-20251109", "20251109T194500Z", "20251109T214500Z", "🏠 [Serie A] Inter vs Lazio", "🏆 Serie A - Giornata 11\\nInter Milano 2 - 0 Lazio Rome\\n✅ Risultato Finale", "San Siro, Milano", "CONFIRMED"),
    ("inter-sa-20251123", "20251123T194500Z", "20251123T214500Z", "🏠 [Serie A] Inter vs Milan 🔥", "🏆 Serie A - Giornata 12 | Derby della Madonnina 🔥\\nInter Milano 0 - 1 AC Milan\\n✅ Risultato Finale", "San Siro, Milano", "CONFIRMED"),
    ("inter-cl-20251126", "20251126T200000Z", "20251126T220000Z", "✈️ [Champions League] Atletico Madrid vs Inter", "🏆 UEFA Champions League\\nAtletico Madrid 2 - 1 Inter Milano\\n✅ Risultato Finale", "Estadio Metropolitano, Madrid", "CONFIRMED"),
    ("inter-sa-20251130", "20251130T140000Z", "20251130T160000Z", "✈️ [Serie A] Pisa vs Inter", "🏆 Serie A - Giornata 13\\nPisa SC 0 - 2 Inter Milano\\n✅ Risultato Finale", "Arena Garibaldi, Pisa", "CONFIRMED"),
    ("inter-ci-20251203", "20251203T200000Z", "20251203T220000Z", "🏠 [Coppa Italia] Inter vs Venezia", "🏆 Coppa Italia - Ottavi di Finale\\nInter Milano 5 - 1 Venezia FC\\n✅ Risultato Finale", "San Siro, Milano", "CONFIRMED"),
    ("inter-sa-20251206", "20251206T170000Z", "20251206T190000Z", "🏠 [Serie A] Inter vs Como", "🏆 Serie A - Giornata 14\\nInter Milano 4 - 0 Como 1907\\n✅ Risultato Finale", "San Siro, Milano", "CONFIRMED"),
    ("inter-cl-20251209", "20251209T200000Z", "20251209T220000Z", "🏠 [Champions League] Inter vs Liverpool", "🏆 UEFA Champions League\\nInter Milano 0 - 1 Liverpool FC\\n✅ Risultato Finale", "San Siro, Milano", "CONFIRMED"),
    ("inter-sa-20251214", "20251214T170000Z", "20251214T190000Z", "✈️ [Serie A] Genoa vs Inter", "🏆 Serie A - Giornata 15\\nGenoa CFC 1 - 2 Inter Milano\\n✅ Risultato Finale", "Stadio Luigi Ferraris, Genova", "CONFIRMED"),
    ("inter-sa-20251228", "20251228T194500Z", "20251228T214500Z", "✈️ [Serie A] Atalanta vs Inter", "🏆 Serie A - Giornata 17\\nAtalanta BC 0 - 1 Inter Milano\\n✅ Risultato Finale", "Gewiss Stadium, Bergamo", "CONFIRMED"),
    ("inter-sa-20260104", "20260104T194500Z", "20260104T214500Z", "🏠 [Serie A] Inter vs Bologna", "🏆 Serie A - Giornata 18\\nInter Milano 3 - 1 Bologna FC\\n✅ Risultato Finale", "San Siro, Milano", "CONFIRMED"),
    ("inter-cl-20260120", "20260120T200000Z", "20260120T220000Z", "🏠 [Champions League] Inter vs Arsenal", "🏆 UEFA Champions League\\nInter Milano 1 - 3 Arsenal FC\\n✅ Risultato Finale", "San Siro, Milano", "CONFIRMED"),
    ("inter-sa-20260114", "20260114T194500Z", "20260114T214500Z", "🏠 [Serie A] Inter vs Lecce", "🏆 Serie A - Giornata 21\\nInter Milano 1 - 0 US Lecce\\n✅ Risultato Finale", "San Siro, Milano", "CONFIRMED"),
    ("inter-cl-20260128", "20260128T200000Z", "20260128T220000Z", "✈️ [Champions League] Borussia Dortmund vs Inter", "🏆 UEFA Champions League\\nBorussia Dortmund 0 - 2 Inter Milano\\n✅ Risultato Finale", "Signal Iduna Park, Dortmund", "CONFIRMED"),
    ("inter-sa-20260117", "20260117T140000Z", "20260117T160000Z", "✈️ [Serie A] Udinese vs Inter", "🏆 Serie A - Giornata 22\\nUdinese Calcio 0 - 1 Inter Milano\\n✅ Risultato Finale", "Stadio Friuli, Udine", "CONFIRMED"),
    ("inter-sa-20260123", "20260123T194500Z", "20260123T214500Z", "🏠 [Serie A] Inter vs Pisa", "🏆 Serie A - Giornata 23\\nInter Milano 6 - 2 Pisa SC\\n✅ Risultato Finale", "San Siro, Milano", "CONFIRMED"),
    ("inter-sa-20260201", "20260201T170000Z", "20260201T190000Z", "✈️ [Serie A] Cremonese vs Inter", "🏆 Serie A - Giornata 24\\nUS Cremonese 0 - 2 Inter Milano\\n✅ Risultato Finale", "Stadio Giovanni Zini, Cremona", "CONFIRMED"),
    ("inter-sa-20260208", "20260208T170000Z", "20260208T190000Z", "✈️ [Serie A] Sassuolo vs Inter", "🏆 Serie A - Giornata 25\\nSassuolo Calcio 0 - 5 Inter Milano\\n✅ Risultato Finale", "Mapei Stadium, Reggio Emilia", "CONFIRMED"),
    ("inter-cl-20260218", "20260218T200000Z", "20260218T220000Z", "✈️ [Champions League] Bodø/Glimt vs Inter", "🏆 UEFA Champions League - Playoff Andata\\nBodø/Glimt 3 - 1 Inter Milano\\n✅ Risultato Finale", "Aspmyra Stadion, Bodø", "CONFIRMED"),
    ("inter-sa-20260214", "20260214T194500Z", "20260214T214500Z", "🏠 [Serie A] Inter vs Juventus 🔥", "🏆 Serie A - Giornata 26 | Derby d'Italia 🔥\\nInter Milano 3 - 2 Juventus Turin\\n✅ Risultato Finale", "San Siro, Milano", "CONFIRMED"),
    ("inter-cl-20260224", "20260224T200000Z", "20260224T220000Z", "🏠 [Champions League] Inter vs Bodø/Glimt", "🏆 UEFA Champions League - Playoff Ritorno\\nInter Milano 1 - 2 Bodø/Glimt\\nEliminati ❌\\n✅ Risultato Finale", "San Siro, Milano", "CONFIRMED"),
    ("inter-sa-20260221", "20260221T170000Z", "20260221T190000Z", "✈️ [Serie A] Lecce vs Inter", "🏆 Serie A - Giornata 27\\nUS Lecce 0 - 2 Inter Milano\\n✅ Risultato Finale", "Via del Mare, Lecce", "CONFIRMED"),
    ("inter-sa-20260228", "20260228T194500Z", "20260228T214500Z", "🏠 [Serie A] Inter vs Genoa", "🏆 Serie A - Giornata 28\\nInter Milano 2 - 0 Genoa CFC\\n✅ Risultato Finale", "San Siro, Milano", "CONFIRMED"),
    ("inter-sa-20260308", "20260308T194500Z", "20260308T214500Z", "✈️ [Serie A] Milan vs Inter 🔥", "🏆 Serie A - Giornata 29 | Derby della Madonnina 🔥\\nAC Milan 1 - 0 Inter Milano\\n✅ Risultato Finale", "San Siro, Milano", "CONFIRMED"),
    ("inter-sa-20260314", "20260314T140000Z", "20260314T160000Z", "🏠 [Serie A] Inter vs Atalanta", "🏆 Serie A - Giornata 30\\nInter Milano 1 - 1 Atalanta BC\\n✅ Risultato Finale", "San Siro, Milano", "CONFIRMED"),
    # FUTURE
    ("inter-sa-20260322", "20260322T194500Z", "20260322T214500Z", "✈️ [Serie A] Fiorentina vs Inter", "🏆 Serie A - Giornata 31\\nACF Fiorentina vs Inter Milano\\n📅 Partita in programma", "Stadio Artemio Franchi, Firenze", "TENTATIVE"),
    ("inter-sa-20260405", "20260405T184500Z", "20260405T204500Z", "🏠 [Serie A] Inter vs Roma", "🏆 Serie A - Giornata 32\\nInter Milano vs AS Roma\\n📅 Partita in programma", "San Siro, Milano", "TENTATIVE"),
    ("inter-sa-20260412", "20260412T130000Z", "20260412T150000Z", "✈️ [Serie A] Como vs Inter", "🏆 Serie A - Giornata 33\\nComo 1907 vs Inter Milano\\n📅 Partita in programma", "Stadio Giuseppe Sinigaglia, Como", "TENTATIVE"),
    ("inter-sa-20260419", "20260419T130000Z", "20260419T150000Z", "🏠 [Serie A] Inter vs Cagliari", "🏆 Serie A - Giornata 34\\nInter Milano vs Cagliari Calcio\\n📅 Partita in programma", "San Siro, Milano", "TENTATIVE"),
    ("inter-ci-20260421", "20260421T190000Z", "20260421T210000Z", "🏠 [Coppa Italia] Inter vs Como", "🏆 Coppa Italia - Semifinale Ritorno\\nInter Milano vs Como 1907\\n📅 Partita in programma", "San Siro, Milano", "TENTATIVE"),
    ("inter-sa-20260426", "20260426T130000Z", "20260426T150000Z", "✈️ [Serie A] Torino vs Inter", "🏆 Serie A - Giornata 35\\nTorino FC vs Inter Milano\\n📅 Partita in programma", "Stadio Olimpico Grande Torino, Torino", "TENTATIVE"),
    ("inter-sa-20260503", "20260503T130000Z", "20260503T150000Z", "🏠 [Serie A] Inter vs Parma", "🏆 Serie A - Giornata 36\\nInter Milano vs Parma Calcio\\n📅 Partita in programma", "San Siro, Milano", "TENTATIVE"),
    ("inter-sa-20260510", "20260510T130000Z", "20260510T150000Z", "✈️ [Serie A] Lazio vs Inter", "🏆 Serie A - Giornata 37\\nLazio Rome vs Inter Milano\\n📅 Partita in programma", "Stadio Olimpico, Roma", "TENTATIVE"),
    ("inter-sa-20260517", "20260517T130000Z", "20260517T150000Z", "🏠 [Serie A] Inter vs Verona", "🏆 Serie A - Giornata 38\\nInter Milano vs Hellas Verona\\n📅 Partita in programma", "San Siro, Milano", "TENTATIVE"),
    ("inter-sa-20260524", "20260524T130000Z", "20260524T150000Z", "✈️ [Serie A] Bologna vs Inter", "🏆 Serie A - Giornata 38 (ultima)\\nBologna FC vs Inter Milano\\n📅 Partita in programma", "Stadio Renato Dall'Ara, Bologna", "TENTATIVE"),
]

header = """BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//Inter Milano Calendario Completo//IT
CALNAME:⚽️ Inter Milano 2025/26
CALDESC:Calendario completo Inter Milano - Serie A, Champions League, Coppa Italia 2025/26
X-WR-CALNAME:⚽️ Inter Milano 2025/26
X-WR-CALDESC:Serie A | Champions League | Coppa Italia
X-WR-TIMEZONE:Europe/Rome
REFRESH-INTERVAL;VALUE=DURATION:PT12H
COLOR:0070B5"""

footer = "END:VCALENDAR"

eventi = []
for p in partite:
    uid, dtstart, dtend, summary, description, location, status = p
    evento = crea_evento(
        uid=f"{uid}@inter-calendar",
        dtstart=dtstart,
        dtend=dtend,
        summary=summary,
        description=description,
        location=location,
        status=status
    )
    eventi.append(evento)

ics_content = header + "\n\n" + "\n\n".join(eventi) + "\n\n" + footer

output_path = "Inter_Milano_Calendario_2526.ics"
with open(output_path, "w", encoding="utf-8") as f:
    f.write(ics_content)

print(f"✅ Calendario aggiornato salvato - {oggi.strftime('%d/%m/%Y')}")
print(f"📅 Totale partite: {len(partite)}")
print(f"🏠 Casa | ✈️ Trasferta")
