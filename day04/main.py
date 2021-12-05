def read_input_to_list(path):
    rolls = []
    inputs = ""
    with open(path) as file:
      for line in file:
          inputs = line.split(",")
    roll = []
    for i in inputs:
      roll.append(i)
      if len(roll) == 5:
        rolls.append(roll)
        roll = []
    return rolls


def read_boards(path):
  boards = []
  with open(path) as file:
    board = []
    for line in file:
        temp = (line.strip("\n").split())
        if (len(temp) == 5):
          board.append(temp)
        
        if len(board) == 5:
          boards.append(board)
          board = []

  return boards


def check_win(board, r, c):
  vertical = True
  horizontal = True

  for row in board:
    vertical = row[c] == "X" and vertical
  for col in board[r]:
    horizontal = col == "X" and horizontal

  return vertical or horizontal


def calculate_score(board, num):
  sum = 0
  for row in board:
    for cell in row:
      if (cell != "X"):
        sum += int(cell)
  
  return int(num) * sum 



def bingo_1(inputs, boards):
  for turn in inputs:
    for num in turn:

      for i in range(len(boards)):
        for row in range(len(boards[i])):
          for col in range(len(boards[i][row])): 
            if boards[i][row][col] == num:
              
              boards[i][row][col] = "X"
              if (check_win(boards[i], row, col)):
                return calculate_score(boards[i], num) 
  return 0


def bingo_2(inputs, boards):
  for turn in inputs:
    for num in turn: 
      i = 0
      while ( i < len(boards)): 
        board = boards[i]
        for row in range(len(board)):
          for col in range(len(board[row])):
            if board[row][col] == num:
              board[row][col] = "X"

              if (check_win(board, row, col) and len(boards) != 1):
                boards.pop(i)
                i -= 1
                
              elif (check_win(board, row, col) and len(boards) == 1):
                return calculate_score(board, num) 
            
        i += 1
  return 0


def main():
  inputs = read_input_to_list('input.txt')
  boards = read_boards('boards.txt')
  print(bingo_2(inputs, boards))
  return


main()