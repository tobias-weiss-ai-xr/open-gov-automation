# Examples — open-gov-automation

## Anwendung der Unix-Prinzipien auf öffentliche Verwaltungen

### Dokumente

| Dokument | Zweck | Prinzip |
|----------|-------|---------|
| [60k-Projekt-Skizze](60k-mesh-cluster-projekt.md) | 60k-Pilot: 2× lokale Geräte, Bauanträge als Beispiel | Referenz-Implementierung |
| [Mittelhessen-Kandidaten](mittelhessen-pilot-kandidaten.md) | Shortlist Mittelhessen (Städte + Kleinstädte) | Engagement / Akquise |
| [Nutzen-ROI-Analyse](nutzen-roi-analyse.md) | Kritische Wirtschaftlichkeitsprüfung der Module | Transparenz |
| [Monte-Carlo-Ergebnis](bauantraege-monte-carlo-ergebnis.md) | Bayesian Monte Carlo Bauanträge (Beweis) | Evidenz |
| [admin-fördermittel-ci.yml](admin-fördermittel-ci.yml) | CI-Pipeline für Fördermittel-Verwaltung | Automatisierte Qualität |

### Übergeordnete Dokumente

| Dokument | Ort |
|----------|-----|
| Prinzipien & Prozess | [`../README.md`](../README.md) |
| ADR 0012 (Architektur-Entscheidung) | [`../adr/0012-unix-philosophy-for-public-admin.md`](../adr/0012-unix-philosophy-for-public-admin.md) |

---

## Wie Sie diese Beispiele verwenden

### 1. CI-Pipeline anpassen

```bash
# Kopieren Sie die Pipeline für Ihr Fachverfahren
cp admin-fördermittel-ci.yml .github/workflows/bauantraege-ci.yml

# Passe die Prüfschritte an Ihren Anwendungsfall an
# - validate: prüfe Ihre Geschäftsregeln
# - check-deadlines: prüfe Ihre Fristen
```

### 2. Modulare Struktur übernehmen

```bash
# Verzeichnisstruktur für Ihr Fachverfahren anlegen
mkdir -p bauantraege/src/{adapters,scoring,deadlines}
mkdir -p bauantraege/tests
mkdir -p bauantraege/docs/ADR
```

### 3. Prinzipien anwenden

Prüfen Sie vor jeder neuen Software:

- [ ] Ist sie Open Source?
- [ ] Kann sie lokal (On-Premise) laufen?
- [ ] Hat sie klare Schnittstellen (API)?
- [ ] Ist der Code testbar?
- [ ] Kann sie durch ein anderes Modul ersetzt werden?

---

## Nächste Schritte

- [x] Fördermittel-Beispiel vorhanden
- [x] 60k-Pilot-Skizze vorhanden
- [ ] Weitere Modul-Vorlagen
