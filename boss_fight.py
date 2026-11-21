import time
import random
import re
from dataclasses import dataclass, field
import game_library


@dataclass
class Fighter:
    name: str
    hp: int
    max_hp: int
    base_damage: int
    challenges: dict = field(default_factory=dict)


@dataclass
class Boss:
    name: str
    difficulty: str
    hp: int
    max_hp: int
    min_damage: int
    max_damage: int
    intro: str
    special_name: str = ""
    special_desc: str = ""


def normalize_code(code: str) -> str:
    """Normalizes spacing around operators/tags so minor whitespace differences still pass."""
    cleaned = code.strip()
    cleaned = re.sub(r"\s+", " ", cleaned)
    cleaned = re.sub(r"\s*([=+\-*/<>(){};:,])\s*", r"\1", cleaned)
    return cleaned


def render_hp_bar(current_hp: int, max_hp: int, bar_length: int = 20) -> str:
    current_hp = max(0, current_hp)
    filled = int((current_hp / max_hp) * bar_length)
    empty = bar_length - filled
    return f"[{'#' * filled}{'-' * empty}] {current_hp}/{max_hp} HP"


def get_fighters() -> dict[str, Fighter]:
    return {
        "HTML": Fighter(
            name="HTML",
            hp=100,
            max_hp=100,
            base_damage=25,
            challenges={
                "Easy Level": [
                    ("Create a top-level heading with the text: Arena", ["<h1>Arena</h1>"]),
                    ("Create a paragraph tag with the text: Attack", ["<p>Attack</p>"]),
                    ("Create a button that says: Strike", ["<button>Strike</button>"]),
                    ("Write a line break tag", ["<br>", "<br/>", "<br />"]),
                ],
                "Normal Level": [
                    ("Create a link to 'hit.html' with text 'Slash'", ['<a href="hit.html">Slash</a>', "<a href='hit.html'>Slash</a>"]),
                    ("Create an image tag with src='sword.png'", ['<img src="sword.png">', '<img src="sword.png" />', "<img src='sword.png'>"]),
                    ("Create an unordered list item with text: Shield", ["<li>Shield</li>"]),
                    ("Create a div with id='arena' (empty inside)", ['<div id="arena"></div>', "<div id='arena'></div>"]),
                    ("Create a bold tag around the word: Crit", ["<b>Crit</b>", "<strong>Crit</strong>"]),
                    ("Create a text input with placeholder='Code'", ['<input type="text" placeholder="Code">', '<input placeholder="Code" type="text">', '<input placeholder="Code">']),
                ],
                "Hard Level": [
                    ("Create a text input field with name='spell'", ['<input type="text" name="spell">', '<input name="spell" type="text">']),
                    ("Create a form with method='POST'", ['<form method="POST"></form>', "<form method='POST'></form>"]),
                ],
            },
        ),
        "Python": Fighter(
            name="Python",
            hp=110,
            max_hp=110,
            base_damage=30,
            challenges={
                "Easy Level": [
                    ("Print the word: Slash", ['print("Slash")', "print('Slash')"]),
                    ("Assign 50 to a variable named dmg", ["dmg = 50"]),
                    ("Get the length of a list named spells", ["len(spells)"]),
                    ("Check if hp is greater than 0", ["hp > 0"]),
                ],
                "Normal Level": [
                    ("List comprehension: squares of x for x in range(5)", ["[x**2 for x in range(5)]", "[x*x for x in range(5)]"]),
                    ("Define a function named crit with no parameters", ["def crit():"]),
                    ("Append 'Fireball' to a list named deck", ['deck.append("Fireball")', "deck.append('Fireball')"]),
                    ("Create a dictionary stats with key 'atk' set to 40", ['stats = {"atk": 40}', "stats = {'atk': 40}"]),
                    ("Convert string variable s to an integer", ["int(s)"]),
                    ("Check if 'boss' is in list enemies", ['"boss" in enemies', "'boss' in enemies"]),
                ],
                "Hard Level": [
                    ("Lambda function taking x and returning x * 2", ["lambda x: x * 2"]),
                    ("Slice the last 3 elements of list arr", ["arr[-3:]"]),
                ],
            },
        ),
        "C": Fighter(
            name="C",
            hp=120,
            max_hp=120,
            base_damage=35,
            challenges={
                "Easy Level": [
                    ("Declare an integer variable hp set to 100", ["int hp = 100;"]),
                    ("Print 'Hit' using printf (include semicolon)", ['printf("Hit");']),
                    ("Declare a pointer p to an int", ["int *p;", "int* p;"]),
                ],
                "Normal Level": [
                    ("Get the memory address of variable x", ["&x"]),
                    ("Allocate 4 bytes using malloc", ["malloc(4)", "malloc(sizeof(int))"]),
                    ("Dereference pointer ptr", ["*ptr"]),
                    ("Declare an int array arr of size 5", ["int arr[5];"]),
                    ("Print integer variable dmg with printf (no newline)", ['printf("%d", dmg);']),
                    ("Return 0 from main (include semicolon)", ["return 0;"]),
                ],
                "Hard Level": [
                    ("Define a struct named Node", ["struct Node {};", "struct Node { };"]),
                    ("Bitwise left-shift variable n by 1", ["n << 1", "n <<= 1;"]),
                ],
            },
        ),
        "C++": Fighter(
            name="C++",
            hp=130,
            max_hp=130,
            base_damage=40,
            challenges={
                "Easy Level": [
                    ("Print 'Strike' using std::cout (include semicolon)", ['std::cout << "Strike";']),
                    ("Declare a std::vector of int named hits", ["std::vector<int> hits;"]),
                    ("Increment variable combo by 1 using ++", ["combo++;", "++combo;"]),
                ],
                "Normal Level": [
                    ("Declare a reference ref to variable hp", ["int& ref = hp;", "int &ref = hp;"]),
                    ("Push 10 into vector v", ["v.push_back(10);"]),
                    ("Read an integer into x using std::cin", ["std::cin >> x;"]),
                    ("Declare a std::string named spell set to \"Fire\"", ['std::string spell = "Fire";']),
                    ("Get the size of vector v", ["v.size()"]),
                    ("Print endl to std::cout (include semicolon)", ["std::cout << std::endl;"]),
                ],
                "Hard Level": [
                    ("Declare a std::unique_ptr to an int named p", ["std::unique_ptr<int> p;"]),
                    ("Sort a std::vector named v using std::sort", ["std::sort(v.begin(), v.end());"]),
                ],
            },
        ),
    }


