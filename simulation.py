import json
import os
import matplotlib.pyplot as plt
from wright_fisher import WrightFisherModel  # Ensure this import matches your project structure
import matplotlib.cm as cm
import numpy as np

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(script_dir, "data", "config.json") 

    with open(config_path, 'r') as config_file:
        config = json.load(config_file)
    num_simulations = config["num_simulations"]
    population_sizes = config["population_sizes"]
    initial_frequencies = config["initial_frequency"]
    generations = config["generations"]
    forward_mutation_rate = config["forward_mutation_rate"]
    reverse_mutation_rate = config["reverse_mutation_rate"]
    
    all_simulations_drift = []
    all_simulations_mutation = []
    titles_drift = []
    titles_mutation = []
    population_colors = {}
    
    # Create a color map for the population sizes
    colors = cm.viridis(np.linspace(0, 1, len(population_sizes)))
    
    for pop_size, color in zip(population_sizes, colors):
        population_colors[pop_size] = color
    
    for population_size in population_sizes:
        for freq in initial_frequencies:
            simulations_drift = run_simulations(population_size, freq, forward_mutation_rate, reverse_mutation_rate, generations, num_simulations, mutation=False)
            simulations_mutation = run_simulations(population_size, freq, forward_mutation_rate, reverse_mutation_rate, generations, num_simulations, mutation=True)
            all_simulations_drift.append((simulations_drift, population_colors[population_size], population_size, freq))
            all_simulations_mutation.append((simulations_mutation, population_colors[population_size], population_size, freq))
            title_drift = f"pop_size={population_size}, init_freq={freq}"
            title_mutation = f"pop_size={population_size}, init_freq={freq}\nu={forward_mutation_rate}, v={reverse_mutation_rate}"
            titles_drift.append(title_drift)
            titles_mutation.append(title_mutation)

    plot_simulations(all_simulations_drift, titles_drift, population_sizes, initial_frequencies, "Without Mutation")
    plot_simulations(all_simulations_mutation, titles_mutation, population_sizes, initial_frequencies, "With Mutation")


def run_simulations(population_size, initial_frequency, forward_mutation_rate, reverse_mutation_rate, generations, num_simulations, mutation):
    simulations = []
    wf_model = WrightFisherModel(population_size, generations, initial_frequency, forward_mutation_rate, reverse_mutation_rate)
    for _ in range(num_simulations):
        if mutation:
            simulations.append(wf_model.simulate_genetic_drift_with_mutation())
        else:
            simulations.append(wf_model.simulate_genetic_drift())
    return simulations

def plot_simulations(all_simulations, titles, population_sizes, initial_frequencies, title_prefix):
    num_pop_sizes = len(population_sizes)
    num_init_freqs = len(initial_frequencies)
    
    # Adjust figsize to ensure square subplots
    fig, axs = plt.subplots(num_pop_sizes, num_init_freqs, figsize=(5 * num_init_freqs, 5 * num_pop_sizes), sharex=True, sharey=True)
    
    # Ensure axs is 2D array
    if num_pop_sizes == 1 and num_init_freqs == 1:
        axs = np.array([[axs]])
    elif num_pop_sizes == 1:
        axs = np.expand_dims(axs, axis=0)
    elif num_init_freqs == 1:
        axs = np.expand_dims(axs, axis=1)
    
    for (simulations, color, pop_size, init_freq), title in zip(all_simulations, titles):
        row = population_sizes.index(pop_size)
        col = initial_frequencies.index(init_freq)
        ax = axs[row, col]
        for sim in simulations:
            ax.plot(sim, alpha=0.5, color=color)
        ax.set_title(title, fontsize=7)
        ax.set_ylim(0, 1)
        if col == 0:
            ax.set_ylabel('Allele Frequency', fontsize=7)
        if row == num_pop_sizes - 1:
            ax.set_xlabel('Generations', fontsize=7)
        
    fig.suptitle(f'Wright-Fisher Model Simulations: {title_prefix}', fontsize=16)
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])  # Add padding for the super title
    plt.show()

if __name__ == "__main__":
    main()
