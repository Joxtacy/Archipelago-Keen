from BaseClasses import Item, ItemClassification
from dataclasses import dataclass

class KeenItem(Item):
    game = "Commander Keen"

@dataclass(frozen=True)
class ItemDef:
    name: str
    classification: ItemClassification
    code: int

# --------------------------------------------------
# Define all items
# --------------------------------------------------

ck_common_items = [
    ItemDef("Pogo Stick", ItemClassification.progression, 101),
    ItemDef("Neural Stunner", ItemClassification.useful, 102),
]

ck_filler_items = [
    ItemDef("Extra Keen", ItemClassification.filler, 900),
    ItemDef("Stunner Ammo", ItemClassification.filler, 901),
]

ck4_unique_items = [
    ItemDef("Wetsuit", ItemClassification.progression, 103),
]

ck4_level_items = [
    ItemDef("Border Village", ItemClassification.progression, 1001),
    ItemDef("Slug Village", ItemClassification.progression, 1002),
    ItemDef("The Perilous Pit", ItemClassification.progression, 1003),
    ItemDef("Cave of the Descendents", ItemClassification.progression, 1004),
    ItemDef("Chasm of Chills", ItemClassification.progression, 1005),
    ItemDef("Crystalus", ItemClassification.progression, 1006),
    ItemDef("Hilville", ItemClassification.progression, 1007),
    ItemDef("Sand Yego", ItemClassification.progression, 1008),
    ItemDef("Miragia", ItemClassification.progression, 1009),
    ItemDef("Lifewater Oasis", ItemClassification.progression, 1010),
    ItemDef("Pyramid of the Moons", ItemClassification.progression, 1011),
    ItemDef("Pyramid of Shadows", ItemClassification.progression, 1012),
    ItemDef("Pyramid of the Gnosticine Ancients", ItemClassification.progression, 1013),
    # ItemDef("Pyramid of the Forbidden", ItemClassification.progression, 1014),
    ItemDef("Isle of Tar", ItemClassification.progression, 1015),
    ItemDef("Isle of Fire", ItemClassification.progression, 1016),
    ItemDef("Well of Wishes", ItemClassification.progression, 1017),
    ItemDef("Bean-With-Bacon Megarocket", ItemClassification.progression, 1018),
]

ck4_gem_items = [
    ItemDef("The Perilous Pit - Red Gem", ItemClassification.progression, 100300),
    ItemDef("The Perilous Pit - Blue Gem", ItemClassification.progression, 100302),
    ItemDef("Cave of the Descendents - Red Gem", ItemClassification.progression, 100400),
    ItemDef("Cave of the Descendents - Yellow Gem", ItemClassification.progression, 100401),
    ItemDef("Crystalus - Red Gem", ItemClassification.progression, 100600),
    ItemDef("Crystalus - Yellow Gem", ItemClassification.progression, 100601),
    ItemDef("Crystalus - Blue Gem", ItemClassification.progression, 100602),
    ItemDef("Crystalus - Green Gem", ItemClassification.progression, 100603),
    ItemDef("Sand Yego - Green Gem", ItemClassification.progression, 100803),
    ItemDef("Lifewater Oasis - Green Gem", ItemClassification.progression, 101003),
    ItemDef("Pyramid of the Moons - Yellow Gem", ItemClassification.progression, 101101),
    ItemDef("Pyramid of Shadows - Blue Gem", ItemClassification.progression, 101202),
    ItemDef("Pyramid of the Gnosticine Ancients - Red Gem", ItemClassification.progression, 101300),
    ItemDef("Pyramid of the Gnosticine Ancients - Green Gem", ItemClassification.progression, 101303),
    # ItemDef("Pyramid of the Forbidden - Red Gem 1", ItemClassification.progression, 101400),
    # ItemDef("Pyramid of the Forbidden - Red Gem 2", ItemClassification.progression, 101410),
    # ItemDef("Pyramid of the Forbidden - Yellow Gem", ItemClassification.progression, 101401),
    # ItemDef("Pyramid of the Forbidden - Blue Gem", ItemClassification.progression, 101402),
    # ItemDef("Pyramid of the Forbidden - Green Gem", ItemClassification.progression, 101403),
    ItemDef("Isle of Tar - Red Gem", ItemClassification.progression, 101500),
    ItemDef("Isle of Tar - Yellow Gem", ItemClassification.progression, 101501),
    ItemDef("Isle of Tar - Blue Gem", ItemClassification.progression, 101502),
    ItemDef("Isle of Fire - Yellow Gem", ItemClassification.progression, 101601),
    ItemDef("Isle of Fire - Blue Gem", ItemClassification.progression, 101602),
]

