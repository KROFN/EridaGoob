# Cluster: accent-localization-ru

## Members

- 1499505784931745963 — Нерабочий испанский акцент (CONFIG_OR_CONTENT_ISSUE/High)
- 1499847578563510303 — OWO акцент (LIKELY_CURRENT_BUG/Medium)

## Common symptom (from individual dossiers)

- 1499505784931745963: SpanishAccent умеет только s→es (латиница) и ¿/¡-пунктуацию; словаря словесных замен нет — для русского текста трейт инертен (контент/локализация).
- 1499847578563510303: Трейт 'отсутствие акцента' не содержит OwOAccent в removes-списке (канонический Accentless закомментирован); OwO фелинидам приходит из трейта/хэтов, плюс пасхалка GameTicker вешает OwOAccent после трейтов.

## Root cause notes

Shared mechanism per member dossiers; where mechanisms diverge the cluster marks a failure FAMILY (same subsystem, distinct causes) rather than a single fix.

## Recommended action

Single fix only where dossiers confirm one root cause; otherwise coordinate fixes per member dossier's Proposed fix section to avoid duplicate investigation.

## Validation matrix

| Thread | Check | Expected |
|---|---|---|
| 1499505784931745963 | re-verify per dossier Validation plan | see dossier |
| 1499847578563510303 | re-verify per dossier Validation plan | see dossier |
