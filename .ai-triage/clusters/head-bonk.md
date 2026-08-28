# Cluster: head-bonk

## Members

- 1368875720373309480 — Баг на следы от жидкостей (LIKELY_CURRENT_BUG/Low)
- 1395874643985829938 — Механика удара головой об предметы. (CONFIG_OR_CONTENT_ISSUE/Medium)

## Common symptom (from individual dossiers)

- 1368875720373309480: Сущность Footprint — статическое физическое тело с фикстурой (не декаль); контакт ползущего тела с ней мешает вставанию на тайле со следами
- 1395874643985829938: Bonk — спроектированное поведение: ClumsySystem.OnBeforeClimbEvent (при game.table_bonk=true шанс-ролл пропускается) + Bonkable столов Blunt 4; жалоба на баланс/тюнинг

## Root cause notes

Shared mechanism per member dossiers; where mechanisms diverge the cluster marks a failure FAMILY (same subsystem, distinct causes) rather than a single fix.

## Recommended action

Single fix only where dossiers confirm one root cause; otherwise coordinate fixes per member dossier's Proposed fix section to avoid duplicate investigation.

## Validation matrix

| Thread | Check | Expected |
|---|---|---|
| 1368875720373309480 | re-verify per dossier Validation plan | see dossier |
| 1395874643985829938 | re-verify per dossier Validation plan | see dossier |
