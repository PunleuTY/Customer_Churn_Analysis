from base_analysis import BaseAnalysis
import pandas as pd
import matplotlib.pyplot as plt  

# Class for analyzing the impact of last customer interaction on churn
class LastInteractionAnalysis(BaseAnalysis):
    def __init__(self, file_path):
        # Initialize the class by calling the parent class constructor
        super().__init__(file_path)

    def perform_analysis(self):
        # Load the dataset and perform analysis on Total Spend and Churn
        df = self.load_data()

        # Find the most recent and longest last interaction times
        min_last_interaction = df["Last Interaction"].min()
        max_last_interaction = df["Last Interaction"].max()
        # Calculate correlation between last interaction and churn
        correlation_last_interaction_churn = df["Last Interaction"].corr(df["Churn"])

        print(f"Most recent customer interaction: {min_last_interaction}")
        print(f"Longest time since customer interaction: {max_last_interaction}")
        print(f"Correlation between Last Interaction and Churn: {correlation_last_interaction_churn:.2f}")

        # Visualize the relationship between last interaction and churn
        self.visualize_data(df)

    def visualize_data(self, df):
        # Create a scatter plot to show the relationship between Last Interaction and Churn
        # df["Last Interaction"]: X-axis values (last interaction times)
        # df["Churn"]: Y-axis values (churn status)
        # alpha: Makes points semi-transparent for better visualization
        plt.scatter(df["Last Interaction"], df["Churn"], alpha=0.2)
        plt.title("Correlation between Last Interaction and Churn") # Title
        plt.xlabel("Last Interaction") # X-axis label
        plt.ylabel("Churn") # Y-axis label
        plt.show()

if __name__ == "__main__":
    file_path = "d:/year2/term2/python/Project/Customer_Churn_Analysis/data/data_500_rec.csv"
    analysis = LastInteractionAnalysis(file_path)
    analysis.perform_analysis()
