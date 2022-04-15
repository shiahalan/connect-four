"""
Game of connect four should function by alternating turns !done
Test suite to make sure there are no invalid inputs !done
Refactor for convenience !done
"""
from time import sleep
from gamestatus.statuschecker import check_game
from gamestatus.droppiece import drop_piece
from gamestatus.animationfolder.animations import *


def game():
    sleep(2)
    print_board()
    token = 'X'
    while True:
        answered = False
        while not answered:
            answer = input("Enter column: ")
            if not drop_piece(answer, token):
                pass
            else:
                answered = True
        drop_piece_anim(int(answer), token)
        if check_game(token):
            print(check_game(token))
            break
        if token == 'X':
            token = 'O'
        else:
            token = 'X'


loading_bar()
print()
print("Welcome to...")
sleep(2)
print("""
   ______                            __     ______                
  / ____/___  ____  ____  ___  _____/ /_   / ____/___  __  _______
 / /   / __ \/ __ \/ __ \/ _ \/ ___/ __/  / /_  / __ \/ / / / ___/
/ /___/ /_/ / / / / / / /  __/ /__/ /_   / __/ / /_/ / /_/ / /    
\____/\____/_/ /_/_/ /_/\___/\___/\__/  /_/    \____/\__,_/_/     

    """)


while True:
    sleep(2)
    decision = input("Menu\n[a]Play!\n[b]Quit!\n>")
    if decision.lower() == 'a' or decision.lower() == 'b':
        if decision.lower() == 'a':
            sleep(2)
            game()
        else:
            sleep(1)
            print("See you next time!")
            sleep(2)
            exit()
    else:
        print("---------------")
        print("Invalid option!")
        print("---------------")
        sleep(2)

