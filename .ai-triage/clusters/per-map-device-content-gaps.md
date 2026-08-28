# Cluster: per-map-device-content-gaps

## Members

- 1416386325006778440 — Алё АВД? Чего? мы вас не слышим (CONFIG_OR_CONTENT_ISSUE/High)
- 1514984863562727596 — как смотреть (CONFIG_OR_CONTENT_ISSUE/High)

## Common symptom (from individual dossiers)

- 1416386325006778440: Maps lack telecom servers carrying the law-department encryption key, so the law radio frequency is relayed nowhere (dev-confirmed in thread)
- 1514984863562727596: Train map camera entities exist (156 SurveillanceCamera occurrences) but are not linked to the SB surveillance camera server, so SB monitor lists nothing (mapper-confirmed)

## Root cause notes

Shared mechanism per member dossiers; where mechanisms diverge the cluster marks a failure FAMILY (same subsystem, distinct causes) rather than a single fix.

## Recommended action

Single fix only where dossiers confirm one root cause; otherwise coordinate fixes per member dossier's Proposed fix section to avoid duplicate investigation.

## Validation matrix

| Thread | Check | Expected |
|---|---|---|
| 1416386325006778440 | re-verify per dossier Validation plan | see dossier |
| 1514984863562727596 | re-verify per dossier Validation plan | see dossier |
