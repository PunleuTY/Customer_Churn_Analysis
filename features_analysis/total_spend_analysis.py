from base_analysis import BaseAnalysis
import pandas as pd
import matplotlib.pyplot as plt

class TotalSpendAnalysis(BaseAnalysis):
    def __init__(self, file_path):
        super().__init__(file_path)
    
    def perform_analysis(self):
        df = self.load_data() 

        average_total_spend = df['Total Spend'].mean()
        correlation_spend_churn = df['Total Spend'].corr(df['Churn'])

        print(f"Average Total Spend: {average_total_spend:.2f}")
        print(f"Correlation between Total Spend and Churn: {correlation_spend_churn:.2f}")

        self.visualize_data(df)

    def visualize_data(self, df):
        plt.scatter(df['Total Spend'], df['Churn'], alpha=0.2)
        plt.title('Total Spend & Churn')
        plt.xlabel('Total Spend')
        plt.ylabel('Churn')
        plt.show()

analysis = TotalSpendAnalysis("d:/year2/term2/python/Project/Customer_Churn_Analysis/data/data_500_rec.csv")
analysis.perform_analysis()
