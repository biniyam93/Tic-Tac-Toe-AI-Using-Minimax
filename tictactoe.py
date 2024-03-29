"""
Tic Tac Toe Player
"""
from copy import deepcopy
import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    count_x = sum(row.count(X) for row in board)
    count_o = sum(row.count(O) for row in board)

    if count_x == count_o:
        return X
    else:
        return O

    #raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()  # Initialize an empty set
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_actions.add((i, j))  # Add each action to the set
    return possible_actions

    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i,j=action

    if action not in actions(board):
        raise NotImplementedError

    new_board = deepcopy(board)
    new_board[i][j] = player(board)
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for row in board:
        if all(element == X for element in row):
            return X
        elif all(element == O for element in row):
            return O

    for j in range(3):
        column = [board[i][j] for i in range(3)]
        if all(element == X for element in column):
            return X
        elif all(element == O for element in column):
            return O

    first_diagonal = [board[i][i] for i in range(3)]
    if all(cell == X for cell in first_diagonal):
        return X
    elif all(cell == O for cell in first_diagonal):
        return O

    second_diagonal = [board[i][2 - i] for i in range(3)]
    if all(cell == X for cell in second_diagonal):
        return X
    elif all(cell == O for cell in second_diagonal):
        return O

    return None
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    return winner(board) is not None or all(all(cell != EMPTY for cell in row) for row in board)

    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board):

        if(winner(board)==X):
            return 1

        elif(winner(board)==O):
            return -1
        else:
            return 0
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    def max_value(board):
        if terminal(board):
            return utility(board)
        v = float("-inf")
        for action in actions(board):
            v = max(v, min_value(result(board, action)))
        return v

    def min_value(board):
        if terminal(board):
            return utility(board)
        v = float("inf")
        for action in actions(board):
            v = min(v, max_value(result(board, action)))
        return v

    if terminal(board):  # If the game is over
        return None
    
    best_action = None
    best_value = float("-inf") if player(board) == X else float("inf")

    for action in actions(board):
        new_board = result(board, action)
        value = min_value(new_board) if player(board) == X else max_value(new_board)

        if player(board) == X:
            if value > best_value:
                best_value = value
                best_action = action
        else:
            if value < best_value:
                best_value = value
                best_action = action

    return best_action
