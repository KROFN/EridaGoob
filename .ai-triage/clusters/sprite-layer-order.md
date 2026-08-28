# Cluster: sprite-layer-order (хвосты над одеждой/телом)

## Members
| Thread | Title | Verdict | Confidence | Sev/Cx |
|---|---|---|---|---|
| 1379120791253418124 | Хвост хаски в лобби (первичный) | CONFIRMED_CURRENT_BUG | High | S4/S |
| 1379904937223520296 | Баг с юбкой-комбинезоном и хвостами | CONFIRMED_CURRENT_BUG | High | S4/S |
| 1382299238423068682 | Хвост кицунэ (+ предметы в руках) | CONFIRMED_CURRENT_BUG | High | S4/S |
| 1471561763647389861 | Мышиный хвост «шишкой» спереди | CONFIRMED_CURRENT_BUG | High | S4/S |

(в досье членов кластер внутренне именовался «marking-layer-order» — это тот же кластер)

## Shared symptom
Tail-marking персонажа отрисовывается ПОВЕРХ одежды и тела на одном или нескольких ракурсах:
- хаски/оти/олень — хвост перекрывает торс/комбинезон спереди (в т.ч. в лобби-превью);
- кицунэ — хвост над одеждой на side-left/back;
- Rodentia — «шишка» хвоста над комбинезоном на front.
Доп. (только 1382299238423068682): предметы в руках рисуются над хвостом.

## Root cause (один на всех)
1. Видовые sprite-слои ставят `enum.HumanoidVisualLayers.Tail` ПОСЛЕ одежды:
   - Resources/Prototypes/_Erida/Entities/Mobs/Species/anthropomorph.yml:109 (после jumpsuit 84/shoes/outerClothing);
   - Resources/Prototypes/_DV/Entities/Mobs/Species/rodentia.yml:91;
   - родовой источник: Resources/Prototypes/Entities/Mobs/Species/base.yml:57 (BaseMobSpeciesOrganic) и :420 (BaseSpeciesDummy — лобби-doll).
2. Content.Client/Humanoid/HumanoidAppearanceSystem.cs:ApplyMarking вставляет marking-спрайт на `targetLayer+1` слоя Tail → хвост над jumpsuit/shoes на всех 4 направлениях.
3. Tail-marking'и (mam_tails.rsi, tail_markings.rsi#mouse) не имеют `layering:` на TailBehind — механизм MarkingPrototype.Layering уже портирован (a2ba0ebe00, 2026-08-01; MarkingPrototype.cs:63), но для хвостов не применён; front-кадры спрайтов содержат пиксели в зоне торса.
4. (Вторичная, 1382299238423068682) Content.Client/Hands/Systems/HandsSystem.cs:342 — `LayerMapReserve` добавляет hand-слои в конец спрайта, выше любых статических слоёв.

## Single recommended fix
Контентный, per-marking (безопаснее переноса слоя): для всех хвостов mam_tails (`Resources/Prototypes/_Erida/Customization/Markings/anthropomorph.yml`, все `AnthropomorphTail*`) и rodentia (`Resources/Prototypes/_DV/Entities/Mobs/Customization/Markings/rodentia.yml`, все `RodentiaTail*`) задать `layering:` на `TailBehind`/`TailBehindBackpack` по образцу `_Imp/Mobs/Customization/moth.yml:646` (LunaWings behind/front-части). Альтернатива XS с большим риском: в species-файлах перенести слой Tail выше Groin/Chest (изменит вид ВСЕХ хвостов вида). «Хвост над предметами в руках» этим фиксом не решается (динамические hand-слои) — отдельная оценка.
Validation: антропоморф (husky/oti/deer/kitsune) и Rodentia в комбинезоне/броне/скафандре, 4 ракурса + лобби-превью (MobAnthropomorphDummy / MobRodentiaDummy).
Severity: S4 COSMETIC / Complexity: S (per-marking) — единая оценка кластера.

## Excluded (смежные, иная причина)
1393135432060899379, 1453499614710857729 — бельё/носки: порядок слоёв КОРРЕКТЕН, причина — видовая неподгонка спрайтов и отсутствие displacement → кластер `underwear-sprite-fit`.
