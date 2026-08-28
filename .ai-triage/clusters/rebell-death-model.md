# Cluster: rebell-death-model

## Members

- 1370396275329073172 — Я умер насмерть. (LIKELY_CURRENT_BUG/Medium)
- 1375074483001491557 — Бесмертие(конечно пока твою голову не раздавят) (CONFIRMED_CURRENT_BUG/High)

## Common symptom (from individual dossiers)

- 1370396275329073172: Смерть при вставании/мгновенная повторная смерть после ревайва: накопленный wound/trauma урон добивает MobThresholds, ревайв не чистит раны и PainShock-парализации
- 1375074483001491557: Бессмертие при 0 крови/макс. кровотечении: ReBell UpdateMobState закомментирован, смерть только по MobThresholds/ForceDead-мозгу/DelayedDeath (сердце+мозг), Bloodloss-урон перехватывается раневой моделью

## Root cause notes

Shared mechanism per member dossiers; where mechanisms diverge the cluster marks a failure FAMILY (same subsystem, distinct causes) rather than a single fix.

## Recommended action

Single fix only where dossiers confirm one root cause; otherwise coordinate fixes per member dossier's Proposed fix section to avoid duplicate investigation.

## Validation matrix

| Thread | Check | Expected |
|---|---|---|
| 1370396275329073172 | re-verify per dossier Validation plan | see dossier |
| 1375074483001491557 | re-verify per dossier Validation plan | see dossier |
