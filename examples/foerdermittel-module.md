# Fördermittel-Verwaltung — Modulare Struktur

## Prinzip: Jedes Modul macht eine Sache gut

```
foerdermittel/
├── .github/workflows/
│   └── ci.yml                    # CI-Pipeline (automatisierte Qualität)
├── src/
│   ├── adapters/                 # Datenquellen (je eine Datei pro Quelle)
│   │   ├── kommunalportal.ts     # Adapters für Kommunalportal
│   │   ├── eu-fonds.ts           # Adapters für EU-Fördermittel
│   │   ├── bmwi.ts               # Adapters für BMWi
│   │   └── bmbf.ts               # Adapters für BMBF
│   ├── scoring/                  # AI-Bewertung (transparent, testbar)
│   │   ├── eligibility.ts        # Berechtigung prüfen
│   │   ├── match-score.ts        # Passung berechnen
│   │   └── explain.ts            # Begründung generieren
│   ├── deadlines/                # Fristen-Überwachung
│   │   ├── monitor.ts            # Fristen überwachen
│   │   ├── notify.ts             # Benachrichtigungen senden
│   │   └── calendar.ts           # Kalender-Export
│   ├── applications/             # Antrags-Management
│   │   ├── validate.ts           # Anträge validieren
│   │   ├── process.ts            # Anträge bearbeiten
│   │   └── audit.ts              # Audit-Log
│   └── api/                      # REST API (textbasiert)
│       ├── routes.ts             # API-Routen
│       └── middleware.ts         # Auth, Logging
├── tests/                        # 100% Testabdeckung
│   ├── adapters/
│   ├── scoring/
│   ├── deadlines/
│   └── applications/
├── docs/                         # Dokumentation (Markdown)
│   ├── ADR/                      # Architecture Decision Records
│   ├── API.md                    # API-Dokumentation
│   └── DEPLOYMENT.md             # Deployment-Anleitung
└── docker-compose.yml            # Infrastruktur als Code
```

---

## Modul-Details

### 1. Adapters — Datenquellen

**Prinzip:** Jede Datenquelle ist ein eigenständiges Modul

```typescript
// src/adapters/kommunalportal.ts
export interface KommunalportalAdapter {
  fetchFördermittel(): Promise<Fördermittel[]>;
  fetchDeadlines(): Promise<Deadline[]>;
  validateCredentials(): Promise<boolean>;
}

// Testbar, ersetzbar, dokumentiert
export async function fetchFördermittel(): Promise<Fördermittel[]> {
  const response = await fetch('https://kommunalportal.de/api/foerdermittel');
  return response.json();
}
```

**Vorteil:** Wenn eine Quelle ausfällt, funktionieren die anderen weiter.

---

### 2. Scoring — AI-Bewertung

**Prinzip:** Transparente, nachvollziehbare Algorithmen

```typescript
// src/scoring/match-score.ts
export function calculateMatchScore(application: Application, funding: Fördermittel): number {
  // 1. Branch-Übereinstimmung (0-30 Punkte)
  const branchScore = application.branch === funding.targetBranch ? 30 : 0;

  // 2. Unternehmensgröße (0-30 Punkte)
  const sizeScore = calculateSizeScore(application.employees, funding.targetSize);

  // 3. Projektart (0-40 Punkte)
  const typeScore = calculateTypeScore(application.type, funding.allowedTypes);

  return branchScore + sizeScore + typeScore;
}

// Jede Funktion ist testbar
describe('calculateMatchScore', () => {
  it('should return 100 for perfect match', () => {
    // Test case...
  });
});
```

**Vorteil:** Keine Blackbox. Jede Bewertung ist nachvollziehbar.

---

### 3. Deadlines — Fristen-Überwachung

**Prinzip:** Automatisierung statt manueller Arbeit

