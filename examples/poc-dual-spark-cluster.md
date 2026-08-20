# PoC: Dual-Spark-Cluster (souveräne KI lokal)

> Externe Referenz: graphwiz.ai — *"Sovereign AI on Your Desk: Why Two DGX Sparks Beat the Cloud"* (2026-08-01)
> https://graphwiz.ai/content/ai/sovereign-ai-dual-spark-cluster/
> Dieser PoC bestätigt unsere **2×-GX10-Kopplung** als realisierbar und produktionserprobt.

---

## Was der PoC zeigt

Zwei **NVIDIA DGX Spark (GB10)** — baugleich zum **ASUS Ascent GX10** unserer Skizze —
werden direkt gekoppelt und betreiben ein fronthauben-taugliches Sprachmodell **lokal, ohne Cloud**.

| Aspekt | PoC (DGX Spark ×2) | Unsere 60k-Skizze |
|--------|--------------------|-------------------|
| Gerät | DGX Spark = GB10, 128 GB | ASUS GX10 = GB10, 128 GB |
| Kopplung | 2× 200 Gbps (gebondet = 400 Gbps) | 2× 200 Gbps Direktlink |
| Speicher (gekoppelt) | ~240 GB nutzbar | 256 GB einheitlich |
| Modell | DeepSeek-V4-Flash (685B MoE, 37B aktiv) | lokales Modell (Bauanträge) |
| Cloud | keine — Daten verlassen das Netz nicht | keine US-Cloud |
| Kontext | bis 200K Token | ausreichend für Dokumente |

---

## Ergebnisse (produktionserprobt seit Mai 2026)

- **Durchsatz:** 15–20 Token/s Decode, ~1.100 Token/s Prefill (2K-Prompt)
- **Kontext:** 200K Token praktisch nutzbar — lang genug für Bauantrags-Dokumente
- **Tool-Calling:** eingebaut → Modell nutzt Werkzeuge, führt mehrstufige Pläne aus
- **Agentenfähig:** exakt der Anwendungsfall für vorausschauende Verwaltungs-KI

---

## Bedeutung für unser Pilot

1. **Risiko reduziert:** Die 2×-GX10-Kopplung ist keine Theorie, sondern läuft in Produktion.
2. **Souveränität belegt:** Kein Datentransfer in die Cloud = DSGVO-konform von sich aus.
3. **Modell tauglich:** Ein Modell der GPT-4-Klasse läuft lokal → Bauantrags-Dokumente
   extrahieren, Baurecht prüfen, Muster vorausschauend erkennen.
4. **Interconnect:** 2× 200 Gbps gebondet (400 Gbps) ist die bewährte Verbindung —
   unsere Spezifikation deckt sich damit.

> **Fazit:** Der PoC macht die These der Skizze greifbar — souveräne, „intelligente" KI
> passt auf zwei Schreibtische und braucht keine US-Cloud.

---

## Unix-Prinzip angewendet

- **Eine Sache:** PoC = nur Machbarkeitsnachweis der Hardware
- **Verifizierbar:** externe Quelle verlinkt, Messwerte genannt
- **Souverän:** Beweis für Cloud-freie KI
