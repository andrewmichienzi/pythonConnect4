#!/usr/bin/python
import sys

class Board:
	def __init__(self, num_rows, num_columns, winSize):
		self.num_rows = num_rows
		self.num_columns = num_columns
		self.winSize = winSize
		self.board = [[0 for i in range(num_rows)]for j in range(num_columns)]
		self.noWinner = True
		self.winner = 0
		self.save = False
		self.save = True
		self.player = 1
		
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

	def getPlayer(self):
		return self.player

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

	def chooseColumn(self, col, player):
			
        	isValidColumn = self.checkColumn(col)
        	while not isValidColumn:
                	col = input('Incorrect column, choose another:\t')
			isValidColumn = self.checkColumn(col)
        	return col


############################
#Place Token
###########################

	def placeToken(self, player, col):
		if col >= self.num_columns:
			sys.stdout.write('\nError: you chose {} but therea re only {} columns on the board!'.format(col, self.num_columns))
        
        	for row in range(self.num_rows-1, -1, -1):
			token = self.board[row][col]
                	if token == 0:
                        	#Actually place token
				self.board[row][col] = player
				return True
        	return False
###########################################
#
#Select Token
#
############################################
	def selectToken(self, col, player):
		self.player = player
		col = self.chooseColumn(col, player)
		self.chooseRow(player, col)
		self.checkBoard()
		if not self.noWinner:
			self.winner = player

################################
#
#Check board for win
#
################################

	def checkBoard(self):
		self.checkHorizontalWin()
		self.checkVerticalWin()	
		self.checkDiagonalWin1()
		self.checkDiagonalWin2()
########################################
#
#Check Horizontal Win
#
######################################


	def checkHorizontalWin(self):
		print "check"
		for row in range(self.num_rows):
			inARow = 1
			temp = self.get(row, 0)
			print self.get(row,0)
			print temp
			print 'hello'
			for col in range(1, self.num_columns, 1):
				if self.get(row, col) == temp and temp != 0:
					inARow += 1
					print 'if'
					#sys.stdout.write('\ninARow:\t{}'.format(inARow))
				else:
					inARow = 1
					temp = self.get(row, col)
					print 'else'

				if inARow == self.winSize:
					print 'Horizontal win'
					self.noWinner = False	

###################################
#
#Check Vertical Win
#
####################################
	

	def checkVerticalWin(self):
		for col in range(self.num_columns):
			inARow = 1
			temp = self.board[0][col]
			for row in range(1,self.num_rows, 1):
				if self.get(row,col) == temp and temp != 0:
					inARow+=1
				else:
					inARow = 1
					temp = self.get(row,col)
				
				if inARow == self.winSize:
					print 'Vertical Win'
					self.noWinner = False


	def checkDiagonalWin1(self):
		coly = self.num_columns - self.winSize
		rowx = self.num_rows - self.winSize
		for col in range(coly+1):
			for row in range(rowx+1):
				y = col
				x = row

				inARow = 1
				temp = self.get(x,y)
				x+=1
				y+=1
				while y < self.num_columns and x < self.num_rows:


					if(self.get(x,y) == temp and temp != 0):
						inARow+=1
					else:
						temp = self.get(x,y)
						inARow = 1
					if inARow == self.winSize:
						print 'Diagonal Win'
						self.noWinner = False
					y+=1
					x+=1


	def checkDiagonalWin2(self):
		rowx = self.winSize
		coly = self.winSize
		for col in range(coly-1, 0, -1):
			for row in range(rowx-1):
				y = col
				x = row
				inARow = 1
				temp = self.get(x, y)
				x += 1
				y -= 1
				while x < self.num_rows and y > -1:
		
					if self.get(x, y) == temp and temp != 0:
						inARow +=1
					else:
						temp = self.get(x, y)
						inARow = 1
					if inARow == self.winSize:
						print 'Diagonal win'
						self.noWinner = False
					x += 1
					y -= 1
			

	
	def get(self, row, col):
		return self.board[row][col]




