import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
class WrightFisherModel:
    
    def __init__(self, population_size: int, generations: int, initial_frequency:float, mutation_rate: float = -1) -> None:
        self.population_size = population_size
        self.generations = generations
        self.initial_freq = initial_frequency
        self.mutation_rate = mutation_rate
        pass


    def simulate(self):
            freq = self.initial_freq
            frequencies = [freq]
            for t in self.generations:
                freq = np.random.binomial(self.population_size, freq)/self.population_size
                frequencies.append(freq)
    
    def run_simulations(population_size, initial_frequency, selection_coefficient, mutation_rate, generations, num_simulations):
        simulations = []
        wf_model = WrightFisherModel(population_size, initial_frequency, selection_coefficient, mutation_rate)
        for _ in range(num_simulations):
            simulations.append(wf_model.simulate(generations))
        return simulations

    def plot_simulations(simulations, title):
        plt.figure(figsize=(10, 6))
        for sim in simulations:
            plt.plot(sim, alpha=0.5)
        plt.xlabel('Generations')
        plt.ylabel('Allele Frequency')
        plt.title(title)
        plt.show()

        
    def get_results(self):
        return pd.DataFrame({
                'Generation': range(self.generations),
                'Allele Frequency': self.allele_frequencies
                }) 