import random

class Deck(object):
	def __init__(self):
		self.cards = range(54)

	def shuffle(self):
		random.shuffle(self.cards)

	def getCard(self):
		return self.cards.pop()

	def getNCards(self, n):
		cards = []
		for i in range(n):
			cards.append(self.getCard())
		return cards

