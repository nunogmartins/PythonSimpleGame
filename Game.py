import pickle
import os

class Game:
	def __init__(self):
		self.board = 'size of board = 0'
		print self.board
		self.it = 0
		self.load()
		
	def load(self):
		if os.path.exists('board.txt'):
			f = open('board.txt','r')
			self.matrix = pickle.load(f)
			f.close()
			print 'loaded board.txt'
		else:
			self.matrix = [] #matrix 10 x 10
			for y in range(10):
				self.matrix.append([])
				for x in range(10):
					self.matrix[y].append(1)
			
	
	def save(self):
		if not os.path.exists('board.txt'):
			f = open('board.txt','w')
			pickle.dump(self.matrix,f)
			f.close()
			print 'saved board.txt'
		else:
			print 'not saved board.txt'
		

	def update(self):
		out = ""
#		for a in range(0,10):
#			if a == self.it:
#				out +='0'
#			else:
#				out +='-'
#		print out
#		self.it +=1
		for y in range(10):
			for x in range(10):
				if y == 5 and x == 5:
					self.matrix[y][x] = 1
				out+=chr(self.matrix[y][x])
			print out
			out = ""
		self.it+=1
	

	def over(self):
		if self.it < 1:
			return bool(0)
		else:
			return bool(1)
