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

## Hardware: 3× Mesh-Knoten

| Position | Spezifikation | Stückpreis | Summe |
|----------|---------------|-----------|-------|
| Knoten A (Primary) | Mini-PC (8C/16GB/512GB NVMe) + WireGuard | 850 € | 850 € |
| Knoten B (Replica) | Mini-PC (8C/16GB/512GB NVMe) | 850 € | 850 € |
| Knoten C (Edge/LB) | Mini-PC (4C/8GB/256GB) + Reverse Proxy | 650 € | 650 € |
| Netzwerk | Managed Switch + USV (1500VA) | 1.200 € | 1.200 € |
| NAS (Backup) | 2-Bay, 2×4TB RAID1 | 600 € | 600 € |
| Montage/Schrank | 19" Wandgehäuse, Kabel | 450 € | 450 € |
| **Hardware gesamt** | | | **4.600 €** |

---

## Software-Budget (60k Gesamt)

| Posten | Beschreibung | Kosten |
|--------|-------------|--------|
| Hardware (s.o.) | 3× Knoten + Infra | 4.600 € |
| Setup & Integration | Cluster-Aufbau, CI/CD, Monitoring | 18.000 € |
| Modul-Implementierung | Fördermittel + Bauanträge + Bürgerportal | 22.000 € |
| Schulung & Handbuch | 2 Tage Admin + Bürger-Support-Doku | 6.000 € |
| Compliance | VVT, TOMs, DSFA (siehe `/compliance`) | 4.000 € |
| Wartung Jahr 1 | Hotline, Updates, 2x Vor-Ort | 5.400 € |
| **Gesamt** | | **60.000 €** |

---

## 3× Mesh-Topologie (Detail)

```
Knoten A (10.0.0.1)  ←→  Knoten B (10.0.0.2)
        ↕                      ↕
Knoten C (10.0.0.3)  ←→  Load Balancer (10.0.0.254)

WireGuard-Peers (je Knoten 2 Tunnel):
  A↔B, B↔C, C↔A  → vollvermascht, kein SPOF
```

**Failover:** Bei Knoten-Ausfall übernimmt B innerhalb < 30s.
Daten liegen repliziert auf A+B (Postgres Streaming Replication).
Knoten C = Reverse Proxy + Cache (entlastet A/B).

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
