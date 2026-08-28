# TRIAGE PROTOCOL (strict, read fully before investigating)

You are investigating Discord bug reports against the CURRENT working fork of
Erida / Space Station 14 (SS14 fork; parent: dead-space-server/EridaGoob; source: Goob-Station).

Repo root (read-only for production code!): /home/z/my-project/erida-triage/erida
Discord export (media + raw data, outside git): /home/z/my-project/discord-bug-export/export

## Absolute rules

1. NEVER modify production code. You may ONLY write:
   - /home/z/my-project/erida-triage/erida/.ai-triage/bugs/<thread_id>.md   (dossier, one per thread)
   - /home/z/my-project/erida-triage/erida/.ai-triage/data/verdicts/batch_<batch>.json (verdicts)
   - /home/z/my-project/erida-triage/erida/.ai-triage/clusters/<cluster-id>.md (ONLY when you have confirmed 2+ threads share one root cause)
2. NEVER store, echo, or commit any credentials/tokens.
3. Evidence standard: a guess is NOT a root cause. Every dossier must cite real files
   (full paths) and symbols you actually found via search. If you cannot prove it, write
   HYPOTHESIS with confidence, or verdict CANNOT_VERIFY. Prefer CANNOT_VERIFY over fiction.
4. Discord report ≠ current bug. The report may be old. ALWAYS check history:
   - `git log --oneline --since=<report date> -- <path>` on relevant files
   - `git log -S'<symbol>' --oneline --all | head -20`
   If the fork already contains a change that fixes the described problem → ALREADY_FIXED_IN_CURRENT_FORK with commit evidence.
5. Do NOT load whole files blindly; use targeted search (rg), read only relevant fragments.

## Search workflow per thread

1. Read the thread data: .ai-triage/data/threads/<thread_id>.json
   (contains title, root message, replies, media file lists, dates, tags).
2. Read/inspect media when it matters: files under
   /home/z/my-project/discord-bug-export/export/attachments/<thread_id>/
   - Images: use the Read tool (it renders images).
   - GIF: Read shows first frame only — treat as hint, not proof for dynamic bugs.
   - Video: `ffprobe -hide_banner <file>`; if needed extract frames:
     `ffmpeg -y -i <file> -vf fps=1/2 /tmp/frames_<tid>_%03d.jpg` then Read frames.
   - Classify media: BUG_EVIDENCE / REPRODUCTION_EVIDENCE / REACTION_MEME / UNRELATED_MEDIA.
3. Build search vocabulary: user terms (often Russian) → SS14 domain terms in English
   (e.g. "визор"→visor/HUD; "скаф"→hardsuit/suit; "шаттл"→shuttle/docking; "следы"→footprints/slip;
   "конвейер"→conveyor; "доступ"→access; "шлюз"→airlock).
4. Search the repo:
   - `rg --files | rg -i '<keyword>'`
   - `rg -n -i '<keyword>' -g '*.cs' -g '*.yml' -g '*.ftl'` (add -g '!bin/**' -g '!obj/**' when needed)
   - Priority order: Resources/Prototypes (YAML) → fork-specific content dirs →
     Resources/Locale (ftl) → Content.Shared* → Content.Server* → Content.Client* → maps → RSI.
5. If a prototype/entity is found: trace parent chain, inherited components, overrides,
   component class, system classes, locale keys.
6. History: `git log` / `git blame` on found files, compare with report date.
7. Upstream comparison when relevant: `git log upstream/master --oneline -- <path> | head`.

## Dossier format (write EXACTLY this structure, in Russian where natural, paths/symbols in English)

# <Discord title>

## Metadata
Thread ID: / Date: / Author: / Tags: / Archive state: / Messages: / Attachments: (count + kinds)

## Discord evidence
- description, reproduction steps if present, expected vs actual, notable replies, media evidence
- (mark media classification)

## Search vocabulary
User terms: / Domain terms: / Prototype-entity candidates: / Code symbols:

## Repository investigation
For each finding:
FILE: path
SYMBOL: class/method/prototype id/locale key
WHY RELEVANT: ...
CURRENT BEHAVIOR: ...

## History
Relevant commits (sha + subject + date), changes after report date, or "no relevant commits found".

## Upstream comparison
Erida upstream: ... / Goob: ... / SS14: ... (if applicable; may be "not investigated — local evidence sufficient")

## Verdict
Exactly ONE of:
- CONFIRMED_CURRENT_BUG (code path + causal chain + evidence)
- LIKELY_CURRENT_BUG (strong hypothesis, some gaps)
- ALREADY_FIXED_IN_CURRENT_FORK (commit sha proof)
- ALREADY_FIXED_UPSTREAM (commit/PR proof)
- DUPLICATE (point to primary thread id + shared root cause)
- CONFIG_OR_CONTENT_ISSUE (works as coded; change is content/config decision)
- USER_ERROR_OR_NOT_BUG (rules/PC hardware/wiki/admin request/out of game scope)
- CANNOT_VERIFY (insufficient info to reproduce or locate)

## Confidence
High / Medium / Low

## Root cause
CONFIRMED: ... (files+symbols+causal chain) or HYPOTHESIS: ... (confidence)

## Proposed fix (do NOT implement!)
files to touch, symbols, minimal change sketch, why it fixes root cause

## Regression risk / Validation plan / Links-Related threads

## Severity & complexity (if actionable)
Severity: S0 BLOCKER | S1 CRITICAL | S2 MAJOR | S3 MINOR | S4 COSMETIC
Complexity: XS | S | M | L | XL

## Verdict JSON (also write to batch file)
Write a JSON array to .ai-triage/data/verdicts/batch_<batch>.json:
[{"thread_id": "...", "verdict": "...", "confidence": "High|Medium|Low",
  "severity": "S2", "complexity": "S", "cluster_hint": "short-slug-or-null",
  "root_cause_short": "one line", "evidence": ["path:symbol", "..."],
  "dossier": ".ai-triage/bugs/<thread_id>.md"}]
