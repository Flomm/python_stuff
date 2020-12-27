import random
from IPython.display import clear_output


def display_board(board):
    clear_output()
    print(f'_________________________')
    print("|       |       |       |")
    print(f'|   {board[7]}   |   {board[8]}   |   {board[9]}   |')
    print("|       |       |       |")
    print(f'-------------------------')
    print("|       |       |       |")
    print(f'|   {board[4]}   |   {board[5]}   |   {board[6]}   |')
    print("|       |       |       |")
    print(f'-------------------------')
    print("|       |       |       |")
    print(f'|   {board[1]}   |   {board[2]}   |   {board[3]}   |')
    print("|       |       |       |")
    print(f'_________________________')


def player_input():
    symbol = " "

    while not (symbol == "X" or symbol == "O"):
        symbol = input(
            "Which symbol would you like to play for? X or O? ").upper()

    if symbol == "X":
        return ("X", "O")

    else:
        return ("O", "X")


def player_choice(board):
    position = 0
    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(
            input("Where would you like to put the next symbol? 1-9? "))
    return position


def place_symbol(board, symbol, position):
    board[position] = symbol


def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or
            (board[4] == mark and board[5] == mark and board[6] == mark) or
            (board[1] == mark and board[2] == mark and board[3] == mark) or
            (board[7] == mark and board[4] == mark and board[1] == mark) or
            (board[8] == mark and board[5] == mark and board[2] == mark) or
            (board[9] == mark and board[6] == mark and board[3] == mark) or
            (board[7] == mark and board[5] == mark and board[3] == mark) or
            (board[9] == mark and board[5] == mark and board[1] == mark))


def choose_first():
    if random.randint(0, 1) == 0:
        return "Player 1"
    else:
        return "Player 2"


def space_check(board, position):
    return board[position] == " "


def full_board_check(board):
    for n in range(1, 10):
        if space_check(board, n):
            return False
    return True


def replay():
    return input('Do you want to play again? Yes or No: ').lower().startswith('y')
