# Abstract Base Class
# OOP Concept Usage: Abstraction

"""

BaseAnalysis is the Abstract Base Class that provide contract for each subclass. Each subclass must perform the
perform_analysis() method.

"""

import pandas as pd
from abc import ABC, abstractmethod

class BaseAnalysis:
    def __init__(self, data_path):
        self.data_path = data_path
    
    def load_data(self):
        try:
            df = pd.read_csv(self.data_path)
        except FileNotFoundError:
            print("Dataset not found.")
        else:
            return df
    
    @abstractmethod
    def perform_analysis(self):
        # Load Dataset and store in df
        df = self.load_data()
        # Implement Here