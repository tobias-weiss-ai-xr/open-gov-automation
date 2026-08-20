# Nutzen- & ROI-Analyse — Use Cases (kritisch)

> Fokus: 60k-Pilot für ~10.000 EW Gemeinde (Mitte der Zielgröße 5–20k)
> Methode: Illustrative Schätzung, **vor Vertrieb zu verifizieren** (0 Kunden, 0 Messwerte)
> Prämisse: Reine Kostenersparnis reicht nicht — Business-Case = Portfolio-Skalierung

---

## 1. Fördermittel — ZWEI unterschiedliche Use Cases (inkonsistent!)

| Variante | Rolle Gemeinde | Schmerz | Benefit |
|----------|----------------|--------|---------|
| **A: Antrags-BEARBEITUNG** | Prozessor (prüft Bürger/Vereine) | Manueller Aufwand | Gering (wenige Anträge/Jahr) |
| **B: Förder-FINDING** | Empfänger (findet Gelder für sich) | Verpasste Fördermittel | Hoch (wenn Geld liegen blieb) |

**Problem:** `foerdermittel-module.md` + CI spec'en Variante A (Bearbeitung).
Der Pitch an Kommunen ("wir finden Fördergelder, die Sie verpassen") ist Variante B.
→ **Beides wird gemischt.** Klärung nötig, bevor wir messen.

### Variante B (Finding) — einzige mit starker ROI
- Mittelhessen-Gemeinde ~10k EW: Fördervolumen ~200k–1M €/Jahr (Klima, Infra, EU/Vogelsberg)
- "Verpasst" durch Unkenntnis: schätzungsweise 5–15% = **10k–150k €/Jahr**
- **ROI:** Bei 60k Invest + ~6k €/Jahr Wartung → Payback **< 1 Jahr** (im Bestfall)
- **Aber:** Benötigt Nachweis, dass die Gemeinde tatsächlich Geld liegen lässt.
  Ohne Evidenz = Schwachstelle (siehe Memory: Value-Prop 44% weak).

### Variante A (Bearbeitung) — schwache ROI für Kleinstadt
- ~20–100 Anträge/Jahr, 2–4h Bearbeitung = 100–600h/Jahr
- Automatisierung spart ~30% = **30–180h/Jahr ≈ 1k–6k €/Jahr**
- Payback: **> 10 Jahre** → rechnet sich nicht allein.

---

## 2. Bauanträge — hohe Haftung, niedrige Direkt-ROI

| Aspekt | Bewertung |
|--------|-----------|
| Schmerz | Lange Bearbeitung, manuelle Baurecht-Prüfung |
| Benefit (€) | Kaum direkt — Gebühren sind fix, keine Extra-Einnahme |
| Nutzen | Bürger-Zufriedenheit, geringere Fristen-Risiken |
| **Haftung** | HOCH — falsche automatische Baurecht-Prüfung = commune haftet |
| Realität | Nur *assistiv* (Vorab-Check, Flag) zulässig, nicht autonom |

**Urteil:** Service-Qualität, kein €-ROI. Für 10k-EW-Gemeinde schwer 60k zu rechtfertigen.
Besser als Zusatz-Modul, nicht als Lead.

---

## 3. Bürgerportal — commoditized, überlappt mit openDesk

| Aspekt | Bewertung |
|--------|-----------|
| Schmerz | Papier, keine Status-Tracking, viele Ämter |
| Benefit (€) | 0,5–4k €/Jahr (Selbstbedienung spart Telefon/Schalter) |
| **Konkurrenz** | openDesk, viele SaaS — Funktions-Overlap hoch |
| USP | Open Source + souverän (echt, aber funktional austauschbar) |

**Urteil:** Wichtig für Bürger-Akzeptanz, aber schwächstes ROI.
Nicht als Alleinstellungsmerkmal verkaufen.

---

## 4. Cross-Modul ROI — 60k-Pilot

### Szenario A — Kleinstadt (~10k EW, Beispiel aus Skizze)
| Szenario | Direkte Ersparnis/Jahr | Payback (60k) | Fazit |
|----------|------------------------|---------------|-------|
| Nur A (Bearbeitung) + Bau + Bürger | 2k–10k € | > 6 Jahre | ❌ rechnet sich nicht |
| **B (Finding) führt** | 10k–150k € | < 1–5 Jahre | ✅ nur mit Finding |
| + Portfolio-Skalierung | Kosten/Commune sinken | Pilot wird Vorlage | ✅ Business-Case |

### Szenario B — Mittelstadt (Gießen ~90k / Marburg ~76k, als Verwaltungseinheit)
| Modul | Volumen/Jahr | Ersparnis/Nutzen | Payback |
|------|--------------|------------------|---------|
| Förder-Finding (B) | mehrere Mio € Förderung | 5% verpasst = **100k–500k €/Jahr** | **< 1 Jahr** ✅ |
| Bauanträge | 500–1.500 Anträge/Jahr | Assist spart **50k–200k €/Jahr** (Personal) | < 1 Jahr ✅ |
| Bürgerportal | hohes Kontaktvolumen | **20k–80k €/Jahr** (Schalter/Telefon) | 1–2 Jahre ✅ |

**Kern-Erkenntnis (korrigiert):** Für EINE **Kleinstadt** rechnet sich das 60k-Paket
kaum auf reine Ersparnis. Für eine **Mittelstadt (Gießen/Marburg)** rechnet es sich
bereits im Einzel-Pilot — das «Single-Commune-ROI schwach»-Problem entfällt.
Der Business-Case steht also sowohl (a) als Stadt-Pilot als auch (b) als
Portfolio-Skalierung auf Kleinstädte.

---

## 5. Kritische Lücken (muss vor Vertrieb geklärt sein)

1. **Fördermittel A vs B** — Use Case definieren, sonst widersprüchliche Pitch.
2. **0 Evidenz** — keine Kunden, keine gemessenen Ersparnisse. Finding-ROI ist Hypothese.
3. **Haftung Bauanträge** — autonome Prüfung rechtlich riskant; nur assistiv.
4. **Bürgerportal-Overlap** — offenDesk bereits vorhanden; Differenzierung nur "souverän".
5. **Vergaberecht (Stadt)** — 60k liegt unter EU-Schwellenwert → «freihändige Vergabe»
   möglich, aber Stadt hat mehr Stakeholder + evtl. Bestands-SaaS (Integration prüfen).
6. **Scope** — Stadt-Pilot ggf. als einzelne Verwaltungseinheit (Amtsbereich), nicht Gesamtstadt.

---

## 6. Empfehlung

**Lead-Pitch:** *Fördermittel-Finding (B)* — konkreter Painkiller, stärkste ROI-Story.
**Pilot-Träger:** **Stadt Gießen oder Marburg** (hohe ROI, Uni-Orbit) — oder Kleinstadt
(Lich/Kirchhain/Schotten) mit Portfolio-Skalierung als Business-Case.
**Vor dem Anschreiben:** 1–2 Referenz-Kommunen mit echten Förder-Daten (Evidence!) gewinnen.

---

## Unix-Prinzip angewendet

- **Ehrlich:** Schwachstellen benannt statt geschönt
- **Messbar:** Zahlen als Range, als "illustrativ" markiert
- **Do one thing:** Diese Datei = nur Nutzenprüfung
