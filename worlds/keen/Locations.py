from BaseClasses import Location

class KeenLocation(Location):
    game = "Commander Keen"

# --------------------------------------------------
# Constants
# --------------------------------------------------

AP_LOC_BASE_LEVEL_COMPLETE = 10000
AP_LOC_BASE_KEYGEM = 20000
AP_LOC_BASE_KEYCARD = 30000
# 40000–99999 was the original pointsanity range when class+instance were
# packed into AP_LOC_LEVEL_STRIDE = 100. Real maps have up to ~124 instances
# of a single point class per level (CK5 IVS 100-pt items), so the packed
# scheme couldn't fit and pointsanity moved to its own per-class 100k ranges
# at AP_LOC_BASE_POINTSANITY below. 40000–99999 is intentionally unused —
# do not repurpose without coordinating with omnispeak-ap's ap_defs.h.
# Centilife pickups (extra-life accumulators, foreground tile misc=4).
# CK5 sprite is a Vitalin Keg; CK4 sprite is a Lifewater Flask. Same engine
# mechanic, different sprite — we use two separate bases so the location
# name space stays clean per episode.
AP_LOC_BASE_KEG = 50000     # CK5 Vitalin Kegs
AP_LOC_BASE_FLASK = 60000   # CK4 Lifewater Flasks
AP_LOC_BASE_POINTSANITY = 100000

AP_LOC_EPISODE_STRIDE = 2000
AP_LOC_LEVEL_STRIDE = 100

AP_EPISODE_CK4 = 1
AP_EPISODE_CK5 = 2

# --------------------------------------------------
# Level IDs
# --------------------------------------------------
# CK4
LEVEL_BV = 1
LEVEL_SV = 2
LEVEL_PP = 3
LEVEL_COTD = 4
LEVEL_COC = 5
LEVEL_CRYS = 6
LEVEL_HIL = 7
LEVEL_SY = 8
LEVEL_MIR = 9
LEVEL_LO = 10
LEVEL_POTM = 11
LEVEL_POS = 12
LEVEL_POTGA = 13
LEVEL_POTF = 14
LEVEL_IOT = 15
LEVEL_IOF = 16
LEVEL_WOW = 17
LEVEL_BWBM = 18

# CK5
LEVEL_IVS = 1
LEVEL_SC = 2
LEVEL_DTV = 3
LEVEL_EFS = 4
LEVEL_DTB = 5
LEVEL_RCC = 6
LEVEL_DTS = 7
LEVEL_NBI = 8
LEVEL_DTT = 9
LEVEL_BMI = 10
LEVEL_GDH = 11
LEVEL_QED = 12

# Gem indexes (match engine values)
GEM_RED = 0
GEM_YELLOW = 1
GEM_BLUE = 2
GEM_GREEN = 3

# --------------------------------------------------
# Location ID builders
# --------------------------------------------------

def loc_level_complete(ep, lvl):
    return (
        AP_LOC_BASE_LEVEL_COMPLETE
        + (ep * AP_LOC_EPISODE_STRIDE)
        + (lvl * AP_LOC_LEVEL_STRIDE)
    )

def loc_keygem(ep, lvl, gem):
    return (
        AP_LOC_BASE_KEYGEM
        + (ep * AP_LOC_EPISODE_STRIDE)
        + (lvl * AP_LOC_LEVEL_STRIDE)
        + gem
    )

def loc_keycard(ep, lvl):
    return (
        AP_LOC_BASE_KEYCARD
        + (ep * AP_LOC_EPISODE_STRIDE)
        + (lvl * AP_LOC_LEVEL_STRIDE)
    )

def loc_keg(ep, lvl, idx):
    return (
        AP_LOC_BASE_KEG
        + (ep * AP_LOC_EPISODE_STRIDE)
        + (lvl * AP_LOC_LEVEL_STRIDE)
        + idx
    )

