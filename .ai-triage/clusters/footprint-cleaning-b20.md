# Cluster: footprint-cleaning (batch B20)

Members: 1368389167616098424 (primary), 1369020340520357968, 1391191286165540995 (partial).
Domain: Content.Goobstation.Server/Footprints/FootprintSystem.cs + Content.Goobstation.Shared/FloorCleaner/FloorCleanerSystem.cs + Content.Shared/Fluids/SharedAbsorbentSystem.cs + Content.Server/Chemistry/TileReactions/CleanTileReaction.cs.

## Confirmed shared root cause (historical)
The [PORT] Footprints refactor 71790ef585 (2025-04-16) shipped footprint creation and cleaning events without a working mop path: pre-2025-05-05 tree (3151f50b91) had no FloorCleanerSystem (git ls-tree empty) and no FloorCleaner component on MopItem (git grep empty). Mopping a footprint only worked via the puddle path and required absorbent reagent (Water) in the mop (SharedAbsorbentSystem.Mop, popup mopping-system-no-water), while a mop filled with trail contaminants reports "full" at the bucket (mopping-system-full). Only sprayer/soap (CleanTileReaction -> FootprintCleanEvent) erased footprints — exactly matching threads 1368389167616098424 ("их можно стереть распылителем") and 1369020340520357968 ("в швабре нет воды... швабра полна").

## Fixes already in HEAD
- 54ce591914 / 9c6d28d2ae: FloorCleanerSystem (mop scrubs FootprintComponent entities in radius 2).
- cba03bc191 (2025-10-30): StartCleaning/Mop integration in FloorCleanerSystem.
- 8122b6a82b (2025-05-18): SpaceLube sticksToSkin:false + slip tuning (slippery-trail formation reduced).
- dbf9930258 (2025-10-22): footprints only form from sufficiently large puddles.

## Residual open issue
Cleaning still re-spills liquid: FootprintCleanEvent -> FootprintSystem.ToPuddle clones the footprint solution and TrySpillAt recreates a (Slippery) puddle; tile overflow at MaxFootprintVolumeOnTile=50 also spawns real puddles. Non-evaporating SpaceLube therefore keeps footprints<->puddles cycling and cancels mop DoAfter via slips (thread 1391191286165540995, LIKELY_CURRENT_BUG). A dry mop silently deletes footprints and destroys reagents (StartCleaning returns true with no absorbent reagent), contradicting cba03bc191's intent — flagged as optional cleanup.
