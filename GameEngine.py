from Game import Game

class GameEngine:
	def __init__(self):
		print 'cons'
		self.game = Game()
	def update(self):
		print 'update'
		while not self.game.over():
			self.game.update()
		
	def load(self):
		print 'load'

	def save(self):
		print 'save'
		self.game.save()

