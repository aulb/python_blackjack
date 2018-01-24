from random import shuffle
from .Card import Card
from .CardEnum import Rank


class Deck:
	"""
	Simple deck. Currently by default produces a simple full "bicycle" deck of cards.
	i.e: 1, 2, 3, ..., J, Q, K, A for all four suits.
	"""
	def __init__(self):
		self.deck = self._initialize_default_deck()

	def _initialize_default_deck(self):
		deck = []
		ranks = list(Rank)
		for _ in range(4):
			for rank in ranks:
				deck.append(Card(rank))
		shuffle(deck)
		return deck

	def take_from_top(self):
		if self.is_empty(): return
		return self.deck.pop()

	def is_empty(self):
		return len(self.deck) == 0