def get_bosses() -> dict[str, Boss]:
    return {
        "Easy Level": Boss(
            name="Syntax Slime (Scratch Trainee)",
            difficulty="Easy Level",
            hp=100,
            max_hp=100,
            min_damage=8,
            max_damage=15,
            intro="A wild Syntax Slime blocks the arena gate! Write clean code to shatter its brackets.",
        ),
        "Normal Level": Boss(
            name="NullPointer Knight (JavaScript Marauder)",
            difficulty="Normal Level",
            hp=160,
            max_hp=160,
            min_damage=14,
            max_damage=24,
            intro="undefined is not a function! Watch out for Type Coercion attacks every 3 turns.",
            special_name="Type Coercion Slam",
            special_desc="The Knight mutates your variable types, dealing +10 bonus damage and resetting your combo!",
        ),
        "Hard Level": Boss(
            name="SegFault Golem (Assembly Titan)",
            difficulty="Hard Level",
            hp=220,
            max_hp=220,
            min_damage=20,
            max_damage=32,
            intro="Raw registers and zero safety nets. One syntax slip and your memory gets wiped.",
            special_name="Core Dump",
            special_desc="Unaligned memory access deals massive shockwave damage!",
        ),
        "Expert Level": Boss(
            name="Deadlock Hydra (Rust Borrow-Checker)",
            difficulty="Expert Level",
            hp=280,
            max_hp=280,
            min_damage=25,
            max_damage=38,
            intro="Every reference is tracked. Prove your lifetimes are valid to land a hit!",
            special_name="Lifetime Violation",
            special_desc="Dangling reference detected—takes an extra bite out of your HP!",
        ),
        "Master Level": Boss(
            name="Kernel Panic Dragon (Malbolge Overlord)",
            difficulty="Master Level",
            hp=350,
            max_hp=350,
            min_damage=30,
            max_damage=45,
            intro="The final guardian of the Arena. Only flawless syntax will survive.",
            special_name="Blue Screen Breath",
            special_desc="System halt wave scorches your active fighter!",
        ),
        "Append Level": Boss(
            name="Infinite Loop Leviathan (Endgame Boss)",
            difficulty="Append Level",
            hp=450,
            max_hp=450,
            min_damage=35,
            max_damage=55,
            intro="O(n!) complexity incarnate. Break out of the loop before your stack overflows!",
            special_name="Stack Overflow",
            special_desc="Infinite recursion crushes your call stack!",
        ),
    }


