#!/usr/bin/env python3
"""Freshness mapper v2: dossier evidence paths vs production delta.
Resolves paths against the git tree, handles - FILE: / inline / dir refs,
3-level ancestor subsystem matching. Outputs freshness_state.json + impacted_dossiers.md.
"""
import json, re, subprocess, sys, datetime, os
from collections import Counter

REPO = "/home/z/my-project/erida-triage/erida"
FROZEN = "origin/ai/discord-bug-triage"
ANALYZED_HEAD = "511cc23b7c596bdd2e12a3a12236db15a18ef309"
CURRENT_HEAD = subprocess.run(["git", "rev-parse", "upstream/master"], cwd=REPO,
                              capture_output=True, text=True).stdout.strip()
OUT_DIR = sys.argv[1] if len(sys.argv) > 1 else os.path.join(REPO, ".ai-triage/freshness")

def git(*args):
    return subprocess.run(["git", *args], cwd=REPO, capture_output=True, text=True).stdout

# ---- delta ----
delta = []
for line in git("diff", "--name-status", "-M", ANALYZED_HEAD, CURRENT_HEAD).splitlines():
    p = line.split("\t")
    if p[0].startswith("R"):
        delta.append(("RENAMED", p[1], p[2]))
    elif p[0] == "D":
        delta.append(("DELETED", p[1], None))
    elif p[0] == "A":
        delta.append(("ADDED", None, p[1]))
    else:
        delta.append(("MODIFIED", p[1], p[1]))
changed_paths = {x for d in delta for x in (d[1], d[2]) if x}

def ancestors(p, maxdepth=3):
    seg = p.split("/")
    return {"/".join(seg[:i]) for i in range(2, min(len(seg), maxdepth + 1))}

changed_dirs = set()
for p in changed_paths:
    changed_dirs |= ancestors(p)

# ---- tree files (resolve dossier refs) ----
tree = set(git("ls-tree", "-r", "--name-only", CURRENT_HEAD).splitlines())

# ---- actionable threads ----
idx = json.loads(git("show", f"{FROZEN}:.ai-triage/bug_index.json"))
actionable = [t for t in idx["threads"]
              if t.get("verdict") in ("CONFIRMED_CURRENT_BUG", "LIKELY_CURRENT_BUG")]

FILE_LINE = re.compile(r"^\s*-?\s*FILE:\s*(.+)$", re.M)
INLINE = re.compile(
    r"\b((?:Content(?:\.Goobstation|\.Common|\.Client|\.Server|\.Shared)?|Resources)"
    r"(?:/[\w.+-]+)+\.(?:cs|xaml|yml|ftl|json))")

def clean_ref(raw):
    out = []
    for tok in re.split(r"\s*\+\s*", raw):           # "a.yml + b.yml"
        tok = tok.strip().strip("`").rstrip(".,;:`*)")
        tok = re.sub(r"\s*[(\[].*$", "", tok)         # "(directory)" / "[SRC]"
        tok = re.sub(r":\d+.*$", "", tok)             # ":939,981"
        tok = tok.rstrip("/")
        if tok and ("/" in tok) and not tok.startswith(("Content", "Resources")):
            continue
        if tok: out.append(tok)
    return out

def resolve(ref):
    """-> (kind, resolved_path_or_None, candidates) kind in file|dir|missing"""
    if ref in tree:
        return ("file", ref, [])
    if any(f.startswith(ref + "/") for f in tree):
        return ("dir", ref, [])
    base = ref.rsplit("/", 1)[-1]
    cands = [f for f in tree if f.rsplit("/", 1)[-1] == base]
    if len(cands) == 1:
        return ("file", cands[0], cands)
    return ("missing", None, cands)

