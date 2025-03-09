from base_analysis import BaseAnalysis
import pandas as pd
import matplotlib.pyplot as plt

# Class for analyzing Churn rate and its distribution
class ChurnAnalysis(BaseAnalysis):
    def __init__(self, data_path):
        # Initialize the class by calling the parent class constructor
        super().__init__(data_path)

    def perform_analysis(self):
        # Load the dataset and analyze the churn rate
        df = self.load_data()

        # Calculate the overall churn rate (percentage of customers who churned)
        churn_rate = df['Churn'].mean()
        print(f"Overall Churn Rate: {churn_rate * 100:.2f}%")

        # Count the number of churned and non-churned customers
        churned_count = df['Churn'].sum()
        not_churned_count = len(df) - churned_count

        print(f"Number of customers who churned: {churned_count}")
        print(f"Number of customers who did not churn: {not_churned_count}")

        # Generate visualizations for churn distribution
        self.graph(churned_count, not_churned_count)

    def graph(self, churned_count, not_churned_count):
        # Bar chart to compare the number of churned vs non-churned customers
        # ['Churned', 'Not Churned']: Labels for churned and non-churned customers
        # [churned_count, not_churned_count]: Number of customers in each category
        # color: Red for churned, Green for non-churned
        plt.bar(['Churned', 'Not Churned'], [churned_count, not_churned_count], color=['red', 'green'])
        plt.title('Number of Churned vs Not Churned Customers') # Title of the bar chart
        plt.ylabel('Number of Customers') # y-axis label
        plt.show()

        # Pie chart to show the proportion of churned vs non-churned customers
        # labels: Assign labels to each section
        # autopct: Format percentages in the chart
        # colors: Red for churned and Green for non-churned
        plt.pie([churned_count, not_churned_count], labels=['Churned', 'Not Churned'], autopct='%1.1f%%', colors=['red', 'green'])
        plt.title('Proportion of Churned vs Not Churned Customers') # Title of the pie chart
        plt.axis('equal') # Equal aspect ratio ensures that pie is drawn as a circle
        plt.show()

if __name__ == "__main__":
    file_path = "d:/year2/term2/python/Project/Customer_Churn_Analysis/data/data_500_rec.csv"
    churn_analysis = ChurnAnalysis(file_path)
    churn_analysis.perform_analysis()