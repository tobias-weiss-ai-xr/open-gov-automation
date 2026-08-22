# Dezentraler Betrieb der KI-Einheit & Hebelwirkung

> Varianten der Aufstellung des Dual-Clusters (2× GX10) — von der lokalen
> Einheit bis zum Verbands-Betrieb. Und warum Automatisierung der öffentlichen
> Hand einen besonders großen Hebel bietet.

---

## Kurzfassung

Die zwei GX10-Geräte sind die **gesamte Infrastruktur** — wo sie stehen, ist
eine Frage der Betriebsstrategie, nicht der Technik:

| Variante | Wo läuft die Einheit? | Wofür geeignet |
|----------|----------------------|----------------|
| **A · Lokal** | Beide Geräte im Rathaus (200 Gb/s Direktlink) | Pilot, schneller Start, volle Kontrolle |
| **B · Stadtweit dezentral** | A im Rathaus, B in einem zweiten städtischen Gebäude | Ausfallsicherheit gegen Störungen im Gebäude |
| **C · Verbands-Betrieb** | Einheit beim Landkreis / Zweckverband, mehrere Kommunen | Größte Effizienz & Hebelwirkung |
| **D · Dienstleister-gehostet** | Geräte beim IT-Dienstleister | Nur Ausnahme (Auftragsverarbeitung) |

**Reihenfolge:** Start mit A → Ausbau zu B → Skalierung zu C. Jede Stufe baut
auf der vorherigen auf, ohne Umbau der Module.

---

## Warum die Aufstellung mehr ist als ein Detail

Das Prinzip bleibt überall gleich: **2 Geräte = gesamte Infrastruktur**, keine
USV, kein NAS, keine Cloud, keine laufenden Lizenzen. Aber die *räumliche*
Verteilung entscheidet über drei Eigenschaften:

1. **Resilienz** — Was passiert bei Brand, Wasser, Stromausfall oder Einbruch?
   Ein einziger Raum ist ein single point of failure in *Raumgröße*.
2. **Effizienz** — Kann eine Einheit mehrere Kommunen bedienen? Dann sinken die
   Kosten je Kommune stark (siehe Kostenmodell).
3. **Hebel** — Ein gemeinsamer Betrieb im Verband vervielfacht die Wirkung von
   Expertise, Beschaffung und Automatisierung.

---

## Variante A · Lokal (Baseline)

```
┌──────────── Rathaus (1 Raum) ────────────┐
│                                          │
│   Gerät A (Primary) ══200Gb/s══ Gerät B  │
│        │                                 │
│        └── Terminals: Verwaltung / Bürger │
└──────────────────────────────────────────┘
```

- Status quo aus der [Projektskizze](60k-mesh-cluster-projekt.md).
- Schnellste Verbindung (200 Gb/s Direktlink, Replikation < 2 s), einfachster
  Betrieb, kein zusätzliches Netz nötig.
- Grenze: Ein Gebäude — ein Stromanschluss — ein Risikobereich.

## Variante B · Stadtweit dezentral

```
  Rathaus                    Zweites städt. Gebäude (z. B. Feuerwache)
+------------------+         +------------------+
| Gerät A Primary  |==VPN==> | Gerät B Replica  |
| (Rechenbetrieb)  |   <==   | (Reserve)        |
+------------------+         +------------------+
      städtisches Glasfaser-/VPN-Netz · verschlüsselt · DSGVO-konform
```

- **Resilienz:** Zwei Gebäude, zwei Stromkreise, getrennte Brandabschnitte.
  Fällt das Rathaus aus, übernimmt Gerät B — Bürger spüren nichts (RTO < 60 s).
- **Verbindung:** Statt des 200-Gb/s-Direktlinks eine kryptographisch gesicherte
  Verbindung über das vorhandene städtische Netz (WireGuard/IPsec, TLS 1.3).
  Replikation bleibt asynchron, RPO wenige Minuten.
