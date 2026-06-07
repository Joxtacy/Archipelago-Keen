from dataclasses import dataclass
from Options import PerGameCommonOptions, Choice, DeathLink, Range, Toggle

class EpisodeSelect(Choice):
    """
    Which episodes should be included in the seed.
    ck4 = Episode 4
    ck5 = Episode 5
    both = Episode 4 & Episode 5
    """
    display_name = "Episode Select"

    option_ck4 = 1
    option_ck5 = 2
    option_both = 0

    default = option_both

class EnableGemsets(Toggle):
    """
    Whether gemsets should be enabled in the seed.
    With this option on, you will receive all level gem items for a specific level at the same time.
    With this option off, you will receive each level gem individually.
    """
    display_name = "Enable Gemsets"

    default = 1

class EnableCK4SecretLevel(Toggle):
    """
    Whether the Keen 4 secret level, the Pyramid of the Forbidden, is included.
    With this option on, it becomes an unlockable level with its own location
    checks and unlock items. It is optional — not required for the Keen 4
    (BWB Megarocket) goal.

    It is harder to reach than the regular levels: its hidden entrance sits
    behind the Pyramid of the Moons. Only applies when Keen 4 is in the seed.
    Off by default.
    """
    display_name = "Enable Keen 4 Secret Level"

    default = 0

class EnableCK5SecretLevel(Toggle):
    """
    Whether the Keen 5 secret level, Korath III Base, is included.
    With this option on, it becomes an unlockable level with its own location
    check and unlock item. It is optional — not required for the Keen 5
    (QED) goal.

    It is harder to reach than the regular levels: it is only reached via the
    Impossible Pogo Trick (pogo + stunner) inside the Gravitational Damping
    Hub. Only applies when Keen 5 is in the seed. Off by default.
    """
    display_name = "Enable Keen 5 Secret Level"

    default = 0

class AdditionalStartingLevels(Range):
    """
    How many additional levels should be randomly unlocked at the start of the game.
    By default, Border Village and Slug Village in Keen 4 and Ion Ventilation System and
    Security Center in Keen 5 are always unlocked. Additionally, the gems and keycards
    needed to complete these levels are also unlocked from the start.
    """
    display_name = "Additional Starting Levels"

    range_start = 3
    range_end = 10
    
    default = 3

class EnableConesanity(Toggle):
    """
    Whether to enable conesanity (Keen 4 only).
    With this option on, every reachable Ice Cream Cone in Keen 4 (the
    5000-point pickup) becomes its own AP location check. Lower point
    tiers (100/200/500/1000/2000) are NOT included; the omnispeak-ap
    engine currently only emits checks for the 5000-pt class.
    """
    display_name = "Enable Conesanity"

    default = 0

class EnableSugarsanity(Toggle):
    """
    Whether to enable sugarsanity (Keen 5 only).
    With this option on, every reachable Bag O' Sugar in Keen 5 (the
    5000-point pickup) becomes its own AP location check. Lower point
    tiers (100/200/500/1000/2000) are NOT included; the omnispeak-ap
    engine currently only emits checks for the 5000-pt class.
    """
    display_name = "Enable Sugarsanity"

    default = 0

class EnableFlasksanity(Toggle):
    """
    Whether to enable flasksanity (Keen 4 only).
    With this option on, every accessible Lifewater Flask in Keen 4 becomes
    its own AP location check. Lifewater Flasks are the extra-life pickups
    (no points; every 100 collected grants an extra life). Flasks known to
    be unreachable in the original maps are excluded automatically.
    """
    display_name = "Enable Flasksanity"

    default = 0

class EnableKegsanity(Toggle):
    """
    Whether to enable kegsanity (Keen 5 only).
    With this option on, every Vitalin Keg in Keen 5 becomes its own AP
    location check. Vitalin Kegs are the extra-life pickups (no points;
    every 100 collected grants an extra life).
    """
    display_name = "Enable Kegsanity"

    default = 0

class RandomizePogo(Choice):
    """
    Whether the pogo stick should be randomized.
    startwith = Start the game with the ability to use the pogo stick. This is vanilla behavior.
    early = The pogo stick will be placed early in the seed.
    randomize = The pogo stick can appear anywhere in the seed.
    """
    display_name = "Randomize Pogo"

    option_startwith = 0
    option_early = 1
    option_randomize = 2

    default = option_early

class RandomizeStunner(Choice):
    """
    Whether the neural stunner should be randomized.
    startwith = Start the game with the ability to use the stunner. This is vanilla behavior.
    early = The stunner will be placed early in the seed.
    randomize = The stunner can appear anywhere in the seed.
    """
    display_name = "Randomize Stunner"

    option_startwith = 0
    option_early = 1
    option_randomize = 2

    default = option_startwith

class RandomizeWetsuit(Choice):
    """
    Whether the wetsuit should be randomized.
    startwith = Start the game with the ability to use the wetsuit.
    early = The wetsuit will be placed early in the seed.
    randomize = The wetsuit can appear anywhere in the seed.
    """
    display_name = "Randomize Wetsuit"

    option_startwith = 0
    option_early = 1
    option_randomize = 2

    default = option_randomize

@dataclass
class KeenOptions(PerGameCommonOptions):
    episode_select: EpisodeSelect
    enable_gemsets: EnableGemsets
    enable_ck4_secret_level: EnableCK4SecretLevel
    enable_ck5_secret_level: EnableCK5SecretLevel
    additional_starting_levels: AdditionalStartingLevels
    enable_conesanity: EnableConesanity
    enable_sugarsanity: EnableSugarsanity
    enable_flasksanity: EnableFlasksanity
    enable_kegsanity: EnableKegsanity
    randomize_pogo: RandomizePogo
    randomize_stunner: RandomizeStunner
    randomize_wetsuit: RandomizeWetsuit
    death_link: DeathLink