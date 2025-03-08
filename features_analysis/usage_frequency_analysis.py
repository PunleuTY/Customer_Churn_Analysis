from base_analysis import BaseAnalysis

# Import Libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

class UsageFrequencyAnalysis(BaseAnalysis):
# Usage Rate
    def perform_analysis(self):
        df = self.load_data()
        
        # Calculate usage frequency average
        usage_frequency_average = df["Usage Frequency"].mean()
        print(f"Usage Frequency Average: {round(usage_frequency_average)} times.")
        
        # Create usage rate and usage rate group
        self.create_usage_rate_and_group(df)
        print("\nUsage Rate and Usage Rate Group: ")
        print(df.head())

        # Churn rate by group
        usage_churn_rate = self.churn_rate_by_group(df)
        print("\n", usage_churn_rate)
        
        # Usage Rate Visualization
        self.usage_rate_visualization(usage_churn_rate)
        
    def create_usage_rate_and_group(self, df):
        df["Usage Rate"] = df["Usage Frequency"] / df["Tenure"]
        df["Usage Rate Group"] = df["Usage Rate"].apply(self.categorize_usage_rate)
        
    
    def categorize_usage_rate(self, usage_rate):
        if usage_rate < 0.016:
            return "Inactive"
        elif 0.016 <= usage_rate <= 9.99:
            return "Low"
        elif 9.99 < usage_rate <= 19.98:
            return "Medium"
        else:
            return "Active"
        
    def churn_rate_by_group(self, df):
        return df.groupby("Usage Rate Group")["Churn"].mean() * 100
    

    def usage_rate_visualization(self, usage_churn_rate):
        # Plot churn rate by age group
        plt.figure(figsize=(8, 5))
        sns.barplot(x = usage_churn_rate.index, y = usage_churn_rate.values, palette = "coolwarm")
        plt.title("Churn Rate by Usage Rate Group")
        plt.ylabel("Churn Rate (%)")
        plt.xlabel("Usage Rate Group")
        plt.ylim(0, 100)

        plt.show()
            
    
if __name__ == "__main__":
    path = "data/data_500_rec.csv"
    obj = UsageFrequencyAnalysis(path)
    obj.perform_analysis()
    