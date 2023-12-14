from copy import deepcopy

with open("input.txt") as infile:
    lines = [list(s) for s in infile.read().splitlines()]

def rotate_clockwise(board):
    rows = len(board)
    cols = len(board[0])
    board = [ [ board[rows - row - 1][col] for row in range(rows)] for col in range(cols) ]
    return board

def tilt_board(board):
    rows = len(board)
    cols = len(board[0])

    for col in range(cols):
        empty_row = 0
        for row in range(rows):
            chr = board[row][col]
            if chr == '#':
                empty_row = row + 1
            elif chr == 'O':
                if empty_row < row:
                    board[empty_row][col] = 'O'
                    board[row][col] = '.'
                empty_row += 1
    return board

def get_load(board):
    rows = len(board)
    cols = len(board[0])
    col_load = 0
    for col in range(cols):
        for row in range(rows):
            if board[row][col] == 'O':
                col_load += rows - row
    return col_load

def spin(orig_board):
    board = deepcopy(orig_board)
    for _ in range(4):
        board = tilt_board(board)
        board = rotate_clockwise(board)
    return board

def hash_board(board):
    rows = len(board)
    cols = len(board[0])
    hash = 0
    for row in range(rows):
        for col in range(cols):
            if board[row][col] == 'O':
                hash += 1
            hash <<= 2
    return hash

board = lines

board_to_spins = {}

TARGET = 10 ** 9
for spins in range(1, TARGET + 1):
    board = spin(board)
    hash = hash_board(board)
    prev_spins = board_to_spins.get(hash, 0)
    if prev_spins == 0:
        board_to_spins[hash] = spins
    else:
        period = spins - prev_spins
        print(f"Board seen at {prev_spins} and {spins} -> period is {period}")
        target_rem = TARGET % period
        print(f"Target remainder is {TARGET} mod {period} = {target_rem}")
        while spins % period != target_rem:
            spins += 1
            board = spin(board)
        print(f"At {spins} spins, remainder is {spins % period}, and load is {get_load(board)}")
        break


