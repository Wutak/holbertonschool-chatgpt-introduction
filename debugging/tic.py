#!/usr/bin/python3

def print_board(board):
    """
    Prints the current state of the board in a user_friendly format.
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    """
    Checks if there is a winner on the board.
    Parameters:
    board(list): The current state of the board.
    Returns:
    bool: True  if there is a winner, False otherwise.
    """
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        retur True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def is_full(board):
    """
    Checks if the board is full, indicating a draw.
    Parameters:
    board (list): The current state of the board.
    Returns:
    bool: True if the board is full, False otherwise.
    """
    for row in board:
        if " " in row:
            return False
        return True

def ttic_tac_toe():
    """
    Main fucntion to play a game of Tic-Tac-Toe.
    """
    board = [[" "] * 3 for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)

        try:
            row = int(input(f"Enter row (0, 1, or 2) for player {current_player}: "))
            col = int(input(f"Enter column (0, 1, or 2) for player {current_player}: "))
            if row not in range(3) or col not in range(3):
                print("Invalid input! Row and column must be 0, 1, or 2. Try again.")
                continue
        except ValueError:
            print("Invalid input! Please enter nu;ners only. Try again.")
            continue

        if board[row][col] != " ":
            print("That spot is already taken! Try again.")
            continue

        board[row][col] = current_player

        if check_winner(board):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        if is_full(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"

if __name__  == "__name__":
    tic_tac_toe()