# Pointsanity uses its own strides (engine: omnispeak-ap commit 451e296),
# separate from the global AP_LOC_*_STRIDE values above, because real maps
# pack up to ~124 instances of a single point class per level — too dense
# to share AP_LOC_LEVEL_STRIDE = 100. Layout:
#     loc = BASE + cls * CLASS_STRIDE + ep * EP_STRIDE + lvl * LVL_STRIDE + inst
# Round-decimal addressing means the class is readable from the 100k digit:
# 1xxxxx = 100 pt, 2xxxxx = 200 pt, ..., 6xxxxx = 5000 pt. Currently only
# class 5 (5000 pt) is emitted by the engine; classes 0..4 are wired but
# disabled there.
AP_POINTSANITY_CLASS_STRIDE = 100000
AP_POINTSANITY_EPISODE_STRIDE = 20000
AP_POINTSANITY_LEVEL_STRIDE = 1000
POINTS5K_CLASS = 5

def loc_pointsanity(ep, lvl, cls, inst):
    return (
        AP_LOC_BASE_POINTSANITY
        + (cls * AP_POINTSANITY_CLASS_STRIDE)
        + (ep * AP_POINTSANITY_EPISODE_STRIDE)
        + (lvl * AP_POINTSANITY_LEVEL_STRIDE)
        + inst
    )

def loc_flask(ep, lvl, idx):
    return (
        AP_LOC_BASE_FLASK
        + (ep * AP_LOC_EPISODE_STRIDE)
        + (lvl * AP_LOC_LEVEL_STRIDE)
        + idx
    )

# --------------------------------------------------
# Location tables
# --------------------------------------------------
ck4_locations_by_region = {
    "K4 Overworld": {
        "Border Village Complete": loc_level_complete(AP_EPISODE_CK4, LEVEL_BV),
        "Slug Village Complete": loc_level_complete(AP_EPISODE_CK4, LEVEL_SV),
        "The Perilous Pit Complete": loc_level_complete(AP_EPISODE_CK4, LEVEL_PP),
        "The Perilous Pit - Red Gem": loc_keygem(AP_EPISODE_CK4, LEVEL_PP, GEM_RED),
        "The Perilous Pit - Blue Gem": loc_keygem(AP_EPISODE_CK4, LEVEL_PP, GEM_BLUE),
        "Cave of the Descendents Complete": loc_level_complete(AP_EPISODE_CK4, LEVEL_COTD),
        "Cave of the Descendents - Red Gem": loc_keygem(AP_EPISODE_CK4, LEVEL_COTD, GEM_RED),
        "Cave of the Descendents - Yellow Gem":  loc_keygem(AP_EPISODE_CK4, LEVEL_COTD, GEM_YELLOW),
        "Chasm of Chills Complete": loc_level_complete(AP_EPISODE_CK4, LEVEL_COC),
        "Crystalus Complete": loc_level_complete(AP_EPISODE_CK4, LEVEL_CRYS),
        "Crystalus - Red Gem": loc_keygem(AP_EPISODE_CK4, LEVEL_CRYS, GEM_RED),
        "Crystalus - Yellow Gem": loc_keygem(AP_EPISODE_CK4, LEVEL_CRYS, GEM_YELLOW),
        "Crystalus - Blue Gem": loc_keygem(AP_EPISODE_CK4, LEVEL_CRYS, GEM_BLUE),
        "Crystalus - Green Gem": loc_keygem(AP_EPISODE_CK4, LEVEL_CRYS, GEM_GREEN),
        "Hilville Complete": loc_level_complete(AP_EPISODE_CK4, LEVEL_HIL),
        "Sand Yego Complete": loc_level_complete(AP_EPISODE_CK4, LEVEL_SY),
        "Sand Yego - Green Gem": loc_keygem(AP_EPISODE_CK4, LEVEL_SY, GEM_GREEN),
        "Miragia Complete": loc_level_complete(AP_EPISODE_CK4, LEVEL_MIR),
        "Lifewater Oasis Complete": loc_level_complete(AP_EPISODE_CK4, LEVEL_LO),
        "Lifewater Oasis - Green Gem": loc_keygem(AP_EPISODE_CK4, LEVEL_LO, GEM_GREEN),
        "Pyramid of the Moons Complete": loc_level_complete(AP_EPISODE_CK4, LEVEL_POTM),
        "Pyramid of the Moons - Yellow Gem": loc_keygem(AP_EPISODE_CK4, LEVEL_POTM, GEM_YELLOW),
        "Pyramid of Shadows Complete": loc_level_complete(AP_EPISODE_CK4, LEVEL_POS),
        "Pyramid of Shadows - Blue Gem": loc_keygem(AP_EPISODE_CK4, LEVEL_POS, GEM_BLUE),
        "Pyramid of the Gnosticine Ancients Complete": loc_level_complete(AP_EPISODE_CK4, LEVEL_POTGA),
        "Pyramid of the Gnosticine Ancients - Red Gem": loc_keygem(AP_EPISODE_CK4, LEVEL_POTGA, GEM_RED),
        "Pyramid of the Gnosticine Ancients - Green Gem": loc_keygem(AP_EPISODE_CK4, LEVEL_POTGA, GEM_GREEN),
        "Bean-With-Bacon Megarocket Complete": loc_level_complete(AP_EPISODE_CK4, LEVEL_BWBM),
    },

    "K4 Lake": {
        "Isle of Tar Complete": loc_level_complete(AP_EPISODE_CK4, LEVEL_IOT),
        "Isle of Tar - Red Gem": loc_keygem(AP_EPISODE_CK4, LEVEL_IOT, GEM_RED),
        "Isle of Tar - Yellow Gem": loc_keygem(AP_EPISODE_CK4, LEVEL_IOT, GEM_YELLOW),
        "Isle of Tar - Blue Gem": loc_keygem(AP_EPISODE_CK4, LEVEL_IOT, GEM_BLUE),
        "Isle of Fire Complete": loc_level_complete(AP_EPISODE_CK4, LEVEL_IOF),
        "Isle of Fire - Yellow Gem": loc_keygem(AP_EPISODE_CK4, LEVEL_IOF, GEM_YELLOW),
        "Isle of Fire - Blue Gem": loc_keygem(AP_EPISODE_CK4, LEVEL_IOF, GEM_BLUE),
        "Well of Wishes Complete": loc_level_complete(AP_EPISODE_CK4, LEVEL_WOW),
    },
}

