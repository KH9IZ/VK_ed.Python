class TicTacGame:

    template = """
    1  |2  |3
     {} | {} | {}
    ___|___|___
    4  |5  |6
     {} | {} | {}
    ___|___|___
    7  |8  |9
     {} | {} | {}
       |   |"""

    field = [[' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' ']]

    prompt = "Enter number in [1, 9]: "

    def show_board(self):
        print(self.template.format(*(cell for row in self.field for cell in row)))

    def validate_input(self, inp):
        try:
            num = int(inp)
        except ValueError:
            return False
        col = (num - 1) % 3
        row = (num - 1) // 3
        return num in range(1, 10) and self.field[row][col] == ' '

    def start_game(self):
        players = ['X', 'O']
        i = 0
        while not (winner := self.check_winner()):
            self.show_board()
            print(f"Player {players[ i % len(players) ]}'s move.")
            raw_input = input(self.prompt)
            if not self.validate_input(raw_input):
                print("Invalid input.")
                continue
            num = int(raw_input) - 1
            col = num % 3
            row = num // 3
            self.field[row][col] = players[i % len(players)]
            i += 1
        self.show_board()
        if winner in players:
            print(f"Player {winner} won!")
        else:
            print("Draw!")

    @staticmethod
    def __checker(seq):
        return seq.count(seq[0]) == len(seq) and seq[0] != ' '

    def check_winner(self):
        rows = self.field
        cols = [*zip(*self.field)]
        for i in range(3):
            if self.__checker(rows[i]) or self.__checker(cols[i]):
                return self.field[i][i]
        if self.field[0][0] == self.field[1][1] == self.field[2][2] != ' ' or \
           self.field[2][0] == self.field[1][1] == self.field[0][2] != ' ':
            return self.field[1][1]
        if not [cell for row in self.field for cell in row if cell == ' ']:
            return ' '
        return ''


if __name__ == "__main__":
    game = TicTacGame()
    game.start_game()
