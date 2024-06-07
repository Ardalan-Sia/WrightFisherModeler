import json
import os


def run_simulations():
        # Load configuration from JSON file
    config_path = os.path.join(os.path.dirname(__file__), 'data', 'config.json')
    with open(config_path, 'r') as config_file:
        config = json.load(config_file)

    num_simulations = config["num_simulations"]
    population_size = config["population_sizes"]
    initial_frequency = config["initial_frequency"]
    generations = config["generations"]
    mutation_rate = config["mutation_rate"]




if __name__ == "main":
    run_simulations
