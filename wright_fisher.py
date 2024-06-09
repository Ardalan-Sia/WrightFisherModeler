import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
class WrightFisherModel:
    
    def __init__(self, population_size: int, generations: int, initial_frequency: float, 
                 forward_mutation_rate: float = -1, reverse_mutation_rate: float = 0) -> None:
        self.population_size = population_size
        self.generations = generations
        self.initial_frequency = initial_frequency
        self.forward_mutation_rate = forward_mutation_rate
        self.reverse_mutation_rate = reverse_mutation_rate
        self.allele_frequencies = []
        
    def simulate_genetic_drift(self):
        """
        Simulate the Wright-Fisher model without mutation.
        """
        freq = self.initial_frequency
        frequencies = [freq]
        for _ in range(self.generations):
            freq = np.random.binomial(self.population_size, freq) / self.population_size
            frequencies.append(freq)
        self.allele_frequencies = frequencies
        return frequencies

    def simulate_genetic_drift_with_mutation(self):
        """
        Simulate the Wright-Fisher model with mutation.
        """
        freq = self.initial_frequency
        frequencies = [freq]
        for _ in range(self.generations):
            # Calculate the expected frequency of allele A after mutation
            expected_A = freq * (1 - self.forward_mutation_rate) + (1 - freq) * self.reverse_mutation_rate
            
            # Sample the frequency of allele A in the next generation
            freq = np.random.binomial(self.population_size, expected_A) / self.population_size
            
            # Update the frequency of allele A
            frequencies.append(freq)
        self.allele_frequencies = frequencies
        return frequencies
    
    # def get_results(self):
    #     """
    #     Get the results as a DataFrame.
    #     """
    #     return pd.DataFrame({
    #         'Generation': range(len(self.allele_frequencies)),
    #         'Allele Frequency': self.allele_frequencies
    #     }) 