from BaseClasses import Region
from .Locations import ck4_locations_by_region, ck5_locations_by_region, KeenLocation

# --------------------------------------------------
# Create regions
# --------------------------------------------------

def create_ck4_regions(world):
    mw = world.multiworld
    player = world.player

    menu = mw.get_region("Menu", player)

    k4_overworld = Region("K4 Overworld", player, mw)
    k4_lake = Region("K4 Lake", player, mw)

    mw.regions += [k4_overworld, k4_lake]
    
    menu.connect(k4_overworld, "Keen4")
    k4_overworld.connect(k4_lake, "Overworld to Lake", lambda state: state.has("Wetsuit", player))

    for region_name in ck4_locations_by_region:
        attach_locations(world, region_name)

def create_ck5_regions(world):
    mw = world.multiworld
    player = world.player

    menu = mw.get_region("Menu", player)

    k5_start = Region("K5 Start", player, mw)
    k5_hub = Region("K5 Hub", player, mw)
    k5_end = Region("End Game", player, mw)

    mw.regions += [k5_start, k5_hub, k5_end]

    # Connect ck5 regions
    menu.connect(k5_start, "Keen5")
    k5_start.connect(k5_hub, "K5 Hub")
    k5_hub.connect(k5_end, "End Game", lambda state:
        (state.has("Energy Flow Systems", player) and
            (
                (
                    state.has("Energy Flow Systems - Red Gem", player) and
                    state.has("Energy Flow Systems - Yellow Gem", player) and
                    state.has("Energy Flow Systems - Blue Gem", player) and
                    state.has("Energy Flow Systems - Green Gem", player)
                ) or
                state.has("Energy Flow Systems Gemset", player)
            )) and
        (state.has("Regulation Control Center", player) and
            (
                (
                    state.has("Regulation Control Center - Red Gem", player) and
                    state.has("Regulation Control Center - Yellow Gem", player) and
                    state.has("Regulation Control Center - Blue Gem", player)
                ) or
                state.has("Regulation Control Center Gemset", player)
            )
        ) and
        (state.has("Neutrino Burst Injector", player) and
            (
                (
                    state.has("Neutrino Burst Injector - Red Gem", player) and
                    state.has("Neutrino Burst Injector - Blue Gem", player)
                ) or
                state.has("Neutrino Burst Injector Gemset", player)
            ) 
        ) and
        (state.has("Brownian Motion Inducer", player) and
            (
                (
                    state.has("Brownian Motion Inducer - Yellow Gem", player) and
                    state.has("Brownian Motion Inducer - Blue Gem", player)
                ) or
                state.has("Brownian Motion Inducer Gemset", player)
            )
        ))
    
    for region_name in ck5_locations_by_region:
        attach_locations(world, region_name)

def attach_locations(world, region_name):
    mw = world.multiworld
    player = world.player
    region = mw.get_region(region_name, player)

    locations = (
        ck4_locations_by_region.get(region_name, {}) or
        ck5_locations_by_region.get(region_name, {})
    )

    for loc_name, loc_id in locations.items():
        region.locations.append(
            KeenLocation(player, loc_name, loc_id, region)
        )