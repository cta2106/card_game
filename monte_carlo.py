from game import Game


class MonteCarlo:
    def __init__(self, n_sim):
        self.game = None
        self.n_sim = n_sim
        self.cum_black_player_payout = 0

    def run_simulation(self):
        self.game = Game()

        for _ in range(self.n_sim):
            self.game.play_game()
            self.cum_black_player_payout += self.game.black_player_payout