ck5_locations_by_region = {
    "K5 Start": {
        "Ion Ventilation System Complete": loc_level_complete(AP_EPISODE_CK5, LEVEL_IVS),
        "Security Center Complete": loc_level_complete(AP_EPISODE_CK5, LEVEL_SC),
        "Security Center - Red Gem": loc_keygem(AP_EPISODE_CK5, LEVEL_SC, GEM_RED),
        "Security Center - Blue Gem": loc_keygem(AP_EPISODE_CK5, LEVEL_SC, GEM_BLUE),
        "Security Center - Keycard": loc_keycard(AP_EPISODE_CK5, LEVEL_SC),
    },

    "K5 Hub": {
        "Defense Tunnel Vlook Complete": loc_level_complete(AP_EPISODE_CK5, LEVEL_DTV),
        "Defense Tunnel Vlook - Red Gem": loc_keygem(AP_EPISODE_CK5, LEVEL_DTV, GEM_RED),
        "Defense Tunnel Vlook - Yellow Gem": loc_keygem(AP_EPISODE_CK5, LEVEL_DTV, GEM_YELLOW),
        "Defense Tunnel Vlook - Keycard": loc_keycard(AP_EPISODE_CK5, LEVEL_DTV),
        "Defense Tunnel Burrh Complete": loc_level_complete(AP_EPISODE_CK5, LEVEL_DTB),
        "Defense Tunnel Burrh - Red Gem": loc_keygem(AP_EPISODE_CK5, LEVEL_DTB, GEM_RED),
        "Defense Tunnel Burrh - Yellow Gem": loc_keygem(AP_EPISODE_CK5, LEVEL_DTB, GEM_YELLOW),
        "Defense Tunnel Burrh - Blue Gem": loc_keygem(AP_EPISODE_CK5, LEVEL_DTB, GEM_BLUE),
        "Defense Tunnel Burrh - Green Gem": loc_keygem(AP_EPISODE_CK5, LEVEL_DTB, GEM_GREEN),
        "Defense Tunnel Burrh - Keycard": loc_keycard(AP_EPISODE_CK5, LEVEL_DTB),
        "Defense Tunnel Sorra Complete": loc_level_complete(AP_EPISODE_CK5, LEVEL_DTS),
        "Defense Tunnel Sorra - Yellow Gem": loc_keygem(AP_EPISODE_CK5, LEVEL_DTS, GEM_YELLOW),
        "Defense Tunnel Sorra - Keycard": loc_keycard(AP_EPISODE_CK5, LEVEL_DTS),
        "Defense Tunnel Teln Complete": loc_level_complete(AP_EPISODE_CK5, LEVEL_DTT),
        "Defense Tunnel Teln - Red Gem": loc_keygem(AP_EPISODE_CK5, LEVEL_DTT, GEM_RED),
        "Defense Tunnel Teln - Yellow Gem": loc_keygem(AP_EPISODE_CK5, LEVEL_DTT, GEM_YELLOW),
        "Defense Tunnel Teln - Blue Gem": loc_keygem(AP_EPISODE_CK5, LEVEL_DTT, GEM_BLUE),
        "Defense Tunnel Teln - Green Gem": loc_keygem(AP_EPISODE_CK5, LEVEL_DTT, GEM_GREEN),
        "Defense Tunnel Teln - Keycard": loc_keycard(AP_EPISODE_CK5, LEVEL_DTT),
        "Energy Flow Systems Complete": loc_level_complete(AP_EPISODE_CK5, LEVEL_EFS),
        "Energy Flow Systems - Red Gem": loc_keygem(AP_EPISODE_CK5, LEVEL_EFS, GEM_RED),
        "Energy Flow Systems - Yellow Gem": loc_keygem(AP_EPISODE_CK5, LEVEL_EFS, GEM_YELLOW),
        "Energy Flow Systems - Blue Gem": loc_keygem(AP_EPISODE_CK5, LEVEL_EFS, GEM_BLUE),
        "Energy Flow Systems - Green Gem": loc_keygem(AP_EPISODE_CK5, LEVEL_EFS, GEM_GREEN),
        "Regulation Control Center Complete": loc_level_complete(AP_EPISODE_CK5, LEVEL_RCC),
        "Regulation Control Center - Red Gem": loc_keygem(AP_EPISODE_CK5, LEVEL_RCC, GEM_RED),
        "Regulation Control Center - Yellow Gem": loc_keygem(AP_EPISODE_CK5, LEVEL_RCC, GEM_YELLOW),
        "Regulation Control Center - Blue Gem": loc_keygem(AP_EPISODE_CK5, LEVEL_RCC, GEM_BLUE),
        "Neutrino Burst Injector Complete": loc_level_complete(AP_EPISODE_CK5, LEVEL_NBI),
        "Neutrino Burst Injector - Red Gem": loc_keygem(AP_EPISODE_CK5, LEVEL_NBI, GEM_RED),
        "Neutrino Burst Injector - Blue Gem": loc_keygem(AP_EPISODE_CK5, LEVEL_NBI, GEM_BLUE),
        "Brownian Motion Inducer Complete": loc_level_complete(AP_EPISODE_CK5, LEVEL_BMI),
        "Brownian Motion Inducer - Yellow Gem": loc_keygem(AP_EPISODE_CK5, LEVEL_BMI, GEM_YELLOW),
        "Brownian Motion Inducer - Blue Gem": loc_keygem(AP_EPISODE_CK5, LEVEL_BMI, GEM_BLUE),
    },

    "End Game": {
        "Gravitational Damping Hub Complete": loc_level_complete(AP_EPISODE_CK5, LEVEL_GDH),
        "Gravitational Damping Hub - Red Gem": loc_keygem(AP_EPISODE_CK5, LEVEL_GDH, GEM_RED),
        "Gravitational Damping Hub - Green Gem": loc_keygem(AP_EPISODE_CK5, LEVEL_GDH, GEM_GREEN),
        "Gravitational Damping Hub - Keycard": loc_keycard(AP_EPISODE_CK5, LEVEL_GDH),
        "Quantum Explosion Dynamo Complete": loc_level_complete(AP_EPISODE_CK5, LEVEL_QED),
        "Quantum Explosion Dynamo - Red Gem": loc_keygem(AP_EPISODE_CK5, LEVEL_QED, GEM_RED),
        "Quantum Explosion Dynamo - Yellow Gem": loc_keygem(AP_EPISODE_CK5, LEVEL_QED, GEM_YELLOW),
        "Quantum Explosion Dynamo - Blue Gem": loc_keygem(AP_EPISODE_CK5, LEVEL_QED, GEM_BLUE),
        "Quantum Explosion Dynamo - Green Gem": loc_keygem(AP_EPISODE_CK5, LEVEL_QED, GEM_GREEN),
    },
}