class Battle:
    def __init__(self, player_name: str, difficulty):
        if isinstance(difficulty, list):
            difficulty = difficulty[0] if difficulty else "Easy Level"
        self.player_name = player_name
        self.difficulty = difficulty
        self.fighters = get_fighters()
        self.boss = get_bosses()[difficulty]
        self.heals_left = 2
        self.combo = 0
        self.turn = 0
        self.last_prompt = ""
        self.active_fighter = self.choose_fighter()

    def choose_fighter(self) -> Fighter:
        alive = [f for f in self.fighters.values() if f.hp > 0]
        labels = [f"{f.name} ({f.hp}/{f.max_hp} HP | ATK: {f.base_damage})" for f in alive]

        selected_label = game_library.bubble.boxed_select(
            "Choose your Programming Language Fighter (UP/DOWN arrows + ENTER):",
            labels,
        )
        chosen_name = selected_label.split(" ")[0]
        return self.fighters[chosen_name]

    def get_challenge(self, fighter: Fighter):
        pool = None
        for tier in [self.difficulty, "Hard Level", "Normal Level", "Easy Level"]:
            if tier in fighter.challenges:
                pool = fighter.challenges[tier]
                break
        if not pool:
            pool = fighter.challenges["Easy Level"]

        # Avoid repeating the exact same prompt back-to-back if multiple exist
        choices = [c for c in pool if c[0] != self.last_prompt] or pool
        chosen = random.choice(choices)
        self.last_prompt = chosen[0]
        return chosen

    def check_code(self, player_code: str, valid_answers: list[str]) -> bool:
        normalized_player = normalize_code(player_code)
        return any(normalized_player == normalize_code(ans) for ans in valid_answers)

    def start(self) -> bool:
        game_library.bubble.boxed_print(
            f"BOSS FIGHT: {self.boss.name}\n"
            f"Difficulty: {self.difficulty}\n\n"
            f"{self.boss.intro}"
        )
        time.sleep(2.5)

        while self.boss.hp > 0 and any(f.hp > 0 for f in self.fighters.values()):
            self.turn += 1

            if self.active_fighter.hp <= 0:
                game_library.bubble.boxed_print(
                    f"{self.active_fighter.name} suffered a Runtime Crash (0 HP)!\n"
                    f"Select another language fighter to stay in the fight!"
                )
                time.sleep(2)
                self.active_fighter = self.choose_fighter()

            prompt, valid_answers = self.get_challenge(self.active_fighter)

            # Warn player if the boss is charging its special attack (every 3rd turn on Normal+)
            special_warning = ""
            if self.boss.special_name and self.turn % 3 == 0:
                special_warning = f"\nWARNING: {self.boss.name} is charging {self.boss.special_name}!"

            arena_ui = (
                f"TURN {self.turn} | BOSS: {self.boss.name}\n"
                f"{render_hp_bar(self.boss.hp, self.boss.max_hp)}{special_warning}\n\n"
                f"FIGHTER: {self.active_fighter.name} (Player: {self.player_name})\n"
                f"{render_hp_bar(self.active_fighter.hp, self.active_fighter.max_hp)} | Heals: {self.heals_left} | Combo: {self.combo}x\n\n"
                f"[{self.active_fighter.name} CHALLENGE]\n"
                f"{prompt}\n\n"
                f"Commands: write code to attack | 'heal' (+35 HP) | 'switch' (change language)"
            )

            player_code = game_library.bubble.boxed_input(arena_ui, prompt_label="Code> ").strip()

            if player_code.lower() == "heal":
                if self.heals_left > 0:
                    self.heals_left -= 1
                    healed = min(35, self.active_fighter.max_hp - self.active_fighter.hp)
                    self.active_fighter.hp += healed
                    game_library.bubble.boxed_print(
                        f"garbage_collect() freed memory!\n"
                        f"{self.active_fighter.name} restored +{healed} HP!"
                    )
                else:
                    game_library.bubble.boxed_print("Out of memory heals! You lost your turn!")
                time.sleep(1.8)

            elif player_code.lower() == "switch":
                self.active_fighter = self.choose_fighter()
                self.turn -= 1  # Switching doesn't advance the boss special timer
                continue

            elif self.check_code(player_code, valid_answers):
                self.combo += 1
                crit = random.random() < 0.25
                combo_bonus = (self.combo - 1) * 3
                dmg = int((self.active_fighter.base_damage + combo_bonus) * (1.5 if crit else 1.0))
                self.boss.hp = max(0, self.boss.hp - dmg)

                header = "CRITICAL HIT! O(1) Execution!" if crit else "Compiled cleanly!"
                game_library.bubble.boxed_print(
                    f"{header}\n"
                    f"Combo: {self.combo}x (+{combo_bonus} bonus)\n"
                    f"{self.active_fighter.name} dealt {dmg} damage to {self.boss.name}!"
                )
                time.sleep(2)

                if self.boss.hp <= 0:
                    break

            else:
                self.combo = 0
                game_library.bubble.boxed_print(
                    f"SyntaxError! Compilation failed (Combo reset)!\n"
                    f"Valid example: {valid_answers[0]}\n\n"
                    f"0 damage dealt!"
                )
                time.sleep(2.5)

            # Boss counter-attack (Special attack triggers every 3 turns on Normal+ difficulties)
            boss_dmg = random.randint(self.boss.min_damage, self.boss.max_damage)
            if self.boss.special_name and self.turn % 3 == 0:
                boss_dmg += 10
                self.combo = 0
                self.active_fighter.hp = max(0, self.active_fighter.hp - boss_dmg)
                game_library.bubble.boxed_print(
                    f"SPECIAL ATTACK: {self.boss.special_name}!\n"
                    f"{self.boss.special_desc}\n\n"
                    f"{self.active_fighter.name} took {boss_dmg} damage!"
                )
            else:
                self.active_fighter.hp = max(0, self.active_fighter.hp - boss_dmg)
                game_library.bubble.boxed_print(
                    f"{self.boss.name} counter-attacks with an Unhandled Exception!\n"
                    f"{self.active_fighter.name} took {boss_dmg} damage!"
                )
            time.sleep(2.2)

        if self.boss.hp <= 0:
            game_library.bubble.boxed_print(
                f"VICTORY!\n\n"
                f"{self.player_name} and {self.active_fighter.name} defeated {self.boss.name}!"
            )
            time.sleep(2.5)
            return True

        game_library.bubble.boxed_print(
            f"GAME OVER — SEGMENTATION FAULT\n\n"
            f"All your programming languages crashed against {self.boss.name}."
        )
        time.sleep(2.5)
        return False