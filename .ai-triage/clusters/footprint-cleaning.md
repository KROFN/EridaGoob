# Cluster: footprint-cleaning

## Members

- 1368389167616098424 — Швабра не чистит следы (ALREADY_FIXED_IN_CURRENT_FORK/High)
- 1369020340520357968 — СЛЕДЫ КОШМАРЯТ НАС ВЕРСИЯ ДВА (ALREADY_FIXED_IN_CURRENT_FORK/Medium)
- 1391191286165540995 — Следы поскальзывают (LIKELY_CURRENT_BUG/Medium)

## Common symptom (from individual dossiers)

- 1368389167616098424: At report time mop had no footprint-cleaning path (no FloorCleaner component/system; dry mop only mopping-system-no-water); current fork scrubs footprints via FloorCleanerSystem
- 1369020340520357968: Report-era mop without FloorCleaner could not erase footprints; 'no water' vs 'mop full' popups stem from UseAbsorberSolution counting only Water as mopping ammo while reservoir fills with contaminants
- 1391191286165540995: Cleaning a footprint re-spills its solution as a puddle (FootprintCleanEvent->ToPuddle) and 50u tile overflow spawns real slippery puddles; non-evaporating lube makes trails effectively unerasesble while slipping cancels the mop DoAfter

## Root cause notes

Shared mechanism per member dossiers; where mechanisms diverge the cluster marks a failure FAMILY (same subsystem, distinct causes) rather than a single fix.

## Recommended action

Single fix only where dossiers confirm one root cause; otherwise coordinate fixes per member dossier's Proposed fix section to avoid duplicate investigation.

## Validation matrix

| Thread | Check | Expected |
|---|---|---|
| 1368389167616098424 | re-verify per dossier Validation plan | see dossier |
| 1369020340520357968 | re-verify per dossier Validation plan | see dossier |
| 1391191286165540995 | re-verify per dossier Validation plan | see dossier |
