# VVT — Verzeichnis von Verarbeitungstätigkeiten (Beispiel)

**Einfach erklärt:** VVT = Verzeichnis von Verarbeitungstätigkeiten (Art. 30 DSGVO). Die Kommune führt darin ein internes Register, welche Bürgerdaten sie zu welchem Zweck verarbeitet.

> DSGVO Art. 30 — Exemplarisch für das Modul **Fördermittel-Management**

## Metadaten

| Feld | Wert |
|------|------|
| VVT-ID | VVT-FM-001 |
| Stand | 2026-08-20 |
| Version | 1.0 |
| Verantwortliche Stelle | Gemeinde Musterstadt (5.200 Einwohner) |
| Datenschutzbeauftragter | [Name], [Kontakt] |

---

## 1. Verantwortliche Stelle

**Name:** Gemeinde Musterstadt  
**Vertreter:** Bürgermeister/in  
**Anschrift:** Rathausplatz 1, 12345 Musterstadt  
**Kontakt:** example@musterstadt.de

## 2. Zweck der Verarbeitung

Digitales Fördermittel-Management: Erfassung, Prüfung und Bewilligung
von Förderanträgen (Konjunktur, Klima, Soziales) für Bürger und Vereine.

## 3. Rechtsgrundlage

- **Art. 6 Abs. 1 lit. e DSGVO** — Wahrnehmung öffentlicher Aufgaben
- **§ 3 BDSG** — Kommunale Selbstverwaltung
- Landesfördergesetz (LFG) Musterland

## 4. Kategorien betroffener Personen

- Antragstellende Bürger (natürliche Personen)
- Vertreter von Vereinen / Unternehmen (natürliche Personen)
- Antragsbearbeiter (interne Mitarbeiter)

## 5. Kategorien personenbezogener Daten

| Datenkategorie | Beispiel | Besondere Kategorie (Art. 9)? |
|----------------|----------|-------------------------------|
| Stammdaten | Name, Anschrift, Geburtsdatum | Nein |
| Kontaktdaten | E-Mail, Telefon | Nein |
| Finanzdaten | IBAN, Einkommensnachweis | Nein |
| Antragsdaten | Förderzweck, Projektbeschreibung | Nein |
| Dokumente | Personalausweis-Kopie (geschwärzt) | Nein |

**Keine** besonderen Kategorien nach Art. 9 DSGVO.

## 6. Empfänger der Daten

| Empfänger | Zweck | Drittland? |
|-----------|-------|------------|
| Fördermittelgeber (Land) | Bewilligung, Auszahlung | Nein |
| Hausbank der Kommune | Überweisung | Nein |
| Keine externen Cloud-Dienste | — | Nein |

## 7. Speicherdauer

| Daten | Frist | Grundlage |
|-------|-------|-----------|
| Antragsunterlagen | 10 Jahre | § 147 AO (steuerliche Aufbewahrung) |
| Log-Daten / Audit | 3 Jahre | IT-Sicherheitskonzept |

Löschung automatisiert nach Ablauf via Cron-Job (`scripts/purge-expired.ts`).

## 8. Technische Umsetzung (open-gov-automation)

- **On-Premise**: 2 gekoppelte Geräte (GX10) im Rathaus – lokale KI-Einheit (keine Cloud)
- **Verschlüsselung**: TLS 1.3 + AES-256 (ruhende Daten)
- **Trennung**: Mandantenisolation via `tenantId`
- **Audit-Log**: Jede Änderung protokolliert (ADR 0012)
- **Transparenz**: Quellcode öffentlich (GPL-3.0)

---

## Vorlage zum Kopieren

```markdown
## [VVT-ID] — [Name der Verarbeitungstätigkeit]

1. Verantwortliche Stelle:
2. Zweck:
3. Rechtsgrundlage:
4. Betroffene Personen:
5. Datenkategorien:
6. Empfänger:
7. Speicherdauer:
8. Technische Umsetzung:
```
