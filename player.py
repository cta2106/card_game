class Player:
    def __init__(self, color):
        self.num_cards = 0
        self.color = color

    def take_cards(self):
        self.num_cards += 2
