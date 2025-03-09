from base_analysis import BaseAnalysis
import pandas as pd
import matplotlib.pyplot as plt

# Class for analyzing Total Spend and its relation to Churn
class TotalSpendAnalysis(BaseAnalysis):
    def __init__(self, file_path):
        # Initialize the class by calling the parent class constructor
        super().__init__(file_path)
    
    def perform_analysis(self):
        # Load the dataset and perform analysis on Total Spend and Churn
        df = self.load_data() 

        # Calculate and print the average total spend and its correlation with churn
        average_total_spend = df['Total Spend'].mean() 
        correlation_spend_churn = df['Total Spend'].corr(df['Churn'])

        print(f"Average Total Spend: {average_total_spend:.2f}")
        print(f"Correlation between Total Spend and Churn: {correlation_spend_churn:.2f}")

        # Visualize the relationship between Total Spend and Churn
        self.visualize_data(df)

    def visualize_data(self, df):
        # scatter plot to show the relationship between Total Spend and Churn
        # df['Total Spend']: X-axis values (represents total spend of customers)
        # df['Churn']: Y-axis values (represents whether a customer churned or not
        # alpha: Makes points semi-transparent for better visualization
        plt.scatter(df['Total Spend'], df['Churn'], alpha=0.2)
        plt.title('Total Spend & Churn') # Title of scatter plot
        plt.xlabel('Total Spend') # x-axis label
        plt.ylabel('Churn') # y-axis label
        plt.show()

if __name__ == "__main__":
    file_path = "d:/year2/term2/python/Project/Customer_Churn_Analysis/data/data_500_rec.csv"
    analysis = TotalSpendAnalysis(file_path)
    analysis.perform_analysis()
