#!/usr/bin/env python3
"""Extract actionable bug tables for TRIAGE_REPORT."""
import json
from collections import Counter

REPO = "/home/z/my-project/erida-triage/erida"
with open(f"{REPO}/.ai-triage/bug_index.json", encoding="utf-8") as f:
    idx = json.load(f)

nt = [e for e in idx["threads"] if e["classification"] == "NEEDS_TRIAGE"]
confirmed = [e for e in nt if e["verdict"] == "CONFIRMED_CURRENT_BUG"]
likely = [e for e in nt if e["verdict"] == "LIKELY_CURRENT_BUG"]
fixed = [e for e in nt if e["verdict"] == "ALREADY_FIXED_IN_CURRENT_FORK"]
dups = [e for e in nt if e["verdict"] == "DUPLICATE"]
cv = [e for e in nt if e["verdict"] == "CANNOT_VERIFY"]
cfg = [e for e in nt if e["verdict"] == "CONFIG_OR_CONTENT_ISSUE"]
ue = [e for e in nt if e["verdict"] == "USER_ERROR_OR_NOT_BUG"]

print(f"confirmed={len(confirmed)} likely={len(likely)} fixed={len(fixed)} dups={len(dups)} cv={len(cv)} cfg={len(cfg)} ue={len(ue)}")
print("\n=== CONFIRMED ===")
for e in sorted(confirmed, key=lambda x: (x.get("severity") or "S9", x["created_at"] or "")):
    print(f"{e.get('severity') or '-':3} {e.get('complexity') or '-':2} {e.get('confidence') or '-':6} {e['thread_id']} | {e['title'][:50]} | {e.get('root_cause_short','')[:110]}")
print("\n=== LIKELY (S1/S2 first) ===")
for e in sorted(likely, key=lambda x: (x.get("severity") or "S9", x["created_at"] or "")):
    if e.get("severity") in ("S1", "S2"):
        print(f"{e.get('severity'):3} {e.get('complexity') or '-':2} {e.get('confidence') or '-':6} {e['thread_id']} | {e['title'][:50]} | {e.get('root_cause_short','')[:110]}")
print("\n=== ALL dossiers:", sum(1 for e in nt if e.get("dossier")), "of", len(nt))
