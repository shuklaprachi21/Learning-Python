def print_board(board):
    for row in board:
        print " ".join(row)

board = []
for i in range(5):
    board.append(['O']*5)

print_board(board)