ck4_gemset_items = [
    ItemDef("The Perilous Pit Gemset", ItemClassification.progression, 100399),
    ItemDef("Cave of the Descendents Gemset", ItemClassification.progression, 100499),
    ItemDef("Crystalus Gemset", ItemClassification.progression, 100699),
    ItemDef("Sand Yego Gemset", ItemClassification.progression, 100899),
    ItemDef("Lifewater Oasis Gemset", ItemClassification.progression, 101099),
    ItemDef("Pyramid of the Moons Gemset", ItemClassification.progression, 101199),
    ItemDef("Pyramid of Shadows Gemset", ItemClassification.progression, 101299),
    ItemDef("Pyramid of the Gnosticine Ancients Gemset", ItemClassification.progression, 101399),
    # ItemDef("Pyramid of the Forbidden", ItemClassification.progression, 101499),
    ItemDef("Isle of Tar Gemset", ItemClassification.progression, 101599),
    ItemDef("Isle of Fire Gemset", ItemClassification.progression, 101699),
]

ck5_level_items = [
    ItemDef("Ion Ventilation System", ItemClassification.progression, 2001),
    ItemDef("Security Center", ItemClassification.progression, 2002),
    ItemDef("Defense Tunnel Vlook", ItemClassification.progression, 2003),
    ItemDef("Energy Flow Systems", ItemClassification.progression, 2004),
    ItemDef("Defense Tunnel Burrh", ItemClassification.progression, 2005),
    ItemDef("Regulation Control Center", ItemClassification.progression, 2006),
    ItemDef("Defense Tunnel Sorra", ItemClassification.progression, 2007),
    ItemDef("Neutrino Burst Injector", ItemClassification.progression, 2008),
    ItemDef("Defense Tunnel Teln", ItemClassification.progression, 2009),
    ItemDef("Brownian Motion Inducer", ItemClassification.progression, 2010),
    ItemDef("Gravitational Damping Hub", ItemClassification.progression, 2011),
    ItemDef("Quantum Explosion Dynamo", ItemClassification.progression, 2012),
]

