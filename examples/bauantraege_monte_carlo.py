#!/usr/bin/env python3
"""
Bayesian Monte Carlo — Bauanträge ROI (Stadt Gießen ~90k EW)

Prüfung: Rechnet sich das 60k open-gov-automation-Pilot für das Modul
Bauanträge? Wir propagieren PRIOR-Unsicherheit über N Simulationen
und berichten NPV-Verteilung, P(NPV>0), Payback.

Bayesian: Parameter als Priors spezifiziert; Szenario 2 zeigt Posterior
nach hypothetischer Pilot-Evidenz (Saving-Fraction via Normal-Normal-Update).

Kein Fördermittel (per Instruction ausgeschlossen).
Reine Standardbibliothek — keine externen Abhängigkeiten.
"""
import random
import math

SEED = 4242
N = 50_000
HORIZON = 5
DISCOUNT = 0.05
random.seed(SEED)

factors = [1 / (1 + DISCOUNT) ** t for t in range(1, HORIZON + 1)]
annuity = sum(factors)


def clip(x, lo, hi):
    return max(lo, min(hi, x))


def simulate(permits_rv, saving_rv, label):
    npvs, paybacks = [], []
    for _ in range(N):
        permits = permits_rv()
        hours = clip(random.gauss(3.0, 0.5), 1.5, 5.0)
        saving = saving_rv()
        hourly = clip(random.gauss(42.0, 4.0), 30.0, 55.0)
        impl = clip(random.gauss(60_000, 5_000), 50_000, 70_000)
        maint = clip(random.gauss(6_000, 800), 4_000, 9_000)

        hours_saved = hours * saving
        annual_gross = permits * hours_saved * hourly
        annual_net = annual_gross - maint

        npv = annual_net * annuity - impl

        cum = 0.0
        pb = float("inf")
        for t in range(HORIZON):
            cum += annual_net * factors[t]
            if cum >= impl:
                pb = t + 1
                break

        npvs.append(npv)
        paybacks.append(pb)

    npvs.sort()
    p05, p50, p95 = npvs[int(0.05 * N)], npvs[int(0.50 * N)], npvs[int(0.95 * N)]
    p_pos = 100 * sum(1 for v in npvs if v > 0) / N
    p3 = 100 * sum(1 for p in paybacks if p <= 3) / N
    pb_finite = [p for p in paybacks if p != float("inf")]
    avg_pb = sum(pb_finite) / len(pb_finite) if pb_finite else float("inf")
    annual_net_avg = sum(npvs) / N / annuity + 6000  # grobe Rückrechnung entfällt

    print(f"\n=== {label} (N={N}) ===")
    print(f"  Erwarteter NPV (5J):   {sum(npvs)/N:>12,.0f} €")
    print(f"  Median NPV:            {p50:>12,.0f} €")
    print(f"  5%/95% Perzentil:      {p05:>12,.0f} € / {p95:>12,.0f} €")
    print(f"  P(NPV > 0):            {p_pos:>11.1f} %")
    print(f"  Erw. Payback:          {avg_pb:>11.2f} Jahre")
    print(f"  P(Payback <= 3J):      {p3:>11.1f} %")
    return npvs, paybacks


# ── Priors (Szenario 1) ──
permits_rv_s1 = lambda: random.lognormvariate(math.log(1000), 0.25)
saving_rv_s1 = lambda: clip(random.gauss(0.30, 0.06), 0.10, 0.50)

print("Bauanträge Monte Carlo — Stadt Gießen (~90k EW), Modul allein")
simulate(permits_rv_s1, saving_rv_s1, "Szenario 1 — Prior (keine Pilot-Daten)")

# ── Bayesian Update: Saving-Fraction Normal-Normal ──
# Prior N(mu0=0.30, sd0=0.06). Pilot n=150, beob. Saving-Mittel 0.32 (SD 0.034).
mu0, sd0 = 0.30, 0.06
xbar, se = 0.32, 0.034
tau0 = 1 / sd0 ** 2
tau1 = 1 / se ** 2
post_mu = (tau0 * mu0 + tau1 * xbar) / (tau0 + tau1)
post_sd = math.sqrt(1 / (tau0 + tau1))

saving_rv_s2 = lambda: clip(random.gauss(post_mu, post_sd), 0.10, 0.50)

print(f"\n[Bayesian Update] Saving: Prior N(0.30,0.06) → Posterior "
      f"N({post_mu:.3f},{post_sd:.3f})  (Pilot n=150, xbar=0.32)")
simulate(permits_rv_s1, saving_rv_s2, "Szenario 2 — Posterior (nach Pilot-Evidenz)")

print("\n────────────────────────────────────────────────────────────")
print("Fazit: P(NPV>0) und Payback entscheiden über Wirtschaftlichkeit.")
print("Bayesian: Pilot-Evidenz verschiebt + verschmälert die Verteilung.")
