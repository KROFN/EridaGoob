# Freshness / delta revalidation subsystem

Purpose: avoid re-running the full 212-dossier audit after every upstream sync.

Cycle: fetch upstream → compare OLD_VALIDATED_HEAD...NEW_HEAD → identify impacted
dossiers → revalidate only impacted findings + selected next candidates → choose fix →
clean branch → implement → adversarial review → test → human PR approval.

## Files

- `freshness_state.json` — machine-readable state: analyzed HEAD, current upstream HEAD,
  delta stats, per-dossier classification + lead revalidation notes.
- `impacted_dossiers.md` — human-readable delta impact view.
- `scripts/map_changed_paths.py` — the mapper (source copy also kept outside the repo).

## Current run

- ANALYZED_HEAD: `511cc23b7c596bdd2e12a3a12236db15a18ef309` (triage-era production HEAD)
- CURRENT_UPSTREAM_HEAD: `28d0c86f9d2e2a502dfb422f5b2fd9eaa7df5a53`
- Delta: 2 commits (large Goob/Trauma upstream sync #36 + automatic changelog), 612 changed files.

## Status semantics

- `REVALIDATION_REQUIRED` — direct evidence file modified by delta; re-check before any fix.
- `ARCHITECTURE_CHANGED` — evidence file deleted/renamed, or the causal model itself replaced.
- `SUBSYSTEM_TOUCHED` — only an ancestor directory (≤3 levels) contains changes; weak signal.
- `UNCHANGED_SINCE_TRIAGE` — no referenced path touched. This does NOT prove the bug still
  exists; it only means the original source evidence was not directly invalidated.
- `REVALIDATED_STILL_PRESENT` — lead independently confirmed the bug signature on current HEAD.

## Key outcome of this run

- 9/9 verifiable TOP-10 findings re-confirmed present on current HEAD.
- IPC/КПБ acid (1537354952094257172): **ARCHITECTURE_CHANGED** — old root cause no longer
  exists (wound treatment moved from C# classification to YAML trauma definitions; Caustic
  wound entity + Caustic-healing reagents appeared). Old proposed fix is STALE. Do not
  implement from the old dossier; full re-investigation required.
- Wound/trauma/Shitmed dossiers: mass SUBSYSTEM_TOUCHED (weak signal) due to sync #36.
- First production fix candidate 1473337621521367151 (uranium directional windows):
  REVALIDATED_STILL_PRESENT, evidence base untouched by delta.
