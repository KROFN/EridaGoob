#!/usr/bin/env python3
"""Generate missing cluster files for cluster_hints with >=2 members, from verified verdict data."""
import json, os, re
from collections import defaultdict

REPO = "/home/z/my-project/erida-triage/erida"
with open(os.path.join(REPO, ".ai-triage", "bug_index.json"), encoding="utf-8") as f:
    idx = json.load(f)

groups = defaultdict(list)
for e in idx["threads"]:
    c = e.get("cluster")
    if c:
        groups[c].append(e)

os.makedirs(os.path.join(REPO, ".ai-triage", "clusters"), exist_ok=True)
existing = set(os.listdir(os.path.join(REPO, ".ai-triage", "clusters")))

def slugfile(slug):
    return slug + ".md"

created, skipped = [], []
for slug, members in sorted(groups.items()):
    if len(members) < 2:
        continue
    if slugfile(slug) in existing:
        skipped.append(slug)
        continue
    lines = [f"# Cluster: {slug}", "",
             "## Members", ""]
    for m in members:
        lines.append(f"- {m['thread_id']} — {m['title']} ({m.get('verdict')}/{m.get('confidence')})")
    lines += ["", "## Common symptom (from individual dossiers)", ""]
    rcs = []
    for m in members:
        rc = m.get("root_cause_short") or "see dossier"
        rcs.append(f"- {m['thread_id']}: {rc}")
    lines += rcs
    lines += ["", "## Root cause notes", "",
              "Shared mechanism per member dossiers; where mechanisms diverge the cluster marks a "
              "failure FAMILY (same subsystem, distinct causes) rather than a single fix.", "",
              "## Recommended action", "",
              "Single fix only where dossiers confirm one root cause; otherwise coordinate fixes "
              "per member dossier's Proposed fix section to avoid duplicate investigation.", "",
              "## Validation matrix", "",
              "| Thread | Check | Expected |", "|---|---|---|"]
    for m in members:
        lines.append(f"| {m['thread_id']} | re-verify per dossier Validation plan | see dossier |")
    path = os.path.join(REPO, ".ai-triage", "clusters", slugfile(slug))
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    created.append(slug)

print("clusters created:", len(created))
for c in created: print("  +", c)
print("already existed:", len(skipped), skipped)
