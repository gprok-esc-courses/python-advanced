class Player:
    def __init__(self, value):
        self.symbol = 'X' if value==1 else 'O'
        self.value = value
        self.score = 0

    def add_win(self):
        self.score += 1

    def get_symbol(self):
        return self.symbol

    def get_value(self):
        return self.value

    def get_score(self):
        return self.score


class Game:
    def __init__(self):
        self.player_x = Player(1)
        self.player_o = Player(2)
        self.current = self.player_x
        self.winner = None
        self.board = [[0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0]]

    def get_score(self):
        return [self.player_x.get_score(), self.player_o.get_score()]

    def reset(self):
        if not self.is_tie():
            self.current = self.winner  # winner plays first in next round
        self.winner = None
        self.board = [[0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0]]

    def play(self, row, col):
        self.board[row][col] = self.current.get_value()
        self.current = self.player_x if self.current == self.player_o else self.player_o
        self.set_winner()

    def get_winner(self):
        return self.winner

    def get_current_symbol(self):
        return self.current.get_symbol()

    def is_tie(self):
        return not any(0 in row for row in self.board)

    def set_winner(self):
        w = self.look_for_winner()
        if w > 0:
            self.winner = self.player_x if w == 1 else self.player_o
            self.winner.add_win()

    def look_for_winner(self):
        for i in range(3):
            if (self.board[i][0] == self.board[i][1] == self.board[i][2]) and self.board[i][0] != 0:
                return self.board[i][0]
            if (self.board[0][i] == self.board[1][i] == self.board[2][i]) and self.board[0][i] != 0:
                return self.board[0][i]
        if (self.board[0][0] == self.board[1][1] == self.board[2][2]) and self.board[1][1] != 0:
            return self.board[1][1]
        if (self.board[0][2] == self.board[1][1] == self.board[2][0]) and self.board[1][1] != 0:
            return self.board[1][1]
        return 0


