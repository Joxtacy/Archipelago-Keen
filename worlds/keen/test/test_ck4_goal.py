from . import KeenTestBase

VICTORY = "Keen 4 Victory"

# The 8 levels that contain a council member (the council_rescue goal). All
# non-secret. See Options.CK4Goal / COUNCIL_LEVEL_COMPLETE.
COUNCIL_LEVELS = [
    "The Perilous Pit",
    "Cave of the Descendents",
    "Crystalus",
    "Lifewater Oasis",
    "Pyramid of Shadows",
    "Pyramid of the Gnosticine Ancients",
    "Isle of Fire",
    "Well of Wishes",
]

# Regular Keen 4 levels with no council member — never required by the
# council_rescue goal (the Megarocket goal requires all of them).
NON_COUNCIL_LEVELS = [
    "Border Village",
    "Slug Village",
    "Chasm of Chills",
    "Hilville",
    "Sand Yego",
    "Miragia",
    "Pyramid of the Moons",
    "Isle of Tar",
    "Bean-With-Bacon Megarocket",
]


class TestCK4CouncilGoal(KeenTestBase):
    """ck4_goal=council_rescue: victory requires completing the 8
    council-member levels and nothing else (not the Megarocket, not the other
    regular levels)."""

    options = {"episode_select": "ck4", "ck4_goal": "council_rescue"}

    def test_victory_needs_a_council_level(self):
        # Drop one council level's unlock — victory must become unreachable.
        # (Each test method gets a fresh world via setUp, so one representative
        # level suffices; the per-level requirements are covered by the
        # tracker's logic unit tests.)
        self.collect_all_but(["Well of Wishes"])
        self.assertFalse(
            self.can_reach_location(VICTORY),
            "council goal should require Well of Wishes (a council level)",
        )

    def test_victory_does_not_need_megarocket_or_other_levels(self):
        # Everything except the Megarocket and the non-council regular levels.
        self.collect_all_but(NON_COUNCIL_LEVELS)
        self.assertTrue(
            self.can_reach_location(VICTORY),
            "council goal must not require the Megarocket or non-council levels",
        )


class TestCK4MegarocketGoal(KeenTestBase):
    """ck4_goal=megarocket (default): victory requires the Bean-With-Bacon
    Megarocket, which transitively needs all regular levels."""

    options = {"episode_select": "ck4", "ck4_goal": "megarocket"}

    def test_victory_needs_megarocket(self):
        self.collect_all_but(["Bean-With-Bacon Megarocket"])
        self.assertFalse(
            self.can_reach_location(VICTORY),
            "megarocket goal should require the Bean-With-Bacon Megarocket",
        )
