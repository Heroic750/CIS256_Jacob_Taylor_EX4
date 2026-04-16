# Jacob Taylor
# CIS256 Spring 2026
# Exercise Assignment 4
"""Purpose: To test the guess_the_word python file. See if it works properly."""

# Unittest module imported to test guess_the_word.py file to see if it works
import unittest

# Import guess_the_word.py file
from guess_the_word import guessing_game

class TestGuessingGame(unittest.TestCase):
    # Testing if the selected word comes from the predefined list
    def test_list_contains_word(self):
        self.assertTrue(guessing_game["ubiquitous", "magnanimous", "spiteful", "love", "condition"])
    # Testing if the guess is correct
    def test_correct_guess(self):
        self.assertTrue(guessing_game["love"])
    # Testing if the guess is incorrect
    def test_incorrect_guess(self):
        self.assertFalse(guessing_game["bigot"])
if __name__ == "__main__":
    unittest.main()