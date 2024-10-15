import math

# define Python user-defined exceptions
class invalidAction(Exception):
    "Raised when the action is invalid"
    pass

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
    Returns which player's turn it is.
    """
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)

    # If X has made the same or more moves than O, it's O's turn
    if x_count > o_count:
        return O
    else:
        return X

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    return [(x, y) for x in range(3) for y in range(3) if board[x][y] == EMPTY]

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # Rozpakowanie krotki action (x, y)
    x, y = action

    if board[x][y] != EMPTY:
        raise invalidAction("This action is not possible!")

    # Tworzenie kopii planszy
    new_board = [row.copy() for row in board]  
    new_board[x][y] = player(board)  # Umieszczanie ruchu na nowej planszy
    return new_board



def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] is not None:
            return row[0]

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] is not None:
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        return board[0][2]

    # No winner yet
    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    return winner(board) is not None or actions(board) == []

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    current_player = player(board)

    if current_player == X:  # Maximizing player
        best_value = -math.inf
        best_action = None
        for action in actions(board):
            simulated_board = result(board, action)
            value = minimax_value(simulated_board)
            if value > best_value:
                best_value = value
                best_action = action
        return best_action

    else:  # Minimizing player
        best_value = math.inf
        best_action = None
        for action in actions(board):
            simulated_board = result(board, action)
            value = minimax_value(simulated_board)
            if value < best_value:
                best_value = value
                best_action = action
        return best_action

def minimax_value(board):
    """
    Returns the minimax value for the board.
    """
    if terminal(board):
        return utility(board)

    current_player = player(board)

    if current_player == X:  # Maximizing player
        best_value = -math.inf
        for action in actions(board):
            simulated_board = result(board, action)
            value = minimax_value(simulated_board)
            best_value = max(best_value, value)
        return best_value

    else:  # Minimizing player
        best_value = math.inf
        for action in actions(board):
            simulated_board = result(board, action)
            value = minimax_value(simulated_board)
            best_value = min(best_value, value)
        return best_value