def make_empty_board():
    return [
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ]


def get_winner(board):
    """Determines the winner of the given board.
    Returns 'X', 'O', or None."""
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] is not None:
            return row[0]

    # Check columns
    for column in range(3):
        if board[0][column] == board[1][column] == board[2][column] and board[0][column] is not None:
            return board[0][column]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        return board[0][2]

    # No winner
    return None


def other_player(player):
    """Given the character for a player, returns the other player."""
    return 'O' if player == 'X' else 'X'
