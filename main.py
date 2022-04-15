"""
Game of connect four should function by alternating turns
Test suite to make sure there are no invalid inputs
Refactor for convenience
"""


cols_list = ['  1  ', ' 2  ', ' 3  ', ' 4  ', ' 5  ', ' 6  ', ' 7']
board_divider = ["+---" * 7, "+"]
board = [["|   "] * 7 for i in range(6)]


def print_board():
    print("".join(cols_list))
    for row in board:
        print("".join(board_divider))
        print("".join(row) + "|")
    print("".join(board_divider))


def drop_piece(col, piece):
    if col.isdigit() and (piece.upper() == 'X' or piece.upper() == 'O'):
        column = int(col)
        if 7 >= column >= 1:
            row_number = 5
            for row in board[::-1]:
                if row[column - 1] == "|   ":
                    board[row_number][column - 1] = f"| {piece.upper()} "
                    return True
                row_number -= 1
            print("Out of spaces!")
            return False
        else:
            print("Not in the range of 1-7!")
            return False
    else:
        print("Not a valid input!")
        return False


def check_game(piece):
    p = piece.upper()
    for row in board:  # Check if full
        if "|   " in row:
            break
    else:
        return "It's a tie!"

    for row in board:  # Check if horizontal win
        count = 0
        for position in row:
            if position == f"| {p} ":
                count += 1
                if count >= 4:
                    return f"{p} won!"
            else:
                count = 0

    for col in range(len(board) + 1):  # Check  for vertical win
        count = 0
        for row in range(6):
            if board[row][col] == f"| {p} ":
                count += 1
                if count >= 4:
                    return f"{p} wins!"
            else:
                count = 0

    for row in range(3):  # Check for left slash
        for col in range(3, 7):
            if board[row][col] == f'| {p} ' and board[row + 1][col - 1] == f'| {p} ':
                if board[row + 2][col - 2] == f'| {p} ' and board[row + 3][col - 3] == f'| {p} ':
                    return f"{p} wins!"

    for row in range(3):  # Check for right slash
        for col in range(4):
            if board[row][col] == f'| {p} ' and board[row + 1][col + 1] == f'| {p} ':
                if board[row + 2][col + 2] == f'| {p} ' and board[row + 3][col + 3]:
                    return f"{p} wins!"


def game():
    print("Welcome to connect four!")
    print_board()
    token = 'X'
    while True:
        answered = False
        while not answered:
            if not drop_piece(input('Enter column:'), token):
                pass
            else:
                answered = True
        if check_game(token):
            print(check_game(token))
            print_board()
            break
        if token == 'X':
            token = 'O'
        else:
            token = 'X'
        print_board()


game()

