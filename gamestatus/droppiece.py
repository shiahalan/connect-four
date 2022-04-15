from gamestatus.board.theboard import *


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


if __name__ == '__main__':
    drop_piece()
