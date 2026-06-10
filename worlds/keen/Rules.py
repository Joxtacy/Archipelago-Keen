from worlds.generic.Rules import add_rule, set_rule

from .Locations import (
    ck4_flask_locations_by_region, ck5_keg_locations_by_region,
    ck4_points5k_locations_by_region, ck5_points5k_locations_by_region,
    ck4_level_id_to_name, ck5_level_id_to_name,
    ck4_level_id_to_name_with_potf,
)

# --------------------------------------------------
# Create location rules
# --------------------------------------------------

# rule builder helper
# Maps each token used in set_location_rule(requires=...) to its AP item
# name. Tokens may be combined with '|' for OR — e.g. requires=("pogo|stunner",)
# means "pogo or stunner".
_REQUIREMENT_ITEM = {
    "pogo": "Pogo Stick",
    "stunner": "Neural Stunner",
    "wetsuit": "Wetsuit",
}


def set_location_rule(world, player, location_name, level_name,
                      gems=None,
                      requires=(),
                      keycard=False,
                      gem_alt=()):
    # gem_alt: requirement tokens (same vocabulary / '|' OR syntax as `requires`)
    # that are an *alternative* to the gem requirement rather than an additional
    # AND. Use when a level has an exit that bypasses the gem door — e.g. the
    # Pyramid of the Moons over-the-top route reached with pogo and no Yellow Gem.

    def rule(state):
        if not state.has(level_name, player):
            return False
        for req in requires:
            options = req.split("|")
            if not any(state.has(_REQUIREMENT_ITEM[o], player) for o in options):
                return False
        if keycard and not state.has(f"{level_name} - Keycard", player):
            return False
        if gems:
            has_all_gems = all(state.has(f"{level_name} - {gem}", player) for gem in gems)
            satisfied = has_all_gems or state.has(f"{level_name} Gemset", player)
            for req in gem_alt:
                options = req.split("|")
                if any(state.has(_REQUIREMENT_ITEM[o], player) for o in options):
                    satisfied = True
                    break
            return satisfied
        return True

    set_rule(world.get_location(location_name, player), rule)


# Per-flask requirements beyond "have the level unlocked". Keyed by the
# location name as built by _build_extralife_locations (1-based engine index,
# skipping entries in ck4_lifewater_flask_excluded). Levels not listed here
# inherit the default rule (level item only); wetsuit-gated levels (IoT, IoF,
# WoW) are additionally gated by the K4 Lake region in Regions.py, so the
# Wetsuit does not need to be repeated as a per-flask requirement.
ck4_flask_rules = {
    "Border Village - Lifewater Flask 1": dict(requires=("pogo",)),
    "Border Village - Lifewater Flask 2": dict(requires=("pogo",)),
    "Border Village - Lifewater Flask 3": dict(requires=("pogo",)),
    "Border Village - Lifewater Flask 4": dict(requires=("pogo",)),
    "Border Village - Lifewater Flask 5": dict(requires=("pogo",)),
    "Border Village - Lifewater Flask 6": dict(requires=("pogo",)),
    "Border Village - Lifewater Flask 7": dict(requires=("pogo",)),
    "Hilville - Lifewater Flask 1": dict(requires=("pogo",)),
    "Sand Yego - Lifewater Flask 1": dict(requires=("pogo",)),
    "Miragia - Lifewater Flask 1": dict(requires=("pogo",)),
    "Pyramid of the Moons - Lifewater Flask 1": dict(requires=("pogo",)),
    "Pyramid of Shadows - Lifewater Flask 1": dict(requires=("stunner",)),
    "Pyramid of Shadows - Lifewater Flask 2": dict(requires=("stunner",)),
    "Pyramid of Shadows - Lifewater Flask 3": dict(requires=("stunner",)),
    "Pyramid of Shadows - Lifewater Flask 4": dict(requires=("stunner",)),
    "Pyramid of Shadows - Lifewater Flask 5": dict(requires=("stunner",)),
    "Pyramid of Shadows - Lifewater Flask 6": dict(requires=("stunner",)),
    "Pyramid of Shadows - Lifewater Flask 7": dict(requires=("stunner",)),
    "Pyramid of Shadows - Lifewater Flask 8": dict(requires=("stunner",)),
    "Pyramid of the Gnosticine Ancients - Lifewater Flask 2": dict(requires=("stunner",)),
    "Pyramid of the Gnosticine Ancients - Lifewater Flask 3": dict(requires=("stunner",)),
    "Pyramid of the Gnosticine Ancients - Lifewater Flask 4": dict(requires=("pogo",)),
    "Isle of Tar - Lifewater Flask 1": dict(requires=("pogo",)),
    "Isle of Tar - Lifewater Flask 2": dict(requires=("pogo",)),
}


