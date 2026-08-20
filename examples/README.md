# Examples — Verwaltung 2.0

## Anwendung der Unix-Prinzipien auf öffentliche Verwaltungen

### Dokumente

| Dokument | Zweck | Prinzip |
|----------|-------|---------|
| [admin-fördermittel-ci.yml](admin-fördermittel-ci.yml) | CI-Pipeline für Fördermittel-Verwaltung | Automatisierte Qualität |
| [60k-mesh-cluster-projekt.md](60k-mesh-cluster-projekt.md) | 60k-Projekt-Skizze: 3× Mesh-Cluster für kleine Kommune | Referenz-Implementierung |

### Übergeordnete Dokumente

| Dokument | Ort |
|----------|-----|
| Manifest | [`../MANIFEST.md`](../MANIFEST.md) |
| Verwaltungs-Prinzipien | [`../ADMIN-VALUES.md`](../ADMIN-VALUES.md) |
| ADR 0012 | [`../adr/0012-unix-philosophy-for-public-admin.md`](../adr/0012-unix-philosophy-for-public-admin.md) |

---

## Wie du diese Beispiele verwendest

### 1. CI-Pipeline adaptieren

```bash
# Kopiere die Pipeline für dein Fachverfahren
cp admin-fördermittel-ci.yml .github/workflows/bauantraege-ci.yml

# Passe die Jobs an deine Anwendungsfälle an
# - validate:prüfe-deine-geschäftsregeln
# - check-deadlines:prüfe-deine-fristen
```

### 2. Modulare Struktur übernehmen

```bash
# Erstelle die Verzeichnisstruktur für dein Fachverfahren
mkdir -p bauantraege/src/{adapters,scoring,deadlines,applications,api}
mkdir -p bauantraege/tests/{adapters,scoring,deadlines,applications}
mkdir -p bauantraege/docs/ADR

# Folge dem Pattern aus foerdermittel-module.md
```

### 3. Prinzipien anwenden

Nutze die Checkliste aus [`ADMIN-VALUES.md`](../ADMIN-VALUES.md):

- [ ] Ist es Open Source?
- [ ] Kann es On-Premise laufen?
- [ ] Gibt es API-Schnittstellen?
- [ ] Ist der Code testbar?
- [ ] Kann es durch ein anderes Modul ersetzt werden?

---

## Nächste Schritte

- [x] Beispiel für Fördermittel hinzufügen
- [ ] CI-Pipeline-Templates für verschiedene Use Cases
