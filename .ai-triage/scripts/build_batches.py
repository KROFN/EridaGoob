#!/usr/bin/env python3
"""Build batch assignment: topic-grouped batches over NEEDS_TRIAGE threads. Verify full coverage."""
import json, os

REPO = "/home/z/my-project/erida-triage/erida"
# map: ordinal number (from list_needs_triage output order) -> thread_id
with open(os.path.join(REPO, ".ai-triage", "bug_index.json"), encoding="utf-8") as f:
    idx = json.load(f)
ordered = sorted([e for e in idx["threads"] if e["classification"] == "NEEDS_TRIAGE"],
                 key=lambda x: x["created_at"] or "")
num2id = {f"{i+1:03d}": e["thread_id"] for i, e in enumerate(ordered)}

BATCHES = {
 "B01": ("meta/out-of-scope: report form, admin screens, wiki, FPS, server connect", ["001","014","098","134","143","091"]),
 "B02": ("client/vague: laptop logs, video-only, vague, content download, clock reset, playtime gate", ["018","024","053","093","198","191"]),
 "B03": ("sprites: tails/socks/underwear layering", ["061","086","064","067","153","166"]),
 "B04": ("species markings/customization: ears, arachne, chest features, felinid, unathi hair, vox tails paint", ["002","068","087","120","151","182"]),
 "B05": ("sprites: hair over skirts, terminator trait, gamley hats, suitcase layer, held-item display, previous held item", ["183","188","160","201","149","177"]),
 "B06": ("loadout UI: trinket tabs, unknown item, duty weapon missing, patrol hat, psych duplicated sections", ["007","016","036","044","054","076"]),
 "B07": ("loadout items missing: medals, emergency kits, OSSt underwear, tech assistant, thief bag, shadowkin loadout", ["077","078","095","096","101","124"]),
 "B08": ("hardsuits/armor: suits for roles, SI helmet, PNV hiding suit, intek jacket stats, stamina resist, who ate stun resist", ["141","116","048","090","106","174"]),
 "B09": ("weapons: RCBZ ammo, headzomba pistol, semicolon desc, UTAP, estok spread, shotgun instagib", ["005","040","165","105","133","065"]),
 "B10": ("cargo/economy/craft: bandanas, CC cargo, lottery currency, trade console, mini reactor price, molotov", ["011","034","072","104","207","210"]),
 "B11": ("kitchen/botany/food/animals: fridge+bag, smart fridge, cake dough, towel edible, mouse digest, breeding", ["015","103","094","130","137","162"]),
 "B12": ("medical core: burnt torso surgery, blood 0-30, cant stand-die, jaw prosthesis, space immortality, rebbel pain", ["026","045","049","055","058","069"]),
 "B13": ("medborg/surgery/blob/CPB: medcyborg op, med units op, FPV drones, MMI borg blind, two blobs, acid wounds", ["041","074","056","171","092","206"]),
 "B14": ("medical misc: arkan HP HUD, pain insensitivity mood, vampire DNA scanner, CPB stamina crit, blind trait, blob cure drop", ["033","027","085","196","211","154"]),
 "B15": ("shadowkin/vampire: free TP, tp no stamina cost, bound abilities, familiar spam, mouse transform, burns", ["017","059","060","057","062","082"]),
 "B16": ("mage/heretic/antag: astral buttons, heretic cloak, ash path, agents late, agent goals, decline target checkbox", ["121","199","204","175","028","205"]),
 "B17": ("access: lockable button, access console override, AVD accesses, genpop, ninja gloves lockers, passengers turrets", ["042","073","080","148","128","155"]),
 "B18": ("comms/AI: invisible buttons, AVD freq dead, sCID sensors, borg laws english, AI holopad language, train cameras", ["004","111","043","109","110","192"]),
 "B19": ("windows/collision: sliding windows block, tables+buttons slip through, grappling through windows, balls stuck, head bonk, crawl footprints", ["019","075","147","158","089","037"]),
 "B20": ("cleaning/printers/masks: mop no clean, unkillable footprints, slippery footprints, stand bump head, doc printer vanish, mask sprite", ["030","039","081","038","066","035"]),
 "B21": ("conveyor/gravity/shuttle physics: item gravity, trash on conveyor, carried rider conveyor, cargo fan, Box cargo fans, shuttles clip station", ["029","050","119","112","127","152"]),
 "B22": ("maps/docking: aspid cargo dock, hive lava shuttle, nukie dock wall, federation box air, aspid kitchen lamp, road model", ["012","022","135","071","023","013"]),
 "B23": ("maps misc: SCK hydroponics, Box double cargo console, delta psych buttons, delta park wiring, wonder fireext, bagel nanomed wall", ["006","159","163","164","195","190"]),
 "B24": ("centcom/craft: Amber printers, CC passenger spawn, RND console window, test crafts, uranium glass craft, nuclear fabricator", ["118","020","025","097","167","200"]),
 "B25": ("research/loc/sprites: long-barrel tech missing, hydroponics dup research, copier time, loc trade, #kits letters, airlock sprites, beaker liquid sprite", ["010","189","146","208","126","070","138"]),
 "B26": ("species traits/accents/emotes: palfeim thirst, moans loud, species tongues, cognizin, spanish accent, OWO accent", ["031","100","102","115","184","186"]),
 "B27": ("shadowkin voice/game rules/meta: shadowkin silent, secret gamemode spam, no brigmed squad, WL roles, donate prostheses, IS bug thread", ["052","113","114","009","003","099"]),
 "B28": ("TTS cluster + roundend manifest: subscribed voices, random tts, Rita, disabled still heard, cant disable, end manifest", ["008","107","122","123","170","084"]),
 "B29": ("intek/expedition/lava/combat: agost scanner loss, intek agent lava walk, agost shadow buttons, intek stomach, melee system, lava headcrabs", ["021","046","047","051","063","194"]),
 "B30": ("interactions: skirt job naked, mannequin dressup, sleeping picked up, HARMKAKA extra slots, coffee machine timing, pie on face", ["079","088","117","145","157","161"]),
 "B31": ("misc: miner lamp flash, expeditions broken, box free-return goal, dragon rift, mapping command, vox poison regen, GW fax", ["083","108","125","129","131","132","136"]),
 "B32": ("misc: vox language name, zombie mecha, directional windows tiles, box ghost dimension, ghost doc sound, diagonal walls", ["139","142","144","150","156","140"]),
 "B33": ("misc: char import, revenant agost push, lunar rovers, doors relogin, cryo respawn, atmos RCD", ["168","169","172","173","176","178"]),
 "B34": ("misc: space action interrupts, akimbo, fire spread npc, bag drag, zombie straitjacket, kungfu dup OSSt", ["179","180","181","185","187","212"]),
 "B35": ("misc: boot puncture, silly atmosphere vague, doll NSFW desc, essence desc, GUBS migration mega-thread, aiming jitter", ["193","197","202","203","209","032"]),
 "B36": ("leftovers sweep", []),
}

# ensure all 212 covered
used = []
for k, (topic, nums) in BATCHES.items():
    used += nums
allnums = list(num2id)
missing = [n for n in allnums if n not in used]
dupes = [n for n in used if used.count(n) > 1]
print("missing:", missing)
print("dupes:", sorted(set(dupes)))
if missing:
    BATCHES["B36"] = ("leftovers sweep", missing)
    used += missing

out = {}
for k, (topic, nums) in sorted(BATCHES.items()):
    if not nums:
        continue
    out[k] = {"topic": topic,
              "threads": [{"num": n, "thread_id": num2id[n]} for n in nums]}
os.makedirs(os.path.join(REPO, ".ai-triage", "data", "verdicts"), exist_ok=True)
with open(os.path.join(REPO, ".ai-triage", "data", "batches.json"), "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=1)
total = sum(len(v["threads"]) for v in out.values())
print(f"batches: {len(out)}, threads assigned: {total}")
for k, v in sorted(out.items()):
    print(k, len(v["threads"]), "|", v["topic"][:70])
