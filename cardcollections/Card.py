from .CardEnum import Face, Rank


def card_rank(rank): 
	"""
	Helper to create a temporary card representation.
	"""
	return str(rank).split('.')[1].lower()

class Card:
	"""
	Simple card object.
	"""
	def __init__(self, rank, suit=None, face=Face.DOWN):
		# i.e: Rank.ONE, Rank.QUEEN, Rank.ACE
		self.rank = rank
		# i.e: Suit.DIAMOND
		self.suit = suit
		# i.e: Face.DOWN
		self.face = face

	def reveal(self):
		self.face = Face.UP

	def __repr__(self):
		"""
		Temporary card representation. 
		>>> print(Card(Rank.ACE, face=Face.UP))
		ace

		>>> print(Card(Rank.ACE))

		"""
		card_repr = '<Card is Hidden>!' 
		if self.face == Face.UP:
			card_repr = '{}'.format(card_rank(self.rank))
		return card_repr

	def __lt__(self, other):
		return self.rank.value < other.rank.value

	def __eq__(self, other):
		return self.rank.value == other.rank.value
