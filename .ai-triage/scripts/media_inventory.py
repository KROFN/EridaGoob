#!/usr/bin/env python3
"""
media_inventory.py — inventory of media files present on disk per thread,
cross-checked against attachment metadata (present / skipped / missing).
Output: .ai-triage/data/media_inventory.json
"""
import json, os, sys

EXPORT_DIR = sys.argv[1] if len(sys.argv) > 1 else "/home/z/my-project/discord-bug-export/export"
REPO = sys.argv[2] if len(sys.argv) > 2 else "/home/z/my-project/erida-triage/erida"

with open(os.path.join(REPO, ".ai-triage", "bug_index.json"), encoding="utf-8") as f:
    idx = json.load(f)

def filetype(fn):
    ext = os.path.splitext(fn)[1].lower()
    if ext in (".png", ".jpg", ".jpeg", ".webp"):
        return "image"
    if ext == ".gif":
        return "gif"
    if ext in (".mp4", ".webm", ".mov", ".mkv", ".avi"):
        return "video"
    return "other"

inv = {}
for e in idx["threads"]:
    tid = e["thread_id"]
    files = e["attachments_on_disk"]
    media = [{"file": fn, "path": os.path.join(EXPORT_DIR, "attachments", tid, fn), "kind": filetype(fn)} for fn in files]
    ext = [{"file": fn, "path": os.path.join(EXPORT_DIR, "external_media", tid, fn), "kind": filetype(fn)} for fn in e["external_media_files"]]
    if media or ext:
        inv[tid] = {"attachments": media, "external": ext}

# also record which NEEDS_TRIAGE threads have metadata attachments but no file on disk
missing = []
for e in idx["threads"]:
    if e["classification"] != "NEEDS_TRIAGE":
        continue
    # count metadata attachments with a download status other than skipped
    if e["attachment_count"] > 0 and not e["attachments_on_disk"]:
        missing.append({"thread_id": e["thread_id"], "title": e["title"], "attachment_count": e["attachment_count"]})

out = {"inventory": inv, "needs_triage_missing_media": missing}
with open(os.path.join(REPO, ".ai-triage", "data", "media_inventory.json"), "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=1)
print("threads with media:", len(inv), "| needs_triage threads with metadata but no file:", len(missing))
