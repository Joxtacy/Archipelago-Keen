from worlds.generic.Rules import set_rule

from .Locations import (
    ck4_flask_locations_by_region, ck5_keg_locations_by_region,
    ck4_level_id_to_name, ck5_level_id_to_name,
)

# --------------------------------------------------
# Create location rules
# --------------------------------------------------

# rule builder helper
def set_location_rule(world, player, location_name, level_name,
                      gems=None,
                      requires_pogo=False,
                      requires_stunner=False,
                      requires_pogo_or_stunner=False,
                      keycard=False):

    def rule(state):
        if not state.has(level_name, player):
            return False
        if requires_pogo and not state.has("Pogo Stick", player):
            return False
        if requires_stunner and not state.has("Neural Stunner", player):
            return False
        if requires_pogo_or_stunner and not (
            state.has("Pogo Stick", player) or state.has("Neural Stunner", player)
        ):
            return False
        if keycard and not state.has(f"{level_name} - Keycard", player):
            return False
        if gems:
            has_all_gems = all(state.has(f"{level_name} - {gem}", player) for gem in gems)
            return has_all_gems or state.has(f"{level_name} Gemset", player)
        return True

    set_rule(world.get_location(location_name, player), rule)

def create_ck_rules(self):
    
    world = self.multiworld
    player = self.player
    ep = self.options.episode_select.value

    # Keen 4 Rules
    if ep in [0, 1]:
        set_location_rule(world, player, "Border Village Complete", "Border Village")
        set_location_rule(world, player, "Slug Village Complete", "Slug Village")
        set_location_rule(world, player, "The Perilous Pit Complete", "The Perilous Pit",
                          ["Red Gem", "Blue Gem"])
        set_location_rule(world, player, "The Perilous Pit - Red Gem", "The Perilous Pit")
        set_location_rule(world, player, "The Perilous Pit - Blue Gem", "The Perilous Pit")
        set_location_rule(world, player, "Cave of the Descendents Complete", "Cave of the Descendents",
                          ["Yellow Gem"], requires_pogo=True)
        set_location_rule(world, player, "Cave of the Descendents - Red Gem", "Cave of the Descendents")
        set_location_rule(world, player, "Cave of the Descendents - Yellow Gem", "Cave of the Descendents",
                          ["Red Gem"])
        set_location_rule(world, player, "Chasm of Chills Complete", "Chasm of Chills")
        set_location_rule(world, player, "Crystalus Complete", "Crystalus",
                          ["Blue Gem"])
        set_location_rule(world, player, "Crystalus - Green Gem", "Crystalus", requires_pogo=True)
        set_location_rule(world, player, "Crystalus - Yellow Gem", "Crystalus",
                          ["Green Gem"], requires_pogo=True)
        set_location_rule(world, player, "Crystalus - Red Gem", "Crystalus",
                          ["Yellow Gem"], requires_pogo=True)
        set_location_rule(world, player, "Crystalus - Blue Gem", "Crystalus",
                          ["Red Gem"], requires_pogo=True)
        set_location_rule(world, player, "Hilville Complete", "Hilville")
        set_location_rule(world, player, "Sand Yego Complete", "Sand Yego",
                          ["Green Gem"], requires_pogo=True)
        set_location_rule(world, player, "Sand Yego - Green Gem", "Sand Yego", requires_pogo=True)
        set_location_rule(world, player, "Miragia Complete", "Miragia", requires_pogo=True)
        set_location_rule(world, player, "Lifewater Oasis Complete", "Lifewater Oasis", ["Green Gem"])
        set_location_rule(world, player, "Lifewater Oasis - Green Gem", "Lifewater Oasis")
        set_location_rule(world, player, "Pyramid of the Moons Complete", "Pyramid of the Moons",
                          ["Yellow Gem"])
        set_location_rule(world, player, "Pyramid of the Moons - Yellow Gem", "Pyramid of the Moons")
        set_location_rule(world, player, "Pyramid of Shadows Complete", "Pyramid of Shadows",
                          ["Blue Gem"], requires_stunner=True)
        set_location_rule(world, player, "Pyramid of Shadows - Blue Gem", "Pyramid of Shadows",
                          requires_stunner=True)
        set_location_rule(world, player, "Pyramid of the Gnosticine Ancients Complete",
                          "Pyramid of the Gnosticine Ancients", ["Red Gem", "Green Gem"], requires_pogo=True)
        set_location_rule(world, player, "Pyramid of the Gnosticine Ancients - Red Gem",
                          "Pyramid of the Gnosticine Ancients")
        set_location_rule(world, player, "Pyramid of the Gnosticine Ancients - Green Gem",
                          "Pyramid of the Gnosticine Ancients", ["Red Gem"], requires_pogo=True)
        set_location_rule(world, player, "Isle of Tar Complete", "Isle of Tar",
                          ["Blue Gem"], requires_pogo=True)
        set_location_rule(world, player, "Isle of Tar - Red Gem", "Isle of Tar", requires_pogo=True)
        set_location_rule(world, player, "Isle of Tar - Yellow Gem", "Isle of Tar", ["Red Gem"])
        set_location_rule(world, player, "Isle of Tar - Blue Gem", "Isle of Tar", ["Yellow Gem"])
        set_location_rule(world, player, "Isle of Fire Complete", "Isle of Fire",
                          ["Yellow Gem", "Blue Gem"])
        set_location_rule(world, player, "Isle of Fire - Yellow Gem", "Isle of Fire")
        set_location_rule(world, player, "Isle of Fire - Blue Gem", "Isle of Fire", ["Yellow Gem"])
        set_location_rule(world, player, "Well of Wishes Complete", "Well of Wishes")

        #BWBM Complete
        set_rule(
            world.get_location("Bean-With-Bacon Megarocket Complete", player),
            lambda state:
                state.has("Bean-With-Bacon Megarocket", player) and
                state.can_reach("Border Village Complete", "Location", player) and
                state.can_reach("Slug Village Complete", "Location",  player) and
                state.can_reach("The Perilous Pit Complete", "Location",  player) and    
                state.can_reach("Cave of the Descendents Complete", "Location",  player) and 
                state.can_reach("Chasm of Chills Complete", "Location",  player) and
                state.can_reach("Crystalus Complete", "Location",  player) and
                state.can_reach("Hilville Complete", "Location",  player) and
                state.can_reach("Sand Yego Complete", "Location",  player) and
                state.can_reach("Miragia Complete", "Location",  player) and
                state.can_reach("Lifewater Oasis Complete", "Location",  player) and
                state.can_reach("Pyramid of the Moons Complete", "Location",  player) and
                state.can_reach("Pyramid of Shadows Complete", "Location",  player) and
                state.can_reach("Pyramid of the Gnosticine Ancients Complete", "Location",  player) and
                state.can_reach("Isle of Tar Complete", "Location",  player) and
                state.can_reach("Isle of Fire Complete", "Location",  player) and
                state.can_reach("Well of Wishes Complete", "Location",  player)
        )

    # Keen 5 Rules
    if ep in [0, 2]:
        set_location_rule(world, player, "Ion Ventilation System Complete", "Ion Ventilation System")
        set_location_rule(world, player, "Security Center Complete", "Security Center",
                          ["Blue Gem"], keycard=True)
        set_location_rule(world, player, "Security Center - Red Gem", "Security Center")
        set_location_rule(world, player, "Security Center - Blue Gem", "Security Center", ["Red Gem"], requires_pogo=True)
        set_location_rule(world, player, "Security Center - Keycard", "Security Center",
                          ["Blue Gem"])
        set_location_rule(world, player, "Defense Tunnel Vlook Complete", "Defense Tunnel Vlook",
                          ["Yellow Gem"], keycard=True)
        set_location_rule(world, player, "Defense Tunnel Vlook - Red Gem", "Defense Tunnel Vlook")
        set_location_rule(world, player, "Defense Tunnel Vlook - Yellow Gem", "Defense Tunnel Vlook",
                          ["Red Gem"])
        set_location_rule(world, player, "Defense Tunnel Vlook - Keycard", "Defense Tunnel Vlook")
        set_location_rule(world, player, "Defense Tunnel Burrh Complete", "Defense Tunnel Burrh",
                          ["Red Gem"], keycard=True)
        set_location_rule(world, player, "Defense Tunnel Burrh - Red Gem", "Defense Tunnel Burrh")
        set_location_rule(world, player, "Defense Tunnel Burrh - Yellow Gem", "Defense Tunnel Burrh")
        set_location_rule(world, player, "Defense Tunnel Burrh - Blue Gem", "Defense Tunnel Burrh",
                          ["Red Gem", "Yellow Gem"])
        set_location_rule(world, player, "Defense Tunnel Burrh - Green Gem", "Defense Tunnel Burrh",
                          ["Red Gem", "Blue Gem"])
        set_location_rule(world, player, "Defense Tunnel Burrh - Keycard", "Defense Tunnel Burrh",
                          ["Red Gem", "Green Gem"])
        set_location_rule(world, player, "Defense Tunnel Sorra Complete", "Defense Tunnel Sorra",
                          ["Yellow Gem"], keycard=True)
        set_location_rule(world, player, "Defense Tunnel Sorra - Yellow Gem", "Defense Tunnel Sorra",
                          requires_pogo=True)
        set_location_rule(world, player, "Defense Tunnel Sorra - Keycard", "Defense Tunnel Sorra")
        set_location_rule(world, player, "Defense Tunnel Teln Complete", "Defense Tunnel Teln",
                          ["Yellow Gem", "Blue Gem"], keycard=True)
        set_location_rule(world, player, "Defense Tunnel Teln - Red Gem", "Defense Tunnel Teln")
        set_location_rule(world, player, "Defense Tunnel Teln - Yellow Gem", "Defense Tunnel Teln",
                          ["Red Gem"])
        set_location_rule(world, player, "Defense Tunnel Teln - Blue Gem", "Defense Tunnel Teln",
                          ["Yellow Gem"])
        set_location_rule(world, player, "Defense Tunnel Teln - Green Gem", "Defense Tunnel Teln",
                          ["Yellow Gem"])
        set_location_rule(world, player, "Defense Tunnel Teln - Keycard", "Defense Tunnel Teln",
                          ["Yellow Gem", "Green Gem"])
        set_location_rule(world, player, "Energy Flow Systems Complete", "Energy Flow Systems",
                          ["Green Gem"], requires_pogo=True)
        set_location_rule(world, player, "Energy Flow Systems - Red Gem", "Energy Flow Systems")
        set_location_rule(world, player, "Energy Flow Systems - Yellow Gem", "Energy Flow Systems",
                          ["Red Gem"])
        set_location_rule(world, player, "Energy Flow Systems - Blue Gem", "Energy Flow Systems",
                          ["Yellow Gem"])
        set_location_rule(world, player, "Energy Flow Systems - Green Gem", "Energy Flow Systems",
                          ["Blue Gem"])
        set_location_rule(world, player, "Regulation Control Center Complete", "Regulation Control Center",
                          ["Red Gem", "Yellow Gem", "Blue Gem"], requires_pogo=True)
        set_location_rule(world, player, "Regulation Control Center - Red Gem", "Regulation Control Center",
                          requires_stunner=True)
        set_location_rule(world, player, "Regulation Control Center - Yellow Gem",
                          "Regulation Control Center", ["Red Gem"], requires_pogo_or_stunner=True)
        set_location_rule(world, player, "Regulation Control Center - Blue Gem",
                          "Regulation Control Center", ["Red Gem", "Yellow Gem"], requires_pogo_or_stunner=True)
        set_location_rule(world, player, "Neutrino Burst Injector Complete", "Neutrino Burst Injector",
                          ["Red Gem", "Blue Gem"], requires_pogo=True)
        set_location_rule(world, player, "Neutrino Burst Injector - Red Gem", "Neutrino Burst Injector")
        set_location_rule(world, player, "Neutrino Burst Injector - Blue Gem", "Neutrino Burst Injector",
                          requires_pogo=True)
        set_location_rule(world, player, "Brownian Motion Inducer Complete", "Brownian Motion Inducer",
                          ["Yellow Gem", "Blue Gem"], requires_pogo=True)
        set_location_rule(world, player, "Brownian Motion Inducer - Yellow Gem", "Brownian Motion Inducer",
                          requires_pogo=True)
        set_location_rule(world, player, "Brownian Motion Inducer - Blue Gem", "Brownian Motion Inducer",
                          requires_pogo=True)
        set_location_rule(world, player, "Gravitational Damping Hub Complete", "Gravitational Damping Hub",
                          ["Green Gem"], keycard=True, requires_pogo=True)
        set_location_rule(world, player, "Gravitational Damping Hub - Red Gem", "Gravitational Damping Hub",
                          ["Green Gem"], requires_pogo=True)
        set_location_rule(world, player, "Gravitational Damping Hub - Green Gem", "Gravitational Damping Hub",
                          requires_pogo=True)
        set_location_rule(world, player, "Gravitational Damping Hub - Keycard", "Gravitational Damping Hub",
                          requires_pogo=True)
        set_location_rule(world, player, "Quantum Explosion Dynamo Complete", "Quantum Explosion Dynamo",
                          ["Red Gem", "Yellow Gem", "Blue Gem", "Green Gem"], requires_pogo=True)
        set_location_rule(world, player, "Quantum Explosion Dynamo - Red Gem","Quantum Explosion Dynamo",
                          requires_pogo=True)
        set_location_rule(world, player, "Quantum Explosion Dynamo - Yellow Gem", "Quantum Explosion Dynamo",
                          requires_pogo=True)
        set_location_rule(world, player, "Quantum Explosion Dynamo - Blue Gem", "Quantum Explosion Dynamo",
                          requires_pogo=True)
        set_location_rule(world, player, "Quantum Explosion Dynamo - Green Gem", "Quantum Explosion Dynamo",
                          requires_pogo=True)

        # QED Rule
        set_rule(
            world.get_location("Quantum Explosion Dynamo Complete", player),
            lambda state:
                state.has("Quantum Explosion Dynamo", player) and
                (
                    (
                        state.has("Quantum Explosion Dynamo - Red Gem", player) and
                        state.has("Quantum Explosion Dynamo - Yellow Gem", player) and
                        state.has("Quantum Explosion Dynamo - Blue Gem", player) and
                        state.has("Quantum Explosion Dynamo - Green Gem", player)
                    ) or
                    state.has("Quantum Explosion Dynamo Gemset", player)
                ) and
                state.can_reach("Ion Ventilation System Complete", "Location", player) and
                state.can_reach("Security Center Complete", "Location", player) and
                state.can_reach("Defense Tunnel Vlook Complete", "Location", player) and
                state.can_reach("Defense Tunnel Burrh Complete", "Location", player) and
                state.can_reach("Defense Tunnel Sorra Complete", "Location", player) and
                state.can_reach("Defense Tunnel Teln Complete", "Location", player) and
                state.can_reach("Energy Flow Systems Complete", "Location", player) and
                state.can_reach("Regulation Control Center Complete", "Location", player) and
                state.can_reach("Neutrino Burst Injector Complete", "Location", player) and
                state.can_reach("Brownian Motion Inducer Complete", "Location", player) and
                state.can_reach("Gravitational Damping Hub Complete", "Location", player)
        )
        
    # Score-item access rules (kegs + flasks).
    # Minimal rule: player must be able to enter the level. Per-pickup
    # refinements (specific gems, pogo for unreachable areas) can be added
    # once the spatial layout of each keg/flask is mapped out.
    def _set_score_rules(locations_by_region, level_to_name):
        for region_dict in locations_by_region.values():
            for loc_name in region_dict:
                # Location names are "<Level Name> - Keg N" / "Flask N".
                # Derive level by matching against the level→name map.
                level_name = None
                for name in level_to_name.values():
                    prefix = f"{name} - "
                    if loc_name.startswith(prefix):
                        level_name = name
                        break
                if level_name is None:
                    continue
                set_rule(world.get_location(loc_name, player),
                         lambda state, ln=level_name: state.has(ln, player))

    if ep in [0, 1] and self.options.enable_flasksanity:
        _set_score_rules(ck4_flask_locations_by_region, ck4_level_id_to_name)

    if ep in [0, 2] and self.options.enable_kegsanity:
        _set_score_rules(ck5_keg_locations_by_region, ck5_level_id_to_name)

    # Victory condition
    if ep == 1:
        self.multiworld.completion_condition[player] = \
            lambda state: state.has("Keen 4 Complete", player)
    elif ep == 2:
        self.multiworld.completion_condition[player] = \
            lambda state: state.has("Keen 5 Complete", player)
    elif ep == 0:
        self.multiworld.completion_condition[player] = \
            lambda state: state.has("Keen 4 Complete", player) and \
                        state.has("Keen 5 Complete", player)