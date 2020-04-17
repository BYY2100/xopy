#X O Game
#BY: BYY2100

import random
from os import system, name 
from time import sleep 

def clear(): 
    if name == 'nt': 
        _ = system('cls')     
    else: 
        _ = system('clear') 

def display_board(board):
    #print("\n"*100)
    clear()
    #sleep(1.5)
    
    print(board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('---------')
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('---------')
    print(board[1] + ' | ' + board[2] + ' | ' + board[3])

def player_input():
    mark = ''
    while mark != 'X' and mark != 'O':
        mark = input('Please choose wether you wanna play with X or O: ')
    p1 = mark
    if p1 == 'X':
        p2 = 'O'
    else:
        p2 == 'X'
    return (p1,p2)

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, mark):
      return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal
    
def choose_first():
    first = random.randint(0,1)
    if first == 0:
        return 'Player 1'
    else:
        return 'Player 2'

def space_check(board, position):
    
    if board[position] != '':
        return True
    else:
        return False

def full_board_check(board):
    
    for i in range (1, 10):
        if space_check(board,i):
            return False
        
    return True

def player_choice(board):
    
    pos = 0
    
    while pos not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        pos = int(input("Please enter the position > "))
    return pos

def replay():
    
    con = input('Do you wanna play again? (enter y to continue) > ')
    if con == 'y' or con == 'Y':
        return True
    else:
        return False
        
#################################################################################
#The main game

print('Welcome to Tic Tac Toe!')
print('This Was Programmed By: BYY2100')

while True:
    theBoard = [' ']*10
    s = input('Do you wanna play? (enter y to start playing)> ')
    p1 , p2 = player_input()
    turn = choose_first()
    print(f'{turn} will go first!')
    sleep(1.5)
    if s == 'y' or s == 'Y':
        game_play = True
    else:
        game_play = False
    position = 0
    while game_play:
        if turn == 'Player 1':
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard,p1,position)
            
            if win_check(theBoard,p1):
                display_board(theBoard)
                print('Congrats Player 1! You Won!!')
                game_play = False
            else:
                if full_board_check(theBoard):
                    print('Draw!')
                    game_play = False
                else:
                    turn = 'Player 2'
        
        else:
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard,p2,position)
            
            if win_check(theBoard,p2):
                display_board(theBoard)
                print('Congrats Player 2! You Won!!')
                game_play = False
            else:
                if full_board_check(theBoard):
                    print('Draw!')
                    game_play = False
                else:
                    turn = 'Player 1'
            
          

    if not replay():
        break