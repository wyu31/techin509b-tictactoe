# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

from logic import make_empty_board, get_winner, other_player


def print_board(board):
    """Prints the current state of the board."""
    for row in board:
        print("|".join(cell if cell is not None else " " for cell in row))
        print("-" * 5)


def get_move():
    """Gets a valid move from the player."""
    while True:
        move = input("Enter your move (row, column): ")
        try:
            row, column = map(int, move.split(","))
            ## transfer the computer language to human language of numbers
            return row-1, column-1
        except ValueError:
            print("Invalid move. Please enter row and column separated by a comma.")


def update_board(board, player, row, column):
    """Updates the board with the player's move."""
    if board[row][column] is None:
        board[row][column] = player
    else:
        print("Invalid move. That cell is already occupied.")


# Reminder to check all the tests

if __name__ == '__main__':
    board = make_empty_board()
    winner = None
    player = 'X'
    while winner is None:
        print_board(board)
        print(f"Player {player}'s turn")
        row, column = get_move()
        update_board(board, player, row, column)
        winner = get_winner(board)
        player = other_player(player)
    print_board(board)
    print(f"Player {winner} wins!")