# Per-keg requirements for CK5 Vitalin Kegs. Engine indices map to in-level
# positions (recovered via OMNISPEAK_DUMP_SCORE_ITEMS=1):
#   SC   Keg 1 (65,14) top-right; Keg 2 (4,33) far-left.
#   DTV  Keg 1 (51,2) middle; Keg 2 (187,3) far-right.
#   QED  Keg 1 (36,31) and Keg 2 (38,31) sit behind the same gate.
# Levels not listed fall through to the default (level item only).
# Per-pickup requirements beyond "have the level unlocked" for 5000-pt
# pointsanity locations. Levels not listed inherit the default rule (level
# item only). Populated from the audit in docs/pointsanity_ck4.md /
# pointsanity_ck5.md. wetsuit-gated levels in CK4 (IoT, IoF, WoW) are
# already region-gated by K4 Lake so the Wetsuit does not need to be
# repeated as a per-pickup requirement here.
#
# Per-pickup rules state ALL requirements (not deltas vs. the level rule),
# matching the convention used by ck4_flask_rules / ck5_keg_rules.
ck4_points5k_rules = {
    "Slug Village - Ice Cream Cone 1": dict(requires=("pogo",)),
    "The Perilous Pit - Ice Cream Cone 1": dict(requires=("pogo",)),
    "Cave of the Descendents - Ice Cream Cone 11": dict(requires=("pogo",)),
    "Chasm of Chills - Ice Cream Cone 3": dict(requires=("pogo",)),
    "Crystalus - Ice Cream Cone 1": dict(requires=("pogo",)),
    "Crystalus - Ice Cream Cone 2": dict(requires=("pogo",)),
    "Crystalus - Ice Cream Cone 3": dict(gems=["Blue Gem"]),
    "Hilville - Ice Cream Cone 1": dict(requires=("pogo",)),
    # Sand Yego Pickup 1 (engine idx 0, tile 32,45) floats up-left of the
    # row-50 platform; reachable via a pogo jump, same as the SY flask.
    "Sand Yego - Ice Cream Cone 1": dict(requires=("pogo",)),
    "Sand Yego - Ice Cream Cone 3": dict(requires=("pogo",)),
    "Miragia - Ice Cream Cone 1": dict(requires=("pogo",)),
    "Miragia - Ice Cream Cone 2": dict(requires=("pogo",)),
    "Pyramid of the Moons - Ice Cream Cone 1": dict(requires=("pogo",)),
    "Pyramid of the Moons - Ice Cream Cone 2": dict(requires=("pogo",)),
    "Pyramid of the Moons - Ice Cream Cone 3": dict(requires=("pogo",)),
    "Pyramid of the Moons - Ice Cream Cone 4": dict(requires=("pogo",)),
    "Pyramid of the Moons - Ice Cream Cone 5": dict(requires=("pogo",)),
    "Pyramid of the Moons - Ice Cream Cone 6": dict(requires=("pogo",)),
    "Pyramid of the Gnosticine Ancients - Ice Cream Cone 1": dict(requires=("pogo",)),
    "Isle of Tar - Ice Cream Cone 1": dict(requires=("pogo",)),
    "Isle of Fire - Ice Cream Cone 1": dict(requires=("pogo",)),
    "Isle of Fire - Ice Cream Cone 2": dict(requires=("pogo",)),
    "Isle of Fire - Ice Cream Cone 3": dict(requires=("pogo",)),
    "Isle of Fire - Ice Cream Cone 4": dict(requires=("pogo",)),
    "Isle of Fire - Ice Cream Cone 5": dict(requires=("pogo",)),
}
ck5_points5k_rules = {
    # Security Center: 28 Bags O' Sugar. Pickups 1–14 sit behind the Blue Gem
    # door; 15–20 need pogo to reach; 21–28 are accessible by default.
    "Security Center - Bag O' Sugar 1": dict(gems=["Blue Gem"]),
    "Security Center - Bag O' Sugar 2": dict(gems=["Blue Gem"]),
    "Security Center - Bag O' Sugar 3": dict(gems=["Blue Gem"]),
    "Security Center - Bag O' Sugar 4": dict(gems=["Blue Gem"]),
    "Security Center - Bag O' Sugar 5": dict(gems=["Blue Gem"]),
    "Security Center - Bag O' Sugar 6": dict(gems=["Blue Gem"]),
    "Security Center - Bag O' Sugar 7": dict(gems=["Blue Gem"]),
    "Security Center - Bag O' Sugar 8": dict(gems=["Blue Gem"]),
    "Security Center - Bag O' Sugar 9": dict(gems=["Blue Gem"]),
    "Security Center - Bag O' Sugar 10": dict(gems=["Blue Gem"]),
    "Security Center - Bag O' Sugar 11": dict(gems=["Blue Gem"]),
    "Security Center - Bag O' Sugar 12": dict(gems=["Blue Gem"]),
    "Security Center - Bag O' Sugar 13": dict(gems=["Blue Gem"]),
    "Security Center - Bag O' Sugar 14": dict(gems=["Blue Gem"]),
    "Security Center - Bag O' Sugar 15": dict(requires=("pogo",)),
    "Security Center - Bag O' Sugar 16": dict(requires=("pogo",)),
    "Security Center - Bag O' Sugar 17": dict(requires=("pogo",)),
    "Security Center - Bag O' Sugar 18": dict(requires=("pogo",)),
    "Security Center - Bag O' Sugar 19": dict(requires=("pogo",)),
    "Security Center - Bag O' Sugar 20": dict(requires=("pogo",)),
    # SC 21–28 default.

    # Defense Tunnel Vlook (7) — all accessible by default (entrance area).
    # Energy Flow Systems (10) — all default.
    # Defense Tunnel Sorra (13) — all default (entrance hall pickups).

    # Defense Tunnel Burrh: all 4 pickups behind a Red Gem door, need pogo.
    "Defense Tunnel Burrh - Bag O' Sugar 1": dict(requires=("pogo",), gems=["Red Gem"]),
    "Defense Tunnel Burrh - Bag O' Sugar 2": dict(requires=("pogo",), gems=["Red Gem"]),
    "Defense Tunnel Burrh - Bag O' Sugar 3": dict(requires=("pogo",), gems=["Red Gem"]),
    "Defense Tunnel Burrh - Bag O' Sugar 4": dict(requires=("pogo",), gems=["Red Gem"]),

    # Neutrino Burst Injector: 1–2 need pogo (ceiling pair); 3–4 default.
    "Neutrino Burst Injector - Bag O' Sugar 1": dict(requires=("pogo",)),
    "Neutrino Burst Injector - Bag O' Sugar 2": dict(requires=("pogo",)),

    # Defense Tunnel Teln: 1–6 behind Yellow + Blue Gem doors; 7–10 behind
    # Yellow Gem only.
    "Defense Tunnel Teln - Bag O' Sugar 1": dict(gems=["Yellow Gem", "Blue Gem"]),
    "Defense Tunnel Teln - Bag O' Sugar 2": dict(gems=["Yellow Gem", "Blue Gem"]),
    "Defense Tunnel Teln - Bag O' Sugar 3": dict(gems=["Yellow Gem", "Blue Gem"]),
    "Defense Tunnel Teln - Bag O' Sugar 4": dict(gems=["Yellow Gem", "Blue Gem"]),
    "Defense Tunnel Teln - Bag O' Sugar 5": dict(gems=["Yellow Gem", "Blue Gem"]),
    "Defense Tunnel Teln - Bag O' Sugar 6": dict(gems=["Yellow Gem", "Blue Gem"]),
    "Defense Tunnel Teln - Bag O' Sugar 7": dict(gems=["Yellow Gem"]),
    "Defense Tunnel Teln - Bag O' Sugar 8": dict(gems=["Yellow Gem"]),
    "Defense Tunnel Teln - Bag O' Sugar 9": dict(gems=["Yellow Gem"]),
    "Defense Tunnel Teln - Bag O' Sugar 10": dict(gems=["Yellow Gem"]),

    # Brownian Motion Inducer: all 8 bags reachable with level access only.

    # Gravitational Damping Hub: 1–6 behind Green Gem + need pogo; 7–13 need
    # pogo only; 14–15 default. (Whole level is also region-gated by End Game
    # completion of EFS+RCC+NBI+BMI — no need to repeat here.) Bags 7–10 sit in
    # the central area reachable from spawn with zero gems — verified by flood-
    # filling the static geometry from the Keen spawn (38,65); only 1–6 (top)
    # are gated by the Green Gem door (tile 30,63).
    "Gravitational Damping Hub - Bag O' Sugar 1": dict(requires=("pogo",), gems=["Green Gem"]),
    "Gravitational Damping Hub - Bag O' Sugar 2": dict(requires=("pogo",), gems=["Green Gem"]),
    "Gravitational Damping Hub - Bag O' Sugar 3": dict(requires=("pogo",), gems=["Green Gem"]),
    "Gravitational Damping Hub - Bag O' Sugar 4": dict(requires=("pogo",), gems=["Green Gem"]),
    "Gravitational Damping Hub - Bag O' Sugar 5": dict(requires=("pogo",), gems=["Green Gem"]),
    "Gravitational Damping Hub - Bag O' Sugar 6": dict(requires=("pogo",), gems=["Green Gem"]),
    "Gravitational Damping Hub - Bag O' Sugar 7": dict(requires=("pogo",)),
    "Gravitational Damping Hub - Bag O' Sugar 8": dict(requires=("pogo",)),
    "Gravitational Damping Hub - Bag O' Sugar 9": dict(requires=("pogo",)),
    "Gravitational Damping Hub - Bag O' Sugar 10": dict(requires=("pogo",)),
    "Gravitational Damping Hub - Bag O' Sugar 11": dict(requires=("pogo",)),
    "Gravitational Damping Hub - Bag O' Sugar 12": dict(requires=("pogo",)),
    "Gravitational Damping Hub - Bag O' Sugar 13": dict(requires=("pogo",)),

    # Quantum Explosion Dynamo: 1–6 deep behind all four gem doors + need
    # pogo; 7–9 need pogo only. (Region-gated by End Game same as GDH.)
    "Quantum Explosion Dynamo - Bag O' Sugar 1": dict(requires=("pogo",),
        gems=["Red Gem", "Yellow Gem", "Blue Gem", "Green Gem"]),
    "Quantum Explosion Dynamo - Bag O' Sugar 2": dict(requires=("pogo",),
        gems=["Red Gem", "Yellow Gem", "Blue Gem", "Green Gem"]),
    "Quantum Explosion Dynamo - Bag O' Sugar 3": dict(requires=("pogo",),
        gems=["Red Gem", "Yellow Gem", "Blue Gem", "Green Gem"]),
    "Quantum Explosion Dynamo - Bag O' Sugar 4": dict(requires=("pogo",),
        gems=["Red Gem", "Yellow Gem", "Blue Gem", "Green Gem"]),
    "Quantum Explosion Dynamo - Bag O' Sugar 5": dict(requires=("pogo",),
        gems=["Red Gem", "Yellow Gem", "Blue Gem", "Green Gem"]),
    "Quantum Explosion Dynamo - Bag O' Sugar 6": dict(requires=("pogo",),
        gems=["Red Gem", "Yellow Gem", "Blue Gem", "Green Gem"]),
    "Quantum Explosion Dynamo - Bag O' Sugar 7": dict(requires=("pogo",)),
    "Quantum Explosion Dynamo - Bag O' Sugar 8": dict(requires=("pogo",)),
    "Quantum Explosion Dynamo - Bag O' Sugar 9": dict(requires=("pogo",)),
}


