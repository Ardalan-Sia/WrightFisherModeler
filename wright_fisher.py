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
            for t in range(self.generations):
                freq = np.random.binomial(self.population_size, freq)/self.population_size
                frequencies.append(freq)
            return frequencies
    

        
    def get_results(self):
        return pd.DataFrame({
                'Generation': range(self.generations),
                'Allele Frequency': self.allele_frequencies
                }) 