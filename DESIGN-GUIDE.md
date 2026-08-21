# open-gov-automation — Design Guide

**Minimal. Stoisch. Unix-Philosophie.**

---

## 🎯 Design-Prinzipien

### 1. **Einfachheit über Alles**
- Keine überflüssigen Elemente
- Keine Animationen, keine Effekte
- Jedes Element hat einen Zweck
- "Weniger ist mehr" — Dieter Rams

### 2. **Geometrische Klarheit**
- **Linien:** Gerade, saubere Kanten
- **Formen:** Rechtecke, Kreise, Polygone
- **Ausrichtung:** Pixel-perfekt (4px Grid)
- **Hierarchie:** Durch Größe und Gewicht, nicht durch Farbe

### 3. **Farben: Minimal & Professionell**

| Farbe | Hex | Verwendung |
|-------|-----|------------|
| **Primary Blue** | `#2563eb` | Akzente, Links, Buttons |
| **Dark Blue** | `#1e40af` | Headlines, wichtige Texte |
| **Light Blue** | `#dbeafe` | Hintergründe (subtil) |
| **Success Green** | `#10b981` | Status, Bestätigungen |
| **Warning Amber** | `#f59e0b` | Hinweise, Warnungen |
| **Error Red** | `#ef4444` | Fehler, kritische Meldungen |
| **Neutral Gray** | `#6b7280` | Sekundärtexte |
| **Dark Gray** | `#374151` | Primärtexte |
| **Black** | `#111827` | Überschriften |
| **White** | `#ffffff` | Hintergrund |

**Regeln:**
- Maximal **3 Farben pro Seite** (inkl. Neutraltöne)
- Primary Blue nur für **interaktive Elemente**
- Success Green nur für **positive Rückmeldungen**
- Keine Gradienten, keine Schatten

### 4. **Typografie**

| Element | Schriftart | Größe | Gewicht | Farbe |
|---------|------------|-------|---------|-------|
| **H1** | Inter | 36px | 700 | `#111827` |
| **H2** | Inter | 24px | 600 | `#111827` |
| **H3** | Inter | 20px | 600 | `#1e40af` |
| **Body** | Inter | 16px | 400 | `#374151` |
| **Small Text** | Inter | 14px | 400 | `#6b7280` |
| **Code** | JetBrains Mono | 14px | 400 | `#1e40af` |

**Fallbacks:**
```css
font-family: Inter, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
```

**Regeln:**
- **Keine kursiven Texte** (ausgenommen Zitate)
- **Keine Unterstreichungen** (außer Links)
- **Maximal 3 Schriftgrößen pro Seite**
- **Zeilenhöhe:** 1.5 für Body, 1.2 für Headlines

### 5. **Abstände (Spacing)**

- **Basis:** 4px Grid
- ** Klein:** 8px (0.5rem)
- **Standard:** 16px (1rem)
- **Groß:** 24px (1.5rem)
- **Sehr groß:** 32px (2rem)

**Regeln:**
- Vertikale Abstände immer **Vielfache von 8px**
- Horizontale Abstände immer **Vielfache von 4px**
- Keine negativen Margins

### 6. **Layout**

- **Maximale Breite:** 800px (Lesbarkeit)
- **Ränder:** 24px (Mobile), 48px (Desktop)
- **Single Column** für Dokumentation
- **Zwei Spalten** nur für Vergleiche (z. B. Lösungsvergleich)

### 7. **Navigation**

- **Keine Dropdowns** (zu komplex)
- **Keine Hamburger-Menüs** (nicht barrierefrei)
- **Maximal 5 Hauptnavigationspunkte**
- **Aktuelle Seite immer hervorgehoben**

### 8. **Interaktion**

