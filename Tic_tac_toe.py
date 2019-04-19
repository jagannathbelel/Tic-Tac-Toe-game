# tic tac toe game 3X3 creted by jagannath Belel

# step 1

def display_board(board):
    '''
    function to display board as number on a numpad
    printing out the board for 3X3
    taking input as an list
    '''
  
    print(board[7] + '|' + board[8] + '|' + board[9])
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(board[1] + '|' + board[2] + '|' + board[3])
    
# step 2 funcion to take input 

def input_player():

    '''
    taking input from user for staring X or O
    '''
    marker = '' # created an empty string

    while marker != 'X' and marker != 'O':
        marker = input(' P1 chose X or O ').upper() # upper() is used
     
    if marker == 'X':
        return('X','O')
    else:
        return ('O','X')

# step 3 function for player input position

def input_position(board, marker, position):
    '''
    input for position on the board id taken 
    3 argumes are passed board, marker=X or O ,positon(1-9)
    '''
    board[position] = marker 

# step 4 winning function

def win_check(board,mark):
    '''
    wining function is checked in all ways
    if not empty will be added later on
    '''

    # to check for row
    return ((board[1] == mark and board[2] == mark and board[3] == mark) or
    (board[4] == mark and board[5] == mark and board[6] == mark) or 
    (board[7] == mark and board[8] == mark and board[9] == mark) or

    # to check for column

    (board[1] == mark and board[4] == mark and board[7] == mark) or
    (board[2] == mark and board[5] == mark and board[8] == mark) or
    (board[3] == mark and board[6] == mark and board[9] == mark) or

    # to check for diagonal

    (board[1] == mark and board[5] == mark and board[9] == mark) or
    (board[3] == mark and board[5] == mark and board[7] == mark) )

# step 5 to randomly select the first player

import random # to used randint()

def select_first():
    '''
    To select Player1 or Player2 will play first
    it select randomly
    '''
    if random.randint(0,1) == 0:
        return 'Player1'
    else:
        return 'Player2'

# step 6 to check of board is empty 

def check_empty(board,position):
    '''
    to cheque if the board is empty or  not
    '''
    return board[position] == ' '
    
# step 7 to check if board is full 

def check_board_full(board):
    '''
    to cheque if the board id full 
    '''

    for i in range(1,10):
        if check_empty(board,i):
            return False
        # if full     
    return True

# step 8 players next choise

def player_choice(board):
    '''
    to take position from player ftom (1 to 9) and check if its empty 
    '''
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not check_empty(board, position):
        position = int(input('Choose your next position: (1-9) '))
        return position

# to ask player if they want to continue or not

def replay():
    '''
    to replay the game again or not 
    '''
    return input('Want to play again Yes or No ') == 'Yes'
  
# final game  main

print('Welcome to TIC TAC ToE')

while True:

    the_board = [' ']*10    
    player1_m, player2_m = input_player()   
    turn = select_first() 
    print(turn + ' Will be first ')
    play_game = input('Want to start the game press yes or no ')

    if play_game == 'y':
        game_on = True
    else:
        game_on = False

    # Game play

    while game_on:

        # player1 chance
        if turn  == 'Player1':
            display_board(the_board)    #display the board
            position = player_choice(the_board) # chose a position 
            input_position(the_board, player1_m, position)  #place the input/marker on the board 

            # check if it win

            if win_check(the_board,player1_m):
                display_board(the_board)
                print('P1 has wone the game')
                game_on = False
                
            else:
                if check_board_full(the_board):
                    display_board(the_board)
                    print('tie')
                    game_on = False
                else:
                    turn = 'Player2'
                      
        #player 2 chance
        else:
            
            if turn  == 'Player2':
                display_board(the_board)  #display the board
                position = player_choice(the_board)     # chose a position 
                input_position(the_board,player2_m,position)    #place the input/marker on the board 

            if win_check(the_board,player2_m):
                display_board(the_board)
                print('P2 has wone the game')
                game_on = False
            else:
                if check_board_full(the_board):
                    display_board(the_board)
                    print('tie')
                    game_on = False
                else:
                    turn = 'Player1'

    if not replay():    # to play the game again or not
        break
