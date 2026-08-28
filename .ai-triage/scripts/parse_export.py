#!/usr/bin/env python3
"""
parse_export.py — Parse Discord bug-forum export into compact per-thread JSON
plus aggregate stats. Raw export stays OUTSIDE git; derived compact JSON
(structured triage metadata only, no full message dump) goes to .ai-triage/data/.

Usage: python3 parse_export.py <export_dir> <repo_root>
"""
import json, os, re, sys
from collections import Counter

EXPORT_DIR = sys.argv[1] if len(sys.argv) > 1 else "/home/z/my-project/discord-bug-export/export"
REPO = sys.argv[2] if len(sys.argv) > 2 else "/home/z/my-project/erida-triage/erida"
DATA = os.path.join(REPO, ".ai-triage", "data", "threads")
os.makedirs(DATA, exist_ok=True)

TAG_RESOLVED = "Исправлено"
TAG_NOTBUG = "Не баг"
TAG_CONFLICT_TAGS = {"В процессе", "На рассмотрении", "Разработка"}

IDENT_RE = re.compile(r"\b[A-Za-z][A-Za-z0-9_.\-]{2,}\b")

def classify(tags):
    tags = tags or []
    conflict = False
    if TAG_RESOLVED in tags:
        if any(t in TAG_CONFLICT_TAGS for t in tags):
            conflict = True
        return "SKIP_RESOLVED", conflict
    if TAG_NOTBUG in tags:
        if any(t in TAG_CONFLICT_TAGS for t in tags):
            conflict = True
        return "SKIP_NOT_BUG", conflict
    return "NEEDS_TRIAGE", False

def attachments_on_disk(tid):
    d = os.path.join(EXPORT_DIR, "attachments", tid)
    if not os.path.isdir(d):
        return []
    return sorted(os.listdir(d))

def external_media(tid):
    d = os.path.join(EXPORT_DIR, "external_media", tid)
    if not os.path.isdir(d):
        return []
    return sorted(os.listdir(d))

def extract_mentions(text):
    if not text:
        return []
    # identifiers that look like code symbols / prototype ids (latin, len>=3)
    ids = set()
    for m in IDENT_RE.findall(text):
        if m.lower() in {"the", "and", "for", "you", "not", "bug", "all", "can", "any", "was", "out", "has", "get", "one", "two"}:
            continue
        ids.add(m)
    return sorted(ids)[:40]

def compact_message(m, max_len=1200):
    a = m.get("author") or {}
    att_meta = m.get("attachment_meta") or []
    atts = []
    for x in att_meta:
        if isinstance(x, dict):
            atts.append({
                "id": x.get("id"),
                "filename": x.get("filename"),
                "content_type": x.get("content_type"),
                "download_status": x.get("download_status"),
                "local_path": x.get("local_path"),
            })
        else:
            atts.append(str(x))
    content = (m.get("content") or "").strip()
    return {
        "id": m.get("id"),
        "date": m.get("date"),
        "author": a.get("display") or a.get("username") or str(a.get("id")),
        "author_role": a.get("server_nick"),
        "content": content[:max_len],
        "content_truncated": len(content) > max_len,
        "attachments": atts,
        "reactions": m.get("reactions") or [],
    }

