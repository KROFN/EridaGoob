# Cluster: species-survival-box-loadout-effects

## Members

- 1388579685453135994 — Аварийные наборы (ALREADY_FIXED_IN_CURRENT_FORK/Medium)
- 1422135237755932723 — Лодаут шадовкинов (ALREADY_FIXED_IN_CURRENT_FORK/Medium)

## Common symptom (from individual dossiers)

- 1388579685453135994: На дату репорта лодаут-реворк был незавершён; сейчас бригмедик получает SurvivalSecurity, врач (хирург = alt-title MedicalDoctor) — SurvivalMedical (hidden, minLimit 3); вида Arkan в форке нет (порт отдельным PR).
- 1422135237755932723: Регрессия: вид Shadowkin временно выпадал из loadoutEffectGroup OxygenBreather при синке — hidden-группа Survival (minLimit 3) не находила подходящего loadout и боксы не спавнились; сейчас Shadowkin (и Hydrakin) в OxygenBreather, игрок подтвердил «Исправлено».

## Root cause notes

Shared mechanism per member dossiers; where mechanisms diverge the cluster marks a failure FAMILY (same subsystem, distinct causes) rather than a single fix.

## Recommended action

Single fix only where dossiers confirm one root cause; otherwise coordinate fixes per member dossier's Proposed fix section to avoid duplicate investigation.

## Validation matrix

| Thread | Check | Expected |
|---|---|---|
| 1388579685453135994 | re-verify per dossier Validation plan | see dossier |
| 1422135237755932723 | re-verify per dossier Validation plan | see dossier |
