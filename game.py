import os
import csv
from datetime import datetime
from board import Board
from player import Player, Bot

class Game:
    def __init__(self, player_mode):
        self.board = Board()
        self.player1 = Player("X")
        self.current_player = self.player1
        self.player2 = Bot("O") if player_mode == 1 else Player("O")
        self.move_count = {'X': [], 'O': []}  # Initialize move history here


    def switch_player(self):
        self.current_player = self.player2 if self.current_player == self.player1 else self.player1

    def play(self):
        winner = None
        while True:
            self.board.print_board()
            row, col = self.current_player.get_move()

            if self.board.board[row][col] is not None:
                print("Cell already taken, try again.")
                continue

            self.board.update_board(row, col, self.current_player.symbol)
            winner = self.board.check_winner()
            self.move_count[self.current_player.symbol].append((row, col))


            if winner or self.board.is_full():
                self.log_game_result(winner) 
                break
            self.switch_player()

        self.board.print_board()
        if winner:
            print(f"Winner is {winner}")
        else:
            print("It's a draw!")

    def log_game_result(self, winner):
        log_dir = 'logs'
        if not os.path.exists(log_dir):  # Create the directory if it does not exist
            os.makedirs(log_dir)
        log_file = os.path.join(log_dir, 'game_logs.csv')  # Use the full path for the log file
        log_exists = os.path.exists(log_file)
        player_o_type = 'Bot' if isinstance(self.player2, Bot) else 'Human'
        if not log_exists:
            print('Creating new log file')
            with open(log_file, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Timestamp', 'Winner', 'Player X Moves', 'Player O Moves', 'Player O Type'])
        with open(log_file, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([
                datetime.now(), 
                winner, 
                self.move_count['X'], 
                self.move_count['O'], 
                player_o_type
            ])