- **Grenze:** Datenverarbeitung weiterhin ausschließlich im Stadtgebiet.

## Variante C · Verbands-/Landkreis-Betrieb (der Hebel)

```
   Landkreis / kommunaler Zweckverband      beigetretene Kommunen
   +--------------------+                  ┌─────────────────────────┐
   │ Gerät A (Primary)  │                  │ Kommune 1 (Mandant)     │
   │ Gerät B (Replica)  │── verschlüsselt ─│ Kommune 2 (Mandant)     │
   │ + Mandanten-Trennung                  │ Kommune 3 … (Mandant)   │
   +--------------------+                  └─────────────────────────┘
   eine Einheit · N Kommunen · geteilte Kosten
```

- **Idee:** Der Landkreis betreibt eine dual-cluster Einheit und stellt sie
  mehreren Kommunen als Dienst zur Verfügung. Eine Anschaffung, eine Expertise,
  N Nutznießerinnen.
- **Technisch:** Mandanten-Isolation (getrennte Verzeichnisse, Protokolle,
  Rechte je Kommune) — jede Kommune sieht nur ihre eigenen Daten.
- **Rechtlich:** Betrieb als Auftragsverarbeitung (AVV zwischen Landkreis und
  Kommunen) oder Form der kommunalen Zusammenarbeit nach Landesrecht.
  Dokumentation: [TOMs](../compliance/toms.md), [VVT](../compliance/vvt.md),
  [DSFA](../compliance/dsfa.md).
- **Grenze:** Kommunikation über Verwaltungsnetz (PKI/VPN), kein Internet-Zwang.

## Variante D · Dienstleister-gehostet (Ausnahme)

- Geräte stehen beim IT-Dienstleister, Betrieb gegen Entgelt.
- Nur sinnvoll, wenn die Kommune selbst keine geeigneten Räume hat.
- Erfordert zwingend Auftragsverarbeitungsvertrag (ADV) und Nachweis der
  Datenverarbeitung im Geltungsbereich der DSGVO.
- Widerspricht teilweise dem Ziel „keine laufende Abhängigkeit" — als
  Übergangslösung denkbar, nicht als Dauerzustand.

---

## Verbindung & Replikation über Standorte

| Kenngröße | A · Lokal | B · Stadtweit | C · Verband |
|-----------|-----------|---------------|-------------|
| Verbindung | 200 Gb/s Direktlink (gebondet) | Stadtnetz / VPN | Verwaltungsnetz / VPN |
| Latenz | 0,3 ms | 1–5 ms | 5–20 ms |
| Replikation | async, RPO < 2 s | async, RPO ~ 1–5 min | async, RPO ~ 5–15 min |
| Failover | < 30 s | < 60 s | < 2 min |
| Verschlüsselung | intern | WireGuard/IPsec + TLS | WireGuard/IPsec + PKI |

> Die Prüfabläufe selbst sind **stateless**: Ein laufender Bauantrag wird als
> Aufgabe neu zugewiesen, nicht als Session gehalten. Deshalb übersteht auch
> eine getrennte Aufstellung jeden Ausfall ohne Datenverlust.

---

## Kostenmodell: Effizienz durch Automatisierung

Automatisierung verschiebt Kosten von **laufender Bearbeitung** (Personal,
Zeit, Rückläufe) zu **einer einmaligen Investition**. Das rechnet sich umso
schneller, je mehr Anträge durchlaufen.

**Einzelbetrieb (Variante A) — eine Kommune:**

| Posten | Betrag |
|--------|--------|
| Hardware (2× GX10 + Verbindung) | 8.298 € |
| Expertise (Architektur, Aufbau, CI/CD, Module) | 45.000 € |
| Schulung der KI-Operatoren | 6.702 € |
| **Summe** | **60.000 €** |
| **Amortisation** | **< 12 Monate** (150+ Anträge/Jahr, Break-even ~80/Jahr) |

