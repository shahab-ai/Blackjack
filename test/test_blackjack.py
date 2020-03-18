import sys
sys.path.append('./code')

from ..code.blackjack import Blackjack
# from ..code.deck import Deck
import nose.tools as n
import nose

def test_blackjack_init():
    game = Blackjack(human=False)
    n.assert_equal(game.players[0].name, "Player")
    n.assert_equal(game.players[0].money, 100)
    n.assert_equal(game.players[0].hand, [])

def test_play_game():
    game = Blackjack(human=False)
    game.deal(game.players[0])
    print(game.players[0])
    game.players[0].reset()
    game.play_game()

def test_multi_player():
    game = Blackjack(human=False, number_of_players=2)
    game.play_game()
