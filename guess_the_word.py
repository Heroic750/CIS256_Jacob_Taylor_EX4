# Jacob Taylor
# CIS256 Spring 2026
# Exercise Assignment 4
"""Purpose: Implement a hangman-esque game, using a predefined list."""

# Random module imported for the word to be selectly randomly, for the user to guess
import random

# Predefined list
guess_word_list = ["ubiquitous", "magnanimous", "spiteful", "love", "condition"]

# Empty list to keep track of letters guessed by the user
guessed_letters = []

# The underscores the Hangman Game uses, showing letters to be guessed
underscore_letters = ""

# Number of attempts user has before all run out, and the game is over
number_of_lives = 10

# Number of attempts used by the user when the guess was wrong 
lives_used = 0

# The TRUE variable to keep the game going until the user either chooses to exit,
# or plays the game until the number of lives are used or the word has been fully guessed
# correctly
active_game = True

print("=====H A N G M A N=====\n")

# Function to turn the randomly chosen word into blank spaces for the user to guess.
# Then reveal one letter of a word at a time, if the guess is right by the user
def letter_reveal():

    for letter1 in random.randrange(guess_word_list):
        if (letter1 != " "):
            underscore_letters += "_"
        else:
            underscore_letters += " "
    print(underscore_letters)
    current_letters = underscore_letters
    while active_game == True:
        print()
        guess_letter = input("Guess a letter: ")
        correct_letters = []
        # To check if letters exist in the blanks. If the letter is right, 
        # the letter(s) is added to the blank(s)
        for letter2 in range(0,len(guess_word_list)):
            if guess_letter == guess_word_list[letter2]:
                correct_letters.append(letter2)
                print(correct_letters)
        # If the letter is wrong, number of attempts decreases and lives used increases
        if len(correct_letters) == 0:
            lives_used += 1
            print(f"Wrong. No {guess_letter} in the word.")
            print(f"Number of lives remaining: {lives_used} / {number_of_lives}")
        # If the letter is right, the letter is revealed to the user and the blanks are updated
        else:
            print(f"Correct. There was/were {correct_letters} {guess_letter} letter(s) in the phrase.")
            for i in correct_letters:
                current_letters = current_letters[:i] + guess_letter + current_letters[i+1:]
        # When the amount of lives have been fully used up or user fills in all blanks
        if(lives_used == number_of_lives or guess_letter == current_letters):
            print("Congratulations! The word has been fully guessed. You have won the game.")
            active_game = False
        # If either one ends the game, the blanks are cleared for another game to start
        correct_letters.clear()


"""
AI Context 1:
Searched up "python trying to code a game similar to hangman. 
Can you give me a hint for how to approach this without giving me the full solution?" via Google
AI Context 2:
Searched up "python 
"""

    

    