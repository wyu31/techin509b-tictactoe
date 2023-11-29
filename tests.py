import unittest
import logs.logic as logic


class TestLogic(unittest.TestCase):

    def test_get_winner(self):
        board = [
            ['X', None, 'O'],
            [None, 'X', None],
            [None, 'O', 'X'],
        ]
        self.assertEqual(logic.get_winner(board), 'X')

    def test_other_player(self):
        self.assertEqual(logic.other_player('X'), 'O')
        self.assertEqual(logic.other_player('O'), 'X')

    def test_make_empty_board(self):
        expected_board = [
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ]
        self.assertEqual(logic.make_empty_board(), expected_board)


if __name__ == '__main__':
    unittest.main()