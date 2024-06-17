"""
Tic Tac Toe Player
"""

import math
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
    # Count the number of the Xs and the number of O's
    # If equal, it's the turn of X. If X is more than O, then it is X
    x_count = sum(x.count(X) for x in board)
    o_count = sum(x.count(O) for x in board)

    if x_count == o_count:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    # We can assume the board is valid
    # Loop over all the rows in the board
    possible_actions = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_actions.append((i, j))
    return set(possible_actions)





def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = copy.deepcopy(board)
    i = action[0]
    j = action[1]
    if new_board[i][j] != EMPTY:
        raise ValueError
    if i >= 3 or j >= 3 or i < 0 or j < 0:
        raise ValueError
    new_board[i][j] = player(board)
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check rows
    for row in board:
        if len(set(row)) == 1 and row[0] is not None:
            return row[0]
        
    # col_0 = [board[i][0] for i in range(len(board))] 
    # col_1 = [board[i][1] for i in range(len(board))] 
    # col_2 = [board[i][2] for i in range(len(board))]

    # Check columns
    for j in range(len(board)):
        col = [board[i][j] for i in range(len(board))]
        if len(set(col)) == 1 and col[0] is not None:
            return col[0]
    

    # Check Diagonals
    diagonals = [
        [board[i][i] for i in range(len(board))], 
        [board[i][len(board) - 1 - i] for i in range(len(board))]
        ]
    for d in diagonals:
        if len(set(d)) == 1 and d[0] is not None:
            return d[0]
        
    # Return None if there is no winner
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    for row in board:
        if None in row:
            return False
        
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    w = winner(board)
    if w == X:
        return 1
    elif w == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    
    def max_value(b):
        v = -100
        if terminal(b):
            return(utility(b))
        for action in actions(b):
            v = max(v, min_value(result(b, action)))
        return v
    
    def min_value(b):
        v = 100
        # If we have a terminal state we return the utility of the state
        if terminal(b):
            return(utility(b))
        # Set v to be a high value first because we will be trying to minimize
        for action in actions(b):
            # Assume that out of all the actions you take, opp will be optimal
            # Then find the path that has the minimum endgoal
            v = min(v, max_value(result(b, action)))
        return v
    
    
    
    # Find out who is the current player
    # Get the moves available to them
    # If max agent, pick the move with the highest min_value

    if player(board) == X:
        outcomes = [
            (action, min_value(result(board, action))) 
            for action in actions(board)
            ]
        sorted_outcomes = sorted(outcomes, key=lambda x : x[1])
        return sorted_outcomes[-1][0]
    else:
        outcomes = [
            (action, max_value(result(board, action))) 
            for action in actions(board)
            ]
        sorted_outcomes = sorted(outcomes, key=lambda x : x[1])
        return sorted_outcomes[0][0]




  