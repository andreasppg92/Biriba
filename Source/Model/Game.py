from Player import Player
from Deck import Deck

class Game(object):
	def __init__(self):
		self.players = []
		for i in range(4):
			self.players.append(Player())

	def start(self):
		self.currentPlayer = 0

		self.deck = Deck()
		self.deck.shuffle()

		# Deal Cards
		i = 0
		for card in self.deck.getNCards(11 * 4):
			self.players[i].hand.append(card);
			i = (i + 1)%4

	def getCurrentPlayersHand(self):
		return sorted(self.players[self.currentPlayer].hand)