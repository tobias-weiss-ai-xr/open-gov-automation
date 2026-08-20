# Monte Carlo Ergebnis — Bauanträge ROI (Bayesian)

> Modul: **Bauanträge** (Stadt Gießen ~90k EW). Fördermittel **ausgeschlossen** (per Instruction).
> Methode: Bayesian Monte Carlo, N=50.000, 5J-Horizont, 5% Diskont. Reine Stdlib.
> Script: `bauantraege_monte_carlo.py` (reproduzierbar, Seed=4242)

---

## Priors (Unsicherheitsannahmen)

| Parameter | Prior | Begründung |
|----------|-------|------------|
| Bauanträge/Jahr | LogNormal(μ=ln 1000, σ=0.25) | ~1000 median, Unsicherheit ± |
| Bearbeitungszeit (h/Antrag) | Normal(3,0; 0,5) | 1,5–5h clipped |
| Zeitersparnis (assistiv) | Normal(0,30; 0,06) | 10–50% clipped |
| Personalkosten (€/h) | Normal(42; 4) | 30–55€ clipped (Tarif) |
| Implementierung | Normal(60k; 5k) | 50–70k clipped |
| Wartung/Jahr | Normal(6k; 800) | 4–9k clipped |

---

## Ergebnisse

| Metrik | Szenario 1 (Prior) | Szenario 2 (Posterior) |
|--------|-------------------|------------------------|
| Erwarteter NPV (5J) | 82.762 € | 91.343 € |
| Median NPV | 72.842 € | 82.575 € |
| 5% Perzentil | −4.467 € | +9.811 € |
| 95% Perzentil | 202.808 € | 201.407 € |
| **P(NPV > 0)** | **93,7 %** | **97,4 %** |
| Erw. Payback | 2,71 J | 2,60 J |
| P(Payback ≤ 3J) | 75,7 % | 83,6 % |

**Bayesian Update (Szenario 2):** Saving-Prior N(0.30, 0.06) → Posterior
N(0.315, 0.030) nach hypothetischem Pilot (n=150, x̄=0.32). Verteilung verschiebt
sich nach oben und wird schmaler (Unsicherheit sinkt).

---

## Interpretation

1. **Rechnet sich:** 94% Wahrscheinlichkeit positiver NPV, Median ~73k € bei 60k Invest.
2. **Payback akzeptabel:** ~2,7 Jahre (im ungünstigen Fall bis 5J, aber P>0 bei 94%).
3. **Robust:** Selbst 5%-Perzentil nahe Break-even; nach Pilot-Evidenz durchweg positiv.
4. **Bayesian:** Mehr Pilot-Daten → schmalere Verteilung → sicherere Entscheidung.

---

## Kritische Einwände (ehrlich)

- **Assistiv zwingend:** Autonome Baurecht-Prüfung = Haftung. Nur Vorab-Check zulässig.
  Die 30%-Ersparnis setzen *unterstützte* Bearbeitung voraus, keine Vollautomatik.
- **Nur 1 Modul:** 60k deckt alle 3 Module. Bauanträge trägt sich allein;
  Fördermittel ist Zusatz (Service), nicht zwingend €-ROI.
- **Prior = Hypothese:** Keine echten Messwerte. Pilot muss Saving-Fraction validieren.
- **Stadt-Skala nötig:** Bei Kleinstadt (10k) fällt Volumen → ROI schwächer (siehe ROI-Analyse).

---

## Fazit

Bauanträge an Mittelstadt-Skala ist ein **tragfähiges, evidenz-updatebares ROI-Beispiel** —
besser als Fördermittel (kein A/B-Use-Case-Confound, harte €-Parameter).
Empfehlung: **Lead-Beispiel für Pilot-Angebot = Bauanträge (Gießen/Marburg).**

---
*Unix-Prinzip: Script = eine Sache (ROI simulieren), reproduzierbar, quelloffen.*

---

## Begriffe einfach erklärt

- **NPV (Kapitalwert):** Wie viel Euro das Projekt über 5 Jahre wirklich einbringt, abzüglich der Kosten – auf heute gerechnet.
- **Monte-Carlo-Simulation:** Wir rechnen das Szenario 50.000 Mal mit leicht unterschiedlichen Annahmen durch, um eine realistische Spanne statt einer falschen Sicherheit zu bekommen.
- **Prior / Posterior:** Unsere Einschätzung vor bzw. nach ersten Pilot-Daten.
- **Perzentil:** Grenzwert, unterhalb dessen ein bestimmter Anteil der Fälle liegt (5 % = unser schlechtester angenommener Fall).
