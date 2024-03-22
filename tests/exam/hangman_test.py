# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 12:56:37 2024

@author: ilsed
"""
from ...exam.hangman import Hangman

def test_ask_input(mocker):
    game = Hangman()
    mocker.patch('builtins.input', return_value ='F')
    assert game.ask_user_for_character() == 'f'

def test_load_words():
    game = Hangman()
    assert game.load_words()[0] == "abruptly"
    assert game.load_words()[4] == "askew"
    
def test_select_word():
    game = Hangman()
    assert game.select_random_word() in game.database
 
def test_check_character():
    game = Hangman()
    game.random_word = 'buffoon'
    game.check_character('b')
    game.check_character('o')
    game.check_character('z')
    assert game.correct_characters == {'b','o'}
    assert game.wrong_characters == {'z'}
        
def test_update_word(mocker):
    # mocker.patch('...exam.hangman.select_random_word', return_value ='buffoon')
    game = Hangman()  
    game.random_word = 'buffoon'
    game.check_character('f')
    game.check_character('b')
    game.check_character('z')
    game.update_word()
    assert game.current_word == 'b_ff___'
    
def test_report_progress(mocker):
    printer = mocker.patch('builtins.print')
    game = Hangman()  
    game.random_word = 'buffoon'
    game.check_character('f')
    game.update_word()
    game.report_progress()
    printer.assert_called_with('Your word:','__ff___','Used (wrong) characters:', [])
    
def test_max_attempts(mocker):
    printer = mocker.patch('builtins.print')
    game = Hangman(max_attempts=2)  
    game.random_word = 'buffoon'
    game.check_character('a')
    game.check_character('c')
    game.check_character('a')
    game.check_character('z')
    printer.assert_called_with('Game over!')

# def test_win_game(mocker):
#     game = Hangman()
#     game.random_word = 'ivy'
#     mocker.patch('builtins.input', return_value ='i')
#     mocker.patch('builtins.input', return_value ='v')
#     mocker.patch('builtins.input', return_value ='y')
#     game.play_game()
    # assert ...
    
def test_win_game_alternative(mocker): 
    printer = mocker.patch('builtins.print')
    game = Hangman()
    game.random_word = 'ivy'
    game.check_character('i')
    game.update_word()
    game.check_if_won()
    game.check_character('v')
    game.update_word()
    game.check_if_won()
    game.check_character('y')
    game.update_word()
    game.check_if_won()
    printer.assert_called_with('Congratulations!')
    


    
    