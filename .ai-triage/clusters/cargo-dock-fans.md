# Cluster: cargo-dock-fans

## Members

- 1417098657832112220 — Проблемы шаттла карго (CANNOT_VERIFY/Low)
- 1424014048726351937 — Не работает вентилятор (LIKELY_CURRENT_BUG/Medium)

## Common symptom (from individual dossiers)

- 1417098657832112220: Саркастичный однострочник без карты/медиа; кодово у AtmosDeviceFanDirectional нет зависимости от света/питания — вероятна маппинговая проблема как в 1424014048726351937
- 1424014048726351937: Вентилятор карго-дока на Box (box.yml uid 831, AtmosDeviceFanDirectional) не перекрывает проём — маппинговая неисправность (тайл/поворот/anchor), подтверждена маппером

## Root cause notes

Shared mechanism per member dossiers; where mechanisms diverge the cluster marks a failure FAMILY (same subsystem, distinct causes) rather than a single fix.

## Recommended action

Single fix only where dossiers confirm one root cause; otherwise coordinate fixes per member dossier's Proposed fix section to avoid duplicate investigation.

## Validation matrix

| Thread | Check | Expected |
|---|---|---|
| 1417098657832112220 | re-verify per dossier Validation plan | see dossier |
| 1424014048726351937 | re-verify per dossier Validation plan | see dossier |
