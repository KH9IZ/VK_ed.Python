from io import StringIO
import sys
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

    def test_show_board(self):
        new_out = StringIO()
        old_out = sys.stdout
        sys.stdout = new_out
        self.game.field = [[' ', 'X', ' '],
                           ['X', ' ', 'X'],
                           [' ', 'X', ' ']]
        self.game.template = "{}{}{}{}{}{}{}{}{}"
        self.game.show_board()
        sys.stdout = old_out
        self.assertEqual(new_out.getvalue(), " X X X X \n")

    def test_start_game(self):
        new_in, new_out = StringIO("1\n5\n2\n2\n4\n3\n"), StringIO()
        old_in, old_out = sys.stdin, sys.stdout
        sys.stdin.flush()
        sys.stdout.flush()
        self.game.template = ""
        sys.stdin, sys.stdout = new_in, new_out
        self.game.start_game()
        sys.stdin, sys.stdout = old_in, old_out
        expect = """
Player X's move.
Enter number in [1, 9]: \nPlayer O's move.
Enter number in [1, 9]: \nPlayer X's move.
Enter number in [1, 9]: \nPlayer O's move.
Enter number in [1, 9]: Invalid input.

Player O's move.
Enter number in [1, 9]: \nPlayer X's move.
Enter number in [1, 9]: \nPlayer X won!\n"""
        self.assertEqual(new_out.getvalue(), expect)


if __name__ == "__main__":
    unittest.main()
