# Cluster: silicon-surgery-ui

## Members

- 1369257553430577222 — Сапожник без сапог (CANNOT_VERIFY/Low)
- 1372947789419516014 — ФПВ-дроны без админ-арбузов (CANNOT_VERIFY/Low)
- 1388553983613730969 — Медицинские юниты не могут начать операцию. (CANNOT_VERIFY/Low)

## Common symptom (from individual dossiers)

- 1369257553430577222: Мед-киборг не может открыть меню операции; в текущем коде блокера нет (SurgeryBui.RefreshUI гейтится SurgeryTargetComponent на ХИРУРГЕ — гипотеза), отчёты старше крупной переработки хирургии #4040
- 1372947789419516014: Мед FPV-дрон без limb-targeting/хирургии — часть кластера silicon-surgery-ui; доступы ЛКП/атмос для инж-дрона и WL-методичка — контентные решения
- 1388553983613730969: Тот же кластер silicon-surgery-ui: заявленный запрет интерфейсов силиконам в текущем коде отсутствует; симптом совпадает с 1369257553430577222

## Root cause notes

Shared mechanism per member dossiers; where mechanisms diverge the cluster marks a failure FAMILY (same subsystem, distinct causes) rather than a single fix.

## Recommended action

Single fix only where dossiers confirm one root cause; otherwise coordinate fixes per member dossier's Proposed fix section to avoid duplicate investigation.

## Validation matrix

| Thread | Check | Expected |
|---|---|---|
| 1369257553430577222 | re-verify per dossier Validation plan | see dossier |
| 1372947789419516014 | re-verify per dossier Validation plan | see dossier |
| 1388553983613730969 | re-verify per dossier Validation plan | see dossier |
