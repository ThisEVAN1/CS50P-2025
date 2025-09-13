from random import randint
import sys


def main():

    while True:
        try:
            # Ask the user for the value of level
            level = int(input("Level: "))
            if level < 1:
                raise ValueError()
        except ValueError:
            print("Incorrect values")
        else:
            # If the value entered is correct, choose a random number between 1 and level
            rand_num = randint(1, level)
            break

    while True:
        try:
            # Ask the user for their guess
            guess = int(input("Guess: "))
            if guess < 1:
                raise ValueError()
        except ValueError:
            # Reprompt if ValueError
            ...
        else:
            # Check if the guess is correct or greater or smaller
            if guess == rand_num:
                sys.exit("Just right!")
            elif guess > rand_num:
                print("Too large!")
            else:
                print("Too small!")


main()
