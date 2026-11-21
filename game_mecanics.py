import sys
import time
import game_library
import boss_fight


class Game:
    def __init__(self):
        self.start_game()
        while True:
            difficulty = self.select_boss()
            fight = boss_fight.Battle(game_library.player, difficulty)
            fight.start()

            again = game_library.bubble.boxed_multiselect(
                "Challenge another boss in the Arena?",
                ["Yes, fight again", "No, exit game"],
            )
            if again.startswith("No"):
                game_library.bubble.boxed_print("Thanks for playing Programming Language Battle Arena!")
                break

    def select_boss(self):
        bosses = [
            "Easy Level",
            "Normal Level",
            "Hard Level",
            "Expert Level",
            "Master Level",
            "Append Level",
        ]

        game_library.bubble.boxed_print(
            f"Welcome {game_library.player}!\n"
            f"Please enjoy this game, its made with pure heart"
        )
        time.sleep(2)

        return game_library.bubble.boxed_multiselect(
            "Select the boss difficulty (UP/DOWN arrows + ENTER):",
            bosses,
        )

    def start_game(self):
        answer = game_library.bubble.boxed_input(
            "Hello and welcome to the Programming Language Battle Arena!\n\n"
            "Here you will be challenging all the unbeatable champions, with the help from the legendary C++ and C to the new ones like Python and HTML.\n\n"
            "Will you be able to fight them all?\n"
            "Yes(Y) / No(n)"
        )

        while True:
            choice = answer.strip().lower()
            if choice == "y":
                game_library.player = game_library.bubble.boxed_input(
                    "Good! Then...\n"
                    "What is your name player?"
                ).strip()
                return game_library.player
            elif choice == "n":
                game_library.bubble.boxed_print("Ok then, see you soon traveler!")
                sys.exit()
            else:
                answer = game_library.bubble.boxed_input(
                    "I didn't understand it quite.\n"
                    "Could you answer again?\n\n"
                    "Yes(Y) / No(n)"
                )