from base_analysis import BaseAnalysis

import pandas as pd
import matplotlib.pyplot as plt

class ChurnAnalysis(BaseAnalysis):
    def __init__(self, data_path):
        super().__init__(data_path)

    def perform_analysis(self):
        df = self.load_data()

        churn_rate = df['Churn'].mean()
        print(f"Overall Churn Rate: {churn_rate * 100:.2f}%")

        churned_count = df['Churn'].sum()
        not_churned_count = len(df) - churned_count

        print(f"Number of customers who churned: {churned_count}")
        print(f"Number of customers who did not churn: {not_churned_count}")

        self.graph(churned_count, not_churned_count)

    def graph(self, churned_count, not_churned_count):
        plt.bar(['Churned', 'Not Churned'], [churned_count, not_churned_count], color=['red', 'green'])
        plt.title('Number of Churned vs Not Churned Customers')
        plt.ylabel('Number of Customers')
        plt.show()

        plt.pie([churned_count, not_churned_count], labels=['Churned', 'Not Churned'], autopct='%1.1f%%', colors=['red', 'green'])
        plt.title('Proportion of Churned vs Not Churned Customers')
        plt.axis('equal')
        plt.show()



if __name__ == "__main__":
    file_path = "d:/year2/term2/python/Project/Customer_Churn_Analysis/data/data_500_rec.csv"
    churn_analysis = ChurnAnalysis(file_path)
    churn_analysis.perform_analysis()