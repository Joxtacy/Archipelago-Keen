from BaseClasses import Location

class KeenLocation(Location):
    game = "Commander Keen"

# --------------------------------------------------
# Constants
# --------------------------------------------------

AP_LOC_BASE_LEVEL_COMPLETE = 10000
AP_LOC_BASE_KEYGEM = 20000
AP_LOC_BASE_KEYCARD = 30000
AP_LOC_BASE_POINTSANITY = 40000
# Centilife pickups (extra-life accumulators, foreground tile misc=4).
# CK5 sprite is a Vitalin Keg; CK4 sprite is a Lifewater Flask. Same engine
# mechanic, different sprite — we use two separate bases so the location
# name space stays clean per episode.
AP_LOC_BASE_KEG = 50000     # CK5 Vitalin Kegs
AP_LOC_BASE_FLASK = 60000   # CK4 Lifewater Flasks

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
# - Cave of the Descendents: both flasks unreachable without cheating or
#   dying through them (the KeenWiki notes flasks don't register on death).
ck4_lifewater_flask_excluded = {
    (LEVEL_LO, 0), (LEVEL_LO, 1), (LEVEL_LO, 2), (LEVEL_LO, 3), (LEVEL_LO, 4),
    (LEVEL_COTD, 0), (LEVEL_COTD, 1),
}

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
                               level_to_name, level_to_region, excluded=None):
    """Generate {region_name: {location_name: location_id, ...}, ...}."""
    excluded = excluded or set()
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
            loc_name = f"{name} - {item_label} {idx + 1}"
            result.setdefault(region, {})[loc_name] = loc_builder(episode, level_id, idx)
    return result


# CK4 Lifewater Flasks live in the FLASK base; CK5 Vitalin Kegs in the KEG
# base. Each episode only has one extra-life sprite, so there's no overlap.
ck4_flask_locations_by_region = _build_extralife_locations(
    AP_EPISODE_CK4, ck4_extralife_counts, "Lifewater Flask", loc_flask,
    ck4_level_id_to_name, ck4_level_id_to_region,
    excluded=ck4_lifewater_flask_excluded,
)

ck5_keg_locations_by_region = _build_extralife_locations(
    AP_EPISODE_CK5, ck5_extralife_counts, "Vitalin Keg", loc_keg,
    ck5_level_id_to_name, ck5_level_id_to_region,
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
    ]
    for region_dict in locations.values()
    for loc_name, loc_id in region_dict.items()
}