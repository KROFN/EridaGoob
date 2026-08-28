# TRIAGE REPORT — Discord bug-forum audit (Erida / Space Station 14)

Date: 2026-08-28 · Working fork: `KROFN/EridaGoob` · Branch: `ai/discord-bug-triage`
Analyzed fork HEAD: `511cc23b7c596bdd2e12a3a12236db15a18ef309` (== origin/master == upstream/master, 0 divergence)
Archive: Google Drive `1TlOjsaTn_iuKc26S7amk3q1qhkirNol7`, SHA256 `676e53bd26a9b0a9011a565694529c3eb4d15e4a86ee1becc6cb3dfb145452d6`

## Summary

| Metric | Count |
|---|---|
| Total Discord threads | 457 |
| Resolved by tag (Исправлено) | 182 |
| Not bug by tag (Не баг) | 63 |
| Needs triage | 212 |
| Investigated (dossier + verdict) | 212 / 212 (100%) |
| **Confirmed current bugs** | **16** |
| **Likely current bugs** | **54** |
| Already fixed in fork | 32 |
| Already fixed upstream | 0 (upstream == fork; all upstream-fix cases collapsed into ALREADY_FIXED_IN_CURRENT_FORK) |
| Duplicates (formal verdict) | 2 |
| Config/content issues | 39 |
| User error / not bug / out of scope | 14 |
| Cannot verify | 55 |
| Tag conflicts | 22 |
| Root-cause clusters | 24 (see `.ai-triage/clusters/`) |
| Dossiers | 212 (`.ai-triage/bugs/<thread_id>.md`) |

No production code was modified in this pass (triage-only, as instructed).

## Top findings

1. **[S1][XL] ReBell death model is structurally disabled** — cluster `rebell-death-model` (1375074483001491557, 1370396275329073172).
   `Content.Shared/_Shitmed/Surgery/Consciousness/Systems/ConsciousnessSystem.Helpers.cs:158-179` — `UpdateMobState` commented out. Creatures survive 0 blood / max bleeding / lethal wound totals; death only via MobThresholds, brain destruction or DelayedDeath (heart+brain). Dev-acknowledged. This single mechanism explains several "immortality / can't die / stand-then-die" reports.