def main():
    with open(os.path.join(EXPORT_DIR, "export.json"), encoding="utf-8") as f:
        data = json.load(f)

    threads = data["threads"]
    index = []
    for t in threads:
        tid = t["id"]
        tags = t.get("tags") or []
        cls, conflict = classify(tags)
        msgs = t.get("messages") or []
        root = compact_message(msgs[0], max_len=3000) if msgs else None
        # follow-ups: skip root, keep up to 14 most informative (with attachments or longer)
        follow = [compact_message(m, max_len=900) for m in msgs[1:]]
        follow.sort(key=lambda x: (bool(x["attachments"]), len(x["content"])), reverse=True)
        follow = sorted(follow[:14], key=lambda x: x["date"] or "")
        disk_att = attachments_on_disk(tid)
        ext = external_media(tid)
        full_root_text = (msgs[0].get("content") or "") if msgs else ""
        entry = {
            "thread_id": tid,
            "title": t.get("title"),
            "author": t.get("author") or {},
            "created_at": t.get("created_at"),
            "archived": bool(t.get("archived")),
            "tags": tags,
            "tag_ids": t.get("tag_ids") or [],
            "message_count": len(msgs),
            "attachment_count": len([a for m in msgs for a in (m.get("attachment_meta") or [])]),
            "attachments_on_disk": disk_att,
            "external_media_files": ext,
            "classification": cls,
            "tag_conflict": conflict,
            "root_message": root,
            "replies": follow,
            "mentions": extract_mentions(full_root_text),
            "verdict": None,
            "cluster": None,
            "dossier": None,
        }
        with open(os.path.join(DATA, f"{tid}.json"), "w", encoding="utf-8") as f:
            json.dump(entry, f, ensure_ascii=False, indent=1)
        index.append(entry)

    # ---- aggregate summary ----
    c = Counter(e["classification"] for e in index)
    conflicts = [e for e in index if e["tag_conflict"]]
    years = Counter((e["created_at"] or "")[:7] for e in index)

    summary = {
        "TOTAL": len(index),
        "SKIP_RESOLVED": c.get("SKIP_RESOLVED", 0),
        "SKIP_NOT_BUG": c.get("SKIP_NOT_BUG", 0),
        "NEEDS_TRIAGE": c.get("NEEDS_TRIAGE", 0),
        "TAG_CONFLICT": len(conflicts),
        "archived": sum(1 for e in index if e["archived"]),
        "active": sum(1 for e in index if not e["archived"]),
        "total_messages": sum(e["message_count"] for e in index),
        "total_attachment_meta": sum(e["attachment_count"] for e in index),
        "threads_with_media_on_disk": sum(1 for e in index if e["attachments_on_disk"]),
        "attachment_files_on_disk": sum(len(e["attachments_on_disk"]) for e in index),
        "threads_with_external_media": sum(1 for e in index if e["external_media_files"]),
        "external_media_files": sum(len(e["external_media_files"]) for e in index),
    }

    with open(os.path.join(REPO, ".ai-triage", "data", "summary.json"), "w", encoding="utf-8") as f:
        json.dump(summary, f, ensure_ascii=False, indent=1)
    with open(os.path.join(REPO, ".ai-triage", "bug_index.json"), "w", encoding="utf-8") as f:
        json.dump({"summary": summary, "threads": index}, f, ensure_ascii=False, indent=1)

    # ---- BUG_INDEX.md ----
    lines = ["# BUG INDEX — Discord bug-forum export (Erida)", "",
             f"Source: Google Drive archive `1TlOjsaTn_iuKc26S7amk3q1qhkirNol7`, exported_at `{data['exported_at']}`.", "",
             "## Summary", "",
             "| Metric | Count |", "|---|---|"]
    for k, v in summary.items():
        lines.append(f"| {k} | {v} |")
    lines += ["", "Tag conflicts (resolved + in-progress style tags present):"]
    for e in conflicts:
        lines.append(f"- {e['thread_id']} — {e['title']} — tags: {', '.join(e['tags'])}")
    lines += ["", "## Index (all threads)", "",
              "| Thread ID | Title | Date | Tags | Arch | Msgs | Att | Class | Verdict | Cluster | Dossier |",
              "|---|---|---|---|---|---|---|---|---|---|---|"]
    for e in sorted(index, key=lambda x: x["created_at"] or ""):
        title = (e["title"] or "").replace("|", "/")[:60]
        date = (e["created_at"] or "")[:10]
        tags = ", ".join(e["tags"]) if e["tags"] else "—"
        lines.append(
            f"| {e['thread_id']} | {title} | {date} | {tags} | {'A' if e['archived'] else 'act'} "
            f"| {e['message_count']} | {e['attachment_count']} | {e['classification']} "
            f"| {e['verdict'] or '—'} | {e['cluster'] or '—'} | {e['dossier'] or '—'} |")
    with open(os.path.join(REPO, ".ai-triage", "BUG_INDEX.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")

    print(json.dumps(summary, ensure_ascii=False, indent=1))
    print(f"\nper-thread JSON written: {len(index)} files in {DATA}")

if __name__ == "__main__":
    main()