- **Links:** Unterstrichen, `#2563eb`
- **Buttons:** Gefüllter Hintergrund, `#2563eb`, weißer Text
- **Hover:** Farbe etwas dunkler (#`1d4ed8`)
- **Focus:** 2px blauer Rahmen (`#2563eb`)
- **Keine Tooltips** (nicht barrierefrei)

### 9. **Barrierefreiheit**

- **Kontrast:** Mindestens **4.5:1** für Texte
- **Schriftgröße:** Mindestens **16px** für Body
- **Alt-Texte:** Für alle Images/PNGs
- **Semantisches HTML:** `<nav>`, `<main>`, `<section>`, `<article>`
- **Keyboard-Navigation:** Alle Elemente per TAB erreichbar

### 10. **Performance**

- **Maximale Ladezeit:** < 1s (ohne JavaScript)
- **Bilder:** SVG wo möglich, sonst **PNG-8** (kein JPEG)
- **Kein JavaScript** für Kernfunktionalität
- **CSS:** Inline oder minimal (keine Frameworks)

---

## 📌 Do's & Don'ts

### ✅ **Do:**
- Halte es einfach
- Nutze geometrische Formen
- Beschränke die Farbpalette
- Schreibe klare, kurze Texte
- Optimiere für Lesbarkeit
- Teste auf allen Geräten

### ❌ **Don't:**
- ❌ Animationen oder Effekte
- ❌ Gradienten oder Schatten
- ❌ Mehr als 3 Farben pro Seite
- ❌ Komplexe Navigation
- ❌ Lange Textblöcke (> 50 Wörter)
- ❌ Externe Abhängigkeiten (CSS/JS Frameworks)

---

## 🎨 Farbpaletten

### 1. **Hauptseiten (hello-gov-automation.html)**
- Hintergrund: `#ffffff`
- Text: `#111827`
- Akzente: `#2563eb`
- Sekundär: `#6b7280`

### 2. **Dokumentation**
- Hintergrund: `#ffffff`
- Text: `#374151`
- Code: `#1e40af`
- Tabellen: `#f3f4f6` (Hintergrund)

### 3. **Compliance-Dokumente**
- Hintergrund: `#ffffff`
- Text: `#111827`
- Status-Icons: `#10b981` (✅), `#ef4444` (❌)

---

## 📏 Grid & Komponenten

### Buttons
```html
<button class="btn">Primär</button>
<button class="btn btn-secondary">Sekundär</button>
```

```css
.btn {
  display: inline-block;
  padding: 12px 24px;
  background: #2563eb;
  color: #fff;
  border: none;
  border-radius: 4px;
  font-size: 16px;
  font-weight: 600;
  cursor: pointer;
  text-decoration: none;
}
.btn:hover { background: #1d4ed8; }
.btn-secondary {
  background: transparent;
  color: #2563eb;
  border: 2px solid #2563eb;
}
```

### Karten
```html
<div class="card">
  <h3>Überschrift</h3>
  <p>Inhalt</p>
</div>
```

```css
.card {
  background: #fff;
  border: 1px solid #e5e7eb;
  border-radius: 8px;
  padding: 24px;
  margin-bottom: 16px;
}
```

### Tabellen
```html
<table>
  <thead>
    <tr><th>Spalte 1</th><th>Spalte 2</th></tr>
  </thead>
  <tbody>
    <tr><td>Wert 1</td><td>Wert 2</td></tr>
  </tbody>
</table>
```

```css
th, td {
  padding: 12px 16px;
  text-align: left;
  border-bottom: 1px solid #e5e7eb;
}
th { background: #f9fafb; }
```

---

## 🔍 Qualitätssicherung

- [ ] **Kontrast-Check:** [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/)
- [ ] **Barrierefreiheit:** [aXe DevTools](https://www.deque.com/axe/)
- [ ] **Performance:** [PageSpeed Insights](https://pagespeed.web.dev/)
- [ ] **Validierung:** [W3C Validator](https://validator.w3.org/)

---

## 📚 Inspiration

- [Dieter Rams — 10 Prinzipien guten Designs](https://www.vitsoe.com/de/ueber-vits/o/design-prinzipien)
- [IBM Design Language](https://www.carbonDesignsystem.com/)
- [Google Material Design — Minimal](https://m3.material.io/)

---

*"Perfection is achieved not when there is nothing more to add, but when there is nothing left to take away." — Antoine de Saint-Exupéry*
