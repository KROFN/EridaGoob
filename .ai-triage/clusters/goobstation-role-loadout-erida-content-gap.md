# Cluster: goobstation-role-loadout-erida-content-gap

## Members

- 1388579548357984378 — Бригмедик (CONFIG_OR_CONTENT_ISSUE/High)
- 1413573121369444403 — Верните ОСЩ трусы (CONFIG_OR_CONTENT_ISSUE/High)

## Common symptom (from individual dossiers)

- 1388579548357984378: Медали существуют как предметы (Entities/Clothing/Neck/medals.yml), но loadoutGroup/loadout с медалями никогда не создавалась и JobBrigmedic их не подключает.
- 1413573121369444403: Форковые группы белья Undershirt/Underwear/Socks добавлены PR 9ebb47b00c только в базовый role_loadouts.yml; roleLoadout JobBlueshieldOfficer в _Goobstation/Loadouts/role_loadouts.yml (25-45) их не содержит.

## Root cause notes

Shared mechanism per member dossiers; where mechanisms diverge the cluster marks a failure FAMILY (same subsystem, distinct causes) rather than a single fix.

## Recommended action

Single fix only where dossiers confirm one root cause; otherwise coordinate fixes per member dossier's Proposed fix section to avoid duplicate investigation.

## Validation matrix

| Thread | Check | Expected |
|---|---|---|
| 1388579548357984378 | re-verify per dossier Validation plan | see dossier |
| 1413573121369444403 | re-verify per dossier Validation plan | see dossier |