# --------------------------------------------------
# Extra-life pickup locations
# --------------------------------------------------
# Lifewater Flask (CK4) and Vitalin Keg (CK5) are the +1 extra-life pickups.
# In the engine they're item index 10, spawned either from info-layer tile
# 67 (object) or from foreground tile misc=27 (tile-layer). The engine
# scans both at level load and assigns each a deterministic 0-based index
# spanning both spawn paths. When Keen picks one up, ap_on_extralife_get
# fires and the engine sends LOC_FLASK(1, lvl, idx) for CK4 or
# LOC_KEG(2, lvl, idx) for CK5.
#
# These are NOT the lifewater drops (those are misc=4 centilives that
# accumulate toward an extra life — out of scope for AP locations).
#
# Counts default to 0; populate from score_item_dump.txt produced by the
# engine when run with OMNISPEAK_DUMP_SCORE_ITEMS=1.
#
# Indices are 0-based to match the engine. Display name uses 1-based for
# readability ("Lifewater Oasis - Lifewater Flask 1").

ck4_extralife_counts = {
    LEVEL_BV: 7, LEVEL_SV: 0, LEVEL_PP: 2, LEVEL_COTD: 2, LEVEL_COC: 1,
    LEVEL_CRYS: 0, LEVEL_HIL: 1, LEVEL_SY: 1, LEVEL_MIR: 1, LEVEL_LO: 5,
    LEVEL_POTM: 1, LEVEL_POS: 8, LEVEL_POTGA: 4, LEVEL_IOT: 2, LEVEL_IOF: 1,
    LEVEL_WOW: 1, LEVEL_BWBM: 0,
}

