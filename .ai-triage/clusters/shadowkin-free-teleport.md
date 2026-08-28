# Cluster: shadowkin-free-teleport

Members:
- 1366269075013111899 (primary) — «Бесплатная тпешка шадоукинов», 2025-04-28, xkttty
- 1375435479725375538 (duplicate) — «Телепортация без потери маны и стамины», 2025-05-23, KARiX

## Confirmation of the pair
- Identical defect: shadowkin teleport executes without spending stamina and without sound; thread 2 demonstrates it on video, thread 1 adds the trigger condition (while carrying/dragging an item or crate).
- Direct testimony linking them: xkttty — author of the primary report — replies in thread 2: «баг с самого открытия эриды, уже кидал насчёт этого баг репорт».
- Admin cybertrash acknowledged thread 2 («Баг с конфы, передам, посмотрю лично»).

## Shared root cause (HYPOTHESIS, Low-Medium)
The EE-style Shadeskip teleport system applies its stamina cost and sound only on a code path that is skipped/bypassed in certain states (e.g., while pulling/carrying an entity), yielding a free, silent teleport. The system code is NOT present in the current fork:
- No shadowkin C# in Content.Server/Content.Shared (rg -i shadowkin *.cs → only LanguagePrototype.cs).
- MobShadowkinBase (Resources/Prototypes/_EinsteinEngines/Entities/Mobs/Species/shadowkin.yml) grants no ability components/actions.
- Data-only remnants: EffectFlashShadowkinShadeskip (Resources/Prototypes/_EinsteinEngines/Entities/Effects/shadow.yml), shadeskip.ogg / darkswap oggs (Resources/Audio/_EinsteinEngines/Effects/Shadowkin/).
- Port commit fa46b517e0 (2025-05-22, "[Port] [Bounty] Shadowkins from EE (#2675)") is data-only.

## Verdicts
- 1366269075013111899: CANNOT_VERIFY (feature absent from current fork), Medium, S2/M.
- 1375435479725375538: DUPLICATE of 1366269075013111899, High, S2/S.

## Fix strategy (once, in the build that has the systems)
Apply stamina cost + sound unconditionally at the start of the teleport handler; forbid or correctly charge teleport while pulling; regression-test with empty hands vs. pulled crate.
