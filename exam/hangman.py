"""
Entry point for the hangman game.

Run the game from the command line with
    python -m exam.hangman

Depending on your installation, you might need
to call python3 instead of python.
"""

import numpy as np
import os
import random

class Hangman():
    
    def __init__(self, max_attempts = 12):
        current_folder = os.path.dirname(__file__)
        self.path_to_file = os.path.join(current_folder, '../resources/words.txt')
        self.database = self.load_words()
        self.random_word = self.select_random_word()
        self.current_word = '_'*len(self.random_word)
        self.correct_characters = set()
        self.wrong_characters = set()
        self.max_attempts = max_attempts
   
    def load_words(self):
        with open(self.path_to_file, 'r') as words_file:
            words_database = words_file.read().splitlines()
        return words_database        
    
    def select_random_word(self):
        return random.choice(self.database)
    
    def ask_user_for_character(self):
        input_character = input('Guess a character:')
        return input_character.lower()
    
    def check_character(self, character):
        if character in self.random_word:
            self.correct_characters.add(character)
        else:
            self.wrong_characters.add(character)
            if len(self.wrong_characters) >= self.max_attempts:
                self.end_game()               
                
    def update_word(self):
        updated_word = ''
        for character in self.random_word:
            if character in self.correct_characters:
                updated_word += character
            else:
                updated_word += '_'
        self.current_word = updated_word
        
    def report_progress(self):
        print('Your word:', self.current_word, 'Used (wrong) characters:', list(self.wrong_characters) )
      
    def make_new_guess(self):
        input_character = self.ask_user_for_character()
        self.check_character(input_character)
        self.update_word()
        self.report_progress()
        self.check_if_won() # Only for testing purposes, otherwise this line is not needed
        
    def play_game(self):
        while self.current_word != self.random_word:
            self.make_new_guess()
        self.win_game()
    
    def check_if_won(self): # Work in progress, currently only for testing purposes
        if self.current_word == self.random_word:
            self.win_game()
        
    def end_game(self):
        print('Game over!')
        
    def win_game(self):
        print('Congratulations!')
    
if __name__ == "__main__":    
    game = Hangman()    
    game.play_game()