```typescript
// src/deadlines/monitor.ts
export async function monitorDeadlines(): Promise<DeadlineAlert[]> {
  const alerts: DeadlineAlert[] = [];
  const deadlines = await fetchDeadlines();

  for (const deadline of deadlines) {
    const daysRemaining = daysUntil(deadline.date);

    if (daysRemaining <= 7 && daysRemaining > 0) {
      alerts.push({
        type: 'WARNING',
        message: `Frist in ${daysRemaining} Tagen: ${deadline.title}`,
        deadline: deadline
      });
    }

    if (daysRemaining <= 0) {
      alerts.push({
        type: 'CRITICAL',
        message: `Frist überschritten: ${deadline.title}`,
        deadline: deadline
      });
    }
  }

  return alerts;
}
```

**Vorteil:** 0 verpasste Fristen. Automatische Benachrichtigung.

---

### 4. Applications — Antrags-Management

**Prinzip:** Jede Änderung ist auditierbar

```typescript
// src/applications/audit.ts
export interface AuditLog {
  timestamp: Date;
  action: 'CREATE' | 'UPDATE' | 'SUBMIT' | 'APPROVE' | 'REJECT';
  userId: string;
  applicationId: string;
  changes?: Record<string, { old: any; new: any }>;
  reason?: string;
}

export async function logAudit(entry: AuditLog): Promise<void> {
  await db.insert('audit_log', entry);
}

// Jede Änderung wird protokolliert
export async function approveApplication(id: string, userId: string, reason: string) {
  const application = await getApplication(id);
  application.status = 'APPROVED';
  application.approvedBy = userId;
  application.approvedAt = new Date();

  await db.update('applications', application);
  await logAudit({
    timestamp: new Date(),
    action: 'APPROVE',
    userId,
    applicationId: id,
    reason
  });
}
```

**Vorteil:** Vollständige Nachvollziehbarkeit. Compliance-ready.

---

## CI-Pipeline als Qualitäts-Gate

```yaml
# .github/workflows/ci.yml
jobs:
  lint:
    # Code-Qualität prüfen
    run: npm run lint

  test:
    # Alle Tests laufen
    run: npm test

  validate:
    # Geschäftliche Regeln prüfen
    run: npm run validate:applications

  check-deadlines:
    # Fristen überwachen
    run: npm run check:deadlines

  security:
    # Sicherheitsaudit
    run: npm audit --audit-level=critical

  deploy:
    # Nur wenn ALLES grün
    needs: [lint, test, validate, check-deadlines, security]
```

**Vorteil:** 0 manuelle Fehler. Immer deploybar.

---

## Deployment — On-Premise First

```bash
# docker-compose.admin.yml
version: '3.8'
services:
  foerdermittel:
    image: foerdermittel:latest
    ports:
      - "3003:3003"
    environment:
      - PG_HOST=postgres
      - DGRAPH_URL=http://dgraph:8080
    depends_on:
      - postgres
      - dgraph

  postgres:
    image: postgres:17-alpine
    volumes:
      - foerdermittel-data:/var/lib/postgresql/data

  dgraph:
    image: dgraph/standalone:v24.0.0
    volumes:
      - dgraph-data:/dgraph

volumes:
  foerdermittel-data:
  dgraph-data:
```

**Vorteil:** Datenhoheit bei der Kommune. Keine Cloud-Abhängigkeit.

---

## Test-Strategie — 100% Abdeckung

```bash
# Unit Tests (schnell, keine Infra)
npm test

# Integration Tests (mit DB)
npm run test:integration

# E2E Tests (realistische Szenarien)
npm run test:e2e

# Geschäftliche Validierung
npm run validate:applications

# Fristen-Check
npm run check:deadlines
```

**Vorteil:** Jede Änderung ist getestet. Keine Regressionen.

---

## Erfolgsmetriken

| Metrik | Ziel | Gemessen via |
|--------|------|--------------|
| Testabdeckung | ≥ 90% | `npm test -- --coverage` |
| CI-Duration | < 10 min | GitHub Actions |
| Verpasste Fristen | 0 | `check:deadlines` |
| Manuelle Fehler | 0 | Audit-Log |
| Downtime | < 0.1% | Health Checks |
