import unittest
from tictactoe import TicTacGame

class TicTacTestCase(unittest.TestCase):

    def test_validate_input(self):
        game = TicTacGame()
        self.assertFalse(game.validate_input('QQ'))
        self.assertFalse(game.validate_input('0'))
        self.assertFalse(game.validate_input('-1'))
        self.assertFalse(game.validate_input('10'))
        self.assertFalse(game.validate_input('1.0'))

        for i in range(1, 10):
            self.assertTrue(game.validate_input(str(i)))

        game.field[0][0] = 'X'
        self.assertFalse(game.validate_input('1'))

    def test_check_winner(self):
        game = TicTacGame()
        game.field = [['X', 'X', 'X'],
                      [' ', ' ', 'O'],
                      [' ', 'O', ' ']]
        self.assertEqual(game.check_winner(), 'X')
        
        game.field = [['X', ' ', 'X'],
                      ['O', 'O', 'O'],
                      [' ', 'X', ' ']]
        self.assertEqual(game.check_winner(), 'O')

        game.field = [[' ', 'O', ' '],
                      [' ', 'O', ' '],
                      ['X', 'X', 'X']]
        self.assertEqual(game.check_winner(), 'X')

        game.field = [['X', 'O', ' '],
                      ['X', 'O', ' '],
                      ['X', ' ', ' ']]
        self.assertEqual(game.check_winner(), 'X')

        game.field = [[' ', 'O', 'X'],
                      ['X', 'O', ' '],
                      [' ', 'O', 'X']]
        self.assertEqual(game.check_winner(), 'O')
        game.field = [['O', 'O', 'X'],
                      [' ', 'O', 'X'],
                      [' ', ' ', 'X']]
        self.assertEqual(game.check_winner(), 'X')
        
        game.field = [['X', 'O', ' '],
                      [' ', 'X', ' '],
                      ['O', ' ', 'X']]
        self.assertEqual(game.check_winner(), 'X')
        game.field = [['O', 'O', 'X'],
                      [' ', 'X', ' '],
                      ['X', ' ', ' ']]
        self.assertEqual(game.check_winner(), 'X')

        game.field = [['O', 'O', 'X'],
                      ['X', 'X', 'O'],
                      ['O', 'X', 'X']]
        self.assertEqual(game.check_winner(), ' ')

        game.field = [[' ', 'O', 'X'],
                      ['X', 'X', 'O'],
                      ['O', 'X', 'X']]
        self.assertFalse(game.check_winner())
        game.field = [['O', 'O', 'X'],
                      ['X', ' ', 'O'],
                      ['O', 'X', 'X']]
        self.assertFalse(game.check_winner())
