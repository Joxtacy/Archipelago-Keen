# Secret Level Worksheet — Pyramid of the Forbidden (Keen 4)

Rendered map (gems/cones/flasks stamped): `images/Ck4lv14.png` in the tracker.

Fill the **Requires** column from in-game testing, then I translate to
`Rules.py`. Tokens (combine with `;`): `default` (level item only),
`pogo`, `stunner`, `pogo|stunner`, `gems:Red,Yellow`, `exclude`.

**Gem doors in this level:** Red @ [(42, 27), (25, 70)], Yellow @ [(23, 40)], Blue @ [(32, 72)], Green @ [(7, 73)]
(POTF is the only level with two Red doors — both reds open both.)

## Gems  (current rule: level + pogo)
Red gem pickups (one shared "Red Gem" check): [(45, 24), (3, 70)]
- Red Gem — pogo
- Yellow Gem ([(27, 36)]) — pogo
- Blue Gem ([(46, 83)]) — pogo
- Green Gem ([(4, 77)]) — pogo

## Complete  (current rule: all gems + pogo)
Exit: see map (CK4 exits aren't encoded as a scannable marker).

## Ice Cream Cones (14)  (current rule: default / level only)

| #   | Tile (X, Y) | Source | Requires |
| --- | ----------- | ------ | -------- |
| 1   | ( 71,  28) | dump   | default |
| 2   | ( 70,  29) | dump   | default |
| 3   | ( 72,  29) | dump   | default |
| 4   | ( 69,  30) | dump   | default |
| 5   | ( 71,  30) | dump   | default |
| 6   | ( 73,  30) | dump   | default |
| 7   | ( 68,  31) | dump   | default |
| 8   | ( 70,  31) | dump   | default |
| 9   | ( 72,  31) | dump   | default |
| 10  | ( 74,  31) | dump   | default |
| 11  | (  5,  47) | dump   | default |
| 12  | (  6,  47) | dump   | default |
| 13  | (  7,  47) | dump   | default |
| 14  | (  8,  47) | dump   | default |

## Lifewater Flasks (2)  (current rule: default / level only)

| #   | Tile (X, Y) | Source | Requires |
| --- | ----------- | ------ | -------- |
| 1   | ( 58,  21) | dump   | default |
| 2   | ( 43,  15) | dump   | default |
