.PHONY: test
test:
	nosetests -s test/test_deck.py
	nosetests -s test/test_player.py
	nosetests -s test/test_blackjack.py

play:
	python code/blackjack.py
