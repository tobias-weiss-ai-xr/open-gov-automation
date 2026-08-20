# 60k-Pilot — Lokale KI für die Verwaltung (Beispiel: Bauanträge)

> Beispielhafte Ausgangslage: eine Mittelstadt (z. B. Gießen oder Marburg, ~90.000 Einwohner)
> oder eine kleine Kommune als Verwaltungseinheit.
> open-gov-automation Pilot — On-Premise, souverän, modular.

---

## Zielbild

Die Kommune betreibt die Verwaltungsmodule **lokal auf zwei gekoppelten Geräten** –
einer lokalen KI-Einheit, hochverfügbar und ohne Abhängigkeit von externen Anbietern:

```
┌──────────── 2× Lokale Einheit (Rathaus) ────────────┐
│                                                      │
│   Gerät A (Primary) ══200Gb/s══ Gerät B (Replica)    │
│        │                                             │
│        └── Lastverteiler ── Bürger / Verwaltung      │
│                                                      │
│   Module: Fördermittel · Bauanträge (vorausschauend) │
└──────────────────────────────────────────────────────┘
```

Keine unterbrechungsfreie Stromversorgung (USV), kein Netzwerkspeicher (NAS), keine
Cloud: Die zwei Geräte sind die gesamte Infrastruktur.

---

## Hardware: 2× ASUS Ascent GX10 — lokale, abhängigkeitsfreie Einheit

| Position | Spezifikation | Stückpreis | Summe |
|----------|---------------|-----------|-------|
| Gerät A (Primary) | ASUS Ascent GX10 — Nvidia GB10, 128 GB, 1 TB SSD | 3.999 € | 3.999 € |
| Gerät B (Replica) | ASUS Ascent GX10 — Nvidia GB10, 128 GB, 1 TB SSD | 3.999 € | 3.999 € |
| Verbindung | 2× 200 Gb/s Direktlink, gebondet (400 Gbps) | 150 € | 300 € |
| **Hardware gesamt** | | | **8.298 €** |

**Lokale Einheit ohne Abhängigkeiten:** Keine USV, kein NAS, keine externe Datenbank
oder Cloud. Die zwei Geräte sind über die 200Gb/s-Verbindung **gekoppelt** und bilden
eine logische Einheit mit **256 GB einheitlichem Speicher** – genug, um ein hinreichend
*intelligentes* Modell lokal zu betreiben, ohne US-Cloud. DSGVO-konform von Grund auf.

> **PoC bestätigt:** Zwei gekoppelte GB10-Geräte (DGX Spark) betreiben produktionserprobt
ein fronthauben-taugliches Modell lokal – ohne Cloud. Details: `examples/poc-dual-spark-cluster.md`
> (Quelle: graphwiz.ai, 2026).

---

## Aufwand & Budget (60.000 € gesamt)

| Posten | Beschreibung | Kosten |
|--------|-------------|--------|
| Hardware | 2× GX10 + 2× 200Gb/s-Kabel | 8.298 € |
| Expertise | Architektur, Einrichtung, CI/CD, Modul-Konfiguration, Bereitstellung | 45.000 € |
| Schulung des Ansprechpartners | 2 Workshops + Handbuch + gemeinsames Arbeiten (Befähigung zur Eigenwartung) | 6.702 € |
| **Gesamt** | | **60.000 €** |

**Grundsatz:** Kein Blackbox-Produkt mit Wartungsvertrag, sondern
*Expertise + Befähigung*. Die Kommune betreibt danach selbst — souverän, ohne laufende
Abhängigkeit. (Optionale Folge-Betreuung separat vereinbar.)

---

## Aufbau (2 Geräte)

```
Gerät A (GX10, Primary) ══200Gb/s══ Gerät B (GX10, Replica)
        │                        │
   Bürger / Verwaltung ← Lastverteiler (auf A)
```

Die zwei Geräte sind über die 200Gb/s-Verbindung **gekoppelt**: Sie bilden eine logische
Einheit mit 256 GB einheitlichem Speicher, auf der ein hinreichend *intelligentes* Modell
lokal läuft — ohne US-Cloud. Gleichzeitig dient B als ständige Kopie (Datenabgleich über
die Verbindung, **kein NAS nötig**): Fällt A aus, übernimmt B in unter 30 Sekunden.
Die zwei Geräte sind die gesamte Infrastruktur — keine externe Abhängigkeit.

**KI-Arbeit:** Das gekoppelte Modell (256 GB, keine Cloud) wertet Bauanträge aus und
erkennt Muster vorausschauend. Die schnelle Verbindung hält die Geräte als eine Einheit.

---

## Design-Prinzip: Vorausschauend statt reaktiv

Die lokale KI wird **nicht** als reagierender Prozessor gebaut, sondern als
*vorausschauende* Instanz: Sie erkennt Muster und Risiken **vor** dem Ereignis.

- **Bauanträge:** Die Planung wird gegen Bebauungsplan und Bauordnung geprüft, *bevor*
  der Bürger einreicht. Konflikte (Abstandsflächen, Höhen) werden proaktiv markiert –
  nicht erst bei Ablehnung. Weniger Rückläufe, kürzere Durchlaufzeiten.
