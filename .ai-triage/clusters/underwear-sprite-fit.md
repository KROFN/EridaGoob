# Cluster: underwear-sprite-fit (бельё/носки на нечеловеческих видах)

## Members
| Thread | Title | Verdict | Confidence | Sev/Cx |
|---|---|---|---|---|
| 1393135432060899379 | Носки и ящеры с антропоморфами (первичный) | CONFIG_OR_CONTENT_ISSUE | Medium | S4/S |
| 1453499614710857729 | Нианы 2.0 — нижнее бельё (ноги) | CONFIG_OR_CONTENT_ISSUE | Medium | S4/S |

## Shared symptom
Пиксели белья/носков видны там, где их быть не должно: «вылезает через одежду» — из-под ботинок и комбинезонов на нечеловеческих видах (ящеры, моль/Нианы, антропоморфы). Порядок слоёв при этом КОРРЕКТЕН (socks/UndergarmentBottom ниже jumpsuit/shoes) — это не кластер sprite-layer-order.

## Root cause (один на всех)
Видовая неподгонка бельевых спрайтов + отсутствие displacement-поддержки для бельевых слоёв/слотов:
1. Универсальные человеческие спрайты: `Resources/Textures/Mobs/Customization/underwear.rsi` (марки Underwear*, cmss13 origin, видов нет), `Mobs/Customization/undergarments.rsi` (только _reptilian/_vox, `_moth` нет), `_Erida/Clothing/Under/Socks|Underwear/*` (equipped-спрайты «Edited by PuroSlavKing», универсальные).
2. Displacement применяется ТОЛЬКО к надетым предметам слотов: Content.Client/Clothing/ClientClothingSystem.cs:287-296,355 (`DisplacementMapSystem.TryAddDisplacement`); марки рисуются Content.Client/Humanoid/HumanoidAppearanceSystem.cs:ApplyMarking без displacement. У мола jumpsuit/shoes сдвинуты картами (`Resources/Prototypes/Entities/Mobs/Species/moth.yml:175-200`, states back/hand/jumpsuit-*/outerclothing/shoes), а бельевой слой остаётся на человеческих координатах → расхождение силуэтов.
3. Конфиг-пробелы displacements: у reptilian `Inventory.displacements` покрывает только jumpsuit/shoes (socks отсутствует) — `Resources/Prototypes/Entities/Mobs/Species/reptilian.yml`.
4. Исторически: bee/coder носки — предметы слота shoes с человеческими спрайтами (`Resources/Prototypes/Entities/Clothing/Under/under.yml`); причина признана разработчиком Yosif 2025-07-15 («спрайт не сделан под них»).

## Recommended fix (единый)
1) Видовые варианты бельевых спрайтов: добавить `_moth`-состояния в `Mobs/Customization/underwear.rsi`/`undergarments.rsi` (по образцу boxers_reptilian/boxers_vox) и подогнать `_Erida` equipped-SOCKS/UNDERWEAR под нечеловеческие тела; 2) добавить недостающие displacement'ы (socks у reptilian и др. видов; опционально underwear) в `Resources/Prototypes/Entities/Mobs/Species/*.yml`; 3) паллиатив — ограничить speciesRestriction бельевых марок до видов с подогнанными спрайтами. Системное расширение displacement на марки (ApplyMarking) — дороже и рискованнее, отдельно.
Validation: ящер/моль/антропоморф в бельё+комбинезон+ботинки, 4 ракурса; лобби; Censor Nudity toggle.
Severity: S4 COSMETIC / Complexity: S (спрайты+displacement) / M (системное).

## Excluded (смежная тема, иная причина)
1379120791253418124, 1379904937223520296, 1382299238423068682, 1471561763647389861 — хвосты: дефект ИМЕННО порядка слоёв → кластер `sprite-layer-order`.
