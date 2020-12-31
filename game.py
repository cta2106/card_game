from player import Player
import itertools
import random


class Game:
    def __init__(self):
        self.black_player = Player(color="Black")
        self.red_player = Player(color="Red")
        self.deck = []
        self.card_colors = []
        self.black_player_payout = -1

    def _create_deck(self):
        card_faces = ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
        card_suits = ["D", "S", "H", "C"]

        self.deck = [item for item in itertools.product(card_faces, card_suits)]
        random.shuffle(self.deck)
        self._create_card_colors()

    def _create_card_colors(self):
        for _, suit in self.deck:
            if suit in ["C", "S"]:
                self.card_colors.append("B")
            else:
                self.card_colors.append("R")

    def play_game(self):
        self._create_deck()
        pairs_list = [
            self.card_colors[i : i + 2] for i in range(0, len(self.card_colors), 2)
        ]

        for first, second in pairs_list:
            if first == "B" and second == "B":
                self.black_player.take_cards()
            elif first == "R" and second == "R":
                self.red_player.take_cards()
            else:
                pass

        self.black_player_payout += (
            max(0, (self.black_player.num_cards - self.red_player.num_cards)) * 3
        )
