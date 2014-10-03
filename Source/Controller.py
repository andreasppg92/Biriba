from Model.Game import Game

class Controller(object):
	def __init__(self):
		self.game = Game()

	def startGame(self):
		self.game.start()

	def getCurrentPlayersHand(self):
		return self.game.getCurrentPlayersHand()
