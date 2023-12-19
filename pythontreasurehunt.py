# python treasure hunt game
import random
import time


def display_game_intro():
    print('''Here is a 5 sentence introduction to a Python treasure hunt game:

Search for Hidden Treasures: A Python Adventure

Eager for adventure and riches beyond your wildest dreams? Embark on and epic quest in search of hidden treasures and lost artifacts using your trusty Python skills. Solving puzzles and overcoming challenges at each stage, you'll traverse mysterious ruins, secret passages, and ancient temples on your way towards the ultimate prize. With danger, surprises, and fun around every corner, this Python-powered treasure hunt promises an experience you won't soon forget. Master loops, strings, lists, and more as you learn to think like a true adventurer-archeologist. The treasures await - do you have the coding chops to uncover their secrets?''')

#functions should be self describing and don't run until they are called. 
    
def choose_cave():
    cave  = ''
    while cave != '1' and cave != '2':
        print('Which cave do you want to enter? (1 or 2)')
        cave = input()
    return cave 

def enter_cave(chosen_cave):

    print("You have entered a cave...")
#stops the program for one second
    time.sleep(1)


    #asking for a random number between 1 and 2
    random_cave = random.randint(1,2)

    #print(random_cave = + str(random+cave))

    if random_cave == int(chosen_cave):
          print("----> Lucky you! You found the cave!")
    else:
        print("----> Aye, mate all  you get is booty filled with...\n Week old socks!")
def main_loop():
    display_game_intro()


def main_loop():
    display_game_intro()
    whatdidenter = choose_cave()

    print("What cave did I choose: " + whatdidenter)

#function is in statis until you call it
#choose cave returns whatever value is in cave

def main_loop():
    
    '''the main loop function controls the flow of the game by calling functions and using conditionals'''

    playGameAgain = "yes"

    while playGameAgain == "yes" or playGameAgain == "y":

        display_game_intro()
        chosen_cave = choose_cave()
        enter_cave(chosen_cave)

        print("\n\nDo you want to try again? (yes or no)")
        playGameAgain = input()
        print("You said" + ' '+ playGameAgain)
        time.sleep(1)

        if playGameAgain == "yes" or playGameAgain == "y":
            print("\nLet'stryagain")

        else:
            print("Ok, hasta luego!")


main_loop()


                     
