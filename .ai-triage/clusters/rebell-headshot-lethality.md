# Cluster: rebell-headshot-lethality

## Members

- 1369105376288575589 — Заберите у него дебаг ган! (CANNOT_VERIFY/Medium)
- 1380911822634225724 — Что за фиговая система урона. (CONFIG_OR_CONTENT_ISSUE/High)

## Common symptom (from individual dossiers)

- 1369105376288575589: HYPOTHESIS: не спец-«дебаг ган», а общая ReBell-летальность ранений головы (TraumaSystem) + обычный пистолет; зомби-роли оружие не выдают, конкретный ствол не идентифицирован (скрин недоступен).
- 1380911822634225724: CONFIRMED (dev Yosif в треде): шансовая органная травма ReBell — TraumaSystem.Process.cs:286 (severity>=15) роллит TraumasChances[OrganDamage] (:481), мозг уничтожается (WoundSystem.Destruction.cs:265); дробь Каммерера копит severity через шлем.

## Root cause notes

Shared mechanism per member dossiers; where mechanisms diverge the cluster marks a failure FAMILY (same subsystem, distinct causes) rather than a single fix.

## Recommended action

Single fix only where dossiers confirm one root cause; otherwise coordinate fixes per member dossier's Proposed fix section to avoid duplicate investigation.

## Validation matrix

| Thread | Check | Expected |
|---|---|---|
| 1369105376288575589 | re-verify per dossier Validation plan | see dossier |
| 1380911822634225724 | re-verify per dossier Validation plan | see dossier |
