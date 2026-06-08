from . import KeenTestBase

LOC = "Pyramid of the Moons Complete"
LEVEL = "Pyramid of the Moons"


class TestPyramidOfTheMoonsExitGems(KeenTestBase):
    """Pyramid of the Moons has three exits: the Yellow Gem door, the secret
    exit (also Yellow), and an over-the-top route reached with pogo and no
    Yellow Gem. So "Pyramid of the Moons Complete" must be reachable with the
    level + (Yellow Gem OR Pogo Stick). Gemsets off so individual gems are in
    the pool."""

    options = {"episode_select": "ck4", "enable_gemsets": 0}

    def test_unreachable_with_level_only(self):
        self.collect_by_name([LEVEL])
        self.assertFalse(self.can_reach_location(LOC),
                         "POTM Complete should need a gem or pogo, not just the level")

    def test_reachable_with_yellow_gem(self):
        self.collect_by_name([LEVEL, f"{LEVEL} - Yellow Gem"])
        self.assertTrue(self.can_reach_location(LOC))

    def test_reachable_with_pogo_no_yellow(self):
        self.collect_by_name([LEVEL, "Pogo Stick"])
        self.assertTrue(self.can_reach_location(LOC),
                        "POTM over-the-top exit needs only pogo (no Yellow Gem)")


class TestPyramidOfTheMoonsExitGemset(KeenTestBase):
    """Same level, gemsets on: the Gemset item is the gem path."""

    options = {"episode_select": "ck4", "enable_gemsets": 1}

    def test_unreachable_with_level_only(self):
        self.collect_by_name([LEVEL])
        self.assertFalse(self.can_reach_location(LOC))

    def test_reachable_with_gemset(self):
        self.collect_by_name([LEVEL, f"{LEVEL} Gemset"])
        self.assertTrue(self.can_reach_location(LOC))

    def test_reachable_with_pogo_no_gemset(self):
        self.collect_by_name([LEVEL, "Pogo Stick"])
        self.assertTrue(self.can_reach_location(LOC),
                        "POTM over-the-top exit needs only pogo (no gems)")