ck5_keg_rules = {
    "Ion Ventilation System - Vitalin Keg 1": dict(requires=("pogo",)),
    "Ion Ventilation System - Vitalin Keg 2": dict(requires=("pogo",)),
    "Ion Ventilation System - Vitalin Keg 3": dict(requires=("pogo",)),
    "Ion Ventilation System - Vitalin Keg 4": dict(requires=("pogo",)),
    "Ion Ventilation System - Vitalin Keg 5": dict(requires=("pogo",)),
    "Ion Ventilation System - Vitalin Keg 6": dict(requires=("pogo",)),
    "Ion Ventilation System - Vitalin Keg 7": dict(requires=("pogo",)),
    "Ion Ventilation System - Vitalin Keg 8": dict(requires=("pogo",)),
    "Ion Ventilation System - Vitalin Keg 9": dict(requires=("pogo",)),
    "Ion Ventilation System - Vitalin Keg 10": dict(requires=("pogo",)),
    "Security Center - Vitalin Keg 1": dict(gems=["Blue Gem"]),
    "Security Center - Vitalin Keg 2": dict(requires=("pogo",)),
    "Defense Tunnel Vlook - Vitalin Keg 1": dict(gems=["Yellow Gem"], requires=("pogo",)),
    "Energy Flow Systems - Vitalin Keg 1": dict(gems=["Yellow Gem"]),
    "Defense Tunnel Burrh - Vitalin Keg 1": dict(requires=("pogo",)),
    "Defense Tunnel Burrh - Vitalin Keg 2": dict(requires=("pogo",)),
    "Defense Tunnel Teln - Vitalin Keg 1": dict(gems=["Red Gem"]),
    # Brownian Motion Inducer - Vitalin Keg 1: level access only (no pogo).
    "Gravitational Damping Hub - Vitalin Keg 1": dict(gems=["Green Gem"], requires=("pogo",)),
    "Quantum Explosion Dynamo - Vitalin Keg 1": dict(requires=("pogo", "stunner")),
    "Quantum Explosion Dynamo - Vitalin Keg 2": dict(requires=("pogo", "stunner")),
}

