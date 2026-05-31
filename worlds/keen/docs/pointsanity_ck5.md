# CK5 Pointsanity Worksheet — Bag O' Sugar

CK5's 5000-pt pickup is the **Bag O' Sugar**. Locations are named
`"<Level Name> - Bag O' Sugar <N>"` in the apworld.

Fill in the `Requires` column for each pickup, then I'll translate to `ck5_points5k_rules` entries in `Rules.py`.

**Allowed tokens** (combine with `,`):
- `default` — level item only (no extras beyond the level's own rule).
- `pogo`, `stunner` — that ability is required.
- `pogo|stunner` — either of those abilities (OR).
- `gems:Red,Yellow` — one or more gems required (matches `Gemset` too via the existing helper).
- `keycard` — the level's keycard is required.
- `exclude` — pickup is unreachable in normal play (will be added to `ck5_points5k_excluded`).

**End Game region note**: Gravitational Damping Hub and Quantum Explosion Dynamo are already region-gated by completing EFS, RCC, NBI, and BMI (all gems). You do not need to repeat those upstream requirements per pickup.

**Source**: `info` = object spawned from the info layer (animated sprite); `tile` = static foreground tile. Behaviour-identical for AP.

---

## Security Center (28 pickups)

- **Level rule** (for the *Complete* check): `gems: Blue; keycard`.
- **Existing keg rules in this level**: Keg 1: gems:Blue.

| #  | Tile (X, Y) | Source | Requires |
|----|-------------|--------|----------|
|  1 | ( 44,   4) | info   |          |
|  2 | ( 45,   4) | info   |          |
|  3 | ( 68,   4) | info   |          |
|  4 | ( 69,   4) | info   |          |
|  5 | ( 44,   5) | info   |          |
|  6 | ( 45,   5) | info   |          |
|  7 | ( 68,   5) | info   |          |
|  8 | ( 69,   5) | info   |          |
|  9 | ( 63,  14) | info   |          |
| 10 | ( 64,  14) | info   |          |
| 11 | ( 62,  15) | info   |          |
| 12 | ( 63,  15) | info   |          |
| 13 | ( 64,  15) | info   |          |
| 14 | ( 65,  15) | info   |          |
| 15 | (  6,  33) | info   |          |
| 16 | (  7,  33) | info   |          |
| 17 | (  8,  33) | info   |          |
| 18 | (  6,  34) | info   |          |
| 19 | (  7,  34) | info   |          |
| 20 | (  8,  34) | info   |          |
| 21 | ( 27,  57) | info   |          |
| 22 | ( 28,  57) | info   |          |
| 23 | ( 27,  58) | info   |          |
| 24 | ( 28,  58) | info   |          |
| 25 | ( 55,  65) | info   |          |
| 26 | ( 56,  65) | info   |          |
| 27 | ( 55,  66) | info   |          |
| 28 | ( 56,  66) | info   |          |

## Defense Tunnel Vlook (7 pickups)

- **Level rule** (for the *Complete* check): `gems: Yellow; keycard`.
- **Existing keg rules in this level**: Keg 1: pogo + gems:Yellow.

| #  | Tile (X, Y) | Source | Requires |
|----|-------------|--------|----------|
|  1 | (181,   3) | info   |          |
|  2 | (182,   3) | info   |          |
|  3 | (186,   3) | info   |          |
|  4 | (181,   4) | info   |          |
|  5 | (182,   4) | info   |          |
|  6 | (186,   4) | info   |          |
|  7 | (187,   4) | info   |          |

## Energy Flow Systems (10 pickups)

- **Level rule** (for the *Complete* check): `pogo; gems: Green`.
- **Existing keg rules in this level**: Keg 1: gems:Yellow.

| #  | Tile (X, Y) | Source | Requires |
|----|-------------|--------|----------|
|  1 | ( 36,  55) | info   |          |
|  2 | ( 37,  55) | info   |          |
|  3 | ( 36,  56) | info   |          |
|  4 | ( 37,  56) | info   |          |
|  5 | ( 30,  16) | tile   |          |
|  6 | ( 30,  17) | tile   |          |
|  7 | ( 17,  51) | tile   |          |
|  8 | ( 18,  51) | tile   |          |
|  9 | ( 19,  51) | tile   |          |
| 10 | ( 20,  51) | tile   |          |

## Defense Tunnel Burrh (4 pickups)

- **Level rule** (for the *Complete* check): `gems: Red; keycard`.
- **Existing keg rules in this level**: Kegs 1-2: pogo.

| #  | Tile (X, Y) | Source | Requires |
|----|-------------|--------|----------|
|  1 | (106,   3) | tile   |          |
|  2 | (107,   3) | tile   |          |
|  3 | (106,   4) | tile   |          |
|  4 | (107,   4) | tile   |          |

## Defense Tunnel Sorra (13 pickups)

- **Level rule** (for the *Complete* check): `gems: Yellow; keycard (gem needs pogo, keycard needs stunner)`.

| #  | Tile (X, Y) | Source | Requires |
|----|-------------|--------|----------|
|  1 | ( 77,   5) | info   |          |
|  2 | ( 77,   6) | info   |          |
|  3 | ( 77,   7) | info   |          |
|  4 | ( 67,  15) | info   |          |
|  5 | ( 68,  15) | info   |          |
|  6 | ( 69,  15) | info   |          |
|  7 | ( 70,  15) | info   |          |
|  8 | ( 71,  15) | info   |          |
|  9 | ( 67,  16) | info   |          |
| 10 | ( 68,  16) | info   |          |
| 11 | ( 69,  16) | info   |          |
| 12 | ( 70,  16) | info   |          |
| 13 | ( 71,  16) | info   |          |

## Neutrino Burst Injector (4 pickups)

- **Level rule** (for the *Complete* check): `pogo; gems: Red, Blue`.

| #  | Tile (X, Y) | Source | Requires |
|----|-------------|--------|----------|
|  1 | ( 63,   3) | info   |          |
|  2 | ( 64,   3) | info   |          |
|  3 | ( 37,  43) | tile   |          |
|  4 | ( 38,  43) | tile   |          |

## Defense Tunnel Teln (10 pickups)

- **Level rule** (for the *Complete* check): `gems: Yellow, Blue; keycard`.
- **Existing keg rules in this level**: Keg 1: gems:Red.

| #  | Tile (X, Y) | Source | Requires |
|----|-------------|--------|----------|
|  1 | ( 17,   2) | info   |          |
|  2 | ( 17,   3) | info   |          |
|  3 | ( 48,  13) | info   |          |
|  4 | ( 48,  14) | info   |          |
|  5 | ( 48,  15) | info   |          |
|  6 | ( 48,  16) | info   |          |
|  7 | (103,  16) | info   |          |
|  8 | (104,  16) | info   |          |
|  9 | (103,  17) | info   |          |
| 10 | (104,  17) | info   |          |

## Brownian Motion Inducer (8 pickups)

- **Level rule** (for the *Complete* check): `pogo; gems: Yellow, Blue`.
- **Existing keg rules in this level**: Keg 1: pogo.

| #  | Tile (X, Y) | Source | Requires |
|----|-------------|--------|----------|
|  1 | ( 63,  29) | info   |          |
|  2 | ( 64,  29) | info   |          |
|  3 | ( 63,  30) | info   |          |
|  4 | ( 64,  30) | info   |          |
|  5 | ( 64,  17) | tile   |          |
|  6 | ( 65,  17) | tile   |          |
|  7 | ( 64,  18) | tile   |          |
|  8 | ( 65,  18) | tile   |          |

## Gravitational Damping Hub (15 pickups)

- **Level rule** (for the *Complete* check): `pogo; gems: Green; keycard (region: End Game — many gates upstream)`.
- **Existing keg rules in this level**: Keg 1: pogo + gems:Green.

| #  | Tile (X, Y) | Source | Requires |
|----|-------------|--------|----------|
|  1 | ( 31,   3) | info   |          |
|  2 | ( 32,   3) | info   |          |
|  3 | ( 33,   3) | info   |          |
|  4 | ( 31,   4) | info   |          |
|  5 | ( 32,   4) | info   |          |
|  6 | ( 33,   4) | info   |          |
|  7 | ( 25,  23) | info   |          |
|  8 | ( 26,  23) | info   |          |
|  9 | ( 25,  24) | info   |          |
| 10 | ( 26,  24) | info   |          |
| 11 | ( 33,  55) | info   |          |
| 12 | ( 35,  55) | info   |          |
| 13 | ( 34,  55) | tile   |          |
| 14 | ( 63,  63) | tile   |          |
| 15 | ( 63,  64) | tile   |          |

## Quantum Explosion Dynamo (9 pickups)

- **Level rule** (for the *Complete* check): `pogo; gems: Red, Yellow, Blue, Green (region: End Game)`.
- **Existing keg rules in this level**: Kegs 1-2: pogo + stunner.

| #  | Tile (X, Y) | Source | Requires |
|----|-------------|--------|----------|
|  1 | ( 74,  14) | tile   |          |
|  2 | ( 75,  14) | tile   |          |
|  3 | ( 74,  15) | tile   |          |
|  4 | ( 75,  15) | tile   |          |
|  5 | ( 74,  16) | tile   |          |
|  6 | ( 75,  16) | tile   |          |
|  7 | ( 26,  63) | tile   |          |
|  8 | ( 27,  63) | tile   |          |
|  9 | ( 28,  63) | tile   |          |