**Verbands-Betrieb (Variante C) — Musterrechnung, 5 Kommunen:**

| Posten | Betrag | Anmerkung |
|--------|--------|-----------|
| Hardware (1 dual cluster) | 8.298 € | eine Anschaffung statt fünf |
| Expertise (einmalig, wiederverwendet) | 45.000 € | identische Module, N Kommunen |
| Gemeinsame Schulung & Betrieb | 11.702 € | Pool statt Einzelbetreuung |
| **Summe** | **65.000 €** | |
| **je Kommune** | **~13.000 €** | statt 60.000 € → **−78 %** |
| 6. Kommune tritt bei | +3.000 € | → je Kommune ~11.400 € |

> **Musterrechnung** auf Basis der Pilotannahmen. Die tatsächliche Kalkulation
> hängt von Kommunenzahl, Antragsvolumen und bestehender IT ab — wir rechnen
> sie im Projekt individuell und transparent vor.

Weil die Software offen ist (GPL-3.0) und die Module einmal gebaut werden,
ist der Grenzbeitrag einer weiteren Kommune klein — genau hier entsteht die
**Effizienz durch Automatisierung**: Die Maschine macht die repetitive Prüfung,
der Mensch entscheidet, und die Kosten pro zusätzlichem Antrag sinken gegen null.

---

## Hebel der öffentlichen Hand

Die öffentliche Verwaltung hat strukturell **mehr Hebelwirkung** als ein
einzelnes Unternehmen:

| Hebel | Was er wirkt |
|-------|--------------|
| **Beschaffungshebel** | Eine Anschaffung für mehrere Kommunen — ein Vertrag, bessere Konditionen, weniger Verwaltung. |
| **Kooperationshebel** | Kommunale Zusammenarbeit (Zweckverband/Landkreis) teilt Expertise, KI-Operatoren und Wartung. |
| **Automatisierungshebel** | Einmal gebaut, mehrfach genutzt: offene Module, keine Lizenz je Kommune, Grenzkosten → null. |
| **Souveränitätshebel** | Offener Stack, kein Vendor-Lock: Die Kommune behält die Entscheidung — dauerhaft. |
| **Skalenhebel** | Mehr Anträge ⇒ kürzere Amortisation; ein gemeinsamer Betrieb nutzt jede Automatisierung N-fach. |

Das bedeutet: **Der größte Effizienzgewinn entsteht nicht im Einzelbetrieb
einer Kommune, sondern in der gemeinsamen Nutzung** — dezentral betrieben,
aber zentral wirksam.

---

## Datenschutz & Verantwortung

- In allen Varianten bleibt die Verarbeitung **im Verwaltungsgebiet** — keine
  US-Cloud, keine Datenabflüsse. DSGVO-by-Design.
- Variante C/D erfordern klare Rollen: **AVV** (Auftragsverarbeitung) bzw.
  Regelung nach Landesrecht, ergänzt durch Verzeichnis von Verarbeitungstätigkeiten
  und TOMs.
- Die KI liefert unterstützende Auskunft; **die Behörde entscheidet** (Mensch
  in der Schleife) — unverändert in jeder Variante.

---

## Empfehlung: Aufbau-Reihenfolge

1. **Start A** — Pilot, 6 Monate, 60.000 €, schnell und kontrolliert.
2. **Ausbau B** — zweiter Standort sobald verfügbar; Resilienz ohne Umbau.
3. **Skalierung C** — Verbands-Betrieb für mehrere Kommunen; maximale Effizienz
   und Hebelwirkung durch gemeinsame Nutzung.

---

## Weitere Unterlagen

- [Projektskizze (60k-Pilot)](60k-mesh-cluster-projekt.md)
- [Wirtschaftlichkeitsanalyse](wirtschaftlichkeit.md)
- [Lösungsvergleich](loesungsvergleich.md)
- [Live-Demo (Terminal-Simulation)](../demo.html)
- [Startseite](../index.html)