# Secret-level (POTF / Korath) score-item rules from the in-game playtest audit
# (docs/secret_{potf,korath}_worksheet.md). Only applied when the level is
# enabled (the locations are absent otherwise — see Regions / the `present`
# guard in _set_score_rules). "Red Gem"/"Blue Gem" need both same-colour items.

# POTF cones: 1-10 are deep behind red+yellow+blue doors; 11-14 behind red+yellow.
ck4_points5k_rules.update({
    f"Pyramid of the Forbidden - Ice Cream Cone {i}":
        dict(gems=["Red Gem 1", "Red Gem 2", "Yellow Gem", "Blue Gem"], requires=("pogo", "stunner"))
    for i in range(1, 11)
})
ck4_points5k_rules.update({
    f"Pyramid of the Forbidden - Ice Cream Cone {i}":
        dict(gems=["Red Gem 1", "Red Gem 2", "Yellow Gem"], requires=("pogo", "stunner"))
    for i in range(11, 15)
})
# POTF flasks: Flask 1 sits behind the same red+yellow+blue doors as cones 1-10
# (needs pogo + stunner + all four gems); Flask 2 needs stunner.
ck4_flask_rules["Pyramid of the Forbidden - Lifewater Flask 1"] = dict(
    gems=["Red Gem 1", "Red Gem 2", "Yellow Gem", "Blue Gem"], requires=("pogo", "stunner"))
