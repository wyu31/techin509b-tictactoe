import random

class Player:
    def __init__(self, symbol):
        self.symbol = symbol

    def get_move(self):
        player_input = input(f"Player {self.symbol} > ")
        row, col = map(int, player_input.split(","))
        return row, col


class Bot(Player):
    def get_move(self):
        row, col = random.randint(0, 2), random.randint(0, 2)
        return row, col
