from board import Board
from player import Player, Bot

class Game:
    def __init__(self, player_mode):
        self.board = Board()
        self.player1 = Player("X")
        self.current_player = self.player1
        self.player2 = Bot("O") if player_mode == 1 else Player("O")

    def switch_player(self):
        self.current_player = self.player2 if self.current_player == self.player1 else self.player1

    def play(self):
        while True:
            self.board.print_board()
            row, col = self.current_player.get_move()

            if self.board.board[row][col] is not None:
                print("Cell already taken, try again.")
                continue

            self.board.update_board(row, col, self.current_player.symbol)
            winner = self.board.check_winner()

            if winner or self.board.is_full():
                break

            self.switch_player()

        self.board.print_board()
        if winner:
            print(f"Winner is {winner}")
        else:
            print("It's a draw!")
