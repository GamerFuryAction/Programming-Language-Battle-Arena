import os
import sys
import game_library
import time

place_holder = "test"

class Game:
    def select_boss():
        bosses = ["Easy Level", "Normal Level", "Hard Level", "Expert Level", "Master Level", "Append Level"]
        #player_name = game_library.Player(name=player_name)

        game_library.bubble.boxed_print(f"""Welcome {game_library.player}!
        Please enjoy this game, its made with pure heart""")
        time.sleep(3)

        while boss_answer != "Easy Level" and boss_answer != "Normal Level" and boss_answer != "Hard Level" and boss_answer != "Expert Level" and boss_answer != "Master Level" and boss_answer != "Append Level":
            boss_answer = game_library.bubble.boxed_input(f"""Ok, so there are 6 dificulties of the game:
                    {bosses}

                    Please select the boss:""")
        return boss_answer

    def Start_Game():
        # first prompt/the start of the game
        answer = game_library.bubble.boxed_input("""Hello and welcome to the Programming Language Battle Arena!

        Here you will be challenging all the unbeatable champions, with the help from the legendary C++ and C to the new ones like Python and HTML.

        Will you be able to fight them all?
        Yes(Y) / No(n)""")
        while answer != "y" or answer != "Y" or answer != "n" or answer != "N":
            if answer == "Y" or answer == "y":
                # asking them for their name
                game_library.player = game_library.bubble.boxed_input("""Good! Then...    
                What is your name player?""")
                return game_library.player
            elif answer == "n" or answer == "N":
                game_library.bubble.boxed_print("""Ok then, see you soon traveler!""")
                sys.exit()

            else:
                answer = game_library.bubble.boxed_input("""I didn't understand it quite.
                Could you answer again?

                Yes(Y) / No(n)""")


    Start_Game()
    answer = select_boss()
    if answer == "Easy Level":
        print("Easy Level")
    elif answer == "Normal Level":
        print("Normal Level")
    elif answer == "Hard Level":
        print("Hard Level")
    elif answer == "Expert Level":
        print("Expert Level")
    elif answer == "Master Level":
        print("Master Level")
    elif answer == "Append Level":
        print("Append Level")