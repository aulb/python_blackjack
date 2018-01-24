from enum import Enum


class Suit(Enum):
	"""
	Simple enum for suits.
	"""
	DIAMOND = 0
	CLUB = 1
	HEART = 2
	SPADE = 3


class Face(Enum):
	"""
	Simple enum for face. Card can be "hidden" or "revealed" 
	(face up or face down respectively).
	"""
	UP = 0
	DOWN = 1
	

class Rank(Enum):
	"""
	Simple enum for rank.
	"""
	TWO = 2
	THREE = 3
	FOUR = 4
	FIVE = 5
	SIX = 6
	SEVEN = 7
	EIGHT = 8
	NINE = 9
	TEN = 10
	JACK = 11
	QUEEN = 12
	KING = 13
	ACE = 14
