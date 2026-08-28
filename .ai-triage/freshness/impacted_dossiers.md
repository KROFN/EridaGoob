# Freshness / delta revalidation — impacted dossiers

Generated: 2026-08-28T21:57:43Z
ANALYZED_HEAD: `511cc23b7c596bdd2e12a3a12236db15a18ef309`
CURRENT_UPSTREAM_HEAD: `28d0c86f9d2e2a502dfb422f5b2fd9eaa7df5a53`
Delta: 2 commits, 614 changed files

| Status | Count |
|---|---|
| SUBSYSTEM_TOUCHED | 50 |
| UNCHANGED_SINCE_TRIAGE | 15 |
| REVALIDATION_REQUIRED | 5 |

## Direct evidence file changed (revalidate before any fix)
- **1368875720373309480** [LIKELY_CURRENT_BUG] Баг на следы от жидкостей
  - changed: `Resources/Prototypes/_White/Entities/Effects/puddle.yml`
- **1413877633594163270** [LIKELY_CURRENT_BUG] Языки у существ
  - changed: `Resources/Prototypes/Entities/Mobs/NPCs/animals.yml`
- **1417926890823356699** [CONFIRMED_CURRENT_BUG] Когнизин не дает общего языка
  - changed: `Resources/Prototypes/Entities/Mobs/NPCs/animals.yml`
- **1432159035876053103** [LIKELY_CURRENT_BUG] Вы не сможете переварить мышь!
  - changed: `Resources/Prototypes/Entities/Mobs/NPCs/animals.yml`
- **1446843043180318743** [LIKELY_CURRENT_BUG] Экипаж VS зомби
  - changed: `Resources/Changelog/GoobChangelog.yml`
  - changed: `Resources/migration.yml`