ck5_gem_items = [
    ItemDef("Security Center - Red Gem", ItemClassification.progression, 200200),
    ItemDef("Security Center - Blue Gem", ItemClassification.progression, 200202),
    ItemDef("Defense Tunnel Vlook - Red Gem", ItemClassification.progression, 200300),
    ItemDef("Defense Tunnel Vlook - Yellow Gem", ItemClassification.progression, 200301),
    ItemDef("Energy Flow Systems - Red Gem", ItemClassification.progression, 200400),
    ItemDef("Energy Flow Systems - Yellow Gem", ItemClassification.progression, 200401),
    ItemDef("Energy Flow Systems - Blue Gem", ItemClassification.progression, 200402),
    ItemDef("Energy Flow Systems - Green Gem", ItemClassification.progression, 200403),
    ItemDef("Defense Tunnel Burrh - Red Gem",  ItemClassification.progression, 200500),
    ItemDef("Defense Tunnel Burrh - Yellow Gem", ItemClassification.progression, 200501),
    ItemDef("Defense Tunnel Burrh - Blue Gem", ItemClassification.progression, 200502),
    ItemDef("Defense Tunnel Burrh - Green Gem", ItemClassification.progression, 200503),
    ItemDef("Regulation Control Center - Red Gem", ItemClassification.progression, 200600),
    ItemDef("Regulation Control Center - Yellow Gem", ItemClassification.progression, 200601),
    ItemDef("Regulation Control Center - Blue Gem", ItemClassification.progression, 200602),
    ItemDef("Defense Tunnel Sorra - Yellow Gem", ItemClassification.progression, 200701),
    ItemDef("Neutrino Burst Injector - Red Gem", ItemClassification.progression, 200800),
    ItemDef("Neutrino Burst Injector - Blue Gem", ItemClassification.progression, 200802),
    ItemDef("Defense Tunnel Teln - Red Gem", ItemClassification.progression, 200900),
    ItemDef("Defense Tunnel Teln - Yellow Gem", ItemClassification.progression, 200901),
    ItemDef("Defense Tunnel Teln - Blue Gem", ItemClassification.progression, 200902),
    ItemDef("Defense Tunnel Teln - Green Gem", ItemClassification.progression, 200903),
    ItemDef("Brownian Motion Inducer - Yellow Gem", ItemClassification.progression, 201001),
    ItemDef("Brownian Motion Inducer - Blue Gem", ItemClassification.progression, 201002),
    ItemDef("Gravitational Damping Hub - Red Gem", ItemClassification.progression, 201100),
    ItemDef("Gravitational Damping Hub - Green Gem", ItemClassification.progression, 201103),
    ItemDef("Quantum Explosion Dynamo - Red Gem", ItemClassification.progression, 201200),
    ItemDef("Quantum Explosion Dynamo - Yellow Gem", ItemClassification.progression, 201201),
    ItemDef("Quantum Explosion Dynamo - Blue Gem", ItemClassification.progression, 201202),
    ItemDef("Quantum Explosion Dynamo - Green Gem", ItemClassification.progression, 201203),
]

ck5_keycard_items = [
    ItemDef("Security Center - Keycard", ItemClassification.progression, 200204),
    ItemDef("Defense Tunnel Vlook - Keycard", ItemClassification.progression, 200304),
    ItemDef("Defense Tunnel Burrh - Keycard", ItemClassification.progression, 200504),
    ItemDef("Defense Tunnel Sorra - Keycard", ItemClassification.progression, 200704),
    ItemDef("Defense Tunnel Teln - Keycard", ItemClassification.progression, 200904),
    ItemDef("Gravitational Damping Hub - Keycard", ItemClassification.progression, 201104),
]

ck5_gemset_items = [
    ItemDef("Security Center Gemset", ItemClassification.progression, 200299),
    ItemDef("Defense Tunnel Vlook Gemset", ItemClassification.progression, 200399),
    ItemDef("Energy Flow Systems Gemset", ItemClassification.progression, 200499),
    ItemDef("Defense Tunnel Burrh Gemset", ItemClassification.progression, 200599),
    ItemDef("Regulation Control Center Gemset", ItemClassification.progression, 200699),
    ItemDef("Defense Tunnel Sorra Gemset", ItemClassification.progression, 200799),
    ItemDef("Neutrino Burst Injector Gemset", ItemClassification.progression, 200899),
    ItemDef("Defense Tunnel Teln Gemset", ItemClassification.progression, 200999),
    ItemDef("Brownian Motion Inducer Gemset", ItemClassification.progression, 201099),
    ItemDef("Gravitational Damping Hub Gemset", ItemClassification.progression, 201199),
    ItemDef("Quantum Explosion Dynamo Gemset", ItemClassification.progression, 201299),
]

# --------------------------------------------------
# Create master item table
# --------------------------------------------------

ck_all_items = (
    ck_common_items
    + ck_filler_items
    + ck4_unique_items
    + ck4_level_items
    + ck4_gem_items
    + ck4_gemset_items
    + ck5_level_items
    + ck5_gem_items
    + ck5_keycard_items
    + ck5_gemset_items
)
item_table = {i.name: i.classification for i in ck_all_items}
item_name_to_id = {i.name: i.code for i in ck_all_items}

# --------------------------------------------------
# Item creation helper
# --------------------------------------------------

def create_item(name: str, player: int) -> KeenItem:
    return KeenItem(
        name,
        item_table[name],
        item_name_to_id[name],
        player
    )