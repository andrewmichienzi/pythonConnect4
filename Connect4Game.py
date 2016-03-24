#!/usr/bin/python
import sys
from Board import Board
import pickle

class Connect4Game:
	def __init__(self, num_rows, num_columns, winSize):
		self.board = Board(num_rows, num_columns, winSize)
		self.isPlayer1 = True

	def play(self):
		self.board.createBoard()
		while self.board.noWinner:
			x = self.getInput()
			if x == -1:
				self.save()
			elif x == -2:
				self.load()
			else:
				self.board.selectToken(x, self.getPlayer())
				self.switchPlayer()
		winner = self.board.winner
		sys.stdout.write('Player {} is the winner.  Congragulations!'.format(winner))

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
	
	def getInput(self):
		self.board.createBoard()
		x = input('Enter a Column Number(-1 for save, -2 for load):\t')
		return x

	def save(self):
		filename = raw_input ('Input filename:\t')
		with open(filename, 'wb') as output:
			pickle.dump(self.board, output, pickle.HIGHEST_PROTOCOL)	

	def load(self):
		filename = raw_input('Input filename:\t')
		with open(filename, 'rb') as ip:
			self.board = pickle.load(ip)
		self.getPlayerFromBoard()	
		
	def getPlayerFromBoard(self):
		player = self.board.getPlayer()
		if player == 1:
			self.isPlayer1 = True
		else:
			self.isPlayer1 = False

	def testBoard(self):
		sys.stdout.write('{}'.format(self.board.get(1,1)))
	


