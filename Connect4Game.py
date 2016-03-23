#!/usr/bin/python
import sys
from Board import Board

class Connect4Game:
	def __init__(self, num_rows, num_columns, winSize):
		self.board = Board(num_rows, num_columns, winSize)
		self.isPlayer1 = True

	def play(self):
		self.board.createBoard()
		while self.board.noWinner:
			self.board.selectToken(self.getPlayer())
			self.switchPlayer()

	def getPlayer(self):
		if self.isPlayer1:
			return 1
		else:
			return 2
			
	def switchPlayer(self):
		if self.isPlayer1:
			self.isPlayer1 = False
		else:
			self.isPlayer1 = True
	
	def testBoard(self):
		sys.stdout.write('{}'.format(self.board.get(1,1)))
