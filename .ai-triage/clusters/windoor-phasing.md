# Cluster: windoor-phasing

## Members

- 1388575425562673282 — Баг со столами и закрытыми кнопками (LIKELY_CURRENT_BUG/Medium)
- 1449508411325677692 — Noclip (LIKELY_CURRENT_BUG/Medium)

## Common symptom (from individual dossiers)

- 1388575425562673282: Падение со стола в downed-состоянии (eject-импульс + SlidingSystem) протыкает тонкую фикстуру закрытого windoor (дискретная физика, tunneling); под-баг с кнопкой/доступом не локализован
- 1449508411325677692: Гарпун не встраивается в закрытый windoor, а reel-joint (MinLength=1 защищает только стены) волочит игрока сквозь windoor — проверки препятствий между точками нет

## Root cause notes

Shared mechanism per member dossiers; where mechanisms diverge the cluster marks a failure FAMILY (same subsystem, distinct causes) rather than a single fix.

## Recommended action

Single fix only where dossiers confirm one root cause; otherwise coordinate fixes per member dossier's Proposed fix section to avoid duplicate investigation.

## Validation matrix

| Thread | Check | Expected |
|---|---|---|
| 1388575425562673282 | re-verify per dossier Validation plan | see dossier |
| 1449508411325677692 | re-verify per dossier Validation plan | see dossier |
