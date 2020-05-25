import numpy as np 
import pygame
import sys

BLUE = (0,0,255)
BLACK = (0,0,0)

ROWCOUNT=8
COLOUMNCOUNT =8

def create_board():            # create board using numpy matrix
  board = np.zeros((8,8))
  return board

def piece(board,row,selection,piece):
  board[row][selection] = piece

def validation(board,selection):
  return board[7][selection] == 0 #checks if coloum has an empty slot

def next_open_row(board,selection):
  for r in range(ROWCOUNT):
    if board[r][selection] == 0: #record the instant it is 0 
      return r

def print_board(board):  #flips the axis of the board using numpy in built function as else pieces will fill from the top
  print(np.flip(board,0))

def win(board,piece):
  for x in range(COLOUMNCOUNT-3):  #checks for a horizontal win
    for r in range(ROWCOUNT):
      if board[r][x] == piece and board[r][x+1] == piece and board[r][x+2] == piece and board[r][x+3] == piece:
        return True

  for x in range(COLOUMNCOUNT-3):  #checks for a vertical win
    for r in range(ROWCOUNT-3):
      if board[r][x] == piece and board[r+1][x] == piece and board[r+2][x] == piece and board[r+3][x] == piece:
        return True

  for x in range(COLOUMNCOUNT-3):  #checks for a positive diagonal win
    for r in range(ROWCOUNT-3):
      if board[r][x] == piece and board[r+1][x+1] == piece and board[r+2][x+2] == piece and board[r+3][x+3] == piece:
        return True

  for x in range(COLOUMNCOUNT-3):  #checks for a negative diagonal win
    for r in range(3,ROWCOUNT):
      if board[r][x] == piece and board[r-1][x+1] == piece and board[r-2][x+2] == piece and board[r-3][x+3] == piece:
        return True

def draw_board(board):
  for c in range(COLOUMNCOUNT):
    for r in range(ROWCOUNT):
      pygame.draw.rect(screen,BLUE,(c* SQUARESIZE, r * SQUARESIZE + SQUARESIZE, SQUARESIZE,SQUARESIZE))
      pygame.draw.circle(screen,BLACK,(int(c * SQUARESIZE + SQUARESIZE/2), int(r *SQUARESIZE +SQUARESIZE+ SQUARESIZE/2)),RADIUS)


board = create_board()
print(board)

game_over = False     # checks if game is over

turn = 0   # indicates whose players turn it is

pygame.init()
 
SQUARESIZE = 80     #100pixels for the screen size
WIDTH = COLOUMNCOUNT * SQUARESIZE
HEIGHT = (ROWCOUNT+1) * SQUARESIZE
SIZE = (WIDTH,HEIGHT)
RADIUS =int(SQUARESIZE/2 -5)
screen = pygame.display.set_mode(SIZE)
draw_board(board)
pygame.display.update()

while not game_over:

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()
      
      if event.type == pygame.MOUSEBUTTONDOWN:
        continue
        #ask for player 1 input
##          if turn == 0:
##              selection = int(input("player 1 make your selection between 0 and 7"))
##              print(selection)
##              if validation(board,selection):
##                row = next_open_row(board,selection)
##                piece(board,row,selection,1)
##
##                if win(board,1):
##                  print("you win :)")
##                  game_over = True
##                
##                
##          else:
##              selection = int(input("player 2 make your selection between 0 and 7"))
##              print(selection)
##              if validation(board,selection):
##                row = next_open_row(board,selection)
##                piece(board,row,selection,2)
##
##          
##                if win(board,2):
##                  print("you win :)")
##                  game_over = True
##                  
##
##          print_board(board)    
##          turn +=1
##          turn = turn % 2 # alternates between 1 and 0 which changes the turns between players

