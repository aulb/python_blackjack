class Hand:
	"""
	Simple hand object. A hand is simply a list of Card objects.
	"""
	def __init__(self, hand=[]):
		self.hand = hand

	def add_card(self, card):
		self.hand.append(card)

	def sort(self):
		self.hand.sort()

	def __getitem__(self, item):
		"""
		This magic function helps the object support indexing.
		"""
		return self.hand[item]
