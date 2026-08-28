# AI Triage Worklog — Discord Bug Audit (Erida / Space Station 14)

## Current state

- Phase: SETUP COMPLETE → ARCHIVE DOWNLOAD
- Working fork (writable, origin): `KROFN/EridaGoob` (default branch: `master`)
  - NOTE: prompt expected a repo named `erida-glob`; no such repo exists on the authenticated account. GitHub API scan (2 pages, 19 repos) found exactly one writable Erida fork: `KROFN/EridaGoob` (parent: `dead-space-server/EridaGoob`, source: `Goob-Station/Goob-Station`). Using it as the working repository.
- Upstream (READ ONLY): `dead-space-server/EridaGoob` (default branch: `master`)
- Working branch: `ai/discord-bug-triage`
- Local repo path: `/home/z/my-project/erida-triage/erida`
- Export extraction path (OUTSIDE git): `/home/z/my-project/discord-bug-export/`
- Archive path (OUTSIDE git): `/home/z/my-project/erida-triage/bug-reports-recovered.zip`
- Fork HEAD SHA (analyzed): `511cc23b7c596bdd2e12a3a12236db15a18ef309`
- origin/master HEAD: `511cc23b7c596bdd2e12a3a12236db15a18ef309`
- upstream/master HEAD: `511cc23b7c596bdd2e12a3a12236db15a18ef309`
- Divergence origin vs upstream: 0 commits (identical)
- Latest checkpoint commit: (initial)
- Next action: download Google Drive archive, validate, extract, parse.

## Rules of engagement

- First pass: NO production code changes. Only `.ai-triage/**` may be committed.
- Checkpoint after every meaningful batch.
- Never store PAT in repo, worklog, remote URL, or commit messages.

## Log

### Session 1 — 2026-08-28 (UTC+8)

- [x] GitHub PAT loaded into session (not stored in repo).
- [x] Authenticated via GitHub API as `KROFN`.
- [x] Repo discovery: `erida-glob` NOT found; `KROFN/EridaGoob` identified as the working fork.
- [x] Clone of `KROFN/EridaGoob` (98,545 files).
- [x] Remotes: origin = KROFN/EridaGoob, upstream = dead-space-server/EridaGoob.
- [x] Fetched upstream/master; SHAs recorded; fork == upstream (0 divergence).
- [x] Branch `ai/discord-bug-triage` created.
- [x] `.ai-triage/` structure created.
- [x] Download + validate bug archive.
- [x] Parse export.json, build BUG_INDEX (457 threads expected).

## Archive validation record

- Google Drive source: `https://drive.google.com/file/d/1TlOjsaTn_iuKc26S7amk3q1qhkirNol7/view?usp=sharing`
- ZIP path (outside git): `/home/z/my-project/erida-triage/bug-reports-recovered.zip`
- ZIP size: 228 MB (239,063,~ bytes as reported by gdown 239M)
- SHA256: `676e53bd26a9b0a9011a565694529c3eb4d15e4a86ee1becc6cb3dfb145452d6`
- `unzip -t`: OK, no errors. 302 files, ~260 MB uncompressed.
- Internal root folder (Cyrillic, normalized on extraction): `_баг-репорты_2026-08-28_12-19-07-167/`
- Extraction path: `/home/z/my-project/discord-bug-export/export/`

### Validation vs baseline (ALL MATCH)

| Metric | Baseline | Actual |
|---|---|---|
| unique threads | 457 | 457 |
| unique messages | 5197 | 5197 (0 duplicate ids) |
| archived threads | 436 | 436 |
| active threads | 21 | 21 |
| attachment metadata | 640 | 640 |
| attachment files on disk | 294 (actual threads) | 294 |
| download jobs | 315 | 315 |
| downloaded | 299 | 299 (294 att + 5 external) |
| failed | 16 (all external) | 16, all `kind=external`, all HTTP 404 |
| skipped by tag (Исправлено/Не баг) | 346 | 346 |
| NEEDS_TRIAGE threads missing downloaded media | 0 expected | 0 |

- recovery_report.json summary: recovered_at 2026-08-28T12:45:54Z, external_enabled: true.
- Forum channel: `📮・баг-репорты` (type 15), guild 1357728304710422680.
- Thread date range: 2025-04-21 → 2026-08-27.

### Tag distribution (threads; a thread may have several tags)

`Исправлено` 182 · `Не баг` 64 · `Разработка` 41 · `unknown_tag_1414266059208265799` 188 ·
`unknown_tag_1365427630660128861` 22 · `В процессе` 20 · `На рассмотрении` 20 · `Визден-Баг` 19 ·
`Незначительный` 18 · `Дискорд-Бот` 13 · `Маппинг` 9 · `Серьёзный` 3 · no tags 60.

Unknown tags cannot be resolved without a Discord bot token; per protocol they are NOT
treated as resolved/not-bug. Both unknown-tag groups contain genuine bug reports.

### Classification (initial, mechanical)

| Class | Count |
|---|---|
| TOTAL | 457 |
| SKIP_RESOLVED (tag Исправлено) | 182 |
| SKIP_NOT_BUG (tag Не баг) | 63 |
| NEEDS_TRIAGE | 212 |
| TAG_CONFLICT | 22 |

## Log
- [ ] Full triage pass.
- [ ] TRIAGE_REPORT.md.
