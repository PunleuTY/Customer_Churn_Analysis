from base_analysis import BaseAnalysis

# Import Libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

class SupportCallAnalysis(BaseAnalysis):
    def perform_analysis(self):
        df = self.load_data()
        
        # Caculate average support calls
        support_call_average = df["Support Calls"].mean()
        print(f"Average Support Calls: {round(support_call_average)} times.")
        
        # Correlation between support call and churn
        support_churn_correlation = df["Churn"].corr(df["Support Calls"])
        print(f"Correlation between Support Calls and Churn: {support_churn_correlation:.2f}")
        
        self.correlation_visualiation(df)
        
    
    def correlation_visualiation(self, df):
        # Correlation visualization through Scatter Plot
        plt.figure(figsize = (8, 5))
        sns.scatterplot(x = df["Support Calls"], y = df["Churn"], alpha = 0.5)
        
        plt.xlabel("Support Calls")
        plt.ylabel("Churn")
        plt.title("Scatter Plot: Support Calls vs Churn")

        plt.show()

if __name__ == "__main__":
    path = "data/data_500_rec.csv"
    obj = SupportCallAnalysis(path)
    obj.perform_analysis()