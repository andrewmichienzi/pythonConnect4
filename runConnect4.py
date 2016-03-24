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
