# Cluster: actionbar-reset-mind-transfer

## Members

- 1420383751082344479 — Маг (LIKELY_CURRENT_BUG/Medium)
- 1536503382355746886 — еретик с путем пепла (LIKELY_CURRENT_BUG/Low)

## Common symptom (from individual dossiers)

- 1420383751082344479: Панель действий мага рассыпается после астрала: действия хранятся/перевыдаются на разум (SpellsGrantSystem.OnMindAdded) и клиент перепривязывает кнопки при mind transfer, сбрасывая порядок.
- 1536503382355746886: Комплекс: подтверждён сброс панели действий после Пепельного Сдвига (общий корень с кластером actionbar-reset-mind-transfer); превью цели без Appearance/Loadout и отсутствие fire immunity на асценденте — гипотезы/контент-баланс (разраб: «Отказано»).

## Root cause notes

Shared mechanism per member dossiers; where mechanisms diverge the cluster marks a failure FAMILY (same subsystem, distinct causes) rather than a single fix.

## Recommended action

Single fix only where dossiers confirm one root cause; otherwise coordinate fixes per member dossier's Proposed fix section to avoid duplicate investigation.

## Validation matrix

| Thread | Check | Expected |
|---|---|---|
| 1420383751082344479 | re-verify per dossier Validation plan | see dossier |
| 1536503382355746886 | re-verify per dossier Validation plan | see dossier |
