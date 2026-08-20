#!/usr/bin/env python3
"""Konsistenzprüfung für open-gov-automation.

Übt, was wir predigen (automatisierte Qualität / CI):
  1. Interne Links müssen auflösen (keine toten Referenzen)
  2. Keine veralteten Begriffe (Bürgerportal, 3× Mesh, gelöschte Dateien)
  3. Example-CI-YAML muss minimale Struktur haben

Exit 1 bei Funden. Reine Standardbibliothek — keine externen Abhängigkeiten.
"""
import os
import re
import sys
import glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FORBIDDEN = [
    "Bürgerportal", "3× Mesh", "3x Mesh",
    "MANIFEST.md", "ADMIN-VALUES.md", "verwaltung-2.0",
]
ERRORS = []


def md_files():
    for dirpath, _, files in os.walk(ROOT):
        for f in files:
            if f.endswith(".md"):
                yield os.path.join(dirpath, f)


# 1) Veraltete Begriffe
for path in md_files():
    with open(path, encoding="utf-8") as fh:
        text = fh.read()
    for term in FORBIDDEN:
        if term in text:
            ERRORS.append(
                f"{os.path.relpath(path, ROOT)}: veralteter Begriff '{term}'"
            )

# 2) Interne Links
LINK_RE = re.compile(r"\]\(([^)]+)\)")
for path in md_files():
    base = os.path.dirname(path)
    with open(path, encoding="utf-8") as fh:
        text = fh.read()
    for m in LINK_RE.finditer(text):
        target = m.group(1).split("#")[0].strip()
        if not target or target.startswith(("http://", "https://", "mailto:")):
            continue
        cand = (
            os.path.join(ROOT, target.lstrip("/"))
            if target.startswith("/")
            else os.path.normpath(os.path.join(base, target))
        )
        if not os.path.exists(cand):
            ERRORS.append(f"{os.path.relpath(path, ROOT)}: toter Link '{target}'")

# 3) Example-CI-YAML Struktur
for yml in glob.glob(os.path.join(ROOT, "examples", "*.yml")):
    with open(yml, encoding="utf-8") as fh:
        content = fh.read()
    if "jobs:" not in content or "on:" not in content:
        ERRORS.append(
            f"{os.path.relpath(yml, ROOT)}: fehlende YAML-Struktur (on:/jobs:)"
        )

if ERRORS:
    print("Konsistenzprüfung FEHLGESCHLAGEN:")
    for e in ERRORS:
        print("  -", e)
    sys.exit(1)
print("Konsistenzprüfung bestanden (Links, veraltete Begriffe, YAML-Struktur).")
