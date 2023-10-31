"""
Tic Tac Toe Player
"""

import copy

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
    # Count number of moves made by each player
    x_count = 0
    o_count = 0

    for row_i in board:
        for cell_j in row_i:
            if cell_j == X:
                x_count += 1
            elif cell_j == O:
                o_count += 1

    # Return X or O based on count
    if x_count == o_count:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    # Store all actions in a set
    allowed_actions = set()

    # Iterate over board checking for possible actions
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                allowed_actions.add((i, j))
    return allowed_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # Check whether action is possible
    i_row, j_cell = action
    if board[i_row][j_cell] != EMPTY:
        raise ValueError

    # Determine whose turn it is
    turn = player(board)

    # Make a deep.copy of given board
    new_board = copy.deepcopy(board)

    # Perform the action on the new board
    new_board[i_row][j_cell] = turn
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check for winner in horizontal case
    for row in board:
        if row[0] == row [1] == row[2] and row[0] != EMPTY:
            return row[0]

    # Check for winner in vertical case
    for j_cell in range(3):
        if board[0][j_cell] == board[1][j_cell] == board[2][j_cell] and board[0][j_cell] != EMPTY:
            return board[0][j_cell]

    # Check for winner in diagonal case
    if board[1][1] != EMPTY:
        if board[0][0] == board[1][1] == board[2][2]:
            return board[1][1]
        if board[2][0] == board[1][1] == board[0][2]:
            return board[1][1]

    # If no winners
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # Count empty squares left
    empty_count = 0
    for row in board:
        for cell in row:
            if cell == EMPTY:
                empty_count += 1

    # Check for winner or 0 empty squares left
    if winner(board) == X or winner(board) == O or empty_count == 0:
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    # Get the winner or None if None
    won = winner(board)

    if won == X:
        return 1
    elif won == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # If board is a terminal board, return None
    if terminal(board):
        return None

    # Check who the computer is playing as (which is X or O)
    computer = player(board)

    if computer == X:
        # He wants max value
        value, action = max_value(board)
        return action

    elif computer == O:
        # He wants min value
        value, action = min_value(board)
        return action


def max_value(state):
    # Look at psuedocode from lecture
    # Base case:
    if terminal(state):
        return utility(state), None

    # Set value and current best_action
    v = -2
    best_action = None

    # Working up to base case:
    for action in actions(state):
        minimal_value, foo = min_value(result(state, action))
        # If this move is better update variables
        if minimal_value > v:
            v = minimal_value
            best_action = action
            # If already found a optimal solution, dont waste time more finding others and return current action
            if v == 1:
                return v, action

    return v, best_action


def min_value(state):
    # Look at psuedocode from lecture
    # Base case:
    if terminal(state):
        return utility(state), None

    # Set value and current best_action
    v = 2
    best_action = None

    # Working up to base case:
    for action in actions(state):
        maximal_value, foo = max_value(result(state, action))
        # If this move is better update variables
        if maximal_value < v:
            v = maximal_value
            best_action = action
            # If already found a optimal solution, dont waste time more finding others and return current action
            if v == -1:
                return v, action

    return v, best_action
