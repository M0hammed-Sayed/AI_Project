import copy
import math



# Constants
EMPTY = 0
PLAYER_X = 1
PLAYER_O = 2
BLACK = 1
WHITE = 2
WKING = 3
BKING = 4
Capture = 0
# Board size
ROWS = 8
COLS = 8

# Initialize the board
board = [
    [0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [2, 0, 2, 0, 2, 0, 2, 0],
    [0, 2, 0, 2, 0, 2, 0, 2],
    [2, 0, 2, 0, 2, 0, 2, 0]
]

# Function to print the board
def print_board(board):
    print("   A B C D E F G H")
    print("  ----------------")
    for i in range(8):
        print(i + 1, "|", end="  ")
        for j in range(8):
            piece = board[i][j]
            if piece == EMPTY:
                print(".", end="  ")
            elif piece == BLACK:
                print("B", end="  ")
            elif piece == WHITE:
                print("W", end="  ")
            elif piece == WKING:
                print("WK", end="  ")
            elif piece == BKING:
                print("BK", end="  ")    
        print()
    print()

# Function to check if a move is valid
def is_valid_move(board, player, start_row, start_col, end_row, end_col):
    # Check if the start and end positions are within the board
    if not (0 <= start_row < ROWS and 0 <= start_col < COLS and 0 <= end_row < ROWS and 0 <= end_col < COLS):
        return False

    # Check if the end position is empty
    if board[end_row][end_col] != EMPTY:
        return False

    # Check if the move is a single step or a capture move
    if abs(start_row - end_row) == 1:
        # Single step move
        if player == BLACK and start_row > end_row:
            return False
        if player == WHITE and start_row < end_row:
            return False
        return True
    elif abs(start_row - end_row) == 2 and abs(start_col - end_col) == 2:
        # Capture move
        middle_row = (start_row + end_row) // 2
        middle_col = (start_col + end_col) // 2
        if player == BLACK and (start_row > end_row or board[middle_row][middle_col] != WHITE):
            return False
        if player == WHITE and (start_row < end_row or board[middle_row][middle_col] != BLACK):
            return False
        return True

    return False

# Function to make a move
def make_move(board, player, start_row, start_col, end_row, end_col):
    if (player == BLACK and end_row == 7):
        board[end_row][end_col] = BKING
        board[start_row][start_col] = EMPTY 
    elif (player == WHITE and end_row == 0):
        board[end_row][end_col] = WKING
        board[start_row][start_col] = EMPTY
    else :
        board[end_row][end_col] = player
        board[start_row][start_col] = EMPTY   
    # Check if it's a capture move and remove the captured piece
    if abs(start_row - end_row) == 2 and abs(start_col - end_col) == 2:
        middle_row = (start_row + end_row) // 2
        middle_col = (start_col + end_col) // 2
        board[middle_row][middle_col] = EMPTY

# Function to generate all possible moves for a player
def generate_moves(board, player):
    moves = []
    for row in range(ROWS):
        for col in range(COLS):
            if board[row][col] == player:
                if player == WHITE:
                    # Check forward left
                    if is_valid_move(board, player, row, col, row - 1, col - 1):
                        moves.append((WHITE,row, col, row - 1, col - 1,0))
                    # Check forward right
                    if is_valid_move(board, player, row, col, row - 1, col + 1):
                        moves.append((WHITE,row, col, row - 1, col + 1,0))
                    # Check capture left
                    if is_valid_move(board, player, row, col, row - 2, col - 2):
                        moves.append((WHITE,row, col, row - 2, col - 2,0))
                    # Check capture right
                    if is_valid_move(board, player, row, col, row - 2, col + 2):
                        moves.append((WHITE,row, col, row - 2, col + 2,0))
                elif player == BLACK:
                    # Check forward left
                    if is_valid_move(board, player, row, col, row + 1, col - 1):
                        moves.append((BLACK,row, col, row + 1, col - 1,1))
                    # Check forward right
                    if is_valid_move(board, player, row, col, row + 1, col + 1):
                        moves.append((BLACK,row, col, row + 1, col + 1,1))
                    # Check capture left
                    if is_valid_move(board, player, row, col, row + 2, col - 2):
                        moves.append((BLACK,row, col, row + 2, col - 2,5))
                    # Check capture right
                    if is_valid_move(board, player, row, col, row + 2, col + 2):
                        moves.append((BLACK,row, col, row + 2, col + 2,5))
                elif player == WKING:
                    # Check forward left
                    if is_valid_move(board, player, row, col, row - 1, col - 1):
                        moves.append((WKING,row, col, row - 1, col - 1,0))
                    # Check forward right
                    if is_valid_move(board, player, row, col, row - 1, col + 1):
                        moves.append((WKING,row, col, row - 1, col + 1,0))
                    # Check capture left
                    if is_valid_move(board, player, row, col, row - 2, col - 2):
                        moves.append((WKING,row, col, row - 2, col - 2,7))
                    # Check capture right
                    if is_valid_move(board, player, row, col, row - 2, col + 2):
                        moves.append((WKING,row, col, row - 2, col + 2,7))
# back moves and captures....................................................................
                    # Check back left
                    if is_valid_move(board, player, row, col, row + 1, col - 1):
                        moves.append((WKING,row, col, row + 1, col - 1,0))
                    # Check back right
                    if is_valid_move(board, player, row, col, row + 1, col + 1):
                        moves.append((WKING,row, col, row + 1, col + 1,0))
                    # Check back left
                    if is_valid_move(board, player, row, col, row + 2, col - 2):
                        moves.append((WKING,row, col, row + 2, col - 2,7))
                    # Check back right
                    if is_valid_move(board, player, row, col, row + 2, col + 2):
                        moves.append((WKING,row, col, row + 2, col + 2,7))            
                elif player == BKING:
                    # Check forward left
                    if is_valid_move(board, player, row, col, row + 1, col - 1):
                        moves.append((BKING,row, col, row + 1, col - 1,1))
                    # Check forward right
                    if is_valid_move(board, player, row, col, row + 1, col + 1):
                        moves.append((BKING,row, col, row + 1, col + 1,1))
                    # Check capture left
                    if is_valid_move(board, player, row, col, row + 2, col - 2):
                        moves.append((BKING,row, col, row + 2, col - 2,6))
                    # Check capture right
                    if is_valid_move(board, player, row, col, row + 2, col + 2):
                        moves.append((BKING,row, col, row + 2, col + 2,6))
# back moves and captures...................................................................                
                # Check back left
                    if is_valid_move(board, player, row, col, row - 1, col - 1):
                        moves.append((BKING,row, col, row - 1, col - 1,1))
                    # Check back right
                    if is_valid_move(board, player, row, col, row - 1, col + 1):
                        moves.append((BKING,row, col, row - 1, col + 1,1))
                    # Check capture left
                    if is_valid_move(board, player, row, col, row - 2, col - 2):
                        moves.append((BKING,row, col, row - 2, col - 2,6))
                    # Check capture right
                    if is_valid_move(board, player, row, col, row - 2, col + 2):
                        moves.append((BKING,row, col, row - 2, col + 2,6))
    return moves

# Function to evaluate the board for a player
def evaluate(board,capture, player):
    score = 0
    for row in range(ROWS):
        for col in range(COLS):
            if board[row][col] == player :
                score += 1   
            elif board[row][col] != EMPTY:    
                score -= 1
            if player == BKING:
                score += 10         
            if player == WKING:
                score += -5        
            if capture == 5:
                score += 20
            if capture == 6:
                score += 50 
            if capture == 7:
                score += -5         
    return score
# minmax algorithm
def minimax(board, capture ,player,depth, maximizing_player):
    if depth == 0 or is_game_over(board):
        return evaluate(board,capture,player), None

    if maximizing_player:
        max_eval = -math.inf
        best_move = None
        M = generate_moves(board,BLACK) 
        N = generate_moves(board,BKING)
        if  N:
            for i in range (len(N)):
                M.append(N[i])
        for move in M:
            new_board = copy.deepcopy(board)
            make_move(new_board,move[0],move[1],move[2],move[3],move[4])
            eval, _ = minimax(new_board,move[5],move[0], depth - 1,False)
            if eval > max_eval:
                max_eval = eval
                best_move = move
        return max_eval, best_move
    else:
        min_eval = float('inf')
        best_move = None
        M = generate_moves(board,WHITE) 
        N = generate_moves(board,WKING)
        if  N:
            for i in range (len(N)):
                M.append(N[i])
        for move in M:
            new_board = copy.deepcopy(board)
            make_move(new_board,move[0],move[1],move[2],move[3],move[4])
            eval, _ = minimax(new_board,move[5],move[0], depth - 1,  True)
            if eval < min_eval:
                min_eval = eval
                best_move = move
        return min_eval, best_move
# alpha_beta algorithm with Alpha-Beta pruning
def alpha_beta(board,capture ,player,depth, alpha, beta, maximizing_player):
    if depth == 0 or is_game_over(board):
        return evaluate(board,capture,player), None

    if maximizing_player:
        max_eval = -math.inf
        best_move = None
        M = generate_moves(board,BLACK) 
        N = generate_moves(board,BKING)
        if  N:
            for i in range (len(N)):
                M.append(N[i])
        for move in M:
            new_board = copy.deepcopy(board)
            make_move(new_board,move[0],move[1],move[2],move[3],move[4])
            eval, _ = alpha_beta(new_board,move[5],move[0], depth - 1, alpha, beta, False)
            if eval > max_eval:
                max_eval = eval
                best_move = move
            alpha = max(alpha, eval)
            if alpha >= beta:
                break
        return max_eval, best_move
    else:
        min_eval = float('inf')
        best_move = None
        M = generate_moves(board,WHITE) 
        N = generate_moves(board,WKING)
        if  N:
            for i in range (len(N)):
                M.append(N[i])
        for move in M:
            new_board = copy.deepcopy(board)
            make_move(new_board,move[0],move[1],move[2],move[3],move[4])
            eval, _ = alpha_beta(new_board,move[5],move[0], depth - 1, alpha, beta, True)
            if eval < min_eval:
                min_eval = eval
                best_move = move
            beta = min(beta, eval)
            if alpha >= beta:
                break
        return min_eval, best_move

# Function to check if the game is over
def is_game_over(board):
    # Check if a player has no more pieces
    white_pieces = 0
    black_pieces = 0

    for row in board:
        for piece in row:
            if piece == WHITE or piece == WKING:
                white_pieces += 1
            elif piece == BLACK or piece == BKING :
                black_pieces += 1

    if white_pieces == 0 or black_pieces == 0:
        return True

    return False


# Main game loop
def play_game():
    fun = 0
    lEasy = 4
    lMid = 6
    lHard = 8
    level = lEasy
    current_player = PLAYER_X
    while not is_game_over(board):
        print_board(board)
        if fun == 0:
            
            if current_player == PLAYER_X:
                print("Player Black's turn:")
                # _, move = alpha_beta(board,0,0, 4, float('-inf'), float('inf'), True)
                _, move = minimax(board,0,0, level, True)
            else:
                print("Player White's turn:")
                # _, move = alpha_beta(board,0,0,4, float('-inf'), float('inf'), False)
                _, move = minimax(board,0,0,level, False)
            if move:
                make_move(board, move[0],move[1],move[2],move[3],move[4])
            else:
                print("No valid moves.")
                break

            current_player = PLAYER_O if current_player == PLAYER_X else PLAYER_X

            print_board(board)
        else :
            
            if current_player == PLAYER_X:
                print("Player Black's turn:")
                _, move = alpha_beta(board,0,0, level, float('-inf'), float('inf'), True)
                # _, move = minimax(board,0,0, 4, True)
            else:
                print("Player White's turn:")
                _, move = alpha_beta(board,0,0,level, float('-inf'), float('inf'), False)
                #_, move = minimax(board,0,0,4, False)
            if move:
                make_move(board, move[0],move[1],move[2],move[3],move[4])
            else:
                print("No valid moves.")
                break

            current_player = PLAYER_O if current_player == PLAYER_X else PLAYER_X

            print_board(board)    
    if is_game_over(board):
        score_x = evaluate(board,0,BLACK)
        score_o = evaluate(board,0,WHITE)
        score_w = evaluate(board,0,WKING)
        score_b = evaluate(board,0,BKING)
        if score_x > score_o or score_b > score_w:
            print("Player White wins!")
        elif score_x < score_o or score_b < score_w:
            print("Player Black wins!")
        else:
            print("It's a draw!")

# Start the game
play_game()
