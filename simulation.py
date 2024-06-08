import json
import os
import matplotlib.pyplot as plt
from wright_fisher import WrightFisherModel
import matplotlib.cm as cm
import numpy as np

def main():

    script_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(script_dir, "data", "config.json") 

    print(config_path)
    with open(config_path, 'r') as config_file:
        config = json.load(config_file)
    num_simulations = config["num_simulations"]
    population_sizes = config["population_sizes"]
    initial_frequencies = config["initial_frequency"]
    generations = config["generations"]
    mutation_rate = config["mutation_rate"]
    
    count = 1
    all_simulations = []
    titles = []
    population_colors = {}
    
    # Create a color map for the population sizes
    colors = cm.viridis(np.linspace(0, 1, len(population_sizes)))
    
    for pop_size, color in zip(population_sizes, colors):
        population_colors[pop_size] = color
    
    for population_size in population_sizes:
        for freq in initial_frequencies:
            simulations = run_simulations(population_size, freq, mutation_rate, generations, num_simulations)
            all_simulations.append((simulations, population_colors[population_size]))
            title = f"Simulation #{count}\npop_size={population_size}, init_freq={freq}"
            titles.append(title)
            count += 1

    plot_all_simulations(all_simulations, titles)


def run_simulations(population_size, initial_frequency, mutation_rate, generations, num_simulations):
    simulations = []
    wf_model = WrightFisherModel(population_size, generations, initial_frequency, mutation_rate)
    for _ in range(num_simulations):
        simulations.append(wf_model.simulate())
    return simulations

def plot_all_simulations(all_simulations, titles):
    num_plots = len(all_simulations)
    rows = cols = 4
    fig, axs = plt.subplots(rows, cols, figsize=(15, 15))
    
    for idx, ((simulations, color), title) in enumerate(zip(all_simulations, titles)):
        row = idx // cols
        col = idx % cols
        ax = axs[row, col]
        for sim in simulations:
            ax.plot(sim, alpha=0.5, color=color)
        ax.set_title(title, fontsize=7)
        ax.set_xlabel('Generations', fontsize=7)
        ax.set_ylabel('Allele Frequency',fontsize=7)
        ax.set_ylim(0, 1)
        
    fig.suptitle('Wright-Fisher Model Simulations', fontsize=16)
    plt.subplots_adjust(wspace=0.6, hspace=0.9)
    plt.show()


if __name__ == "__main__":
    main()