ck4_flask_rules["Pyramid of the Forbidden - Lifewater Flask 2"] = dict(requires=("stunner",))

# Korath sugar: all reachable with pogo (no stunner / gems).
ck5_points5k_rules.update({
    f"Korath III Base - Bag O' Sugar {i + 1}": dict(requires=("pogo",))
    for i in range(20)
})
# Korath kegs: Keg 1 behind the green door, Keg 2 behind the yellow door.
ck5_keg_rules["Korath III Base - Vitalin Keg 1"] = dict(gems=["Green Gem"], requires=("pogo",))
ck5_keg_rules["Korath III Base - Vitalin Keg 2"] = dict(gems=["Yellow Gem"], requires=("pogo",))


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
                          ["Yellow Gem"], requires=("pogo",))
        set_location_rule(world, player, "Cave of the Descendents - Red Gem", "Cave of the Descendents")
        set_location_rule(world, player, "Cave of the Descendents - Yellow Gem", "Cave of the Descendents",
                          ["Red Gem"])
        set_location_rule(world, player, "Chasm of Chills Complete", "Chasm of Chills")
        set_location_rule(world, player, "Crystalus Complete", "Crystalus",
                          ["Blue Gem"])
        set_location_rule(world, player, "Crystalus - Green Gem", "Crystalus", requires=("pogo",))
        set_location_rule(world, player, "Crystalus - Yellow Gem", "Crystalus",
                          requires=("pogo",))
        set_location_rule(world, player, "Crystalus - Red Gem", "Crystalus",
                          ["Yellow Gem"], requires=("pogo",))
        set_location_rule(world, player, "Crystalus - Blue Gem", "Crystalus",
                          ["Red Gem"], requires=("pogo",))
        set_location_rule(world, player, "Hilville Complete", "Hilville")
        set_location_rule(world, player, "Sand Yego Complete", "Sand Yego",
                          ["Green Gem"], requires=("pogo",))
        # The Green Gem holder is reachable without pogo (playtest audit).
        set_location_rule(world, player, "Sand Yego - Green Gem", "Sand Yego")
        set_location_rule(world, player, "Miragia Complete", "Miragia", requires=("pogo",))
        set_location_rule(world, player, "Lifewater Oasis Complete", "Lifewater Oasis", ["Green Gem"])
        set_location_rule(world, player, "Lifewater Oasis - Green Gem", "Lifewater Oasis")
        # Three exits: the Yellow Gem door, the secret exit (also Yellow), and an
        # over-the-top route reached with pogo and no Yellow Gem (gem_alt=pogo).
        set_location_rule(world, player, "Pyramid of the Moons Complete", "Pyramid of the Moons",
                          ["Yellow Gem"], gem_alt=("pogo",))
        set_location_rule(world, player, "Pyramid of the Moons - Yellow Gem", "Pyramid of the Moons")
        set_location_rule(world, player, "Pyramid of Shadows Complete", "Pyramid of Shadows",
                          ["Blue Gem"], requires=("stunner",))
        set_location_rule(world, player, "Pyramid of Shadows - Blue Gem", "Pyramid of Shadows",
                          requires=("stunner",))
        set_location_rule(world, player, "Pyramid of the Gnosticine Ancients Complete",
                          "Pyramid of the Gnosticine Ancients", ["Green Gem"], requires=("pogo",))
        set_location_rule(world, player, "Pyramid of the Gnosticine Ancients - Red Gem",
                          "Pyramid of the Gnosticine Ancients")
        set_location_rule(world, player, "Pyramid of the Gnosticine Ancients - Green Gem",
                          "Pyramid of the Gnosticine Ancients", requires=("pogo",))
        # Pyramid of the Forbidden (secret level, opt-in). It has TWO red gem
        # holders, so completion needs both red items (Red Gem 1 + Red Gem 2);
        # the omnispeak-ap client grants a red count of 2 when both are held
        # (or via the gemset). The two physical red pickups share a single
        # "- Red Gem" check (gem pickups are keyed by colour engine-side).
        # Requirements are conservative (all gem doors + pogo) pending an
        # exact level-map / in-engine reachability audit; over-requiring is
        # logic-safe and POTF is optional (not part of the BWBM goal).
        # Per-pickup requirements from the in-game playtest audit (see
        # docs/secret_potf_worksheet.md). "Red Gem" needs both red items since
        # POTF has two red doors. Complete does not need the green door.
        if self.options.enable_ck4_secret_level:
            set_location_rule(world, player, "Pyramid of the Forbidden Complete",
                              "Pyramid of the Forbidden",
                              ["Red Gem 1", "Red Gem 2", "Yellow Gem", "Blue Gem"],
                              requires=("pogo", "stunner"))
            set_location_rule(world, player, "Pyramid of the Forbidden - Red Gem",
                              "Pyramid of the Forbidden", requires=("stunner",))
            set_location_rule(world, player, "Pyramid of the Forbidden - Yellow Gem",
                              "Pyramid of the Forbidden",
                              ["Red Gem 1", "Red Gem 2"], requires=("stunner",))
            set_location_rule(world, player, "Pyramid of the Forbidden - Blue Gem",
                              "Pyramid of the Forbidden",
                              ["Red Gem 1", "Red Gem 2", "Yellow Gem"], requires=("pogo", "stunner"))
            set_location_rule(world, player, "Pyramid of the Forbidden - Green Gem",
                              "Pyramid of the Forbidden",
                              ["Red Gem 1", "Red Gem 2", "Yellow Gem"], requires=("pogo", "stunner"))
        # The exit is reachable by pogoing across the top without the Blue Gem
        # door, so pogo alone (no gem) completes the level (playtest audit).
        set_location_rule(world, player, "Isle of Tar Complete", "Isle of Tar",
                          requires=("pogo",))
        set_location_rule(world, player, "Isle of Tar - Red Gem", "Isle of Tar", requires=("pogo",))
        set_location_rule(world, player, "Isle of Tar - Yellow Gem", "Isle of Tar", ["Red Gem"])
        # Pogo can reach the Blue Gem holder over the top, bypassing the Yellow
        # Gem door (gem_alt=pogo), same as the POTM over-the-top route.
        set_location_rule(world, player, "Isle of Tar - Blue Gem", "Isle of Tar",
                          ["Yellow Gem"], gem_alt=("pogo",))
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
        set_location_rule(world, player, "Security Center - Blue Gem", "Security Center", ["Red Gem"], requires=("pogo",))
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
                          requires=("pogo",))
        set_location_rule(world, player, "Defense Tunnel Sorra - Keycard", "Defense Tunnel Sorra",
                          requires=("stunner",))
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
                          ["Green Gem"], requires=("pogo",))
        set_location_rule(world, player, "Energy Flow Systems - Red Gem", "Energy Flow Systems")
        set_location_rule(world, player, "Energy Flow Systems - Yellow Gem", "Energy Flow Systems",
                          ["Red Gem"])
        set_location_rule(world, player, "Energy Flow Systems - Blue Gem", "Energy Flow Systems",
                          ["Yellow Gem"])
        set_location_rule(world, player, "Energy Flow Systems - Green Gem", "Energy Flow Systems",
                          ["Blue Gem"])
        set_location_rule(world, player, "Regulation Control Center Complete", "Regulation Control Center",
                          ["Red Gem", "Yellow Gem", "Blue Gem"], requires=("pogo",))
        set_location_rule(world, player, "Regulation Control Center - Red Gem", "Regulation Control Center",
                          requires=("stunner",))
        set_location_rule(world, player, "Regulation Control Center - Yellow Gem",
                          "Regulation Control Center", ["Red Gem"], requires=("pogo|stunner",))
        set_location_rule(world, player, "Regulation Control Center - Blue Gem",
                          "Regulation Control Center", ["Red Gem", "Yellow Gem"], requires=("pogo|stunner",))
        set_location_rule(world, player, "Neutrino Burst Injector Complete", "Neutrino Burst Injector",
                          ["Red Gem", "Blue Gem"], requires=("pogo",))
        set_location_rule(world, player, "Neutrino Burst Injector - Red Gem", "Neutrino Burst Injector")
        set_location_rule(world, player, "Neutrino Burst Injector - Blue Gem", "Neutrino Burst Injector",
                          requires=("pogo",))
        set_location_rule(world, player, "Brownian Motion Inducer Complete", "Brownian Motion Inducer",
                          ["Yellow Gem", "Blue Gem"], requires=("pogo",))
        set_location_rule(world, player, "Brownian Motion Inducer - Yellow Gem", "Brownian Motion Inducer",
                          requires=("pogo",))
        set_location_rule(world, player, "Brownian Motion Inducer - Blue Gem", "Brownian Motion Inducer",
                          requires=("pogo",))
        set_location_rule(world, player, "Gravitational Damping Hub Complete", "Gravitational Damping Hub",
                          ["Green Gem"], keycard=True, requires=("pogo",))
        set_location_rule(world, player, "Gravitational Damping Hub - Red Gem", "Gravitational Damping Hub",
                          ["Green Gem"], requires=("pogo",))
        set_location_rule(world, player, "Gravitational Damping Hub - Green Gem", "Gravitational Damping Hub",
                          requires=("pogo",))
        set_location_rule(world, player, "Gravitational Damping Hub - Keycard", "Gravitational Damping Hub",
                          requires=("pogo",))
        set_location_rule(world, player, "Quantum Explosion Dynamo Complete", "Quantum Explosion Dynamo",
                          ["Red Gem", "Yellow Gem", "Blue Gem", "Green Gem"], requires=("pogo",))
        set_location_rule(world, player, "Quantum Explosion Dynamo - Red Gem","Quantum Explosion Dynamo",
                          requires=("pogo",))
        set_location_rule(world, player, "Quantum Explosion Dynamo - Yellow Gem", "Quantum Explosion Dynamo",
                          requires=("pogo",))
        set_location_rule(world, player, "Quantum Explosion Dynamo - Blue Gem", "Quantum Explosion Dynamo",
                          requires=("pogo",))
        set_location_rule(world, player, "Quantum Explosion Dynamo - Green Gem", "Quantum Explosion Dynamo",
                          requires=("pogo",))
        # Korath III Base (secret level, opt-in). Reached via the hidden
        # teleporter inside the Gravitational Damping Hub; it lives in the End
        # Game region (inherits the EFS/RCC/NBI/BMI gating) and is optional
        # (not part of the QED goal). It has two blue gem holders, so completion
        # needs both blue items (Blue Gem 1 + Blue Gem 2; the client grants a
        # blue count of 2) plus the yellow/green gems and the keycard — the
        # intended path (the no-gem fuse skip is the Impossible Pogo Trick).
        # Every Korath check requires pogo+stunner: reaching the level at all
        # needs the trick, so this is the safe over-approximation for fill.
        # Per-pickup requirements from the in-game playtest audit (see
        # docs/secret_korath_worksheet.md). Reaching the level needs pogo (not
        # stunner); the secret fuse-skip is the only thing needing stunner+pogo
        # together. "Blue Gem" (for the keycard) needs both blue items (two blue
        # doors). Complete needs the green door + pogo and the keycard (the exit
        # is gated behind the keycard door, same as Security Center / DTV).
        if self.options.enable_ck5_secret_level:
            set_location_rule(world, player, "Korath III Base Complete", "Korath III Base",
                              ["Green Gem"], requires=("pogo",), keycard=True)
            set_location_rule(world, player, "Korath III Base - Yellow Gem", "Korath III Base",
                              requires=("pogo",))
            set_location_rule(world, player, "Korath III Base - Blue Gem", "Korath III Base",
                              requires=("pogo", "stunner"))
            set_location_rule(world, player, "Korath III Base - Green Gem", "Korath III Base",
                              ["Yellow Gem"], requires=("pogo", "stunner"))
            set_location_rule(world, player, "Korath III Base - Keycard", "Korath III Base",
                              ["Blue Gem 1", "Blue Gem 2"], requires=("pogo", "stunner"))

    # Score-item access rules (kegs + flasks).
    # Default rule: player must be able to enter the level. Per-pickup
    # refinements live in ck4_flask_rules / ck5_keg_rules below and are
    # merged in by location name.
    def _set_score_rules(locations_by_region, level_to_name, overrides=None):
        overrides = overrides or {}
        # Some score locations in these dicts may not be attached this seed
        # (e.g. Korath III Base's keg/sugar when the CK5 secret level is off but
        # kegsanity/sugarsanity is on). Only rule locations that actually exist.
        present = {loc.name for loc in world.get_locations(player)}
        for region_dict in locations_by_region.values():
            for loc_name in region_dict:
                if loc_name not in present:
                    continue
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
                extra = overrides.get(loc_name, {})
                set_location_rule(world, player, loc_name, level_name, **extra)

    if ep in [0, 1] and self.options.enable_flasksanity:
        _set_score_rules(ck4_flask_locations_by_region, ck4_level_id_to_name,
                         ck4_flask_rules)

    if ep in [0, 2] and self.options.enable_kegsanity:
        _set_score_rules(ck5_keg_locations_by_region, ck5_level_id_to_name,
                         ck5_keg_rules)

    # Conesanity = CK4 Ice Cream Cones; sugarsanity = CK5 Bag O' Sugar.
    # Both are 5000-pt pickups (engine class 5). The _with_potf map is used so
    # POTF's cone pickups resolve a level name; it is currently equivalent to
    # ck4_level_id_to_name, which already includes POTF.
    if ep in [0, 1] and self.options.enable_conesanity:
        _set_score_rules(ck4_points5k_locations_by_region,
                         ck4_level_id_to_name_with_potf,
                         ck4_points5k_rules)

    if ep in [0, 2] and self.options.enable_sugarsanity:
        _set_score_rules(ck5_points5k_locations_by_region,
                         ck5_level_id_to_name,
                         ck5_points5k_rules)

    # Secret-level entry gates (cross-level prerequisites). A secret level is
    # only physically reachable by traversing another level, which set_location_rule's
    # single-level gems= mechanism can't express — so AND the gate onto every
    # location of each secret level (gems, Complete, cones/flasks/sugar/kegs)
    # after the per-pickup rules are set.
    #   POTF: reached only by gathering the inchworms in the Pyramid of the
    #         Moons, behind its Yellow Gem door (== being able to complete POM).
    #   Korath: reached only via the hidden teleporter deep in the Gravitational
    #         Damping Hub, past GDH's green + red doors (same as the GDH Vitalin
    #         Keg's green-gem+pogo requirement, plus the red gem for the
    #         teleporter door).
    def _has_gem(state, level, gem):
        return (state.has(f"{level} - {gem}", player)
                or state.has(f"{level} Gemset", player))

    if ep in [0, 1] and self.options.enable_ck4_secret_level:
        def potf_gate(state):
            return (state.has("Pyramid of the Moons", player)
                    and _has_gem(state, "Pyramid of the Moons", "Yellow Gem"))
        for loc in world.get_locations(player):
            if loc.name.startswith("Pyramid of the Forbidden"):
                add_rule(loc, potf_gate)

    if ep in [0, 2] and self.options.enable_ck5_secret_level:
        def korath_gate(state):
            return (state.has("Gravitational Damping Hub", player)
                    and _has_gem(state, "Gravitational Damping Hub", "Green Gem")
                    and _has_gem(state, "Gravitational Damping Hub", "Red Gem")
                    and state.has("Pogo Stick", player))
        for loc in world.get_locations(player):
            if loc.name.startswith("Korath III Base"):
                add_rule(loc, korath_gate)

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