#!/usr/bin/python
import sys

class Board:
	def __init__(self, num_rows, num_columns, winSize):
		self.num_rows = num_rows
		self.num_columns = num_columns
		self.winSize = winSize
		self.board = [[0 for i in range(num_rows)]for j in range(num_columns)]
		self.noWinner = True
		self.temp = 0
###################################
# createBoard()
##################################		
		
	def createBoard(self):
        	print '\n\n  '
        	row = 0
        	col = 0
        	sys.stdout.write('  ')
        	for row in range(self.num_rows):
                	sys.stdout.write('{} '.format(row))
        	print '\n'

        	row = 0
        	for row in range(self.num_rows):
                	sys.stdout.write('{} '.format(row))
                	for col in range (self.num_columns):
                        	sys.stdout.write('{} '.format(self.board[row][col]))
                	print '\n'
        	print '\n\n'

##################################
#Check and Choose row
##################################

	def checkRow(self, row):
        	if row == -1:
                	print 'Error: column full'
                	return False
       		return True

	def chooseRow(self, player, col):
        	isValidRow = self.placeToken(player,col)
        	while not isValidRow:
			print 'Incorrect column, choose another'
			col = self.chooseColumn(player)
                	isValidRow = self.placeToken(player, col)
	
################################
#Check and Choose Columns
###############################

	def checkColumn(self, col):
        	if col < self.num_columns and col > -1:
                	return True
        	return False

	def chooseColumn(self, player):

        	sys.stdout.write('Player {}s turn\n'.format(player))
        	col = input('Choose a column:\t')
        	isValidColumn = self.checkColumn(col)
        	while not isValidColumn:
                	col = input('Incorrect column, choose another:\t')
			isValidColumn = checkColumn(col)
        	return col


############################
#Place Token
###########################

	def placeToken(self, player, col):
		if col >= self.num_columns:
			sys.stdout.write('\nError: you chose {} but therea re only {} columns on the board!'.format(col, self.num_columns))
        
        	for row in range(self.num_rows-1, -1, -1):
			sys.stdout.write('\nrow:\t{}'.format(row))
                	sys.stdout.write('\ncol:\t{}'.format(col))
			token = self.board[row][col]
			sys.stdout.write('\ntoken:\t{}'.format(token))
                	if token == 0:
                        	#Actually place token
				self.board[row][col] = player
				return True
        	return False

	def selectToken(self, player):
		col = self.chooseColumn(player)
		self.chooseRow(player, col)
		self.checkHorizontalWin()
		self.createBoard()

	def checkHorizontalWin(self):
		for row in range(self.num_rows):
			inARow = 1
			self.temp = self.get(row, 0)
			sys.stdout.write('{}'.format(self.get(row,0)))
			
			for col in range(1, self.num_columns, 1):
				sys.stdout.write('\ntemp:\t'.format(self.temp))
				if self.get(row, col) == self.temp and self.temp != 0:
					inARow += 1
					print 'if'
					#sys.stdout.write('\ninARow:\t{}'.format(inARow))
				else:
					inARow = 1
					self.temp = self.get(row, col)
					print 'else'

				if inARow == self.winSize:
					print 'Horizontal win'
					self.noWinner = False	

	def get(self, row, col):
		return self.board[row][col]




