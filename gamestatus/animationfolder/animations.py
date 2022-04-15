from time import sleep
from gamestatus.board.theboard import *


def loading_bar():
    print('Loading...')
    for i in range(50):
        bar = "[" + "+" * i + "-" * (49 - i) + "]"
        sleep(0.08)
        print(f'\r{bar}', end='')


def print_board():
    print("".join(cols_list))
    for row in board:
        print("".join(board_divider))
        print("".join(row) + "|")
    print("".join(board_divider))


def drop_piece_anim(col, piece):
    p = piece
    for row in board:
        if row[col-1] == "|   ":
            row[col - 1] = f'| {p} '
            print_board()
            sleep(0.3)
            print('\n' * 100)
            row[col-1] = '|   '
        else:
            board[board.index(row)-1][col-1] = f"| {piece.upper()} "
            break
    if board[5][col-1] == '|   ':
        row[col - 1] = f'| {piece.upper()} '
    print_board()


if __name__ == '__main__':
    loading_bar()
    print_board()
    drop_piece_anim()
