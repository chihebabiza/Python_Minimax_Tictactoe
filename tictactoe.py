"""
Tic Tac Toe Player
"""

import copy
import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]


def is_valid_board(board):
    if len(board) != 3:
        return False
    for row in board:
        if len(row) != 3:
            return False
        for cell in row:
            if cell not in (X, O, EMPTY):
                return False
    return True


def validate_board(board):
    """Raise exception if board is invalid"""
    if not is_valid_board(board):
        raise Exception("Invalid board! Must be 3x3 with X, O, or EMPTY.")


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    validate_board(board)

    X_Count = sum(row.count(X) for row in board)
    O_Count = sum(row.count(O) for row in board)

    if X_Count > O_Count:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    validate_board(board)

    possible_actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_actions.add((i, j))
    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    validate_board(board)

    if action not in actions(board):
        raise Exception("Invalid action")

    new_board = copy.deepcopy(board)
    i, j = action
    new_board[i][j] = player(board)
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    validate_board(board)

    for row in board:
        if row[0] == row[1] == row[2] != EMPTY:
            return row[0]

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != EMPTY:
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    validate_board(board)

    if winner(board) is not None:
        return True

    if all(cell != EMPTY for row in board for cell in row):
        return True

    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    validate_board(board)

    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal move for the current player.
    """
    validate_board(board)

    if terminal(board):
        return None

    turn = player(board)
    best_action = None

    def max_value(state, alpha, beta):
        if terminal(state):
            return utility(state)
        v = -math.inf
        for action in actions(state):
            v = max(v, min_value(result(state, action), alpha, beta))
            if v >= beta:
                return v
            alpha = max(alpha, v)
        return v

    def min_value(state, alpha, beta):
        if terminal(state):
            return utility(state)
        v = math.inf
        for action in actions(state):
            v = min(v, max_value(result(state, action), alpha, beta))
            if v <= alpha:
                return v
            beta = min(beta, v)
        return v

    if turn == X:
        best_score = -math.inf
        alpha = -math.inf
        beta = math.inf
        for action in actions(board):
            score = min_value(result(board, action), alpha, beta)
            if score > best_score:
                best_score = score
                best_action = action
            alpha = max(alpha, best_score)
    else:
        best_score = math.inf
        alpha = -math.inf
        beta = math.inf
        for action in actions(board):
            score = max_value(result(board, action), alpha, beta)
            if score < best_score:
                best_score = score
                best_action = action
            beta = min(beta, best_score)

    return best_action