ck5_extralife_counts = {
    LEVEL_IVS: 10, LEVEL_SC: 2, LEVEL_DTV: 2, LEVEL_EFS: 1, LEVEL_DTB: 2,
    LEVEL_RCC: 0, LEVEL_DTS: 0, LEVEL_NBI: 0, LEVEL_DTT: 1, LEVEL_BMI: 1,
    LEVEL_GDH: 1, LEVEL_QED: 2,
}

# (level_id, scan_index) tuples for CK4 Lifewater Flasks that exist in the
# level data but cannot be reached during normal gameplay. Confirmed by
# cross-referencing the KeenWiki:
# - Lifewater Oasis: all 5 flasks sit on the same Y row at the bottom of the
#   level, unreachable due to a known level-design oversight.
# - The Perilous Pit: both flasks unreachable in normal gameplay.
# - Pyramid of the Gnosticine Ancients flask 0 (engine index): reachable in
#   Apogee v1.0/v1.1 only. Omnispeak ships v1.4 data (see
#   data/keen4/EPISODE.CK4 in the omnispeak fork), so it cannot be obtained.
#
# Cave of the Descendents' two flasks are reachable via a secret passage in
# the lower-right (drop through the shaft with the moving shovels). The
# pocket they sit in has no exit, so the player must die to leave — but the
# pickups register before death and dying nets +1 life overall, so the trip
# is not punishing. They are valid AP checks.
ck4_lifewater_flask_excluded = {
    (LEVEL_LO, 0), (LEVEL_LO, 1), (LEVEL_LO, 2), (LEVEL_LO, 3), (LEVEL_LO, 4),
    (LEVEL_PP, 0), (LEVEL_PP, 1),
    (LEVEL_POTGA, 0),
}

