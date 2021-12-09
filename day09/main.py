def read_input_to_list(path):
    lines = []
    with open(path) as file:
        for line in file:
            lines.append([int(x) for x in line.rstrip()])

    return lines


def is_low(board, row, col):
    is_low = True
    if row != 0:
        is_low = is_low and board[row - 1][col] > board[row][col]
    if row != len(board) - 1:
        is_low = is_low and board[row + 1][col] > board[row][col]
    if col != 0:
        is_low = is_low and board[row][col - 1] > board[row][col]
    if col != len(board[row]) - 1:
        is_low = is_low and board[row][col + 1] > board[row][col]
    return is_low


def get_basin_size(board, row, col):
    if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
        return 0
    if board[row][col] == 9 or board[row][col] == -2:
        return 0
    else:
        board[row][col] = -2
        return 1 + get_basin_size(board, row + 1, col) + get_basin_size(
            board, row - 1, col) + get_basin_size(
                board, row, col + 1) + get_basin_size(board, row, col - 1)


def get_lows(board):
    sum_lows = 0
    for r in range(len(board)):
        for c in range(len(board[r])):
            if board[r][c] != 9 and board[r][c] != -1:
                if is_low(board, r, c):
                    sum_lows += board[r][c] + 1

    return sum_lows


def get_basins(board):
    basins = []
    for r in range(len(board)):
        for c in range(len(board[r])):
            if board[r][c] != 9 and board[r][c] != -1:
                if is_low(board, r, c):
                    size = get_basin_size(board, r, c)
                    basins.append(size)

    basins.sort(reverse=True)

    return basins[0] * basins[1] * basins[2]


def main():
    inputs = read_input_to_list('input.txt')
    print(get_basins(inputs))
    return


main()
