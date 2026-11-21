# Programming Language Battle Arena

A terminal-based RPG boss-battler built in Python using only the standard library and custom ANSI escape-code box menus. Instead of clicking normal attack buttons, you fight bosses by writing real syntax in **HTML**, **Python**, **C**, and **C++**.

## How It Works

1. **Pick a Boss Difficulty:** Choose from 6 tiers using the arrow-key terminal menu:
   - `Easy Level` — **Syntax Slime** (100 HP)
   - `Normal Level` — **NullPointer Knight** (160 HP, casts *Type Coercion Slam* every 3 turns)
   - `Hard Level` — **SegFault Golem** (220 HP)
   - `Expert Level` — **Deadlock Hydra** (280 HP)
   - `Master Level` — **Kernel Panic Dragon** (350 HP)
   - `Append Level` — **Infinite Loop Leviathan** (450 HP)
2. **Choose Your Language Fighter:** Play as **HTML**, **Python**, **C**, or **C++**, each with its own HP pool, base attack damage, and language-specific coding prompts.
3. **Write Code to Deal Damage:**
   - **Valid syntax:** Compiles cleanly, deals damage, builds a **Combo multiplier** (`+3` bonus damage per streak), and has a 25% chance to land a **Critical Hit** (`1.5x` damage).
   - **Syntax error:** Deals `0` damage, resets your combo, and leaves you open to a counter-attack.
   - **Battle commands:** Type `heal` to restore `+35 HP` (2 uses per battle) or `switch` to swap to another language mid-fight without losing your turn timer.

## Project Structure

- `main.py` — Entry point that launches the game loop.
- `game_mecanics.py` — Handles the intro prompt, player setup, boss difficulty selection, and replay flow.
- `boss_fight.py` — Combat engine, `Fighter` and `Boss` dataclasses, HP bars, syntax normalization/checking, and the coding challenge pools.
- `game_library.py` — Custom cross-platform terminal UI (`bubble.boxed_print`, `bubble.boxed_input`, `bubble.boxed_select`, `bubble.boxed_multiselect`) powered by ANSI escape codes, `textwrap`, `termios`/`tty` (Linux/macOS), and `msvcrt` (Windows).

## Running the Game

No external packages or `pip install` needed—just Python 3.10+:

```bash
git clone [https://github.com/GamerFuryAction/Programming-Language-Battle-Arena.git](https://github.com/GamerFuryAction/Programming-Language-Battle-Arena.git)
cd Programming-Language-Battle-Arena
python3 main.py