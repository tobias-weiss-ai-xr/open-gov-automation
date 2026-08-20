# ADR 0012: Unix-Philosophie für Öffentliche Verwaltungen

**Status:** Proposed  
**Datum:** 2026-08-20  
**Betreff:** Anwendung minimaler, modularer Prinzipien auf Verwaltungssysteme

---

## Problem

Öffentliche Verwaltungen arbeiten mit:
- Monolithischen, undurchsichtigen Systemen
- Manuellen, fehleranfälligen Prozessen
- Vendor Lock-in bei proprietärer Software
- Keine Nachvollziehbarkeit von Entscheidungen
- Keine automatisierte Qualitätssicherung

## Entscheidung

Wir wenden die Unix-Philosophie auf Verwaltungssysteme an:

### 1. **Jedes Modul macht eine Sache gut**
```
Verwaltung
├── Fördermittel (ein Modul)
├── Bauanträge (ein Modul)
└── Jede Schnittstelle ist textbasiert (API/JSON)
```

### 2. **Automatisierte Qualitätssicherung via CI**
- Jede Änderung wird getestet vor dem Merge
- Pipelines sind dokumentiert, reproduzierbar
- Health Checks zeigen Systemzustand transparent

### 3. **Textbasierte, durchsichtige Schnittstellen**
- YAML für Konfiguration
- JSON für Daten
- Markdown für Dokumentation
- Git für Versionierung

### 4. **Resilienz durch Modularität**
- Ein Modul kann ausfallen ohne Gesamtzusammenbruch
- Austauschbarkeit ohne Systemstillstand
- Rollback-Fähigkeit bei Problemen

## Konsequenzen

### Positive
- **Transparenz**: Jede Entscheidung ist nachvollziehbar
- **Wartbarkeit**: Kleine Module sind einfacher zu pflegen
- **Unabhängigkeit**: Kein Vendor Lock-in
- **Qualität**: Automatisierte Tests verhindern Regressionen

### Negative
- **Initiale Komplexität**: Mehr Setup-Aufwand am Anfang
- **Lernkurve**: Teams müssen CI/CD-Prinzipien verstehen
- **Fragmentierung**: Koordination zwischen Modulen erforderlich

## Alternativen

1. **Monolithisches Verwaltungssystem** (aktuell)
   - ❌ Keine Transparenz
   - ❌ Vendor Lock-in
   - ❌ Manuelle Prozesse

2. **Cloud-only SaaS-Lösung**
   - ❌ Datenhoheit bei Drittanbieter
   - ❌ Keine On-Premise Option
   - ❌ Laufende Lizenzkosten

## Referenzen

- CI-Pipeline: `.github/workflows/ci.yml`
- Dokumentation: [README.md](../README.md)