# Per-level engine-index → display-name override. Without an entry here,
# location names follow engine scan order (idx+1). Use this only when the
# engine's scan order does not match the visual layout players reason about.
#
# Engine scan order is info-plane first (in row-major order), then
# tile-plane misc=27 (also row-major). So info-plane spawns always get
# lower indices than tile-plane spawns, regardless of where they sit in
# the level.
#
# Pyramid of the Gnosticine Ancients (v1.4):
#   engine idx 0 → info  (4, 35)  — excluded (v1.0/v1.1 only)
#   engine idx 1 → info  (37, 92) — lone bottom flask (pogo)
#   engine idx 2 → tile  (36, 65) — upper-left paired flask (stunner)
#   engine idx 3 → tile  (37, 65) — upper-right paired flask (stunner)
# Players naturally label the paired upper flasks "2" and "3" and the
# lone bottom flask "4". The Rules.py rules are written under that visual
# convention ("Flask 4" = pogo, "Flasks 2/3" = stunner), so remap here.
ck4_flask_display_index = {
    (LEVEL_POTGA, 1): 4,
    (LEVEL_POTGA, 2): 2,
    (LEVEL_POTGA, 3): 3,
}

ck5_keg_display_index = {}

ck4_level_id_to_name = {
    LEVEL_BV: "Border Village",
    LEVEL_SV: "Slug Village",
    LEVEL_PP: "The Perilous Pit",
    LEVEL_COTD: "Cave of the Descendents",
    LEVEL_COC: "Chasm of Chills",
    LEVEL_CRYS: "Crystalus",
    LEVEL_HIL: "Hilville",
    LEVEL_SY: "Sand Yego",
    LEVEL_MIR: "Miragia",
    LEVEL_LO: "Lifewater Oasis",
    LEVEL_POTM: "Pyramid of the Moons",
    LEVEL_POS: "Pyramid of Shadows",
    LEVEL_POTGA: "Pyramid of the Gnosticine Ancients",
    LEVEL_IOT: "Isle of Tar",
    LEVEL_IOF: "Isle of Fire",
    LEVEL_WOW: "Well of Wishes",
    LEVEL_BWBM: "Bean-With-Bacon Megarocket",
}

ck5_level_id_to_name = {
    LEVEL_IVS: "Ion Ventilation System",
    LEVEL_SC: "Security Center",
    LEVEL_DTV: "Defense Tunnel Vlook",
    LEVEL_EFS: "Energy Flow Systems",
    LEVEL_DTB: "Defense Tunnel Burrh",
    LEVEL_RCC: "Regulation Control Center",
    LEVEL_DTS: "Defense Tunnel Sorra",
    LEVEL_NBI: "Neutrino Burst Injector",
    LEVEL_DTT: "Defense Tunnel Teln",
    LEVEL_BMI: "Brownian Motion Inducer",
    LEVEL_GDH: "Gravitational Damping Hub",
    LEVEL_QED: "Quantum Explosion Dynamo",
}

# Mirrors the regional grouping in ck4_locations_by_region / ck5_locations_by_region
# so kegs/flasks land in the same region as their level's completion check.
ck4_level_id_to_region = {
    LEVEL_BV: "K4 Overworld", LEVEL_SV: "K4 Overworld",
    LEVEL_PP: "K4 Overworld", LEVEL_COTD: "K4 Overworld",
    LEVEL_COC: "K4 Overworld", LEVEL_CRYS: "K4 Overworld",
    LEVEL_HIL: "K4 Overworld", LEVEL_SY: "K4 Overworld",
    LEVEL_MIR: "K4 Overworld", LEVEL_LO: "K4 Overworld",
    LEVEL_POTM: "K4 Overworld", LEVEL_POS: "K4 Overworld",
    LEVEL_POTGA: "K4 Overworld", LEVEL_BWBM: "K4 Overworld",
    LEVEL_IOT: "K4 Lake", LEVEL_IOF: "K4 Lake", LEVEL_WOW: "K4 Lake",
}

