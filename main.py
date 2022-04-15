"""
Game of connect four should function by alternating turns !done
Test suite to make sure there are no invalid inputs !done
Refactor for convenience !done
"""
from gamestatus.statuschecker import check_game
from gamestatus.droppiece import drop_piece
from gamestatus.board.theboard import *


def print_board():
    print("".join(cols_list))
    for row in board:
        print("".join(board_divider))
        print("".join(row) + "|")
    print("".join(board_divider))


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

