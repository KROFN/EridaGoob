# Cluster: vampire-polymorph-revert

Members:
- 1373596253383954522 (primary) — «Вампир и превращение, шучу. Спам фамильярами.», 2025-05-18, WhatApple
- 1379189259877093508 (duplicate) — «Аннигиляция из вселенной», 2025-06-02, Фобос

## Confirmation of the pair
- Same ability family: vampire transformation into Remilia (bat) / mouse forms.
- Same failure signature in both threads: the transform action SPAWNS the form entity (Remilia / white mouse) as a separate "familiar" WITHOUT replacing the player's body.
- Same terminal mechanic: death/consumption of the spawned form acts back on the player — killing Remilia teleports the player's body to its place in crit (then revives); killing/eating the mouse chain ends in permanent character annihilation (no body, no brain, no items; other "familiars" ghosted).
- Both accepted by admin cybertrash as main-build bugs («Баг основного билда», «попробую разобрать лично»).

## Shared root cause (HYPOTHESIS, Medium — mechanism mapped to existing code)
Failure of the vampire polymorph configuration/execution in the live build, consistent with the generic PolymorphSystem present in the fork:
- Content.Server/Polymorph/Systems/PolymorphSystem.cs : PolymorphEntity (L214+) spawns the form entity and attaches PolymorphedEntityComponent{Parent=uid}; repeated morphs gated only by AllowRepeatedMorphs/Cooldown from the (absent) vampire config.
- Update (L95-119) / OnDestruction (L176-182) / OnPolymorphedTerminating (L184+) / OnBeforeFullySliced (L163, RevertOnEat) revert to the Parent on death/crit/destroy/slice — matching "killing the form teleports me into crit" and "after eating the last mouse I was annihilated".
- If the original body was already consumed/deleted by an overlapping transform, a later Revert has no valid body → permanent mind/body loss.

## Blocking context
The vampire content itself is ABSENT from the current fork (rg -i vampire in prototypes/locale/C#: only cosmetics + _Lavaland GunUpgradeVampirism; no vampire polymorph prototypes; no vampire C#; none in git history). MobBatRemilia exists in the fork only as the chaplain's familiar (Resources/Prototypes/Entities/Mobs/Player/familiars.yml). Hence both members are CANNOT_VERIFY as to the triggering configuration; verdicts are carried at pair level.

## Verdicts
- 1373596253383954522: CANNOT_VERIFY (vampire content absent; mechanism mapped), Medium, S1/M.
- 1379189259877093508: DUPLICATE of 1373596253383954522, High, S1/M.

## Fix strategy (once, in the build that has the vampire content)
Enforce UseDelay/Cooldown and AllowRepeatedMorphs=false on vampire form polymorphs; make mind transfer + original-body deletion atomic; add a single-revert guard per Parent; never allow RevertOnEat/RevertOnDeath on a Parent that is already deleted. Regression-test: spam transform → exactly one form entity; kill/eat form → exactly one revert; no orphan PolymorphedEntityComponent.
