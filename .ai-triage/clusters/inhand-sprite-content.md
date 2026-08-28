# Cluster: inhand-sprite-content

## Members

- 1449885909653651496 — Некорректное отображение (LIKELY_CURRENT_BUG/Medium)
- 1535027750082056404 — Чемодан (LIKELY_CURRENT_BUG/Medium)

## Common symptom (from individual dossiers)

- 1449885909653651496: У RSI интековского ПП / mg-90l отсутствует state `inhand-right` (вторая рука) — ItemSystem.OnGetVisuals/TryGetDefaultVisuals не находят состояние и рука рендерится пустой.
- 1535027750082056404: Крупные 32x32 боковые inhand-left/right состояния briefcase_brown.rsi рендерятся на held-слое носителя без оффсетов и пересекают ноги унатха.

## Root cause notes

Shared mechanism per member dossiers; where mechanisms diverge the cluster marks a failure FAMILY (same subsystem, distinct causes) rather than a single fix.

## Recommended action

Single fix only where dossiers confirm one root cause; otherwise coordinate fixes per member dossier's Proposed fix section to avoid duplicate investigation.

## Validation matrix

| Thread | Check | Expected |
|---|---|---|
| 1449885909653651496 | re-verify per dossier Validation plan | see dossier |
| 1535027750082056404 | re-verify per dossier Validation plan | see dossier |
