# TOMs — Technische und organisatorische Maßnahmen (Beispiel)

**Einfach erklärt:** TOMs = Technische und organisatorische Maßnahmen (Art. 32 DSGVO). Damit wird festgelegt, wie personenbezogene Daten technisch und organisatorisch geschützt werden.

> DSGVO Art. 32 — Maßnahmen zum Schutz der Verarbeitung
> Exemplarisch für **open-gov-automation** (2 gekoppelte GX10, lokale KI-Einheit, On-Premise)

## Maßnahmenkatalog

| Nr | Maßnahme (Art. 32) | Umsetzung im Cluster | Status |
|----|--------------------|----------------------|--------|
| T1 | **Zugangskontrolle** | SSH-Key-only, 2FA für Admin, kein Passwort-Login | ✅ |
| T2 | **Zugriffskontrolte** | RBAC via `orgId` + `role`, JWT mit kurzer Laufzeit (15 min) | ✅ |
| T3 | **Weitergabekontrolle** | TLS 1.3 zwischen Knoten, kein unverschlüsselter Export | ✅ |
| T4 | **Eingabekontrolle** | Validierung aller Eingaben, Audit-Log pro Mutation | ✅ |
| T5 | **Auftragskontrolle** | Keine Unterauftragsverarbeiter (reine Eigeninfrastruktur) | ✅ |
| T6 | **Verfügbarkeitskontrolle** | 3-Knoten-Mesh, Auto-Failover, tägliche Backups | ✅ |
| T7 | **Trennungsgebot** | Container-Isolation (Docker), separate DB pro Modul | ✅ |
| T8 | **Pseudonymisierung** | Hash-IDs statt Klartext-Schlüssel in Logs | ✅ |

---

## 1. Zugangskontrolle (T1)

```yaml
# sshd_config (alle Knoten)
PasswordAuthentication no
PubkeyAuthentication yes
PermitRootLogin no
MaxAuthTries 3
```

- Nur autorisierte Admins via ED25519-Keys
- 2FA via TOTP für Web-Admin-Oberfläche

## 2. Zugriffskontrolle (T2)

```typescript
// RBAC: Rolle prüft Berechtigung pro Modul
interface Permission {
  module: 'foerdermittel' | 'bauantraege';
  action: 'read' | 'write' | 'approve';
}
// JWT enthält: { sub, orgId, roles: Permission[], exp: 15min }
```

## 3. Weitergabekontrolle (T3)

- Inter-Knoten-Kommunikation: WireGuard-VPN (Mesh-Topologie)
- Datenexport: Nur verschlüsselt (GPG), Empfänger whitelisted

## 4. Eingabekontrolle (T4)

- Jede Mutation schreibt in `audit_log` (wer, wann, was, alter/new Wert)
- CI-Pipeline testet Validierungsregeln vor jedem Deploy

## 5. Verfügbarkeitskontrolle (T6)

```
Knoten A ──┐
           ├── Mesh (WireGuard) ── Load Balancer ── Bürger
Knoten B ──┤
           │
Knoten C ──┘  (Failover < 30s bei Knoten-Ausfall)
```

- Tägliche Backups auf lokalen NAS (verschlüsselt)
- Wöchentlicher Offsite-Test-Restore

## 6. Dokumentation der Maßnahmen

Alle TOMs versioniert in Git (`compliance/toms-beispiel.md`).
Änderungen via Pull-Request mit Review-Pflicht.

---

## Checkliste für eigene TOMs

- [ ] Zugang (Wer darf aufs System?)
- [ ] Zugriff (Wer darf welche Daten?)
- [ ] Weitergabe (Wie verlassen Daten das System?)
- [ ] Eingabe (Wie werden Daten validiert?)
- [ ] Auftrag (Welche Dienstleister involviert?)
- [ ] Verfügbarkeit (Wie bei Ausfall?)
- [ ] Trennung (Wie sind Module isoliert?)
- [ ] Pseudonymisierung (Wo stehen Klartext-Namen?)
