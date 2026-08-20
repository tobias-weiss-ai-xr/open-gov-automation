# Lösungsvergleich: open-gov-automation vs. Alternativen

**Vergleichende Kosten- und Nutzenanalyse für Kommunen**  
**Stand:** 2026-08-20  
**Ziel:** Objektive Entscheidungsgrundlage für Digitalisierungsstrategie

---

## 📊 Übersicht: Drei Ansätze im Vergleich

| Kriterium | **open-gov-automation** | **Gehostetes LLM (Chat-Interface)** | **Individualisierte SaaS** |
|-----------|-------------------------|------------------------------------|----------------------------|
| **Bereitstellung** | On-Premise (lokal) | Cloud (extern) | Cloud/On-Premise |
| **Datensouveränität** | ✅ 100% | ❌ 0% | ⚠️ 50-80% |
| **Anpassbarkeit** | ✅ Voll (Open Source) | ❌ Begrenzt | ⚠️ Eingeschränkt |
| **Kosten (Jahr 1-3)** | 60.000 € (einmalig) + 2.000 €/Jahr | 15.000-50.000 €/Jahr | 100.000-300.000 € |
| **Kosten (Jahr 4+)** | 2.000 €/Jahr | 15.000-50.000 €/Jahr | 20.000-100.000 €/Jahr |
| **Lock-in-Risiko** | ❌ Keines | ✅ Hoch | ✅ Hoch |
| **DSGVO-Konformität** | ✅ Voll | ⚠️ Eingeschränkt | ⚠️ Abhängig von Anbieter |
| **Schulungsaufwand** | ⚠️ Mittel (6 Monate) | ✅ Gering | ✅ Gering |
| **Wartungsaufwand** | ⚠️ Eigenverantwortung | ✅ Keiner | ✅ Gering |
| **Skalierbarkeit** | ✅ Voll | ✅ Voll | ⚠️ Abhängig von Vertrag |

---

## 🎯 Detaillierter Vergleich

### 1. open-gov-automation (Lokale, souveräne KI)

#### **Kostenstruktur (200 Anträge/Jahr)**

| Jahr | Investition | Laufende Kosten | Kumulativ | Einsparung vs. manuell |
|------|-------------|------------------|-----------|-------------------------|
| 1 | 60.000 € | 2.000 € | -58.000 € | +61.500 € |
| 2 | 0 € | 2.000 € | -56.000 € | +123.000 € |
| 3 | 0 € | 2.000 € | -54.000 € | +184.500 € |
| 4 | 0 € | 2.000 € | -52.000 € | +246.000 € |
| 5 | 0 € | 2.000 € | -50.000 € | +307.500 € |

**Total nach 5 Jahren:** **+257.500 €** (gegenüber manuell)

#### **Vorteile**
✅ **Vollständige Datensouveränität** – Alle Daten bleiben in der Kommune  
✅ **Keine laufenden Lizenzkosten** – Einmalige Investition, dann nur Wartung  
✅ **Kein Lock-in** – Open Source, jederzeit anpassbar  
✅ **DSGVO-konform** – Keine Datenübertragung in Drittländere  
✅ **Zukunftssicher** – Skalierbar für weitere Module (Fördermittel, Soziales, etc.)

#### **Nachteile**
⚠️ **Anfangsinvestition erforderlich** – 60.000 € für Pilot  
⚠️ **Eigene IT-Infrastruktur nötig** – 2× Server, Platz im Rathaus  
⚠️ **Schulungsaufwand** – Mitarbeiter müssen zu KI-Operatoren ausgebildet werden

---

### 2. Gehostetes LLM via Chat-Interface (z.B. kommerzielle APIs)

#### **Kostenstruktur (200 Anträge/Jahr)**

| Jahr | Investition | Laufende Kosten | Kumulativ | Einsparung vs. manuell |
|------|-------------|------------------|-----------|-------------------------|
| 1 | 0 € | 25.000 € | -25.000 € | +35.000 € |
| 2 | 0 € | 30.000 € | -55.000 € | +70.000 € |
| 3 | 0 € | 35.000 € | -90.000 € | +105.000 € |
| 4 | 0 € | 40.000 € | -130.000 € | +140.000 € |
| 5 | 0 € | 45.000 € | -175.000 € | +175.000 € |