results = []
for t in actionable:
    tid = t["thread_id"]
    md = git("show", f"{FROZEN}:.ai-triage/bugs/{tid}.md")
    refs = []
    for m in FILE_LINE.finditer(md):
        refs += clean_ref(m.group(1))
    inline = {c for m in INLINE.finditer(md) for c in clean_ref(m.group(1))}
    refs = list(dict.fromkeys(refs))
    ev_files, ev_dirs, missing = set(), set(), set()
    for r in refs:
        kind, path, _ = resolve(r)
        if kind == "file": ev_files.add(path)
        elif kind == "dir": ev_dirs.add(path)
        else: missing.add(r)
    inl_files = set()
    for r in inline:
        kind, path, _ = resolve(r)
        if kind == "file": inl_files.add(path)
        elif kind == "dir": ev_dirs.add(path)

    direct, arch, weak, inl_hit = [], [], set(), []
    for f in sorted(ev_files):
        for st, old, new in delta:
            if old == f or (st == "RENAMED" and new == f):
                if st in ("DELETED", "RENAMED"):
                    arch.append(f"{f} [{st}" + (f" -> {new}]" if new else "]"))
                else:
                    direct.append(f)
                break
        else:
            if ancestors(f) & changed_dirs:
                weak.add(f)
    for d in ev_dirs:
        if d in changed_dirs:
            weak.add(d + "/")
    for f in sorted(inl_files - ev_files):
        if any(old == f for _, old, _ in delta):
            inl_hit.append(f)
        elif ancestors(f) & changed_dirs:
            weak.add(f + " (inline)")

    if arch:
        status = "ARCHITECTURE_CHANGED" if all("DELETED" in a or "RENAMED" in a for a in arch) and not direct else "REVALIDATION_REQUIRED"
    elif direct:
        status = "REVALIDATION_REQUIRED"
    elif weak:
        status = "SUBSYSTEM_TOUCHED"
    else:
        status = "UNCHANGED_SINCE_TRIAGE"
    results.append({
        "thread_id": tid, "title": t["title"], "verdict": t["verdict"],
        "evidence_files": sorted(ev_files), "evidence_dirs": sorted(ev_dirs),
        "unresolved_refs": sorted(missing),
        "direct_changed": direct, "architecture_changed": arch,
        "subsystem_touched": sorted(weak), "inline_changed": inl_hit,
        "status": status,
    })

now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
state = {
    "generated_at": now, "analyzed_head": ANALYZED_HEAD,
    "current_upstream_head": CURRENT_HEAD, "frozen_triage_branch": FROZEN,
    "delta": {"commit_count": git("rev-list", "--count", f"{ANALYZED_HEAD}..{CURRENT_HEAD}").strip(),
              "changed_file_count": len(changed_paths)},
    "classification_rules": {
        "REVALIDATION_REQUIRED": "direct evidence file modified in delta",
        "ARCHITECTURE_CHANGED": "evidence file deleted/renamed",
        "SUBSYSTEM_TOUCHED": "ancestor directory (<=3 levels) contains changed files",
        "UNCHANGED_SINCE_TRIAGE": "no referenced path touched (does NOT prove bug still exists)"},
    "dossiers": results,
}
os.makedirs(OUT_DIR, exist_ok=True)
json.dump(state, open(os.path.join(OUT_DIR, "freshness_state.json"), "w"), ensure_ascii=False, indent=1)

cnt = Counter(r["status"] for r in results)
L = ["# Freshness / delta revalidation — impacted dossiers", "",
     f"Generated: {now}", f"ANALYZED_HEAD: `{ANALYZED_HEAD}`",
     f"CURRENT_UPSTREAM_HEAD: `{CURRENT_HEAD}`",
     f"Delta: {state['delta']['commit_count']} commits, {len(changed_paths)} changed files",
     "", "| Status | Count |", "|---|---|"]
for k, v in cnt.most_common():
    L.append(f"| {k} | {v} |")
L += ["", "## Direct evidence file changed (revalidate before any fix)"]
for r in results:
    if r["direct_changed"] or r["architecture_changed"]:
        L.append(f"- **{r['thread_id']}** [{r['verdict']}] {r['title']}")
        L += [f"  - changed: `{p}`" for p in r["direct_changed"]]
        L += [f"  - {p}" for p in r["architecture_changed"]]
L += ["", "## Subsystem-level touches (weak signal)"]
for r in results:
    if r["status"] == "SUBSYSTEM_TOUCHED":
        L.append(f"- {r['thread_id']} [{r['verdict']}] {r['title']} → {', '.join('`'+s+'`' for s in r['subsystem_touched'])}")
open(os.path.join(OUT_DIR, "impacted_dossiers.md"), "w").write("\n".join(L) + "\n")

print("statuses:", dict(cnt))
print("state ->", os.path.join(OUT_DIR, "freshness_state.json"))