## Subsystem-level touches (weak signal)
- 1365367741560913970 [CONFIRMED_CURRENT_BUG] ТТС и кол-во персонажей → `Resources/Prototypes/_Erida/Voice/tts-voices.yml`
- 1366747516258881536 [LIKELY_CURRENT_BUG] Раздвижные окна → `Resources/Locale/ru-RU/ss14-ru/prototypes/entities/structures/doors/windoors/windoor.ftl`, `Resources/Prototypes/Entities/Structures/Doors/Windoors/windoor.yml`
- 1367646136298504222 [LIKELY_CURRENT_BUG] Скорее всего баг с хирургией → `Content.Shared/_Shitmed/Surgery/Consciousness/Systems/ConsciousnessSystem.Helpers.cs (inline)`
- 1367781435938832436 [LIKELY_CURRENT_BUG] Нечувствительность не работает в настроении → `Resources/Locale/ru-RU/traits/traits.ftl`, `Resources/Prototypes/_Erida/Traits/erida_traits.yml`
- 1368389636531163186 [LIKELY_CURRENT_BUG] что такое жажда? → `Resources/Locale/ru-RU/_backmen/body/parts/shark.ftl (inline)`, `Resources/Prototypes/_Erida/Species/shark.yml`
- 1368606729440333845 [LIKELY_CURRENT_BUG] А на цк НЕ РАБОТАЕТ → `Resources/Locale/ru-RU/navmap-beacons/station-beacons.ftl`, `Resources/Prototypes/Entities/Stations/base.yml`
- 1369541733196496936 [LIKELY_CURRENT_BUG] Дальнозоркость цИИ или почему цИИ фиксирует датчики с сЦК → `Content.Server/Medical/CrewMonitoring/CrewMonitoringConsoleSystem.cs`, `Content.Server/Medical/CrewMonitoring/CrewMonitoringServerSystem.cs (inline)`
- 1370366183689293944 [LIKELY_CURRENT_BUG] пнв → `Resources/Prototypes/_Goobstation/Entities/Clothing/OuterClothing/hardsuits.yml`, `Resources/Prototypes/_White/Shaders/shaders.yml (inline)`
- 1370396275329073172 [LIKELY_CURRENT_BUG] Я умер насмерть. → `Content.Shared/_Shitmed/Surgery/Consciousness/Systems/ConsciousnessSystem.Helpers.cs (inline)`, `Resources/Prototypes/Entities/Mobs/base.yml (inline)`
- 1370482031624061070 [LIKELY_CURRENT_BUG] Летаем. Мусор. Летаем → `Content.Server/Materials/MaterialReclaimerSystem.cs`
- 1372567955899940864 [CONFIRMED_CURRENT_BUG] Киберпанк 1984 → `Content.Shared/Body/Part/BodyPartComponent.cs (inline)`, `Resources/Prototypes/_Shitmed/Body/Parts/cybernetic.yml (inline)`, `Resources/Prototypes/_Shitmed/Recipes/Lathes/robotics.yml (inline)`
- 1375074483001491557 [CONFIRMED_CURRENT_BUG] Бесмертие(конечно пока твою голову не раздавят) → `Content.Server/_Shitmed/DelayedDeath/DelayedDeathSystem.cs (inline)`, `Content.Shared/_Shitmed/Surgery/Consciousness/Systems/ConsciousnessSystem.Helpers.cs (inline)`, `Resources/Prototypes/Entities/Mobs/base.yml (inline)`
- 1379120791253418124 [CONFIRMED_CURRENT_BUG] Хвост хаски в лобби → `Resources/Prototypes/Entities/Mobs/Species/base.yml`, `Resources/Prototypes/_Erida/Customization/Markings/anthropomorph.yml`, `Resources/Prototypes/_Erida/Entities/Mobs/Species/anthropomorph.yml`, `Resources/Prototypes/_Erida/Species/anthropomorph.yml`
- 1379904937223520296 [CONFIRMED_CURRENT_BUG] Баг с юбкой-комбинезоном и хвостами → `Resources/Prototypes/_Erida/Customization/Markings/anthropomorph.yml`, `Resources/Prototypes/_Erida/Entities/Mobs/Species/anthropomorph.yml`
- 1382299238423068682 [CONFIRMED_CURRENT_BUG] Хвост кицунэ. → `Resources/Prototypes/_Erida/Customization/Markings/anthropomorph.yml`, `Resources/Prototypes/_Erida/Entities/Mobs/Species/anthropomorph.yml`
- 1382754417589358672 [LIKELY_CURRENT_BUG] Арахны → `Resources/Prototypes/Body/Prototypes/arachnid.yml`, `Resources/Prototypes/Entities/Mobs/Species/arachnid.yml`, `Resources/Prototypes/Species/arachnid.yml`
- 1388575425562673282 [LIKELY_CURRENT_BUG] Баг со столами и закрытыми кнопками → `Resources/Prototypes/Entities/Structures/Doors/Windoors/windoor.yml`
- 1389672150151200924 [LIKELY_CURRENT_BUG] грузчик цк → `Resources/Locale/en-US/preferences/loadout-groups.ftl`, `Resources/Prototypes/Loadouts/loadout_groups.yml`, `Resources/Prototypes/Loadouts/role_loadouts.yml`, `Resources/Prototypes/_Goobstation/Loadouts/Jobs/Cargo/cargo_technician.yml`
- 1391191286165540995 [LIKELY_CURRENT_BUG] Следы поскальзывают → `Resources/Prototypes/Entities/Effects/puddle.yml`, `Resources/Prototypes/Reagents/cleaning.yml`
- 1394835847324504235 [LIKELY_CURRENT_BUG] На манекен нельзя напялить очки, маску и шапку. → `Resources/Prototypes/Entities/Structures/Decoration/mannequin.yml`, `Resources/Prototypes/InventoryTemplates/inventorybase.yml`, `Resources/Prototypes/InventoryTemplates/mannequin_inventory_template.yml`
- 1414517676541349909 [LIKELY_CURRENT_BUG] Экспедиции сломаны → `Resources/Locale/ru-RU/procedural/expeditions.ftl`
- 1420383751082344479 [LIKELY_CURRENT_BUG] Маг → `Content.Server/_Shitcode/Wizard/Systems/SpellsGrantSystem.cs`, `Resources/Prototypes/_Goobstation/Wizard/spellbook_catalog.yml`
- 1424014048726351937 [LIKELY_CURRENT_BUG] Не работает вентилятор → `Resources/Prototypes/Entities/Structures/Piping/Atmospherics/special.yml`
- 1430774622957338646 [LIKELY_CURRENT_BUG] Косой Эсток → `Resources/Locale/ru-RU/ss14-ru/prototypes/entities/objects/weapons/guns/rifles/rifles.ftl (inline)`, `Resources/Prototypes/Entities/Objects/Weapons/Guns/Rifles/rifles.yml (inline)`
- 1431376123060555828 [LIKELY_CURRENT_BUG] Как рулить → `Resources/Prototypes/GameRules/roundstart.yml (inline)`, `Resources/Prototypes/_Goobstation/GameRules/roundstart.yml`
- 1432362211908653066 [LIKELY_CURRENT_BUG] Воксы языки → `Resources/Locale/en-US/_EinsteinEngines/language/languages.ftl`, `Resources/Locale/ru-RU/_EinsteinEngines/chat/managers/chat-language.ftl`, `Resources/Locale/ru-RU/_EinsteinEngines/language/languages.ftl`, `Resources/Prototypes/_EinsteinEngines/Language/Species-Specific/vox.yml`
- 1438072028904030238 [LIKELY_CURRENT_BUG] Диагональные стены. → `Resources/Prototypes/Recipes/Construction/structures.yml`
- 1448396633736741045 [LIKELY_CURRENT_BUG] Направленные окна и плитка → `Resources/Prototypes/Entities/Structures/Windows/window.yml`
- 1449885909653651496 [LIKELY_CURRENT_BUG] Некорректное отображение → `Resources/Locale/ru-RU/_Erida/accent/streetrebel.ftl`
- 1451208282411761756 [LIKELY_CURRENT_BUG] Призрак коробки → `Resources/Prototypes/Entities/Mobs/Player/jaunt_mobs.yml`, `Resources/Prototypes/Entities/Objects/Devices/desynchronizer.yml`, `Resources/Prototypes/Polymorphs/polymorph.yml`
- 1452510092305104927 [CONFIRMED_CURRENT_BUG] У унатхов нет волос. → `Resources/Prototypes/Species/human.yml`, `Resources/Prototypes/Species/reptilian.yml`
- 1455157816800317595 [LIKELY_CURRENT_BUG] Нет, я не буду блобом сейчас Уолтер → `Resources/Locale/ru-RU/ss14-ru/prototypes/_goobstation/blob/blob_mobs.ftl`, `Resources/Prototypes/_Goobstation/Blob/blob_mobs.yml`
- 1459054342719148285 [LIKELY_CURRENT_BUG] Кофемашина выдаёт кофе раньше, чем анимация закончится → `Resources/Prototypes/Entities/Structures/Machines/vending_machines.yml`
- 1463805725422911500 [LIKELY_CURRENT_BUG] Пироги и их отображение на лице → `Content.Shared/EntityEffects/Effects/WashCreamPieEntityEffectSystem.cs`
- 1471561763647389861 [CONFIRMED_CURRENT_BUG] Мышиный хвост отображается спереди так же как и сзади → `Resources/Prototypes/_DV/Entities/Mobs/Customization/Markings/rodentia.yml`, `Resources/Prototypes/_DV/Entities/Mobs/Species/rodentia.yml`
- 1473337621521367151 [CONFIRMED_CURRENT_BUG] Нет направленных урановых стекол в меню крафта → `Resources/Prototypes/Entities/Structures/Windows/uranium.yml (inline)`, `Resources/Prototypes/Recipes/Construction/Graphs/structures/windowdirectional.yml (inline)`, `Resources/Prototypes/Recipes/Construction/structures.yml (inline)`
- 1479939209883160776 [CONFIRMED_CURRENT_BUG] Ревенант и агост → `Resources/Prototypes/Entities/Mobs/NPCs/revenant.yml`, `Resources/Prototypes/Entities/Mobs/Player/observer.yml`
- 1492169522671653104 [CONFIRMED_CURRENT_BUG] Невозможность респавна после крио → `Content.Client/UserInterface/Systems/Ghost/GhostUIController.cs`, `Content.Client/UserInterface/Systems/Ghost/Widgets/GhostGui.xaml.cs`, `Resources/Locale/ru-RU/_DV/respawn-system.ftl (inline)`
- 1499505469025419389 [LIKELY_CURRENT_BUG] Минус юбка → `Resources/Prototypes/_Goobstation/Entities/Mobs/Customization/Markings/human_hair.yml`, `Resources/Textures/_Goobstation/Mobs/Customization/human_hair.rsi/meta.json`
- 1499847578563510303 [LIKELY_CURRENT_BUG] OWO акцент → `Resources/Prototypes/Entities/Clothing/Head/misc.yml (inline)`, `Resources/Prototypes/Nyanotrasen/Entities/Mobs/Species/felinid.yml`, `Resources/Prototypes/Traits/speech.yml`, `Resources/Prototypes/_Erida/Traits/erida_traits.yml`
- 1500984548438179910 [LIKELY_CURRENT_BUG] Скованная кукла, превращенная в зомби не может расковаться → `Content.Shared/EntityEffects/Effects/ZombieEntityEffectsSystem.cs`, `Resources/Locale/ru-RU/ss14-ru/prototypes/entities/objects/misc/handcuffs.ftl`, `Resources/Prototypes/Entities/Objects/Misc/handcuffs.yml`
- 1531689725554069685 [LIKELY_CURRENT_BUG] огнетушитель дельта вондер → `Resources/Prototypes/_Goobstation/Maps/delta.yml (inline)`
- 1532607747986558977 [LIKELY_CURRENT_BUG] КПБ и стекло. → `Resources/Prototypes/Entities/Objects/Materials/shards.yml`, `Resources/Prototypes/_EinsteinEngines/Entities/Mobs/Player/ipc.yml`
- 1534480920327880776 [LIKELY_CURRENT_BUG] Наплак на еретика → `Content.Shared/_Shitcode/Heretic/Components/HereticCloakedStatusEffectComponent.cs`, `Content.Shared/_Shitcode/Heretic/Systems/Abilities/SharedHereticAbilitySystem.Void.cs`, `Content.Shared/_Shitcode/Heretic/Systems/HereticCloakSystem.cs`, `Content.Shared/_Shitcode/Heretic/Systems/SharedShadowCloakSystem.cs`
- 1534609752284463224 [CONFIRMED_CURRENT_BUG] Ядерный Фабрикатор → `Resources/Locale/ru-RU/_CorvaxGoob/fission-generator/entities.ftl`, `Resources/Prototypes/Recipes/Lathes/machine_boards.yml (inline)`
- 1535027750082056404 [LIKELY_CURRENT_BUG] Чемодан → `Resources/Prototypes/Entities/Objects/Misc/briefcases.yml`, `Resources/Textures/_Erida/Objects/Storage/Briefcases/briefcase_brown.rsi/meta.json`
- 1536503382355746886 [LIKELY_CURRENT_BUG] еретик с путем пепла → `Content.Shared/_Shitcode/Heretic/Heretic.Abilites.cs`
- 1537354952094257172 [CONFIRMED_CURRENT_BUG] баг с лечением кпб → `Content.Shared/_Shitmed/`, `Resources/Locale/ru-RU/_EinsteinEngines/species/species.ftl`
- 1540061285029257266 [LIKELY_CURRENT_BUG] Баги перехода на губы → `Content.Client/_Shitmed/Antags/Abductor/AbductorCameraConsoleWindow.xaml.cs (inline)`, `Resources/Prototypes/_DV/CosmicCult/Objects/censer.yml`
- 1542496476415000757 [LIKELY_CURRENT_BUG] Дюп пособников по Кунг-Фу на ОСЩ. → `Resources/Prototypes/_Goobstation/MartialArts/dragonkungfu.yml`