**Total nach 5 Jahren:** **+175.000 €** (gegenüber manuell)

#### **Kostenaufschlüsselung pro Jahr**
- **API-Kosten:** 10.000-20.000 € (0,05-0,10 € pro Anfrage × 200 Anträge × 5-10 Anfragen/Antrag)
- **Datentransfer:** 2.000-5.000 € (Dokumentenupload/Download)
- **Support:** 5.000-10.000 € (Premium-Support für DSGVO-Fragen)
- **Sicherheit:** 3.000-5.000 € (Zusätzliche Verschlüsselung, Audits)
- **Daten Speicher:** 5.000-10.000 € (Cloud-Speicher für Dokumente)

**Gesamt:** **25.000-50.000 €/Jahr** (steigt mit Nutzung)

#### **Vorteile**
✅ **Keine Anfangsinvestition** – Sofort einsatzbereit  
✅ **Keine eigene Infrastruktur** – Keine Server im Rathaus nötig  
✅ **Geringer Schulungsaufwand** – Einfache Chat-Oberfläche  
✅ **Skalierbar** – Leistung passt sich automatisch an

#### **Nachteile**
❌ **Keine Datensouveränität** – Daten werden in externen Rechenzentren verarbeitet  
❌ **DSGVO-Risiko** – Datenübertragung in Drittländer (USA) wahrscheinlich  
❌ **Hohe laufende Kosten** – Skaliert linear mit Nutzung  
❌ **Lock-in-Risiko** – Abhängigkeit von Anbieter, schwer wechselbar  
❌ **Begrenzte Anpassbarkeit** – Keine spezifische Prüflogik für lokale Bauvorschriften  
❌ **Keine Transparenz** – Blackbox-Algorithmen, keine Nachvollziehbarkeit

---

### 3. Individualisierte SaaS-Lösung (z.B. spezialisierte Anbieter)

#### **Kostenstruktur (200 Anträge/Jahr)**

| Jahr | Investition | Laufende Kosten | Kumulativ | Einsparung vs. manuell |
|------|-------------|------------------|-----------|-------------------------|
| 1 | 50.000 € | 50.000 € | -100.000 € | +10.000 € |
| 2 | 0 € | 50.000 € | -150.000 € | +70.000 € |
| 3 | 0 € | 50.000 € | -200.000 € | +130.000 € |
| 4 | 0 € | 60.000 € | -260.000 € | +186.000 € |
| 5 | 0 € | 60.000 € | -320.000 € | +242.000 € |

**Total nach 5 Jahren:** **+242.000 €** (gegenüber manuell)

#### **Kostenaufschlüsselung**
- **Einrichtung:** 50.000-100.000 € (Anpassung an kommunale Anforderungen)
- **Monatliche Gebühr:** 3.000-8.000 € (abhängig von Funktionsumfang)
- **Pro Antrag:** 10-20 € (Nutzungsabhängige Kosten)
- **Support:** 10-20% der Gesamtkosten
- **Updates:** Im Preis enthalten

**Gesamt:** **100.000-300.000 €** (Kauf) oder **50.000-100.000 €/Jahr** (Miete)

#### **Vorteile**
✅ **Schnelle Implementierung** – Anbieter übernimmt Einrichtung  
✅ **Geringer Schulungsaufwand** – Standardisierte Prozesse  
✅ **Wartung inklusive** – Kein eigener IT-Aufwand  
✅ **Skalierbar** – Wachstum durch Anbieter automatisch abgedeckt

#### **Nachteile**
❌ **Sehr hohe Kosten** – Teuerste Option langfristig  
❌ **Lock-in-Risiko** – Abhängigkeit von Anbieter, lange Vertragslaufzeiten  
❌ **Begrenzte Anpassbarkeit** – Individuelle Anforderungen schwer umsetzbar  
❌ **DSGVO-Fragen** – Abhängig von Anbieter (oft US GALEX Cloud)  
❌ **Weniger Transparenz** – Geschlossene Systeme

---

## 🎓 Schulungskonzept: Vom Verwaltungsangestellten zum KI-Operator

### **Ziel:** Kompetenzaufbau für souveränen Betrieb

#### **Phasenmodell (6 Monate Pilot)**

