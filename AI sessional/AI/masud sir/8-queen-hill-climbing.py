N = 8

def print_board(board):
    for row in board:
        print(" ".join("Q" if x else "." for x in row))
    print()

def is_safe(board, row, col):
    # Check this column
    for i in range(row):
        if board[i][col]:
            return False
    # Check upper left diagonal
    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if board[i][j]:
            return False
    # Check upper right diagonal
    for i, j in zip(range(row-1, -1, -1), range(col+1, N)):
        if board[i][j]:
            return False
    return True

def solve(board, row=0):
    if row == N:
        print_board(board)  # Found a solution
        return
    for col in range(N):
        if is_safe(board, row, col):
            board[row][col] = 1
            solve(board, row+1)
            board[row][col] = 0  # backtrack

# Run
board = [[0]*N for _ in range(N)]
solve(board)
