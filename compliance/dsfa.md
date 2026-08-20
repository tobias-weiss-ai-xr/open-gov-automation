# Datenschutz-Folgenabschätzung (DSFA)

**DSGVO Art. 35** — Bewertung der Risiken für betroffene Personen durch die Verarbeitung personenbezogener Daten.

**Geltungsbereich:** Modul Bauanträge (Verwaltungsleistung, betroffene Personen: Antragstellende)

## 1. Prüfung der DSFA-Pflicht

| Kriterium (Art. 35 Abs. 3) | Zutreffend? | Begründung |
|----------------------------|-------------|------------|
| Umfangreiche automatisierte Entscheidung | Nein | Menschliche Prüfung vor Bewilligung |
| Großflächige Überwachung | Nein | Keine Tracking/Video |
| Besondere Kategorien (Art. 9) | Nein | Keine Gesundheit/Religion etc. |
| Umfangreiche Verarbeitung | Ja | Alle Bürger betroffen |
| Hohes Risiko | Gering | On-Premise, keine Profilbildung |

**Ergebnis:** DSFA empfohlen (Vorsorgeprinzip), nicht zwingend.

## 2. Beschreibung der Verarbeitung

- **Zweck:** Bauantragsprüfung & -genehmigung (prädiktive Vorab-Prüfung)
- **Umfang:** ~Antragstellende, 2 Module (Fördermittel, Bauanträge)
- **Technik:** 2× Mesh-Cluster (GX10), On-Premise, Open Source

## 3. Notwendigkeit & Verhältnismäßigkeit

| Maßstab | Bewertung |
|---------|-----------|
| Zweckbindung | ✅ Klar definiert (Verwaltungsleistung Bau) |
| Datenminimierung | ✅ Nur Pflichtfelder, keine Optional-Daten |
| Speicherbegrenzung | ✅ Auto-Löschung nach Frist |

## 4. Risikobewertung

| Risiko | Wahrscheinlichkeit | Auswirkung | Maßnahme |
|--------|-------------------|------------|----------|
| Unbefugter Zugriff | Gering | Hoch | TOMs T1-T3 (2FA, RBAC, TLS) |
| Datenverlust | Gering | Mittel | T6 (Backups, Failover) |
| Falschzuweisung | Gering | Mittel | T4 (Validierung + Audit) |
| Profilbildung | Sehr gering | Hoch | Keine Cross-Modul-Analyse |

**Restrisiko:** Gering — durch TOMs adressiert.

## 5. Maßnahmen zur Risikominderung

- Privacy by Design: Datenminimierung im Datenmodell
- Privacy by Default: Opt-in für alle Nicht-Pflichtfelder
- Transparenz: Quellcode öffentlich einsehbar
- Betroffenenrechte: Löschantrag über Verwaltung

## 6. Konsultation

- Datenschutzbeauftragter: [x] befragt
- Betroffene: [ ] Information via Bürgerbrief
- Aufsichtsbehörde: Nur bei verbleibendem hohen Risiko (hier: Nein)

## 7. Freigabe

| Rolle | Unterschrift | Datum |
|-------|--------------|-------|
| IT-Leitung | ____________ | ______ |
| Datenschutzbeauftragter | ____________ | ______ |

---

## Wann ist eine DSFA PFLICHT?

Nach Art. 35 Abs. 3 DSGVO bei:
1. Systematischer **Profilevaluation** (Scoring)
2. **Umfangreicher Verarbeitung** besonderer Kategorien (Art. 9)
3. **Großflächiger Überwachung** (Öffentlicher Raum)

Im open-gov-automation Ansatz werden diese vermieden durch:
- Keine Blackbox-Algorithmen (transparent)
- Keine Art.-9-Daten (Stammdaten nur)
- Keine Überwachung (Service, nicht Surveillance)
