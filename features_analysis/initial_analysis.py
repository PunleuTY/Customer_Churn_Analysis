from base_analysis import BaseAnalysis

# Import Libraries
import pandas as pd

class InitialAnalysis(BaseAnalysis):
    def perform_analysis(self):
        # Load Data
        df = self.load_data()
        
        # Data columns and rows
        shape = df.shape
        print(f"Rows: {shape[0]}")
        print(f"Columns: {shape[1]}")

        
        # Inspect Data Head
        print(f"\nInspect Data Head:\n {df.head()}")
        
        # Inspect Data Tail
        print(f"\nInspect Data Tail:\n {df.tail()}")
        
        # Inspect Dataset Columns
        print(f"\nDataset Columns: {list(df.columns)}")
        
        # Datatype
        # print(f"\nData Types:\n {df.dtypes}")
        
        # Data info
        print("\nData Info:")
        print(df.info())
        
        # Statistic Summarize of Nnumeric Data
        print(f"\nStatistical Summarize:\n {df.describe().T}")
        
        # Find Null Values
        print(f"\nNull Values:\n {df.isnull().sum()}")
    
    
if __name__ == "__main__":
    path = "data/data_500_rec.csv"
    initial_analysis_obj = InitialAnalysis(path)
    initial_analysis_obj.perform_analysis()