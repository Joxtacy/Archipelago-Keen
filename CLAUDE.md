# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository purpose

This is a **continuation fork** of [kodbyte/Archipelago-Keen](https://github.com/kodbyte/Archipelago-Keen) (archived), itself a fork of upstream Archipelago. The only code this fork *owns* is the Commander Keen world under `worlds/keen/`. Everything else (`BaseClasses.py`, `Generate.py`, `MultiServer.py`, `WebHost*`, `worlds/<other-games>/`, etc.) is upstream Archipelago code and should generally be left alone unless a change is genuinely required.

- Active branch: **`keen-ap`** (not `main`). PRs and releases target this branch.
- Game-side client (Omnispeak fork that speaks the AP protocol): https://github.com/Joxtacy/omnispeak-ap
- Default release artifact is `keen.apworld` — an importable AP world, not a full Archipelago build.

## Common commands

```bash
# Install / refresh Python deps (run once, and after pulls that touch requirements.txt)
python ModuleUpdate.py --yes --force --append "WebHostLib/requirements.txt"

# Generate default YAMLs (writes to Players/Templates/, including "Commander Keen.yaml")
python Launcher.py --update_settings

# Generate a multiworld from YAMLs in Players/
python Generate.py

# Host the generated multiworld locally
python MultiServer.py <path/to/generated.archipelago>   # add --log_network for protocol debugging

# Run the launcher (clients, tools, etc.)
python Launcher.py

# Tests — pytest is the runner; configured in pytest.ini
pytest                              # everything
pytest -n12                         # parallel via pytest-xdist
pytest worlds/keen                  # just the Keen world's tests (none exist yet — add to worlds/keen/test/)
pytest test/general                 # generic tests run against every registered world (includes Keen)
pytest -k test_fill                 # filter by name

# Lint / type-check
ruff check .                        # config in ruff.toml (line-length 120, py311 target)
mypy <path>                         # config in mypy.ini; typings/ holds stubs

# Build the apworld zip locally (mirrors the release workflow)
(cd worlds && zip -r ../keen.apworld keen \
   -x 'keen/__pycache__/*' 'keen/**/__pycache__/*' 'keen/*.pyc' 'keen/**/*.pyc')
```

Python support is **3.11 ≤ version < 3.14**. The release workflow pins 3.12.

## Releasing keen.apworld

Releases are cut by GitHub Actions, not locally. Trigger `.github/workflows/release-apworld.yml` via `workflow_dispatch` with a semver `version` input (e.g. `0.0.5`). The workflow:

1. Validates the version is semver and the tag does not already exist.
2. Generates a changelog scoped to `worlds/keen/` only (the rest of the repo is upstream and noise).
3. Builds `keen.apworld` from `worlds/keen/` and a `Commander.Keen.yaml` template (renamed from Archipelago's default `Commander Keen.yaml` for parity with kodbyte's old releases — keep the dotted filename).
4. Creates a `v<version>` tag and a GitHub Release containing both artifacts.

Do not push tags by hand — the workflow owns tag creation. Commits to `worlds/keen/**` between releases automatically become release notes.

## Keen world architecture (`worlds/keen/`)

The world entry point is `worlds/keen/__init__.py` → `KeenWorld(World)` with `game = "Commander Keen"`. Generation is split across:

- **`Options.py`** — `KeenOptions` dataclass (extends `PerGameCommonOptions`). Includes upstream `DeathLink`. The pivotal option is `episode_select` with values **`ck4=1`, `ck5=2`, `both=0`**. All region/item/rule logic branches on this value (`ep in [0, 1]` = Keen 4, `ep in [0, 2]` = Keen 5). `enable_gemsets` toggles between per-gem items and bundled "Gemset" items — this changes both the item pool and the access rules.
- **`Items.py`** — item lists segmented by episode and by gemset/no-gemset mode (`ck4_level_items`, `ck4_gem_items` vs `ck4_gemset_items`, `ck5_keycard_items`, etc.). `create_item(name, player)` is the canonical constructor — never instantiate `KeenItem` directly elsewhere.
- **`Locations.py`** — `location_table` mapping location names → IDs. `KeenWorld.location_name_to_id` points at it.
- **`Regions.py`** — `create_ck4_regions` and `create_ck5_regions`; both are called when `episode_select=both`.
- **`Rules.py`** — `create_ck_rules` plus the `set_location_rule(world, player, location, level, gems=..., requires_pogo=..., keycard=...)` helper. The helper encodes the standard pattern: a location is reachable iff the level item is owned, plus optional pogo / keycard / per-gem (or gemset) checks. New levels should reuse this helper rather than inlining rules.

### Generation flow in `KeenWorld`

`generate_early` → `create_regions` → `create_items` → `set_rules` → `fill_slot_data`.

- `generate_early` is responsible for **precollected items**: always-unlocked starter levels (Border Village + Slug Village for ck4; Ion Ventilation System + Security Center plus its gems/keycard or Security Center Gemset for ck5), `additional_starting_levels` random picks, and `startwith`/`early` handling for Pogo Stick, Neural Stunner, and Wetsuit. Items pushed into `starting_items` here are then *excluded* from the pool in `create_items` — keep these two methods in sync.
- `create_regions` also injects two locked progression events (`Keen 4 Complete` / `Keen 5 Complete`) attached to the BWB Megarocket / QED Complete locations. These are the goal flags.
- `create_items` fills the remainder of the location count with weighted filler (~67% Stunner Ammo, ~33% Extra Keen). If you add locations, the counts auto-balance; if you add non-filler items, subtract them from the filler space.
- `fill_slot_data` is what the in-game client reads on connect — currently `episode_select`, `enable_gemsets`, `death_link`. Anything the client needs to know about the slot must be added here (and read on the omnispeak-ap side).

### Adding a level / location / item

1. Add the level item and any gem/keycard items in `Items.py` (in the right episode list and the right gemset/non-gemset list).
2. Add locations to `Locations.py` with unique IDs (do not reuse IDs).
3. Wire the region in `Regions.py`.
4. Add a `set_location_rule(...)` call in `Rules.py`.
5. If it changes the goal or starter set, update `generate_early` and the event injection in `create_regions`.
6. Run `pytest test/general -k Keen` to confirm the generic per-world tests still pass (fill, reachability, etc.).

## Version control

A global instruction prefers `jj` (Jujutsu) over `git` whenever a `.jj/` directory exists. This repo has both `.git/` and `.jj/` — use `jj` for commits, log, diff, bookmarks, etc., and only fall back to `git` for things `jj` cannot do (e.g. `git push` via the colocated git remote is fine; tagging is handled by the release workflow).

## Style and lint

- `ruff.toml` enables a broad ruleset (B, C, E, F, W, I, N, Q, UP, RET, RSE, RUF, ISC, PLC, PLE, PLW, T20, PERF) with deliberate ignores (notably `B011` — `assert False` is intentional; `PLC0415` — local imports are fine in AP).
- Line length 120, 4-space indent, target Python 3.11.
- `mypy.ini` adds `typings/` to the mypy path. Some upstream modules are not fully typed — don't chase strict typing across the whole repo, only what you're touching.

## What not to touch unprompted

- Files outside `worlds/keen/` are upstream Archipelago. Patching them risks breaking sync with upstream and is rarely necessary for this fork.
- Do not edit the upstream README, `Generate.py`, `MultiServer.py`, or `BaseClasses.py` unless the task explicitly requires it.
- `keen.apworld` and `Commander.Keen.yaml` at the repo root are release artifacts produced by CI; they should not be committed.
