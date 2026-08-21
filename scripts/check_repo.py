#!/usr/bin/env python3
"""Konsistenzprüfung für open-gov-automation.

Übt, was wir predigen (automatisierte Qualität / CI):
  1. Interne Links müssen auflösen (keine toten Referenzen)
  2. Keine veralteten Begriffe
  3. Minimale Strukturprüfung

Exit 1 bei Funden. Reine Standardbibliothek — keine externen Abhängigkeiten.
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FORBIDDEN = [
    "Bürgerportal", "3× Mesh", "3x Mesh",
    "MANIFEST.md", "ADMIN-VALUES.md", "verwaltung-2.0",
    "bauantraege-monte-carlo", "nutzen-roi-analyse",
    "poc-dual-spark", "foerdermittel-module",
    "Beispiel", "beispiel",
]
ERRORS = []


def check_files(file_extensions):
    """Generator für alle Dateien mit gegebenen Endungen."""
    for dirpath, _, files in os.walk(ROOT):
        for f in files:
            if any(f.endswith(ext) for ext in file_extensions):
                yield os.path.join(dirpath, f)


# 1) Veraltete Begriffe in MD-Dateien
for path in check_files([".md"]):
    with open(path, encoding="utf-8") as fh:
        text = fh.read()
    for term in FORBIDDEN:
        if term in text:
            ERRORS.append(
                f"{os.path.relpath(path, ROOT)}: veralteter Begriff '{term}'"
            )

# 2) Interne Links in MD-Dateien
LINK_RE = re.compile(r"\)\(([^)]+)\)")
for path in check_files([".md"]):
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
        # Prüfe mit und ohne .md-Erweiterung
        if not os.path.exists(cand):
            if not os.path.exists(cand + ".md"):
                # Prüfe ob HTML-Datei in Root existiert
                if target == "index.html" and not os.path.exists(os.path.join(ROOT, "index.html")):
                    ERRORS.append(f"{os.path.relpath(path, ROOT)}: toter Link '{target}'")
                elif not target.endswith(".html"):
                    ERRORS.append(f"{os.path.relpath(path, ROOT)}: toter Link '{target}'")

if ERRORS:
    print("Konsistenzprüfung FEHLGESCHLAGEN:")
    for e in ERRORS:
        print("  -", e)
    sys.exit(1)
print("Konsistenzprüfung bestanden (Links, veraltete Begriffe).")
