import unittest
from unittest.mock import patch
from board import Board
from player import Player, Bot
from game import Game 

class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_initial_board_empty(self):
        for row in self.board.board:
            self.assertTrue(all(cell is None for cell in row), "Initial board should be empty.")

    def test_update_board(self):
        self.board.update_board(0, 0, 'X')
        self.assertEqual(self.board.board[0][0], 'X', "Board update failed.")

    def test_board_full(self):
        for i in range(3):
            for j in range(3):
                self.board.update_board(i, j, 'X')
        self.assertTrue(self.board.is_full(), "Board should be full.")

    def test_board_not_full(self):
        self.board.update_board(0, 0, 'X')
        self.assertFalse(self.board.is_full(), "Board should not be full.")

    def test_check_winner_rows(self):
        self.board.board = [['X', 'X', 'X'], [None, None, None], [None, None, None]]
        self.assertEqual(self.board.check_winner(), 'X', "Row winner check failed.")

    def test_check_winner_columns(self):
        self.board.board = [['X', None, None], ['X', None, None], ['X', None, None]]
        self.assertEqual(self.board.check_winner(), 'X', "Column winner check failed.")

    def test_check_winner_diagonals(self):
        self.board.board = [['X', None, None], [None, 'X', None], [None, None, 'X']]
        self.assertEqual(self.board.check_winner(), 'X', "Diagonal winner check failed.")

    def test_no_winner(self):
        self.assertIsNone(self.board.check_winner(), "Should be no winner.")

class TestPlayer(unittest.TestCase):
    def test_player_symbol(self):
        player = Player('X')
        self.assertEqual(player.symbol, 'X', "Player symbol incorrect.")

    # Mocking input for player move
    @patch('builtins.input', return_value='0,0')
    def test_get_move(self, mocked_input):
        player = Player('X')
        move = player.get_move()
        self.assertEqual(move, (0, 0), "Player move incorrect.")

class TestBot(unittest.TestCase):
    def setUp(self):
        self.bot = Bot('O')

    def test_bot_symbol(self):
        self.assertEqual(self.bot.symbol, 'O', "Bot symbol incorrect.")

    def test_bot_move(self):
        move = self.bot.get_move()
        self.assertIsInstance(move, tuple, "Bot move should be a tuple.")
        self.assertEqual(len(move), 2, "Bot move should have two elements.")
        self.assertTrue(all(0 <= x <= 2 for x in move), "Bot move out of range.")

class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game(player_mode=1)

    def test_initial_current_player(self):
        self.assertIsInstance(self.game.current_player, Player, "Initial current player should be a Player instance.")

    def test_switch_player(self):
        first_player = self.game.current_player
        self.game.switch_player()
        self.assertNotEqual(first_player, self.game.current_player, "Switch player failed.")


if __name__ == '__main__':
    unittest.main()

