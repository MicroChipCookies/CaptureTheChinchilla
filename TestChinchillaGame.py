# Author: Valerie Armstrong
# GitHub username: MicroChipCookies
# Date: 08/08/2025
# Description: This module contains unit tests for the game in CaptureTheChinchilla.py

import unittest
from CaptureTheChinchilla import *

class MyTestCase(unittest.TestCase):


    def test_board(self):
        """Game board initializes properly"""
        game_1 = AnimalGame()
        squares = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7',
                   'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7',
                   'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7',
                   'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7',
                   'E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7',
                   'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7',
                   'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7'
                   ]
        board = game_1.get_game_board()

        # Game board has all rows/columns it should, and only those
        for square in squares:
            self.assertTrue(square in board.keys(), f'{square} not in game board')
        self.assertEqual(len(squares), len(board.keys()),
                         'incorrect number of game board squares generated')

        # Starting a game properly initializes pieces and places them in correct places
        self.assertTrue(str(board['A1']) == 'N1T', 'A1 wrong name')
        self.assertTrue(str(board['B1']) == 'M1T', 'A2 wrong name')
        self.assertTrue(str(board['C1']) == 'O1T', 'A3 wrong name')
        self.assertTrue(str(board['D1']) == 'CHT', 'A4 wrong name')
        self.assertTrue(str(board['E1']) == 'O2T', 'A5 wrong name')
        self.assertTrue(str(board['F1']) == 'M2T', 'A6 wrong name')
        self.assertTrue(str(board['G1']) == 'N2T', 'A7 wrong name')
        self.assertTrue(str(board['A7']) == 'N1A', 'G1 wrong name')
        self.assertTrue(str(board['B7']) == 'M1A', 'G2 wrong name')
        self.assertTrue(str(board['C7']) == 'O1A', 'G3 wrong name')
        self.assertTrue(str(board['D7']) == 'CHA', 'G4 wrong name')
        self.assertTrue(str(board['E7']) == 'O2A', 'G5 wrong name')
        self.assertTrue(str(board['F7']) == 'M2A', 'G6 wrong name')
        self.assertTrue(str(board['G7']) == 'N2A', 'G7 wrong name')

    def test_turn_taking(self):
        """Checks whether turns are switching properly."""
        game_1 = AnimalGame()
        self.assertTrue(game_1.make_move('C1', 'C2'), "should be tangerine's turn")
        self.assertFalse(game_1.make_move('E1', 'E2'), "should not be tangerine's turn")
        self.assertTrue(game_1.make_move('C7', 'C6'), "should be amethyst's turn")
        self.assertFalse(game_1.make_move('E7', 'E6'), "should not be amethyst's turn")
        self.assertTrue(game_1.make_move('E1', 'E2'), "should be tangerine's turn")

    def test_simple_narwhal(self):
        """
        Checks that narwhals make basic legal moves (no captures, unimpeded), and don't make illegal ones.
        Also ensure that spaces not on the board are not allowed.
        Narwhals can jump exactly 2 spaces diagonally (or one space orthogonally), not farther or shorter
        """
        game_1 = AnimalGame()
        self.assertFalse(game_1.make_move('A1', 'B2'), 'illegal move made: diagonal too short')      # Tangerine
        self.assertFalse(game_1.make_move('A1', 'D4'), 'illegal move made: diagonal too far')
        self.assertFalse(game_1.make_move('A1', 'A3'), 'illegal move made: down too far')
        self.assertTrue(game_1.make_move('A1', 'C3'), 'should be legal: diagonal 2')
        self.assertFalse(game_1.make_move('A7', 'B6'), 'illegal move made: diagonal too short')      # Amethyst
        self.assertFalse(game_1.make_move('A7', 'D4'), 'illegal move made: diagonal too far')
        self.assertFalse(game_1.make_move('A7', 'A5'), 'illegal move made: up too far')
        self.assertFalse(game_1.make_move('G7', 'G8'), "illegal move made: destination square doesn't exist")
        self.assertTrue(game_1.make_move('A7', 'C5'), 'should be legal: diagonal 2')
        self.assertFalse(game_1.make_move('C3', 'A3'), 'illegal move made: left too far')            # Tangerine
        self.assertFalse(game_1.make_move('C3', 'E3'), 'illegal move made: right too far')
        self.assertTrue(game_1.make_move('C3', 'B3'), 'should be legal: left 1')
        self.assertFalse(game_1.make_move('C5', 'C3'), 'illegal move made: up too far')              # Amethyst
        self.assertTrue(game_1.make_move('C5', 'C6'), 'should be legal: down 1')
        self.assertFalse(game_1.make_move('B3', 'B5'), 'illegal move made: down too far')            # Tangerine
        self.assertTrue(game_1.make_move('B3', 'C3'), 'should be legal: right 1')
        self.assertTrue(game_1.make_move('C6', 'C5'), 'should be legal: up 1')                       # Amethyst
        self.assertTrue(game_1.make_move('C3', 'A1'), 'should be legal: diagonal 2')                 # Tangerine
        self.assertTrue(game_1.make_move('C5', 'A7'), 'should be legal: diagonal 2')                 # Amethyst
        self.assertFalse(game_1.make_move('G1', 'E2'), 'illegal move made: neither diagonal, nor orthogonal')    # Tangerine
        self.assertFalse(game_1.make_move('A1', 'A0'), "illegal move made: destination square doesn't exist")

    def test_simple_marmoset(self):
        """
        Checks that marmosets make basic legal moves (no captures, unimpeded), and don't make illegal ones
        Marmosets can slide up to 4 spaces diagonally (or one space orthogonally), no farther.
        """
        game_1 = AnimalGame()
        self.assertFalse(game_1.make_move('B1', 'B3'), "illegal move made: down too far")        # Tangerine
        self.assertTrue(game_1.make_move('B1', 'C2'), 'should be legal: diagonal 1 down-right')
        self.assertFalse(game_1.make_move('B7', 'B5'), "illegal move made: up too far")          # Amethyst
        self.assertTrue(game_1.make_move('B7', 'E4'), 'should be legal: diagonal 3 up-right')
        self.assertFalse(game_1.make_move('C2', 'A2'), "illegal move made: left too far")        # Tangerine
        self.assertFalse(game_1.make_move('C2', 'E2'), "illegal move made: right too far")
        self.assertTrue(game_1.make_move('F1', 'D3'), 'should be legal: diagonal 2 down-left')
        self.assertTrue(game_1.make_move('F7', 'B3'), 'should be legal: diagonal 4 up-left')     # Amethyst
        self.assertTrue(game_1.make_move('C2', 'B1'), 'should be legal: diagonal 1 up-left')     # Tangerine
        self.assertTrue(game_1.make_move('E4', 'B7'), 'should be legal: diagonal 3 down-left')   # Amethyst
        self.assertTrue(game_1.make_move('D3', 'F1'), 'should be legal: diagonal 2 up-right')    # Tangerine
        self.assertTrue(game_1.make_move('B3', 'F7'), 'should be legal: diagonal 4 down-right')  # Amethyst
        self.assertFalse(game_1.make_move('B1', 'G6'), "illegal move made: diagonal too far")    # Tangerine

    def test_okapi(self):
        """
        Checks that okapis can make basic legal moves (no captures, unimpeded), and don't make illegal ones
        Okapis can jump 1 space in any direction (or one space orthogonally), no farther
        """
        game_1 = AnimalGame()
        self.assertFalse(game_1.make_move('C1', 'C3'), "illegal move made: down too far")        # Tangerine
        self.assertFalse(game_1.make_move('C1', 'A3'), "illegal move made: diagonal too far")
        self.assertTrue(game_1.make_move('C1', 'C2'), 'should be legal: down 1')
        self.assertTrue(game_1.make_move('E7', 'E6'), 'should be legal: up 1')                   # Amethyst
        self.assertTrue(game_1.make_move('C2', 'B2'), 'should be legal: left 1')                 # Tangerine
        self.assertTrue(game_1.make_move('E6', 'F6'), 'should be legal: right 1')                # Amethyst
        self.assertTrue(game_1.make_move('B2', 'C3'), 'should be legal: diagonal 1 down-right')  # Tangerine
        self.assertTrue(game_1.make_move('F6', 'E5'), 'should be legal: diagonal 1 up-left')     # Amethyst
        self.assertTrue(game_1.make_move('C3', 'B4'), 'should be legal: diagonal 1 down-left')   # Tangerine
        self.assertTrue(game_1.make_move('E5', 'F4'), 'should be legal: diagonal 1 up-right')    # Amethyst

    def test_chinchilla(self):
        """
        Checks that chinchillas can make basic legal moves (no captures, unimpeded), and don't make illegal ones
        Chinchillas can slide orthogonally up to 3 spaces (or 1 space diagonally), not farther.
        """
        game_1 = AnimalGame()
        self.assertFalse(game_1.make_move('D1', 'D5'), "illegal move made: down too far")        # Tangerine
        self.assertFalse(game_1.make_move('D1', 'B3'), "illegal move made: diagonal too far")
        self.assertTrue(game_1.make_move('D1', 'D2'), 'should be legal: down 1')
        self.assertTrue(game_1.make_move('D7', 'D6'), 'should be legal: up 1')                   # Amethyst
        self.assertTrue(game_1.make_move('D2', 'C2'), 'should be legal: left 1')                 # Tangerine
        self.assertTrue(game_1.make_move('D6', 'E6'), 'should be legal: right 1')                # Amethyst
        self.assertTrue(game_1.make_move('C2', 'C4'), 'should be legal: down 2')                 # Tangerine
        self.assertTrue(game_1.make_move('E6', 'E4'), 'should be legal: up 2')                   # Amethyst
        self.assertTrue(game_1.make_move('C4', 'A4'), 'should be legal: left 2')                 # Tangerine
        self.assertTrue(game_1.make_move('E4', 'G4'), 'should be legal: right 2')                # Amethyst
        self.assertTrue(game_1.make_move('A4', 'B3'), 'should be legal: diagonal 1 up-right')    # Tangerine
        self.assertTrue(game_1.make_move('G4', 'F5'), 'should be legal: diagonal 1 down-left')   # Amethyst
        self.assertTrue(game_1.make_move('B3', 'E3'), 'should be legal: right 3')                # Tangerine
        self.assertTrue(game_1.make_move('F5', 'C5'), 'should be legal: left 3')                 # Amethyst
        self.assertTrue(game_1.make_move('E3', 'E6'), 'should be legal: down 3')                 # Tangerine
        self.assertTrue(game_1.make_move('C5', 'C2'), 'should be legal: up 3')                   # Amethyst
        self.assertTrue(game_1.make_move('E6', 'D5'), 'should be legal: diagonal 1 up-left')     # Tangerine
        self.assertTrue(game_1.make_move('C2', 'D3'), 'should be legal: diagonal 1 down-right')  # Amethyst


    def test_blocking(self):
        """
        Test that sliding moves are blocked when another piece is between the start and destination squares.
        Test that narwhals are NOT blocked when a piece is between them and their destination.
        """
        game_1 = AnimalGame()
        game_1.make_move('B1', 'E4')                                                                  # Tangerine
        self.assertFalse(game_1.make_move('B7', 'F3'), "marmoset should be blocked by opponent")      # Amethyst
        game_1.make_move('D7', 'D5')
        game_1.make_move('C1', 'B2')                                                                  # Tangerine
        self.assertFalse(game_1.make_move('F7', 'C4'), 'marmoset should be blocked by own team')      # Amethyst
        game_1.make_move('G7', 'E5')
        self.assertTrue(game_1.make_move('A1', 'C3'), 'narwhal should not be blocked')                # Tangerine
        game_1.make_move('C7', 'C6')                                                                  # Amethyst
        game_1.make_move('E4', 'F4')                                                                  # Tangerine
        self.assertTrue(game_1.make_move('E5', 'G3'), 'narwhal should not be blocked')                # Amethyst


    def test_captures(self):
        """
        Tests that captured pieces are removed from the board, and friendly pieces can't be captured. Tests that
        game is won when a chinchilla is captured. Ensures that the game state is correctly reported.
        """
        game_1 = AnimalGame()
        board = game_1.get_game_board()
        tang_chinchilla = board['D1']
        tang_marmoset_2 = board['F1']
        ame_okapi_2 = board['E7']
        ame_narwhal_1 = board['A7']
        self.assertEqual('UNFINISHED', game_1.get_game_state(), 'game should start in unfinished state')
        self.assertFalse(game_1.make_move('A1', 'B1'), 'narwhal should not capture its own team')     # Tangerine
        self.assertFalse(game_1.make_move('B1', 'A1'), 'marmoset should not capture its own team')
        self.assertFalse(game_1.make_move('C1', 'D1'), 'okapi should not capture its own team')
        self.assertFalse(game_1.make_move('D1', 'E1'), 'chinchilla should not capture its own team')
        game_1.make_move('D1', 'D4')
        game_1.make_move('F7', 'D5')                                                                  # Amethyst
        self.assertTrue(game_1.make_move('D4', 'D5'), 'chinchilla should capture opponent')           # Tangerine
        self.assertTrue(board['D5'] is tang_chinchilla)
        self.assertEqual('UNFINISHED', game_1.get_game_state(), 'game should not end with this capture')
        game_1.make_move('G7', 'E5')                                                                  # Amethyst
        game_1.make_move('F1', 'B5')                                                                  # Tangerine
        game_1.make_move('C7', 'C6')                                                                  # Amethyst
        self.assertTrue(game_1.make_move('B5', 'C6'), 'marmoset should capture opponent')             # Tangerine
        self.assertTrue(board['C6'] is tang_marmoset_2)
        self.assertEqual('UNFINISHED', game_1.get_game_state(), 'game should not end with this capture')
        game_1.make_move('E7', 'D6')                                                                  # Amethyst
        game_1.make_move('G1', 'E3')                                                                  # Tangerine
        self.assertTrue(game_1.make_move('D6', 'C6'), 'okapi should capture opponent')                # Amethyst
        self.assertTrue(board['C6'] is ame_okapi_2)
        game_1.make_move('E3', 'C5')                                                                  # Tangerine
        self.assertTrue(game_1.make_move('A7', 'C5'), 'narwhal should capture opponent')              # Amethyst
        self.assertTrue(board['C5'] is ame_narwhal_1)
        self.assertTrue(game_1.make_move('D5', 'D7'), 'chinchilla should capture chinchilla')         # Tangerine
        self.assertTrue(board['D7'] is tang_chinchilla)
        self.assertEqual('TANGERINE_WON', game_1.get_game_state(), 'tangerine should have won the game')

        game_2 = AnimalGame()
        board_2 = game_2.get_game_board()
        ame_marmoset_1 = board_2['B7']
        game_2.make_move('D1', 'D3')                                                                  # Tangerine
        game_2.make_move('B7', 'E4')                                                                  # Amethyst
        game_2.make_move('C1', 'C2')                                                                  # Tangerine
        self.assertTrue(game_2.make_move('E4', 'D3'), 'marmoset should capture chinchilla')           # Amethyst
        self.assertTrue(board_2['D3'] is ame_marmoset_1)
        self.assertEqual('AMETHYST_WON', game_2.get_game_state(), 'amethyst should have won the game')



if __name__ == '__main__':
    unittest.main()
