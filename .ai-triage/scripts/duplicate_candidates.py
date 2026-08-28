#!/usr/bin/env python3
"""
duplicate_candidates.py — candidate duplicate/cluster detection over thread
titles + root messages using token Jaccard similarity. Only a candidate list:
final duplicate decisions require root-cause verification per cluster.
Output: .ai-triage/data/duplicate_candidates.json
"""
import json, os, re, sys
from collections import defaultdict

REPO = sys.argv[1] if len(sys.argv) > 1 else "/home/z/my-project/erida-triage/erida"

STOP = set("""это для что как или не на и в с по у от до из-за при из о об а но же бы мне вас мы вы он она они оно
the a an and or of to in on for with at by is are was were be been being this that these those it its as from not no
yes very bug баг баги ошибка ошибки сломался сломана сломано сломались работает работаеть неработает
""".split())

def norm(s):
    s = (s or "").lower().replace("ё", "е")
    s = re.sub(r"[^\w\s]", " ", s)
    return [w for w in s.split() if len(w) > 2 and w not in STOP]

with open(os.path.join(REPO, ".ai-triage", "bug_index.json"), encoding="utf-8") as f:
    idx = json.load(f)

threads = [e for e in idx["threads"] if e["classification"] == "NEEDS_TRIAGE"]
sets = {}
texts = {}
for e in threads:
    root = e["root_message"] or {}
    text = (e["title"] or "") + " " + (root.get("content") or "")[:800]
    toks = set(norm(text))
    sets[e["thread_id"]] = toks
    texts[e["thread_id"]] = text[:160]

cands = []
ids = list(sets)
for i in range(len(ids)):
    for j in range(i + 1, len(ids)):
        a, b = sets[ids[i]], sets[ids[j]]
        if not a or not b:
            continue
        inter = len(a & b)
        if inter < 3:
            continue
        jac = inter / len(a | b)
        if jac >= 0.30:
            cands.append({"a": ids[i], "b": ids[j], "jaccard": round(jac, 3),
                          "shared": sorted(a & b)[:10],
                          "ta": texts[ids[i]], "tb": texts[ids[j]]})

cands.sort(key=lambda x: -x["jaccard"])
with open(os.path.join(REPO, ".ai-triage", "data", "duplicate_candidates.json"), "w", encoding="utf-8") as f:
    json.dump(cands, f, ensure_ascii=False, indent=1)
print("duplicate candidate pairs:", len(cands))
for c in cands[:25]:
    print(f"  {c['jaccard']:.2f}  [{c['a']}] {c['ta'][:60]}  <->  [{c['b']}] {c['tb'][:60]}")
