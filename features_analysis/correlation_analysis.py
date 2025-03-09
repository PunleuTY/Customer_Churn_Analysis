from base_analysis import BaseAnalysis
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

class CorrelationAnalysis(BaseAnalysis):
    def __init__(self, data_path):
        super().__init__(data_path)

    def perform_analysis(self):
        df = self.load_data()

        df['Gender'] = df['Gender'].factorize()[0]
        df['Subscription Type'] = df['Subscription Type'].factorize()[0]

        features = ['Age','Gender','Tenure','Usage Frequency','Support Calls','Payment Delay','Subscription Type','Total Spend','Last Interaction']
        correlation_matrix = df[features].corr()

        print(correlation_matrix)
        
        self.correlation_matrix(correlation_matrix)
    
    def correlation_matrix(self, correlation_matrix):
        sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.4)
        plt.title("Correlation Matrix of Features")
        plt.show()

if __name__ == "__main__":
    file_path = "d:/year2/term2/python/Project/Customer_Churn_Analysis/data/data_500_rec.csv"
    churn_analysis = CorrelationAnalysis(file_path)
    churn_analysis.perform_analysis()
