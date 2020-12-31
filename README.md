# card_game
Solves a simple card game involving two players.

## Card Game: Would You Care to Play?
From Alexander Bogomolny's [book](https://www.amazon.com/Cut-Knot-Probability-Alexander-Bogomolny/dp/157955041X): 
[@CutTheKnotMath](https://twitter.com/CutTheKnotMath)

## Problem
I invite you to play the following card game:
Shuffle an ordinary deck of cards and deal them in pairs, face up. If both cards of a pair are black, you get them; if both are red, I get them. Otherwise, the cards are ignored.

You pay \$1 for the privilege of playing the game. Wen the deck is exhausted, the game is over, and you pay nothing if you have no more cards than I have. On the other hand, I wil pay you \$3 for every card that you have more than I have. 

Would you care to play with me?

## Solution
No! Both players will always end up having the same number of cards, and hence, the black player will always lose \$1.

## Running Monte-Carlo Simulation
Update the desired number of iterations in your simulation by modifying `n_iter` in `config.yml` and run the following command in your terminal.

```python
python main.py
```

