values = "23456789XJQKA"
suits  = "SHDC"
jokers = "+-"

class Card(object):
	def __init__(self, cid):
		self.cid = cid

	def isJoker(self):
		return self.cid > 51

	def getValue(self):
		return self.cid % 13

	def getSuit(self):
		return (self.cid + 26) % 4 # For elegance :)

	def getFilename(self):
		filename = ""
		value = self.getValue()

		if self.isJoker():
			filename += ["red", "black"][value] + "_joker"
		elif value in range(2, 11):
			filename += str(value)
		elif value in range(11,15):
			filename += ["jack", "queen", "king", "ace"][value - 11]

		filename += "_of_"
		filename += ["spades", "hearts", "diamonds", "clubs"][self.getSuit()]
		filename += ".svg"

		return filename

	def __str__(self):
		value = self.getValue()
		if self.isJoker():
			return jokers[value] * 2
		else:
			return values[value] + suits[self.getSuit()]

	def __eq__(self, other):
	 	return self.cid == other.cid

	def __neq__(self, other):
	 	return not (self == other)

	def __lt__(self, other):
		return self.getValue() < other.getValue() and self.getSuit() < other.getSuit()

	def __le__(self, other):
		return self < other or self == other

	def __gt__(self, other):
		return not (self <= other)

	def __ge__(self, other):
		return not (self < other)