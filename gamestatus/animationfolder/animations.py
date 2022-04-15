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


if __name__ == '__main__':
    loading_bar()
    print_board()