2. **[S2][M] IPC (КПБ) acid damage untreatable** — 1537354952094257172. Regression of Woundmed Port (`8706b5039e`, #1859): `Caustic` removed from treatable wound classification for mechanical bodyparts. Cluster `ipc-caustic-untreatable`. Admin-engaged thread.
3. **[S2][S] Carrying a sleeping player wakes them** — 1419456892413022248. `Content.Shared/_DV/Carrying/CarryingSystem.cs:Drop` unconditionally `RemComp<KnockedDownComponent>` + `Stand()` — erases sleep/nocturine knockdown while `SleepingComponent` persists.
4. **[S2][M] Loadout exclusive-kit clamp is client-only → kung-fu book dupe** — 1542496476415000757 (OSSt). `RoleLoadout.cs:129/299-302` clamps MaxLimit client-side; server apply path lacks dedup → spamming issues infinite `GrantMartialArtKnowledge` books. Exploit-adjacent.
5. **[S2][M] Latejoin can spawn players on CC/foreign grids** — 1366802698430578818. `Content.Server/Spawners/EntitySystems/SpawnPointSystem.cs:37-59` queries all world SpawnPoints without station/map filter and falls back to "any spawner".
6. **[S2][M] Dead/zombie pilot keeps driving Ripley** — 1446843043180318743. Mech pilot not tied to alive-state (`Content.Shared/Mech` has no Dead/Death handling).
7. **[S2][S] TTS cannot be muted** — cluster `tts-volume-mute` (1480519345594568866, 1421848934644449382). `Content.Client/_CorvaxGoob/TTS/TTSSystem.cs:AdjustVolume` adds constant -10 dB floor; sliders not bound to CCvars; announcements averaged.
8. **[S2][S] Contact fire spread ignores protection** — 1498713547704631360. `FlammableSystem.OnStartCollide:245-260` transfers firestacks without checking victim's fire protection; FireStackHeat bypasses armor.
9. **[S2][S] Grappling hook noclips through closed windoors** — 1449508411325677692 (cluster `windoor-phasing`). Reel joint's MinLength protects only walls; table-slide→windoor tunneling (1388575425562673282) is a related physics family.
10. **[S3][M] Expeditions spawn empty** — 1414517676541349909. `SpawnSalvageMissionJob` fails on empty dungeon gen; job failure ignored in `SalvageSystem.Expeditions.cs` → live expedition with no destination/mobs/loot.

## QUICK_WINS (High confidence · XS/S · low regression risk)

| Thread | Fix | Sev | Cx |
|---|---|---|---|
| 1473337621521367151 | Add `UraniumWindowDirectional`/`UraniumReinforcedWindowDirectional` construction recipes (graphs/materials/entities already exist) | S3 | XS |
| 1417926890823356699 | `MakeSentientEntityEffectSystem`: also add common-language knowledge (language-system migration gap) | S3 | S |
| 1452510092305104927 | Unathi hair: add Hair/FacialHair layers to `MobReptilianSprites` or restrict markingPoints (maintainer already admitted missing layer) | S3 | S |
| 1479939209883160776 | revenant/aghost mutual collision: split `GhostImpassable` layer/mask on `Incorporeal` descendant | S4 | S |
| 1419456892413022248 | Carrying: only clear knockdown if not sleeping (check `SleepingComponent`) | S2 | S |
| 1492169522671653104 | Cryo respawn: show timer in the "Я ознакомился" window instead of console-only reply | S3 | S |
| 1379120791253418124 + cluster `sprite-layer-order` (4 threads) | Move tail markings to `TailBehind`/add `layering:` for mam_tails/rodentia marking prototypes | S4 | S |
| 1419998003447468153 | Conveyor: skip entities with `BeingCarriedComponent` in `SharedConveyorController` | S3 | S |
| 1365367741560913970 | TTS tab: honor patron voice gating + character-limit config (dev said "didn't have time") | S3 | M |

## HIGH_IMPACT (serious bugs, any complexity)

- rebell-death-model cluster (S1/XL) — core lethality semantics.
- IPC/КПБ acid untreatable (S2/M) — species-unplayability regression.
- Loadout exclusive-kit server clamp (S2/M) — dupe exploit.
- SpawnPoint station filter (S2/M) — CC-spawn rule violation.
- Zombie mech piloting (S2/M); burnt-torso surgery lock (S2/M); Shark species placeholder body (S2/M); cargo-tech loadout copy-paste artifacts (S2/M); expedition empty spawns (S2/M); windoor phasing cluster (S2/S-M); TTS mute (S2/S); flammable contact spread (S2/S); gubs-migration regression batch 1540061285029257266 (S2/L — needs per-claim split: CharacterSize, censer fuel, abductor console, faxes, nose-vs-modsuit).

## ROOT-CAUSE CLUSTERS (24 files, `.ai-triage/clusters/`)

Confirmed single-fix clusters:
- `rebell-death-model` (2) — ReBell UpdateMobState disabled.
- `sprite-layer-order` (4) — species Tail layer above clothing.
- `tts-volume-mute` (2) — volume formula + slider binding.
- `ipc-caustic-untreatable` / `rebell-headshot-lethality` / `rebell-pain-balance` — Shitmed wound-pipeline family.
- `security-duty-weapon-removed` (3) — stale Goobstation loadout content removed by syncs.
- `duplicate-loadout-group-labels` (3) — same-name loadout groups (labels split by Loadouts redux).
- `silicon-surgery-ui` (3) — silicon surgery access gate (needs live repro to finalize).
- `vampire-polymorph-revert` (2), `shadowkin-free-teleport` (2) — ABSENT content: vampire/shadowkin ability code is not in this git tree (data-only port) — live server runs additional content.
- `footprint-cleaning` (3) — mop/footprint reagent pipeline (one remaining actionable: lube re-spill loop).
- `species-survival-box-loadout-effects` (2), `goobstation-role-loadout-erida-content-gap` (2), `id-console-access-write` (2), `underwear-sprite-fit` (2), `language-knowledge-migration` (2), `accent-localization-ru` (2), `actionbar-reset-mind-transfer` (2), `windoor-phasing` (2), `cargo-dock-fans` (2), `inhand-sprite-content` (2), `per-map-device-content-gaps` (2), `intek-agent` (2), `head-bonk` (2).

Failure-family note: clusters marked "family" group same-subsystem reports with distinct causes — do not apply a single fix blindly.

## ALREADY FIXED BUT DISCORD STALE (32)

Notable examples (full list in BUG_INDEX): 1364960599544561746 (vulp markings, Species #12), 1394565743768768653 (chest markings, multilayer port a2ba0ebe00), 1388579685453135994/1422135237755932723 (survival boxes), 1422135237755932723 (shadowkin oxygen group; player confirmed «Исправлено»), 1540089010599366757 (molotov tag, 0572564025), 1470887025711513893 (shotgun desc, 4cf391efb1), 1368659829916434494 (mask sprite, upstream #40332), 1483498644257640691 (door lights, bc02215fde), 1496225961996193902 (RCD configs, b54bf7cec1), 1369302532916252772 (lockable button, c360583d4c), 1368604669160591390 (Arkan heal/HUD), 1371049112593764362 (shadowkin speech), 1368389167616098424 (mop scrubs footprints), 1368366125208965151 (weightlessness rewrite).

## DUPLICATES

- 1375435479725375538 → primary 1366269075013111899 (shadowkin free teleport; same reporter).
- 1379189259877093508 → primary 1373596253383954522 (vampire mouse polymorph).
- Cross-batch same-root pairs also linked in dossiers (e.g. 1368872733877731388 ↔ 1369663765662007297; 1380911822634225724 ↔ 1383537990382649396 pain family).

## CANNOT VERIFY (55)

Dominant causes: (a) Erida live-server custom maps/content absent from this git tree (Aspid, The Hive, live loadouts/shadowkin-vampire implementations); (b) Backmen-era reports against a codebase that no longer exists in history; (c) client-side/network issues without logs; (d) media-only or empty reports. Each dossier lists exactly what is missing to verify. Highest-value unblocks: obtain live-content repo snapshot; re-test silicon surgery UI gate and akimbo on current build.

## BUILD STATUS

**FEASIBLE / WORKING** (verified in sandbox):
- .NET SDK 10.0.400 installed (`dotnet --version` → 10.0.400).
- RobustToolbox submodule initialized (`git submodule update --init --recursive`).
- `dotnet build Content.Server/Content.Server.csproj -c Debug` → **0 errors** (803 warnings).
- Full `SpaceStation14.slnx` Debug build compiles all production projects; the only failure was MSB3021 "No space left on device" while copying integration-test runtimes — sandbox disk quota (9.9 GB), not a code issue. On a normal dev machine the standard project scripts (`Tools/RunScripts/sh/buildAllDebug.sh`) should complete.

## Recommended fix order (TOP 10 by value / effort / confidence)

| # | Thread | Why first |
|---|---|---|
| 1 | 1419456892413022248 carrying/sleep | S2, S-size, High conf, tiny guarded change, big RP impact |
| 2 | 1537354952094257172 IPC acid | S2 regression from a known port; clear fix point; admin-engaged |
| 3 | 1542496476415000757 loadout kit dupe | exploit class; server-side clamp is contained |
| 4 | 1473337621521367151 uranium windows | XS pure content-add, zero risk |
| 5 | 1417926890823356699 cognizin language | S-size, language-system migration correctness |
| 6 | 1366802698430578818 spawn point filter | S2 rule violation; bounded system |
| 7 | 1492169522671653104 respawn feedback | S-size UX correctness |
| 8 | 1452510092305104927 unathi hair | S-size; maintainer-confirmed; content-only |
| 9 | 1479939209883160776 ghost collision | S-size YAML/physics-mask fix |
| 10 | 1375074483001491557 rebell death model | highest gameplay value (S1) but XL + design decision — start after quick wins |

### FIRST 3–5 BUGS TO FIX

1. **IPC acid untreatable (1537354952094257172)** — a regression with a precise known cause (Woundmed port dropped `Caustic` classification); un-breaks an entire species' medical loop.
2. **Carrying wakes sleepers (1419456892413022248)** — small, High-confidence, fixes a visible RP-breaking behavior.
3. **Loadout exclusive-kit server clamp (1542496476415000757)** — closes an item-dupe vector.
4. **Uranium directional windows recipes (1473337621521367151)** — ten-minute additive content fix.
5. **Cognizin language knowledge (1417926890823356699)** — S-size correctness fix in the new language system.

Rationale: all five are High-confidence, XS/S effort, verifiable by manual repro in minutes, zero architectural risk — ideal first batch before touching the S1 death-model redesign.

## Completeness

- 457/457 threads in `bug_index.json`; 212/212 NEEDS_TRIAGE have final verdict + dossier on disk (programmatic check `scripts/merge_verdicts.py` + index inspection).
- Cluster member references validated against index; all 24 cluster files present.
- WORKLOG updated; branch `ai/discord-bug-triage` pushed to origin with checkpointed history.
- Per STOP-POINT agreement: no production code changed; no fixes committed; no PRs opened.