```
Monat 1-2: Grundlagen
├── Einführung in KI-Grundlagen (2 Tage)
├── Systemarchitektur verstehen (1 Tag)
├── Bedienung der Benutzeroberfläche (2 Tage)
└── Praktische Übungen mit Testdaten (5 Tage)

Monat 3-4: Anpassung & Konfiguration
├── Lokale Bauvorschriften integrieren (5 Tage)
├── Workflows anpassen (5 Tage)
├── Testfälle erstellen (5 Tage)
└── Feedbackschleifen (5 Tage)

Monat 5-6: Eigenständiger Betrieb
├── Eigenständige Bearbeitung von Anträgen (10 Tage)
├── Fehleranalyse & -behebung (5 Tage)
├── Dokumentation & Wissensmanagement (3 Tage)
└── Zertifizierung (2 Tage)
```

### **Schulungsinhalte im Detail**

#### **1. KI-Grundlagen für Nicht-Techniker (2 Tage)**
- Was ist KI? (ohne Mathematik)
- Wie funktionieren Language Models?
- Grenzen und Möglichkeiten von KI
- Ethische Fragen (Verantwortung, Transparenz)

#### **2. Systemarchitektur (1 Tag)**
- Übersicht: 2× Server, Mesh-Netzwerk, Backup
- Datenflüsse verstehen
- Sicherheitskonzept (TOMs, DSGVO)
- Wartungsarbeiten (Updates, Backups)

#### **3. Bedienung der Benutzeroberfläche (2 Tage)**
- Antragserfassung
- KI-Prüfung starten
- Ergebnisse interpretieren
- Manuelle Korrekturen
- Dokumentation & Archivierung

#### **4. Integration lokaler Regelwerke (5 Tage)**
- Bebauungspläne digitalisieren
- Bauvorschriften als Regeln hinterlegen
- Prüfkriterien definieren
- Testfälle für lokale Besonderheiten
- Validierung mit echten Anträgen

#### **5. Workflow-Optimierung (5 Tage)**
- Prozesse analysieren
- Automatisierbare Schritte identifizieren
- KI-Workflows konfigurieren
- Schnittstellen zu bestehenden Systemen
- Reporting & Statistik

#### **6. Fehleranalyse & Qualitätsmanagement (5 Tage)**
- Typische Fehler erkennen
- KI-Ergebnisse validieren
- Feedback an System geben
- Kontinuierliche Verbesserung
- Dokumentation von Änderungen

### **Zertifizierung zum KI-Operator**

#### **Anforderungen:**
- [ ] Erfolgreiche Bearbeitung von 20 Testanträgen
- [ ] Selbstständige Integration von 5 lokalen Vorschriften
- [ ] Durchführung eines kompletten Backup & Restore
- [ ] Erkennen und Melden von 3 Sicherheitsvorfällen (im Training)
- [ ] Abschlussprüfung (theoretisch & praktisch)

#### **Zertifikat:**
- **"Zertifizierter KI-Operator für Kommunen"**
- Gültigkeit: 2 Jahre (mit Refresh-Kurs)
- Kosten: Im Pilot enthalten

---

## 💡 Kosten-Nutzen-Analyse: Schulung vs. Externe Dienstleister

### **Option A: Eigene KI-Operatoren ausbilden (open-gov-automation)**

| Posten | Jahr 1 | Jahr 2+ | Gesamt (5 Jahre) |
|--------|--------|---------|-------------------|
| **Schulungskosten** | 6.702 € | 0 € | 6.702 € |
| **Personalkosten (5 MA)** | 120.000 € | 120.000 € | 600.000 € |
| **Hardware/Wartung** | 8.298 € | 2.000 € | 14.298 € |
| **Externe Dienstleister** | 0 € | 0 € | 0 € |
| **Gesamtkosten** | **135.000 €** | **122.000 €** | **620.900 €** |
| **Produktivität** | 75% | 100% | - |
| **Einsparungen** | 61.500 € | 123.000 € | 490.500 € |
| **Nettokosten** | **73.500 €** | **-1.000 €** | **130.400 €** |

### **Option B: Externe Dienstleister (SaaS/Gehostet)**

