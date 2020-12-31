from monte_carlo import MonteCarlo
import yaml

if __name__ == "__main__":

    config = yaml.safe_load(open("config.yml"))
    mc = MonteCarlo(config["n_iter"])
    mc.run_simulation()
    print('Average payout: ${}'.format(mc.cum_black_player_payout/config['n_iter']))