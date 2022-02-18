from operator import le
from time import sleep
from xml.etree.ElementInclude import include
import json
from termcolor import colored, cprint


def give_it_straight():
    print("Damn dude you're in a sketchy position, but we'll get it done though no worries.")
    text = colored('Hello, World!', 'red', attrs=['reverse', 'blink'])
    print(text)


def play_with_them():
    word_color = []
    colored_list = []
    last_guess= input("Perfect! What was the last word you guessed? " )
    print("Okay I need some more, care to highlight what colors you got on each letter?")
    print("Use B for Grey, Y for yellow and G for Green")
    for letter in last_guess: 
        print(letter,  end =" ")
        word_color.append(input())
    for index, letter in enumerate(last_guess):
        if word_color[index] == 'G':
            colored_list.append(colored(letter, 'green'))
        elif word_color[index] == 'Y':
            colored_list.append(colored(letter, 'yellow'))
        else:
            colored_list.append(colored(letter, 'white'))
    print("Just confirming, this is what you have")
    for letter in colored_list: 
        print (letter, end =" ")
    confirmation = input("Press Y to confirm N to try entering your word again ")
    if confirmation == 'Y': 
        print("This is it!")
        ## TODO: Implement functionality
    else: 
        play_with_them()


print("Hey, welcome to Wordler, this simple program guide you to solving the days wordle!")
sleep(2)
guesses_left = input("Okay let's take it slow, how many guesses do you have left: ")
if int(guesses_left)< 2: 
    give_it_straight()
else :
   play_with_them()

