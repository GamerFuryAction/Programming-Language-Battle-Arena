import os
import sys
import game_library

place_holder = "test"

def Start_Game():
    #first prompt/the start of the game
    answer = game_library.bubble.boxed_input("""Hello and welcome to the Programming Language Battle Arena!

    Here you will be challenging all the unbeatable champions, from the legendary C++ and C to the new ones like Python and HTML.

    Will you be able to fight them all?
    Yes(Y) / No(n)""")
    while(answer != "y" or answer != "Y" or answer != "n" or answer != "N"):
        if answer == "Y" or answer == "y":
            #asking them for their name
            player_name = game_library.bubble.boxed_input("""Good! Then...    
            What is your name player?""")


            game_library.Player(name=player_name) 
            Game.start()


        elif answer == "n" or answer == "N":
            game_library.bubble.boxed_print("""Ok then, see you soon traveler!""")
            return 0


        else:
            answer = game_library.bubble.boxed_input("""I didn't understand it quite.
            Could you answer again?

            Yes(Y) / No(n)""")

class Game:
    def start():
        bosses = ["Beginer level", "Hard level", "Expert level", "Master level", "Append level"]
        #player_name = game_library.Player(name=player_name)

        game_library.bubble.boxed_print(f"""Welcome {place_holder}!
        Please enjoy this game, its mafe with pure heart""")

        os.system('pause')
