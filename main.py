#Programming Language Battle Arena
import os
import sys
import game

player = "place_holder"
enemy = ["Python", "C++", "C#", "C", "Java", "Javascript", "HTML", "GO", "CSS"]

print("|---------------------------------------------------|")
print()

print('''    Hello and welcome to the Programing Language Battle Arena!
    Here you will be challenging all the unbeatable champions, from the legendary C++ and C to the new ones like Python and HTML.
    
    Will you be able to fight them all?''')

answer = input('''    Yes(Y) / No(n)
    Input: ''')

print()
print("|---------------------------------------------------|")

while(True):
    if answer == "Y" or answer == "y":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("|---------------------------------------------------|")
        print()

        player = input('''    Good! Then...    
        What is your name player?
        Name: ''')

        print()
        print("|---------------------------------------------------|")

        Game()
    elif answer == "n":
        sys.exit()
    else:
        answer = input('''    I didn't understand quite, could you retype it?
            Input: ''')



