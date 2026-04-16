# Jacob Taylor
# CIS256 Spring 2026
# Exercise Assignment 4
"""Purpose: Implement a hangman-esque game, using a predefined list."""

# Random module imported for the word to be selectly randomly, for the user to guess
import random

# Predefined list
guess_word_list = ["ubiquitous", "magnanimous", "spiteful", "love", "condition"]
# Said list randomized for the user to guess
word_choice = random.choice(guess_word_list)
# The word's length randomly chose 
total_length = len(word_choice)

# Number of attempts user has before all run out, thus ending the game
number_of_lives = 10

# The TRUE variable to keep the game going until the user either 
# plays the game until the number of lives are used or the word has been fully guessed
# correctly
active_game = True

# To display the chosen word via blanks, with title
word_display = ["_"] * total_length
print("=====H A N G M A N=====\n")
print(" ".join(word_display))


while active_game == True:
    print()
    guess_letter = input("Guess a letter: ").lower()

    # Guessed letter checking
    # If right
    if guess_letter in word_choice:
         for fill in range(total_length):
              letter = word_choice[fill]
              if letter == guess_letter:
                   word_display[fill] = letter
                   print("Correct. Keep going.")
                   print(" ".join(word_display))
    # If wrong
    elif guess_letter not in guess_word_list:
         number_of_lives -= 1
         print(f"Wrong. Lives left: {number_of_lives}")
         print(" ".join(word_display))
    
    # If all attempts are used, the game is over and the user loses
    if number_of_lives == 0:
        print(f"Game over! The correct word was: {word_choice}")
        active_game = False
    # If all blanks are filled, the user wins
    elif "_" not in word_display:
        print("Congratulations! You win!")
        active_game = False
          
    

         


    


"""
AI Context 1:
Searched up "python trying to code a game similar to hangman. 
Can you give me a hint for how to approach this without giving me the full solution?" via Google
AI Context 2:
Searched up "python trying to make a hangman game to show blanks" via Google to correct the random
object used (from randrange to choice) and figure out the hangman-esque syntax
AI Context 3:
Searched up "python 
"""

    

    