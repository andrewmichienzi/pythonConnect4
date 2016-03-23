#! /usr/bin/python
import sys
#import exceptions
from Connect4Game import Connect4Game
from Board import Board
# Get the total number of args passed to the demo.py
total = len(sys.argv)
#try:
if total != 4:
	print "InvalidArgumentException"
        sys.exit(0)
                #raise exceptions.InvalidArgumentsException(total)
#except(InvalidArgumentsException):
        #sys.exit(0)


# Get the arguments list 
cmdargs = str(sys.argv)

# Print it
print ("The total numbers of args passed to the script: %d " % total)
print ("Args list: %s " % cmdargs)

num_rows = int(sys.argv[1])
num_columns = int(sys.argv[2])
winSize = int(sys.argv[3])

game = Connect4Game(num_rows, num_columns, winSize)
game.play()
print 'out'

'''









if not correctSize(num_rows, num_columns, winSize):
        print "Invalid win size.  Will not work with board"
        sys.exit(0)

board = [[0 for i in range(num_rows)]for j in range(num_columns)]

createBoard(num_rows, num_columns, board)

############################################
#Player Turn
############################################

isPlayer1 = True


player = getPlayer(isPlayer1)
col = chooseColumn(player, board, num_rows, num_columns)
row = chooseRow(player, col, num_rows, num_columns, board)

board[row][col] = player

createBoard(num_rows, num_columns, board)
isPlayer1 = False






'''
