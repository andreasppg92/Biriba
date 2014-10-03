class Pair(object):
	def __init__(self, players):
		self.players = players
		self.score = 0
		self.currentPlayer = 0

	def nextPlayer(self):
		self.currentPlayer = (self.currentPlayer + 1) % 2;
		return self.players[self.currentPlayer]