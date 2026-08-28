#!/usr/bin/env python3
"""
merge_verdicts.py — merge verdict batch JSONs into bug_index.json + regenerate BUG_INDEX.md.
Usage: python3 merge_verdicts.py
"""
import json, os, glob
from collections import Counter

REPO = "/home/z/my-project/erida-triage/erida"
IDX = os.path.join(REPO, ".ai-triage", "bug_index.json")

with open(IDX, encoding="utf-8") as f:
    data = json.load(f)

by_id = {e["thread_id"]: e for e in data["threads"]}
merged = 0
for path in sorted(glob.glob(os.path.join(REPO, ".ai-triage", "data", "verdicts", "batch_*.json"))):
    try:
        with open(path, encoding="utf-8") as f:
            batch = json.load(f)
    except Exception as ex:
        print(f"WARN: cannot parse {path}: {ex}")
        continue
    for v in batch:
        tid = v.get("thread_id")
        if tid not in by_id:
            print(f"WARN: unknown thread {tid} in {path}")
            continue
        e = by_id[tid]
        e["verdict"] = v.get("verdict")
        e["confidence"] = v.get("confidence")
        e["severity"] = v.get("severity")
        e["complexity"] = v.get("complexity")
        e["cluster"] = v.get("cluster_hint")
        e["root_cause_short"] = v.get("root_cause_short")
        e["evidence"] = v.get("evidence")
        e["dossier"] = v.get("dossier")
        merged += 1

# recompute summary
c = Counter(e["classification"] for e in data["threads"])
v = Counter(e["verdict"] for e in data["threads"] if e["verdict"])
data["summary"]["VERDICTS"] = dict(v)
data["summary"]["VERDICT_COVERAGE"] = sum(1 for e in data["threads"] if e["verdict"])

with open(IDX, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=1)

# regenerate BUG_INDEX.md
s = data["summary"]
lines = ["# BUG INDEX — Discord bug-forum export (Erida)", "",
         "Source: Google Drive archive `1TlOjsaTn_iuKc26S7amk3q1qhkirNol7`.", "",
         "## Summary", "", "| Metric | Count |", "|---|---|"]
for k in ["TOTAL", "SKIP_RESOLVED", "SKIP_NOT_BUG", "NEEDS_TRIAGE", "TAG_CONFLICT",
          "archived", "active", "total_messages", "total_attachment_meta",
          "threads_with_media_on_disk", "attachment_files_on_disk",
          "threads_with_external_media", "external_media_files", "VERDICT_COVERAGE"]:
    lines.append(f"| {k} | {s.get(k, '—')} |")
for k, n in v.most_common():
    lines.append(f"| verdict:{k} | {n} |")
lines += ["", "## Index (all threads)", "",
          "| Thread ID | Title | Date | Tags | Arch | Msgs | Att | Class | Verdict | Conf | Sev | Cx | Cluster | Dossier |",
          "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
for e in sorted(data["threads"], key=lambda x: x["created_at"] or ""):
    title = (e["title"] or "").replace("|", "/")[:55]
    date = (e["created_at"] or "")[:10]
    tags = ", ".join(e["tags"]) if e["tags"] else "—"
    lines.append(
        f"| {e['thread_id']} | {title} | {date} | {tags} | {'A' if e['archived'] else 'act'} "
        f"| {e['message_count']} | {e['attachment_count']} | {e['classification']} "
        f"| {e['verdict'] or '—'} | {e.get('confidence') or '—'} | {e.get('severity') or '—'} "
        f"| {e.get('complexity') or '—'} | {e.get('cluster') or '—'} | {e.get('dossier') or '—'} |")
with open(os.path.join(REPO, ".ai-triage", "BUG_INDEX.md"), "w", encoding="utf-8") as f:
    f.write("\n".join(lines) + "\n")

print(f"merged verdicts: {merged}; coverage: {data['summary']['VERDICT_COVERAGE']}/{s['NEEDS_TRIAGE']} needs-triage")
for k, n in v.most_common():
    print(f"  {k}: {n}")
