# Cluster: duplicate-loadout-group-labels

## Members
- 1365350238667280396 (две вкладки безделушек, инженер)
- 1366049076361166888 (две иконки безделушек, инженер + техассистент)
- 1388579384419553460 (два раздела униформы, психолог)

## Common symptom
В редакторе лодаута отображались несколько секций с одинаковым названием («Безделушки», «Униформа») — визуальные «дубли».

## Actual shared root cause
В старом Goobstation-лайнадже roleLoadout ролей содержал НЕСКОЛЬКО loadout-групп одного класса (общая `Trinkets` + должностная `*JobTrinkets`; аналогично униформ-группы), отображавшиеся одним и тем же локализованным именем → UI показывал «одинаковые» вкладки/секции.

## Relevant code (current)
- Resources/Prototypes/Loadouts/role_loadouts.yml — JobStationEngineer/JobTechnicalAssistant (Trinkets + *JobTrinkets), JobPsychologist (одна униформ-группа).
- Resources/Locale/en-US/preferences/loadout-groups.ftl:26-27 — `loadout-group-trinkets = Trinkets` vs `loadout-group-jobtrinkets = Job trinkets`.
- Коммит 12766fe6e3 «Loadouts redux (#25715)» — переработка, разделившая имена.

## Status
ALREADY_FIXED_IN_CURRENT_FORK (и в upstream): имена групп теперь различны; «дублей» нет.

## Recommended action
Ничего не требуется. Опционально: различить русскую локализацию («Безделушки» / «Должностные безделушки») для UX-ясности.

## Validation matrix
| Thread | Check | Expected |
|---|---|---|
| 1365350238667280396 | лодаут инженера | вкладки Trinkets / Job trinkets различимы |
| 1366049076361166888 | лодаут техассистента | то же |
| 1388579384419553460 | лодаут психолога | один раздел униформы |
