#!/usr/bin/env python3
"""Strukturprüfung für die Web-Dateien (gh-pages).

Ergänzt check_repo.py um HTML-spezifische Prüfungen:
  1. Ausgeglichene Tags in allen .html-Dateien
  2. Keine doppelten id-Attribute
  3. Interne Links (href/src) lösen auf; Fragment-Anker (#id) existieren
  4. sitemap.xml wohlgeformt, referenzierte Dateien vorhanden
  5. Verbotene Begriffe auch in .html

Exit 1 bei Funden. Reine Standardbibliothek — keine externen Abhängigkeiten.
"""
import os
import re
import sys
import xml.etree.ElementTree as ET
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ERRORS = []

FORBIDDEN_HTML = ["Bürgerportal", "3× Mesh", "3x Mesh"]
SKIP_PREFIXES = ("http://", "https://", "mailto:", "tel:", "data:", "javascript:")
VOID_TAGS = {"meta", "link", "img", "br", "hr", "input", "source", "area",
             "base", "col", "embed", "track", "wbr"}


def html_files():
    for dirpath, _, files in os.walk(ROOT):
        if ".git" in dirpath:
            continue
        for f in files:
            if f.endswith(".html"):
                yield os.path.join(dirpath, f)


# 1) + 2) Tags & IDs
class Checker(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.path = path
        self.stack = []
        self.ids = []

    def handle_starttag(self, tag, attrs):
        if tag not in VOID_TAGS:
            self.stack.append((tag, self.getpos()))
        attrs = dict(attrs)
        if attrs.get("id"):
            self.ids.append(attrs["id"])

    def handle_endtag(self, tag):
        if self.stack and self.stack[-1][0] == tag:
            self.stack.pop()
        else:
            ERRORS.append(f"{self.path}: unbalanciertes </{tag}> bei {self.getpos()}")


for path in html_files():
    parser = Checker(path)
    parser.feed(open(path, encoding="utf-8").read())
    if parser.stack:
        ERRORS.append(f"{path}: ungeschlossene Tags: "
                      f"{[t for t, _ in parser.stack]}")
    dups = {i for i in parser.ids if parser.ids.count(i) > 1}
    if dups:
        ERRORS.append(f"{path}: doppelte id-Attribute: {sorted(dups)}")

# 3) Links & Anker
ids_by_file = {}
for path in html_files():
    ids_by_file[path] = set(
        re.findall(r'id="([^"]+)"', open(path, encoding="utf-8").read()))

HTML_ATTR = re.compile(r'(?:href|src)="([^"]+)"')
for path in html_files():
    base = os.path.dirname(path)
    text = open(path, encoding="utf-8").read()
    for target in HTML_ATTR.findall(text):
        target, _, frag = target.partition("#")
        if not target or target.startswith(SKIP_PREFIXES):
            continue
        if not target:  # reiner Fragment-Anker
            if frag and frag not in ids_by_file.get(path, set()):
                ERRORS.append(f"{path}: fehlender Anker #{frag}")
            continue
        cand = (os.path.join(ROOT, target.lstrip("/"))
                if target.startswith("/")
                else os.path.normpath(os.path.join(base, target)))
        rel = os.path.relpath(path, ROOT)
        if not os.path.exists(cand):
            ERRORS.append(f"{rel}: toter Link '{target}'")
        elif frag and cand.endswith(".html") and frag not in ids_by_file.get(cand, set()):
            ERRORS.append(f"{rel}: fehlender Anker '{target}#{frag}'")

# 4) sitemap.xml & robots.txt
sm_path = os.path.join(ROOT, "sitemap.xml")
try:
    tree = ET.parse(sm_path)
    for url in tree.getroot().iter("{http://www.sitemaps.org/schemas/sitemap/0.9}url"):
        loc = url.find("{http://www.sitemaps.org/schemas/sitemap/0.9}loc")
        if loc is None or not loc.text:
            ERRORS.append("sitemap.xml: <loc> fehlt")
            continue
        name = loc.text.rstrip("/").rsplit("/", 1)[-1]
        if name and name != "open-gov-automation" and not os.path.exists(os.path.join(ROOT, name)):
            ERRORS.append(f"sitemap.xml: verweist auf fehlende Datei '{name}'")
except ET.ParseError as exc:
    ERRORS.append(f"sitemap.xml: nicht wohlgeformt ({exc})")

if not os.path.exists(os.path.join(ROOT, "robots.txt")):
    ERRORS.append("robots.txt fehlt")

# 5) Verbotene Begriffe in HTML
for path in html_files():
    text = open(path, encoding="utf-8").read()
    for term in FORBIDDEN_HTML:
        if term in text:
            ERRORS.append(f"{os.path.relpath(path, ROOT)}: veralteter Begriff '{term}'")

if ERRORS:
    print("Web-Strukturprüfung FEHLGESCHLAGEN:")
    for e in ERRORS:
        print("  -", e)
    sys.exit(1)
print("Web-Strukturprüfung bestanden (Tags, IDs, Links, sitemap, Begriffe).")
