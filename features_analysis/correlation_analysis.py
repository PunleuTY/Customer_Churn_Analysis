from base_analysis import BaseAnalysis
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

class CorrelationAnalysis(BaseAnalysis):
    def __init__(self, data_path):
        super().__init__(data_path)

    def perform_analysis(self):
        df = self.load_data()

        features = ['Age', 'Tenure', 'Usage Frequency', 'Support Calls', 'Payment Delay', 'Total Spend', 'Last Interaction', 'Churn']
        
        correlation_churn = df[features].corr()[['Churn']]

        print(correlation_churn)
        self.plot_correlation_heatmap(correlation_churn)

    def plot_correlation_heatmap(self, correlation_matrix):
        sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.4)
        plt.title("Correlation Matrix with Churn")
        plt.show()

if __name__ == "__main__":
    file_path = "d:/year2/term2/python/Project/Customer_Churn_Analysis/data/data_500_rec.csv"
    churn_analysis = CorrelationAnalysis(file_path)
    churn_analysis.perform_analysis()