- **Strategisch:** Statt Anträge nur zu *bearbeiten*, werden Chancen und Risiken
  *vorhergesagt* — genau die Lücke, die laut Marktüberblick bei vergleichbaren Piloten
  fehlt (strategische Intelligenz statt Prozess-Automation).

> Vorausschauend schlägt reaktiv — in Zeit, in Kosten, in Bürgerzufriedenheit.

---

## Baurecht im Detail (Beispiel Hessen)

Damit das Beispiel konkret wird, prüft die KI reale Vorschriften. Für Hessen sind das
unter anderem:

- **Abstandsflächen (§§ 5–9 Hessische Bauordnung):** Das geplante Gebäude muss einen
  bestimmten Abstand zur Grundstücksgrenze einhalten (etwa 0,4 × Gebäudehöhe, mindestens
  3 m). Die KI berechnet den nötigen Abstand aus der Skizze und markiert, wenn er
  unterschritten wird.
- **GRZ / GFZ (Bebauungsplan):** Wie viel Grundfläche bzw. Geschossfläche darf genutzt
  werden? Die KI prüft die Planung gegen die festgesetzten Zahlen.
- **Art der Nutzung (Baunutzungsverordnung):** Darf an diesem Ort eine Praxis, ein Laden
  oder eine Werkstatt sein? Die KI vergleicht die geplante Nutzung mit dem Bebauungsplan.
- **§ 34 / § 35 BauGB:** Liegt das Grundstück im Innenbereich (eingefügt in die Umgebung)
  oder im Außenbereich (strenger)? Die KI erkennt die Lage.

**Wichtig — Haftung:** Die KI liefert eine *Hilfe*, keine rechtsverbindliche Entscheidung.
Die Baugenehmigung erteilt die Behörde. Deshalb ist die KI als unterstützende Auskunft
ausgelegt, der Mensch entscheidet. (Datenschutz: Bauantragsdaten sind personenbezogen —
unsere DSGVO-Vorlagen greifen.)

---

## Module (im Budget enthalten)

| Modul | Anwendungsfall | CI-Pipeline |
|-------|---------------|-------------|
| Fördermittel *(optionales Modul)* | Anbindung (Kommunalportal, EU), KI-Bewertung, Fristen | `examples/admin-fördermittel-ci.yml` |
| Bauanträge *(Lead-Beispiel)* | **Vorausschauende** Baurecht-Prüfung (vorab) | (Vorlage) |

Jedes Modul: eigenes Containerverfahren, eigener Datenbereich,
eigene automatische Prüfung (Lint → Test → Validierung → Bereitstellung).

**Hinweis:** Bauanträge ist das Lead-Beispiel dieser Skizze; Fördermittel bleibt
optionales Zusatzmodul (nicht das quantitative Lead-Beispiel).

---

## Ablauf: Problemanalyse → gemeinsame Spec → GovOps-Loops

1. **Problemanalyse** — Gemeinsam mit dem Ansprechpartner klären wir den Ist-Zustand:
   Wo klemmt es (z. B. lange Bauantragszeiten, viele unvollständige Einreichungen)?
2. **Gemeinsame Spezifikation** — Berater und Kommune schreiben *zusammen* fest, was die
   KI prüfen soll (welche Paragraphen, welche Annahmen). Versioniert und nachvollziehbar.
3. **Agile GovOps-Loops** — Kurze Schleifen: Inkrement bauen → auf den 2 Geräten
   bereitstellen → mit echten (anonymisierten) Fällen testen → Feedback → nächste
   Schleife. Alle zwei Wochen ein lauffähiges Zwischenergebnis. So wird die KI
   schrittweise auf die örtlichen Regeln „geformt".

---

## Zeitplan (6 Monate)

| Phase | Monat | Inhalt |
|-------|-------|--------|
| 1 | M1 | Geräte, lokaler Verbund, automatische Prüfung (CI/CD) |
| 2 | M2 | Fördermittel-Modul (Anbindung + Bewertung) |
| 3 | M3 | Bauanträge-Modul (vorausschauende Prüfung) |
| 4 | M4 | KI auf örtliche Regeln formen (Expertise-Phase) |
| 5 | M5 | Compliance (VVT, TOMs, DSFA), Schulung |
| 6 | M6 | Pilotbetrieb, Go-Live, Dokumentation |

---

## Erfolgskriterien

| Metrik | Ziel |
|--------|------|
| Verfügbarkeit | ≥ 99,9 % (2 Geräte) |
| Bearbeitungszeit | −50 % ggü. Papier |
| Manuelle Fehler | 0 (durch automatische Validierung) |
| Hersteller-Zwang | Kein (Open Source, lokal) |
| DSGVO | Konform (VVT/TOMs/DSFA vorhanden) |

---

## Wiederverwendbarkeit

Diese Skizze ist eine **Vorlage**. Andere Kommunen kopieren:
- `examples/60k-mesh-cluster-projekt.md` → eigene Variante
- `compliance/*` → angepasste VVT/TOMs/DSFA
- `examples/admin-fördermittel-ci.yml` → eigene Pipeline

**Unix-Prinzip:** Einmal gebaut, oft kopiert. **Souveränität:** Daten bleiben in der Kommune.
