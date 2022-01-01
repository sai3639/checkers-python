# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 11:47:15 2021

@author: saira

"""

# Date:              14 October 2021
#checkers game

# board = {}
# # row = 0
# # columns = 0
# # make a checker board 
# for row in range(8):
#     for column in range(8):
#         board[(row, column)] = 0
# print(board)


# board = [['.', 'O', '.', 'O', '.', 'O', '.', 'O' ],
#          ['O', '.', 'O', '.', 'O', '.', 'O', '.'],
#          ['.', 'O', '.', 'O', '.', 'O', '.', 'O' ],
#          ['.', '.', '.', '.','.','.','.','.'],
#          ['.', '.', '.', '.','.','.','.','.'],
#          ['O', '.', 'O', '.', 'O', '.', 'O', '.'],
#          ['O', '.', 'O', '.', 'O', '.', 'O', '.']]

# print(board)

# if row = even 
# board = [['O','.']*8 for i in range (8)]
# print(board)




#initializes values, checkerboard will always be 8x8
numRows = 8
numCols = 8
board = []
stop = False

#Gives the user instructions
print("This program displays a checkerboard.When the user enters coordinates of a piece and a place for the piece to go, the piece will move")
print("Enter 'Stop' to end the program.")

#initial board layout
for i in range(numRows):
    row = []
    for j in range(numCols):
        if i % 2 == 0 and j % 2 == 1 and i < 3:
            row.append("O")
        elif i % 2 == 1 and j % 2 == 0 and i < 3:
            row.append("O")
        elif i % 2 == 0 and j % 2 == 1 and i > 4:
            row.append("o")
        elif i % 2 == 1 and j % 2 == 0 and i > 4:
            row.append("o")
        else:
            row.append(".")
    board.append(row)
            
#prints board for user to see           
for i in range(len(board)):
        print(board[i])
        
while stop != True:                                                                   
    #asks for user input on piece
    rowPiece = int(input("Enter the row of the piece you would like to move (1 through 8): "))
    colPiece = int(input("Enter the column of the piece you would like to move (1 through 8): "))
    #since the range of values is actually 0-7, subrtact 1 from user inputs
    rowPiece -= 1
    colPiece -= 1
    #checks if there is a piece there
    if board[rowPiece][colPiece] == ("O") or board[rowPiece][colPiece] == ("o"):
        #asks for user input on location
        store = board[rowPiece][colPiece]
        rowLoc = int(input("Enter the row of the location you would like to move the piece to (1 through 8): "))
        colLoc = int(input("Enter the column of the location you would like to move the piece to (1 through 8): "))
        #since the range of values is actually 0-7, subrtact 1 from user inputs
        rowLoc -= 1
        colLoc -= 1
        if (rowLoc % 2 == 0 and colLoc % 2 == 1) or (rowLoc % 2 == 1 and colLoc % 2 == 0):
            board[rowPiece][colPiece] = "."
            board[rowLoc][colLoc] = store
            for i in range(len(board)):
                print(board[i])
        #tells user if inputs are invalid
        else:
            print("Please enter a valid input")
    else:
        print("Please enter a valid input")
    #asks the user if they want to stop the program
    askStop = input("Would you like to stop? (Type 'Stop' to stop): ")
    if askStop == "Stop":
        stop = True