ck5_level_id_to_region = {
    LEVEL_IVS: "K5 Start", LEVEL_SC: "K5 Start",
    LEVEL_DTV: "K5 Hub", LEVEL_EFS: "K5 Hub", LEVEL_DTB: "K5 Hub",
    LEVEL_RCC: "K5 Hub", LEVEL_DTS: "K5 Hub", LEVEL_NBI: "K5 Hub",
    LEVEL_DTT: "K5 Hub", LEVEL_BMI: "K5 Hub",
    LEVEL_GDH: "End Game", LEVEL_QED: "End Game",
}


def _build_extralife_locations(episode, level_counts, item_label, loc_builder,
                               level_to_name, level_to_region, excluded=None,
                               display_index=None):
    """Generate {region_name: {location_name: location_id, ...}, ...}.

    display_index optionally remaps (level_id, engine_idx) → display number
    when the engine's scan order does not match the visual layout players
    reason about. Defaults to idx+1.
    """
    excluded = excluded or set()
    display_index = display_index or {}
    result = {}
    for level_id, count in level_counts.items():
        if count <= 0:
            continue
        region = level_to_region.get(level_id)
        name = level_to_name.get(level_id)
        if region is None or name is None:
            continue
        for idx in range(count):
            if (level_id, idx) in excluded:
                continue
            display_num = display_index.get((level_id, idx), idx + 1)
            loc_name = f"{name} - {item_label} {display_num}"
            result.setdefault(region, {})[loc_name] = loc_builder(episode, level_id, idx)
    return result


# CK4 Lifewater Flasks live in the FLASK base; CK5 Vitalin Kegs in the KEG
# base. Each episode only has one extra-life sprite, so there's no overlap.
ck4_flask_locations_by_region = _build_extralife_locations(
    AP_EPISODE_CK4, ck4_extralife_counts, "Lifewater Flask", loc_flask,
    ck4_level_id_to_name, ck4_level_id_to_region,
    excluded=ck4_lifewater_flask_excluded,
    display_index=ck4_flask_display_index,
)

ck5_keg_locations_by_region = _build_extralife_locations(
    AP_EPISODE_CK5, ck5_extralife_counts, "Vitalin Keg", loc_keg,
    ck5_level_id_to_name, ck5_level_id_to_region,
    display_index=ck5_keg_display_index,
)

# --------------------------------------------------
# Pointsanity (5000-pt pickups)
# --------------------------------------------------
# The omnispeak-ap engine currently only emits AP location checks for the
# 5000-pt class (class 5). When the engine flips additional classes on, add
# the matching counts dictionaries here and extend _build_pointsanity_locations
# to walk every enabled class. Until then, "pointsanity" in the apworld means
# "5000-pt pickups only".
#
# Counts are populated from score_item_dump.txt produced by the engine when
# run with OMNISPEAK_DUMP_SCORE_ITEMS=1. Indices are 0-based to match the
# engine's per-class scan counter; display names use 1-based for readability
# ("Crystalus - 5000pt Pickup 1").

ck4_points5k_counts = {
    LEVEL_BV: 0,   LEVEL_SV: 3,    LEVEL_PP: 1,    LEVEL_COTD: 11, LEVEL_COC: 7,
    LEVEL_CRYS: 3, LEVEL_HIL: 1,   LEVEL_SY: 4,    LEVEL_MIR: 5,   LEVEL_LO: 0,
    LEVEL_POTM: 6, LEVEL_POS: 1,   LEVEL_POTGA: 1,
    # Pyramid of the Forbidden is intentionally not wired into the apworld
    # (no level item, no completion check; see commented-out lines in
    # Items.py). Its 14 5000-pt pickups exist in the level data but cannot
    # be exposed as checks until the level itself is added. Engine-side
    # those pickups will still fire ap_on_pointitem_get → the AP server
    # will ignore the unknown location IDs.
    LEVEL_POTF: 0,
    LEVEL_IOT: 3,  LEVEL_IOF: 5,   LEVEL_WOW: 0,   LEVEL_BWBM: 0,
}

