# Kritische Prüfung — Multi-Stakeholder-Review

> Selbstkritik des open-gov-automation-Konzepts aus sechs Perspektiven.
> Ziel: Schwachstellen offenlegen, bevor sie ein Partner, Prüfer oder Wettbewerber findet.
> Gegengewicht zur sonst zu siegessicheren Außenwirkung.

---

## 1. Kommunen (Zielgruppe)

**Positive:** Datensouveränität (keine US-Cloud), DSGVO-by-Design, 60.000 € sind für eine
Mittelstadt tragbar, Besitz statt Miete.

**Kritik:**
- **Betriebsfähigkeit:** Zwei Blackwell-Superchips plus lokaler LLM-Betrieb übersteigen
  typische Kommunal-IT. Die Schulung (6.702 €) macht keine Sachbearbeiterin zum
  Cluster-Admin → faktische Abhängigkeit vom Anbieter (widerspricht „souverän/selbst betreiben").
- **Haftung:** „KI = Hilfe, Mensch entscheidet" ist rechtlich korrekt, aber Kommunen sind
  risikoavers und trauen sich die Nutzung u.U. nicht zu.
- **Integration:** Bestehende Fachverfahren (BauKG, FIS, eKommunal) werden nicht ersetzt.
  Die Module sind Greenfield → Integrationslücke.
- **0 Referenzen, 0 im Pilot gemessene Werte** → die Wirtschaftlichkeitsanalyse
  (`examples/wirtschaftlichkeit.md`) rechnet mit konservativen Schätzungen, kein Realwert.

**Konsequenz:** Pilot nur mit IT-fähigem Partner (Gießen eher als 5.000-Einwohner-Gemeinde);
Begleitung als laufende Leistung statt Einmal-Schulung.

---

## 2. Bund (BMI, Fitko, OZG, Portalverbund)

**Positive:** Open Source, „build once, copy", Transparenz.

**Kritik:**
- **Gegentrend zur Konsolidierung:** Fitko/OZG treiben standardisierte, geteilte Plattformen.
  Lokaler Cluster pro Kommune = Fragmentierung.
- **OZG-Lücke:** Das (gestrichene) Portal-Modul fehlt → keine OZG-Pflichtdienste abgedeckt;
  Bauanträge ist Back-Office, kein OZG-Service.
- **Fördermittel-Ironie:** Bund/Länder finanzieren Verwaltungs-KI; der Pilot ließe sich co-finanzieren.

**Konsequenz:** Positionierung schärfen: „Lokaler Cluster = souveräne Ergänzung zum
Portalverbund, nicht Konkurrenz."

---

## 3. Länder (Hessen)

**Positive:** Hessische Bauordnung ist Landessache → Baurecht-Prüfung ist landesspezifisch passend.

**Kritik:**
- **Doubletten zu Landes-IT:** Hessen hat eigene eGovernment-Rahmen/IT-Dienstleister
  (Verifikation nötig). Warum eigenes Cluster statt Landes-Plattform?
- **Portabilität:** Baurecht ist landesrechtlich → Skalierung auf andere Länder = Rework.
- **Pflege:** Bauordnungen werden novelliert → wer pflegt die Regeln im Modell?

**Konsequenz:** Klären, ob Hessen souveräne KI/Cloud anbietet; ggf. auf Landes-Infrastruktur aufsetzen.

---

## 4. Wettbewerb

**Etablierte Player:** openDesk (souveräne Büro-Suite, mehrfach landeseingesetzt),
Aleph Alpha (europäisches LLM, Heidelberg), Telekom/T-Systems „Sovereign Cloud"
(KI-as-a-Service, deutsche Jurisdiktion), komm.unity (Schleswig-Holstein, erfolgreiche
kommunale Plattform).

**Kritik:** Unsere Differenzierung (lokal, owned, kein Token-Rent) ist echt, aber Nische.
Ein Bürgermeister vergleicht uns mit „Aleph Alpha via Telekom Sovereign Cloud" und fragt:
warum Hardware besitzen? Unsere Antwort (kein Recurring, volle Datenkontrolle) ist stark,
aber wir übertragen Betriebsverantwortung — manche Kommune will das nicht.

**Konsequenz:** „Besitz statt Miete" betonen; Bauanträge-Predictive als fokussierten
Use-Case, den die Konkurrenz nicht so bedient. Der Lösungsvergleich
(`examples/loesungsvergleich.md`) stützt das, ist aber einseitig zugunsten der Eigenlösung.

---

## 5. Universität Marburg

**Kritik (scharf):**
- **Baurecht ist interpretativ:** Jura-Fakultät zerlegt „KI prüft §§ 5–9 LBO". Baurecht ist
  Ermessen, fallbezogen → LLM-Check ist Heuristik, keine Rechtsprüfung. **Validierung
  gegen Rechtsprechung fehlt.**
- **Modell-Herkunft:** DeepSeek (chinesisch) stößt bei Datenschutz-Verfechtern auf
  Widerstand; Uni zieht europäische Modelle (Aleph Alpha, Mistral) vor.
- **Fehlende Wissenschaftlichkeit:** Pilot ohne Evaluation/IRB → keine akademische Partnerschaft.

**Konsequenz:** Baurecht-Claim als „Entscheidungshilfe, evaluiert mit Jura-Fakultät" framen;
europäisches Modell als Option; Pilot als Forschungs-/Praxis-Projekt.

---

## 6. Universität Gießen (JLU)

Analog Marburg: Jura-Prüfung der Baurecht-Claims, Informatik-Prüfung der KI-Validität.
- **Zusatz:** JLU hat Digital-Humanities/starke Rechtsfakultät → ideale Evaluations-Partnerin.
- **Kritik:** Unis als „Orbit" benannt, aber nicht akademisch eingebunden → ungenutzter
  Hebel (HiWi, Abschlussarbeiten) und potenzielle Konkurrenten mit eigener KI-Agenda.

**Konsequenz:** Unis als Co-Piloten (Evaluation, studentische Mitentwicklung) gewinnen.

---

## Synthese: 5 härteste Risiken

| # | Risiko | Perspektive | Richtung |
|---|--------|-------------|----------|
| 1 | Kommune kann Cluster nicht selbst betreiben | Kommune | Begleitung statt Einmal-Schulung; oder Landes-Infra |
| 2 | „Souverän" = US-Silicon + chinesisches Modell | Uni/Land | Europäisches Modell-Option; „Datensouveränität" präziser |
| 3 | Keine Integration in Bestands-Fachverfahren | Kommune/Land | Integrations-Kapitel (BauKG/FIS-Adapter) |
| 4 | Baurecht-Claim rechtlich unvalidiert | Uni (Jura) | Evaluierung mit Fakultät; „Hilfe, nicht Bescheid" |
| 5 | Starke Konkurrenz (Aleph Alpha, Telekom, openDesk, komm.unity) | Wettbewerb | „Besitz statt Miete" + fokussierter Use-Case |

---

## Konsequenzen für das Repo

Substanz ist solide: Datensouveränität, Machbarkeitsnachweis der Hardware (Dual-Spark,
extern via graphwiz.ai bestätigt), Wirtschaftlichkeitsanalyse (`examples/wirtschaftlichkeit.md`),
Lösungsvergleich (`examples/loesungsvergleich.md`), DSGVO-Vorlagen (`compliance/`).
Unterbelichtet: Betriebsfähigkeit, Integration, Rechtsvalidierung, Modell-Herkunft,
Wettbewerb. Diese Prüfung ist das Gegengewicht — und sollte sichtbar bleiben.
