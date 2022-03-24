import unittest
from tictactoe import TicTacGame


class TicTacTestCase(unittest.TestCase):

    def setUp(self):
        self.game = TicTacGame()
        self.game.field = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

    def test_validate_input(self):
        self.assertFalse(self.game.validate_input('QQ'))
        self.assertFalse(self.game.validate_input('0'))
        self.assertFalse(self.game.validate_input('-1'))
        self.assertFalse(self.game.validate_input('10'))
        self.assertFalse(self.game.validate_input('1.0'))

        self.assertTrue(self.game.validate_input('1'))
        self.assertTrue(self.game.validate_input('2'))
        self.assertTrue(self.game.validate_input('3'))
        self.assertTrue(self.game.validate_input('4'))
        self.assertTrue(self.game.validate_input('5'))
        self.assertTrue(self.game.validate_input('6'))
        self.assertTrue(self.game.validate_input('7'))
        self.assertTrue(self.game.validate_input('8'))
        self.assertTrue(self.game.validate_input('9'))

        self.game.field[0][0] = 'X'
        self.assertFalse(self.game.validate_input('1'))

    def test_check_winner(self):
        self.game.field = [['X', 'X', 'X'],
                           [' ', ' ', 'O'],
                           [' ', 'O', ' ']]
        self.assertEqual(self.game.check_winner(), 'X')

        self.game.field = [['X', ' ', 'X'],
                           ['O', 'O', 'O'],
                           [' ', 'X', ' ']]
        self.assertEqual(self.game.check_winner(), 'O')

        self.game.field = [[' ', 'O', ' '],
                           [' ', 'O', ' '],
                           ['X', 'X', 'X']]
        self.assertEqual(self.game.check_winner(), 'X')

        self.game.field = [['X', 'O', ' '],
                           ['X', 'O', ' '],
                           ['X', ' ', ' ']]
        self.assertEqual(self.game.check_winner(), 'X')

        self.game.field = [[' ', 'O', 'X'],
                           ['X', 'O', ' '],
                           [' ', 'O', 'X']]
        self.assertEqual(self.game.check_winner(), 'O')
        self.game.field = [['O', 'O', 'X'],
                           [' ', 'O', 'X'],
                           [' ', ' ', 'X']]
        self.assertEqual(self.game.check_winner(), 'X')

        self.game.field = [['X', 'O', ' '],
                           [' ', 'X', ' '],
                           ['O', ' ', 'X']]
        self.assertEqual(self.game.check_winner(), 'X')
        self.game.field = [['O', 'O', 'X'],
                           [' ', 'X', ' '],
                           ['X', ' ', ' ']]
        self.assertEqual(self.game.check_winner(), 'X')

        self.game.field = [['O', 'O', 'X'],
                           ['X', 'X', 'O'],
                           ['O', 'X', 'X']]
        self.assertEqual(self.game.check_winner(), ' ')

        self.game.field = [[' ', 'O', 'X'],
                           ['X', 'X', 'O'],
                           ['O', 'X', 'X']]
        self.assertFalse(self.game.check_winner())
        self.game.field = [['O', 'O', 'X'],
                           ['X', ' ', 'O'],
                           ['O', 'X', 'X']]
        self.assertFalse(self.game.check_winner())


if __name__ == "__main__":
    unittest.main()