ck5_points5k_counts = {
    LEVEL_IVS: 0,  LEVEL_SC: 28,  LEVEL_DTV: 7,  LEVEL_EFS: 10, LEVEL_DTB: 4,
    LEVEL_RCC: 0,  LEVEL_DTS: 13, LEVEL_NBI: 4,  LEVEL_DTT: 10, LEVEL_BMI: 8,
    LEVEL_GDH: 15, LEVEL_QED: 9,
}

# Same shape as ck4_lifewater_flask_excluded: (level_id, engine_idx) tuples
# for 5000-pt pickups present in level data but unreachable in normal play.
# Populate as concrete unreachables are found.
ck4_points5k_excluded: set[tuple[int, int]] = {
    # Sand Yego engine idx 0 = tile (31, 45), info-layer. Could not be
    # located during the manual audit — flagging as excluded until/unless
    # a route is confirmed. Worst case: a missing check, never a softlock.
    (LEVEL_SY, 0),
}
ck5_points5k_excluded: set[tuple[int, int]] = set()

# Per-level engine-index → display-number override. Use only when the engine
# scan order (info-plane row-major first, then tile-plane row-major) does not
# match how a player visually labels the pickups.
ck4_points5k_display_index: dict[tuple[int, int], int] = {}
ck5_points5k_display_index: dict[tuple[int, int], int] = {}

# POTF doesn't appear in the existing level→region map (it's not in the flask
# locations either because there are zero flasks there) — patch it in for
# pointsanity so its 5000-pt pickups land in the right region.
LEVEL_POTF_REGION = "K4 Overworld"
ck4_level_id_to_region_with_potf = {**ck4_level_id_to_region, LEVEL_POTF: LEVEL_POTF_REGION}
ck4_level_id_to_name_with_potf = {**ck4_level_id_to_name, LEVEL_POTF: "Pyramid of the Forbidden"}


def _build_pointsanity_locations(episode, level_counts, level_to_name,
                                 level_to_region, excluded=None,
                                 display_index=None):
    """{region_name: {location_name: location_id}} for 5000-pt pickups only.

    Mirrors _build_extralife_locations but routes through loc_pointsanity with
    class=POINTS5K_CLASS. Returns nothing for levels with count=0.
    """
    excluded = excluded or set()
    display_index = display_index or {}
    result = {}
    for level_id, count in level_counts.items():
        if count <= 0:
            continue
        region = level_to_region.get(level_id)
        name = level_to_name.get(level_id)
        if region is None or name is None:
            continue
        for idx in range(count):
            if (level_id, idx) in excluded:
                continue
            display_num = display_index.get((level_id, idx), idx + 1)
            loc_name = f"{name} - 5000pt Pickup {display_num}"
            result.setdefault(region, {})[loc_name] = loc_pointsanity(
                episode, level_id, POINTS5K_CLASS, idx)
    return result


ck4_points5k_locations_by_region = _build_pointsanity_locations(
    AP_EPISODE_CK4, ck4_points5k_counts,
    ck4_level_id_to_name_with_potf, ck4_level_id_to_region_with_potf,
    excluded=ck4_points5k_excluded,
    display_index=ck4_points5k_display_index,
)

ck5_points5k_locations_by_region = _build_pointsanity_locations(
    AP_EPISODE_CK5, ck5_points5k_counts,
    ck5_level_id_to_name, ck5_level_id_to_region,
    excluded=ck5_points5k_excluded,
    display_index=ck5_points5k_display_index,
)


# Full name→id table covers every potentially registered location so the
# AP client and tracker can resolve names regardless of generation options.
# Locations only become real (attached to a region) when the corresponding
# option is enabled in Regions.py.
location_table = {
    loc_name: loc_id
    for locations in [
        ck4_locations_by_region, ck5_locations_by_region,
        ck4_flask_locations_by_region, ck5_keg_locations_by_region,
        ck4_points5k_locations_by_region, ck5_points5k_locations_by_region,
    ]
    for region_dict in locations.values()
    for loc_name, loc_id in region_dict.items()
}