import os
from random import shuffle
from cardcollections import *


def clear():
	"""
	Clear screen.
	"""
	if os.name == 'nt': 
		os.system('CLS')
	elif os.name == 'posix':
		os.system('clear')

def _input(message):
	"""
	Wrapper around raw_input method to get input from user.

	>>> Do you want to hit, stand, or quit? [H|S|Q]
	> user: H
	> h

	"""
	return input(message).lower()

class OnePlayerBlackjack:
	"""
	Implementation for a two player (CPU v player) game.
	CPU in this case is the dealer.
	"""
	def __init__(self):
		self.blackjack = 21
		self.game_count = 1
		self.game_won = 0
		self.starting_hand_count = 2

	def _initialize_new_game(self):
		"""
		To initialize a new game all we need to do is refresh the deck and
		shuffle two cards from the top of the deck to both the dealer and player.
		"""
		self.deck = Deck()

		# Player cards are both revealed (turned Face.UP)
		player_hand = [self.deck.take_from_top() for _ in range(2)]
		for card in player_hand:
			card.reveal()

		# Only the first of the dealer's card is revealed
		dealer_hand = [self.deck.take_from_top() for _ in range(2)]
		dealer_hand[0].reveal()

		self.player_hand = Hand(player_hand)
		self.dealer_hand = Hand(dealer_hand)

	def hit(self, hand):
		"""
		When hitting, the player that requesting it gets a card added to his/her hand.
		"""
		hand.add_card(self.deck.take_from_top())

	def card_sum(self, hand):
		"""
		Blackjack specific card sum. Ideally the hand should be sorted (two first, ace last), 
		so we can automatically score aces as 1s.

		All numbered cards are taken as its face value.
		All royal cards are taken as 10s.
		Aces can either be 1 or 11 depending on the total accumulated so far.

		Sum examples, pun intended:
		[Queen, Ace] -> 21 instead of 11
		[9, Ace, 8] -> 18 instead of 28
		"""
		total = 0
		hand.sort()
		for card in hand:
			if card.rank != Rank.ACE:
				total += min(card.rank.value, 10)
			else:
				total += 1 + 10 * (total >= 11)
		return total

	def play_again(self):
		"""
		Play again prompt.
		"""
		choice = _input('Do you want to play again? [Y|N]')

		if choice == 'y':
			self.game_count += 1
			self.play()
		else:
			print('Bye!')
			exit(0)

	def play(self):
		"""
		The main method of this class. Simply reset the game states and clear
		the screen.
		"""
		choice = 0
		clear()
		self._initialize_new_game()

		print('Welcome to Blackjack! Game {}'.format(self.game_count))
		if self.game_won:
			print('You\'ve won {} game{} so far'.format(self.game_won, 's' * (self.game_won > 1)))
		print('Dealer is showing {}'.format(self.dealer_hand[0]))

		print('You have {} and {}'.format(*self.player_hand))
		print('Your total is {}'.format(self.card_sum(self.player_hand)))
		self.score(self.dealer_hand, self.player_hand)

		choice = _input('Do you want to hit, stand, quit? [H|S|Q]?')
		if choice == 'q':
			print('Bye!')
			exit(0)
		elif choice == 'h':
			self.hit(self.player_hand)
			# Show the player's latest hand
			self.player_hand[-1].reveal()
			print('You are dealt {}'.format(self.player_hand[-1]))
			print('{}'.format(self.card_sum(self.player_hand)))

		# CPU logic, draw while less than 17 stand on 17 or more
		while self.card_sum(self.dealer_hand) < 17:
			print('Dealer is drawing...')
			self.hit(self.dealer_hand)
		
		self.score(self.dealer_hand, self.player_hand, beginning_of_game=False)
		self.play_again()

	def score(self, dealer_hand, player_hand, beginning_of_game=True):
		"""
		Checks the winning/losing state of the hands for each player.
		"""
		dealer_sum = self.card_sum(self.dealer_hand)
		player_sum = self.card_sum(self.player_hand)
		if player_sum == self.blackjack:
			print('Congratulations you have a blackjack! You won!')
			self.game_won += 1
			self.play_again()
		elif dealer_sum == self.blackjack:
			print('Dealer has a blackjack, womp womp.')
			self.play_again()

		# If its the beginning of the game we just want to check if we've already
		# won the game or not
		if beginning_of_game: return
		
		# Otherwise continue with the checks
		if player_sum > self.blackjack:
			print('Busted, you lose.')
		elif dealer_sum > self.blackjack:
			print('Dealer busted. You win!!')
			self.game_won += 1
		elif player_sum > dealer_sum:
			print('You win! Your score is higher!')
			self.game_won += 1
		elif dealer_sum > player_sum:
			print('You lose, your score is lower...')
		print('Final score. Dealer: {} Player: {}'.format(dealer_sum, player_sum))
			

if __name__ == '__main__':
	game = OnePlayerBlackjack()
	game.play()
