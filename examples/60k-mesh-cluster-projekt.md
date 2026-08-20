# 60k-Projekt-Skizze — 3× Mesh-Cluster für kleine Kommune

> Exemplarisch: Gemeinde Musterstadt (5.200 Einwohner)
> open-gov-automation Pilot — On-Premise, Souverän, Modular

---

## Zielbild

Eine kleine Kommune betreibt drei Verwaltungs-Module lokal, hochverfügbar
und ohne Vendor Lock-in:

```
┌─────────────────── 3× Mesh-Cluster (Rathaus) ───────────────────┐
│                                                                  │
│   Knoten A ───┐                                                 │
│               ├── WireGuard-Mesh ─── Load Balancer ─── Bürger   │
│   Knoten B ───┤                              │                   │
│               │                              ├── Fördermittel    │
│   Knoten C ───┘                              ├── Bauanträge      │
│                                              └── Bürgerportal    │
│                                                                  │
│   Backups: lokaler NAS (täglich, verschlüsselt)                  │
└──────────────────────────────────────────────────────────────────┘
```

---

## Hardware: 3× ASUS Ascent GX10 (GB10)

| Position | Spezifikation | Stückpreis | Summe |
|----------|---------------|-----------|-------|
| Knoten A | ASUS Ascent GX10 — Nvidia GB10 Blackwell Superchip, 128GB, 1TB SSD, DOS | 3.999 € | 3.999 € |
| Knoten B | ASUS Ascent GX10 — Nvidia GB10 Blackwell Superchip, 128GB, 1TB SSD, DOS | 3.999 € | 3.999 € |
| Knoten C | ASUS Ascent GX10 — Nvidia GB10 Blackwell Superchip, 128GB, 1TB SSD, DOS | 3.999 € | 3.999 € |
| Interconnect | 200 Gb/s Kabel (Knoten-verbund) | 150 € | 450 € |
| NAS (Backup) | 2-Bay, 2×4TB RAID1, verschlüsselt | 600 € | 600 € |
| USV + Schrank | 19" Wandgehäuse, USV 1500VA, Montage | 450 € | 450 € |
| **Hardware gesamt** | | | **13.497 €** |

> **AI-Souveränität:** Jeder Knoten hat 128 GB einheitlichen Speicher →
> lokale LLM-Inferenz (Fördermittel-Scoring, Dokumenten-Extraktion) ohne Cloud.
> Kein Datentransfer zu US-Anbietern. DSGVO-by-Design.

---

## Software-Budget (60k Gesamt)

| Posten | Beschreibung | Kosten |
|--------|-------------|--------|
| Hardware (s.o.) | 3× GX10 + 200Gb/s-Kabel + Infra | 13.497 € |
| Setup & Integration | Cluster-Aufbau, Mesh-Netz, CI/CD, Monitoring | 14.000 € |
| Modul-Implementierung | Fördermittel + Bauanträge + Bürgerportal | 18.000 € |
| Schulung & Handbuch | 2 Tage Admin + Bürger-Support-Doku | 5.000 € |
| Compliance | VVT, TOMs, DSFA (siehe `/compliance`) | 3.500 € |
| Wartung Jahr 1 | Hotline, Updates, 2× Vor-Ort | 6.003 € |
| **Gesamt** | | **60.000 €** |

---

## 3× Mesh-Topologie (Detail)

```
Knoten A (GX10) ──200Gb/s── Knoten B (GX10)
     ↕                        ↕
Knoten C (GX10) ──200Gb/s── Load Balancer (10.0.0.254)

Alle Knoten identisch (GB10, 128GB) → vollvermascht, kein SPOF.
Interconnect: 200 Gb/s Direktverbindung (Cable, 150 €/Stk).
Control-Plane: WireGuard-Mesh für verschlüsselte Orchestrierung.
```

**Failover:** Bei Knoten-Ausfall übernimmt B innerhalb < 30s.
Daten liegen repliziert auf A+B (Postgres Streaming Replication).
Jeder Knoten kann alle 3 Module allein betreiben (Capacity Headroom: ~384 GB gesamt).

**AI-Last:** Fördermittel-Scoring läuft lokal auf einem Knoten (GB10,
kein Cloud). 200Gb/s-Link entlastet Replikation/Daten-Shift zwischen Knoten.

---

## Module (im Budget enthalten)

| Modul | Fachverfahren | CI-Pipeline |
|-------|---------------|-------------|
| Fördermittel | Adapters (Kommunalportal, EU), AI-Scoring, Fristen | `examples/admin-fördermittel-ci.yml` |
| Bauanträge | Baurecht-Validierung, Genehmigungsworkflow | (Template) |
| Bürgerportal | Anmeldung, Umzug, Pass, OIDC/ELSTER | (Template) |

Jedes Modul: eigenes Docker-Image, eigene DB-Schema-Namespace,
eigene CI-Pipeline (Lint → Test → Validate → Deploy).

---

## Zeitplan (6 Monate)

| Phase | Monat | Inhalt |
|-------|-------|--------|
| 1 | M1 | Cluster-Hardware, Mesh-Setup, CI/CD-Grundgerüst |
| 2 | M2 | Fördermittel-Modul (Adapters + Scoring) |
| 3 | M3 | Bauanträge-Modul (Validierung + Workflow) |
| 4 | M4 | Bürgerportal (Anmeldung + Auth) |
| 5 | M5 | Compliance (VVT, TOMs, DSFA), Schulung |
| 6 | M6 | Pilotbetrieb, Go-Live, Dokumentation |

---

## Erfolgskriterien

| Metrik | Ziel |
|--------|------|
| Verfügbarkeit | ≥ 99.9% (3× Mesh) |
| Bearbeitungszeit | −50% vs. Papier |
| Manuelle Fehler | 0 (durch CI-Validierung) |
| Vendor Lock-in | Kein (Open Source, On-Premise) |
| DSGVO | Konform (VVT/TOMs/DSFA vorhanden) |
| Kosten pro Bürger | ~11,50 € (60k / 5.200) |

---

## Wiederverwendbarkeit

Diese Skizze ist ein **Template**. Andere Kommunen kopieren:
- `examples/60k-mesh-cluster-projekt.md` → eigene Variante
- `compliance/*` → angepasste VVT/TOMs/DSFA
- `examples/admin-fördermittel-ci.yml` → eigene CI-Pipeline

**Unix-Prinzip:** Einmal gebaut, unendlich oft kopiert.
**Souveränität:** Daten bleiben in der Kommune.
**Transparenz:** Jeder Euro nachvollziehbar.
