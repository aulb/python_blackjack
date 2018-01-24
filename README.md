# Simple Terminal Python Blackjack
Welcome to a simple Blackjack game. This is a Python implementation of a one player (dealer being the CPU) Blackjack game with very simple rules.

# Simple Blackjack Gameplay
1) Dealer are dealt two cards, one of which is a face up card known to the player
2) You are dealt two cards, face up
3) If one of the initial hands are a Blackjack (21) then the player with 21 wins
Sidenote: Player are always checked first.
4) If your hand total score is lower than 21, you may hit, stand, or just quit the game.
Hitting: Add an extra face up card to your hand
Standing: Do nothing
Quit: Quit the game
Sidenote: Press H to hit, S to stand, or Q to quit, any other commands are regarded as stands
5) Dealer's hitting logic is standard, if dealer's hand total is below 17, keep hitting
6) Compare final score, player still get a priority check. 

# How to run?
Make sure to have Python3 installed. You can use virtualenv to generate a fully detachable Python3. Afterwards no extra packages are needed. Please download virtualenv if you do not have Python3+. 

`git clone https://github.com/aulb/python_blackjack`
`cd python_blackjack`
`virtualenv --no-site-packages -p python3.6 venv`
`source venv/bin/activate`
`python OnePlayerBlackjack.py`

To deactivate/escape the virtual environment just simply type `deactivate`.
