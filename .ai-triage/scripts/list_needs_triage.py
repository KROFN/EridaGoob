#!/usr/bin/env python3
"""List NEEDS_TRIAGE threads compactly for bucketing (title + first 160 chars of root)."""
import json, os

REPO = "/home/z/my-project/erida-triage/erida"
with open(os.path.join(REPO, ".ai-triage", "bug_index.json"), encoding="utf-8") as f:
    idx = json.load(f)

n = 0
for e in sorted(idx["threads"], key=lambda x: x["created_at"] or ""):
    if e["classification"] != "NEEDS_TRIAGE":
        continue
    n += 1
    root = e["root_message"] or {}
    txt = (root.get("content") or "").replace("\n", " ")[:160]
    att = len(e["attachments_on_disk"])
    print(f"{n:03d} [{e['thread_id']}] {(e['created_at'] or '')[:10]} att={att} | {e['title']}")
    print(f"     {txt}")
print(f"\nNEEDS_TRIAGE total: {n}")
