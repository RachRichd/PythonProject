import random

def print_board(board):
    print(" +---+---+---+")
    for row in range(len(board)):
        print(" |", end="")
        for col in range(len(board[row])):
            if col > 0:
                print("|", end="")
            print(f" {board[row][col]} ", end="")
        print("|")
        if row < len(board) - 1:
            print(" +---+---+---+")
    print(" +---+---+---+")

def check_winner(board, player):
    for row in board:
        if all(s == player for s in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def get_computer_move(board): 
    available_moves = [(i, j) for i in range(3) for j in range(3) if board[i][j] not in ["X", "O"]] 
    return random.choice(available_moves)

def tic_tac_toe():
    board = [["1", "2", "3"],
             ["4", "5", "6"],
             ["7", "8", "9"]]
    current_player = "O"
    
    for _ in range(9):
        print_board(board)
        
        if current_player == "O": 
           move = input(f"Player {current_player}, enter your move: ")
           move = int(move) - 1 
           row, col = divmod(move, 3) 
        else: 
            row, col = get_computer_move(board)
            print(f"Computer chooses: {row * 3 + col + 1}") 
            
        if board[row][col] in ["X", "O"]: 
            print("This spot is already taken. Try again." 
                  if current_player == "O" 
                  else "Computer tried to choose an invalid move.") 
            continue
            
        board[row][col] = current_player
        
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            return
        
        current_player = "O" if current_player == "X" else "X"
    
    print_board(board)
    print("It's a tie!")

tic_tac_toe()