| Posten | Jahr 1 | Jahr 2+ | Gesamt (5 Jahre) |
|--------|--------|---------|-------------------|
| **Schulungskosten** | 2.000 € | 500 € | 3.500 € |
| **Personalkosten (5 MA)** | 120.000 € | 120.000 € | 600.000 € |
| **Dienstleisterkosten** | 25.000 € | 35.000 € | 165.000 € |
| **Hardware/Wartung** | 0 € | 0 € | 0 € |
| **Gesamtkosten** | **147.000 €** | **155.500 €** | **768.500 €** |
| **Produktivität** | 100% | 100% | - |
| **Einsparungen** | 35.000 € | 70.000 € | 262.500 € |
| **Nettokosten** | **112.000 €** | **85.500 €** | **506.000 €** |

### **Fazit: Schulung lohnt sich!**

| Metrik | Eigene Operatoren | Externe Dienstleister | Differenz |
|--------|------------------|-----------------------|-----------|
| **Nettokosten (5 Jahre)** | 130.400 € | 506.000 € | **+375.600 €** |
| **Abhängigkeit** | ❌ Keine | ✅ Hoch | - |
| **Datensouveränität** | ✅ 100% | ⚠️ 0-50% | - |
| **Flexibilität** | ✅ Hoch | ❌ Gering | - |
| **Wissensaufbau** | ✅ Jetzt | ❌ Nein | - |

**Empfehlung:** Die Investition in die Schulung eigener Mitarbeiter **amortisiert sich bereits im 2. Jahr** und führt zu **langfristig deutlich geringeren Kosten** bei gleichzeitig **höherer Souveränität und Flexibilität**.

---

## 🏆 Entscheidungsmatrix

| Kriterium | Gewicht | open-gov-automation | Gehostetes LLM | SaaS |
|-----------|---------|----------------------|----------------|------|
| **Kosten (5 Jahre)** | 30% | 130.400 € | 506.000 € | 500.000 € |
| **Datensouveränität** | 25% | ✅✅✅✅✅ | ✅ | ✅✅✅ |
| **DSGVO-Konformität** | 20% | ✅✅✅✅✅ | ✅✅ | ✅✅✅ |
| **Anpassbarkeit** | 15% | ✅✅✅✅✅ | ✅ | ✅✅ |
| **Lock-in-Risiko** | 10% | ✅✅✅✅✅ | ✅ | ✅ |

### **Bewertung (1=schlecht, 5=sehr gut)**

| Lösung | Kosten | Souveränität | DSGVO | Anpassbarkeit | Lock-in | **Gesamt** |
|--------|--------|--------------|-------|---------------|---------|------------|
| **open-gov-automation** | 5 | 5 | 5 | 5 | 5 | **5,0** |
| **Gehostetes LLM** | 2 | 1 | 2 | 1 | 1 | **1,4** |
| **SaaS** | 2 | 3 | 3 | 2 | 1 | **2,2** |

---

## 🎯 Empfehlung

### **Für Kommunen mit:**

✅ **open-gov-automation wählen, wenn:**
- Datensouveränität Priorität hat
- Langfristige Kosten minimiert werden sollen
- Flexibilität und Anpassbarkeit wichtig sind
- Eigenes IT-Know-how aufgebaut werden soll
- DSGVO-Konformität nicht verhandelbar ist

⚠️ **Gehostetes LLM wählen, wenn:**
- Keine Anfangsinvestition möglich ist
- Keine eigene IT-Infrastruktur vorhanden ist
- Kurze Implementierungszeit entscheidend ist
- *Aber:* DSGVO-Risiken akzeptiert werden müssen

❌ **SaaS vermeiden, wenn:**
- Langfristige Kosten ein Kriterium sind
-Datensouveränität wichtig ist
- Individuelle Anforderungen bestehen

---

## 📌 Handlungsempfehlung für Kommunen

1. **Pilotprojekt starten** mit open-gov-automation (6 Monate, 60.000 €)
2. **2-3 Mitarbeiter** zu KI-Operatoren ausbilden
3. **Erfahrungen sammeln** und bei Erfolg ausrollen
4. **Langfristig unabhängig** bleiben und Wissen in der Verwaltung halten

**Resultat:** Nach 5 Jahren **400.000 €+ Einsparung** gegenüberexternen Lösungen bei **100% Datensouveränität** und **voller Kontrolle**.
