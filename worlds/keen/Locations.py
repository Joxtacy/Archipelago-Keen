# Locations.py
from BaseClasses import Location

class KeenLocation(Location):
    game = "Commander Keen"

# --------------------------------------------------
# Constants
# --------------------------------------------------

AP_LOC_BASE_LEVEL_COMPLETE = 10000
AP_LOC_BASE_KEYGEM = 20000
AP_LOC_BASE_KEYCARD = 30000

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
    return(
        AP_LOC_BASE_KEYCARD
        + (ep * AP_LOC_EPISODE_STRIDE)
        + (lvl * AP_LOC_LEVEL_STRIDE)
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

location_table = {
    loc_name: loc_id
    for locations in [ck4_locations_by_region, ck5_locations_by_region]
    for region_dict in locations.values()
    for loc_name, loc_id in region_dict.items()
}