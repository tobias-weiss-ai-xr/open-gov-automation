# Verwaltung 2.0 — Minimal Stoic Unix Principles

> "Weniger, aber wesentlicher. Transparent. Resilient."

## Die vier Grundprinzipien

### 1. **Einfachheit** — Do One Thing Well

Jedes Fachverfahren macht eine Sache und macht sie gut:

```bash
# Statt monolithischem System:
verwaltungs-suite.exe  # 500 Funktionen, niemand versteht es

# Modulare Verwaltung:
buergerportal    # Bürgerkommunikation
foerdermittel    # Fördermittel-Management
bauantraege      # Baugenehmigungen
einwohneramt     # Meldewesen
```

**Vorteil:** Jedes Modul ist verständlich, testbar, ersetzbar.

---

### 2. **Transparenz** — Text über Binär

Alles ist textbasiert und nachvollziehbar:

| Statt | Durch |
|-------|-------|
| Proprietäre Datenbank | JSON/API |
| Blackbox-Algorithmus | Open Source Code |
| Manuelle Genehmigung | Git Pull Request |
| Undurchsichtige Logdatei | CI-Pipeline-Logs |

**Vorteil:** Jede Entscheidung ist auditierbar, jede Änderung nachvollziehbar.

---

### 3. **Resilienz** — Automatisierte Qualität

CI-Pipelines als moderne Qualitätskontrolle:

```yaml
# .github/workflows/foerdermittel-ci.yml
jobs:
  lint:        # Code-Qualität
  test:        # Automatisierte Tests
  security:    # Sicherheitsaudit
  deploy:      # Nur wenn alles grün
```

**Vorteil:** Fehler werden vor dem Produktivgang erkannt. Keine manuellen Fehler.

---

### 4. **Souveränität** — On-Premise First

Datenhoheit bleibt bei der Kommune:

```bash
# Deployment in eigener Infrastruktur
docker compose -f docker-compose.admin.yml up -d

# Keine Cloud-Abhängigkeit
# Keine US-Server
# Keine Lizenzkosten pro Nutzer
```

**Vorteil:** Unabhängigkeit von Vendor-Lock-in. Datenschutz nach DSGVO.

---

## Stoische Tugenden in der Technik

| Tugend | Technische Umsetzung |
|--------|---------------------|
| **Weisheit** | Einfache Systeme statt komplexer Blackboxen |
| **Mut** | Open Source statt sicherem Vendor-Lock-in |
| **Gerechtigkeit** | Transparente Algorithmen, keine Diskriminierung |
| **Mäßigung** | Minimaler Ressourcenbedarf (Alpine, ~250MB Images) |

---

## Konkrete Anwendung: Fördermittel-Management

### Problem (aktuell)
- Anträge per Post/E-Mail
- Manuelle Prüfung
- Keine Fristen-Überwachung
- Keine Nachvollziehbarkeit

### Lösung (Unix-Prinzipien)

```
foerdermittel/
├── .github/workflows/
│   └── ci.yml              # Automatisierte Tests
├── src/
│   ├── adapters/           # Datenquellen (Kommunalportal, EU)
│   ├── scoring/            # AI-Bewertung (transparent)
│   └── deadlines/          # Fristen-Überwachung
├── tests/                  # 100% Testabdeckung
└── docs/                   # Jede Entscheidung dokumentiert
```

### CI-Pipeline für Fördermittel

```yaml
name: Fördermittel CI

on: [push, pull_request]

jobs:
  validate:
    # 1. Prüfe: Sind alle Anträge validiert?
    run: npm run validate:applications

  check-deadlines:
    # 2. Prüfe: Sind Fristen eingehalten?
    run: npm run check:deadlines

  security-audit:
    # 3. Prüfe: Keine Sicherheitslücken
    run: npm audit --audit-level=critical

  deploy:
    # 4. Nur wenn alles grün
    needs: [validate, check-deadlines, security-audit]
```

**Ergebnis:**
- 0 manuelle Fehler
- 100% Nachvollziehbarkeit
- Fristen werden automatisch überwacht
- Jede Änderung ist getestet

---

## Migration von Bestehendem

### Phase 1: CI einführen (4 Wochen)
- Git-Repository für jedes Fachverfahren
- CI-Pipeline mit Lint + Tests
- Health Checks für alle Systeme

### Phase 2: Modularisierung (8 Wochen)
- Monolith in Module aufteilen
- API-Schnittstellen definieren
- Ersetzbare Komponenten

### Phase 3: Automatisierung (12 Wochen)
- Alle manuellen Prozesse automatisieren
- CI/CD für alle Module
- Monitoring + Alerting

---

## Erfolgskriterien

| Metrik | Ziel |
|--------|------|
| Testabdeckung | ≥ 90% |
| CI-Duration | < 10 Minuten |
| Manuelle Schritte | 0 |
| Downtime | < 0.1% |
| Vendor Lock-in | 0 (alle Open Source) |

---

## Referenzen

- [CI-Pipeline](.github/workflows/ci.yml)
- [Deployment Guide](DEPLOYMENT.md)
- [ADR-Log](adr/)
- [Docker Compose](docker-compose.prod.yml)

---

## Prinzipien anwenden — Checkliste

Bevor du neue Software einführst:

- [ ] Ist es Open Source?
- [ ] Kann es On-Premise laufen?
- [ ] Gibt es API-Schnittstellen?
- [ ] Ist der Code testbar?
- [ ] Kann es durch ein anderes Modul ersetzt werden?
- [ ] Sind alle Entscheidungen nachvollziehbar?
- [ ] Gibt es CI/CD-Automatisierung?

**Wenn NEIN zu einer Frage: Nicht einführen.**
