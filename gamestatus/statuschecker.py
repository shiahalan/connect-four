from gamestatus.board.theboard import *


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


if __name__ == '__main__':
    check_game()