import time
import XO_functions as fc

print('Welcome to this epic game!')
time.sleep(1)

while True:
    # Setting the game up
    theBoard = [' '] * 10
    player1_symbol, player2_symbol = fc.player_input()
    turn = fc.choose_first()
    print(f' {turn} starts!')

    play_game = input('Are you ready to play? Yes or No.')

    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:

        if turn == "Player 1":

            fc.display_board(theBoard)
            position = fc.player_choice(theBoard)
            fc.place_symbol(theBoard, player1_symbol, position)

            if fc.win_check(theBoard, player1_symbol):
                fc.display_board(theBoard)
                print('Congrats! Player 1 won!')
                game_on = False

            else:
                if fc.full_board_check(theBoard):
                    fc.display_board(theBoard)
                    print("Tie")
                    break
                else:
                    turn = "Player 2"

        else:
            fc.display_board(theBoard)
            position = fc.player_choice(theBoard)
            fc.place_symbol(theBoard, player2_symbol, position)

            if fc.win_check(theBoard, player2_symbol):
                fc.display_board(theBoard)
                print('Congrats! Player 2 won!')
                game_on = False

            else:
                if fc.full_board_check(theBoard):
                    fc.display_board(theBoard)
                    print("Tie")
                    break
                else:
                    turn = "Player 1"

    if not fc.replay():
        print("The end")
        break
