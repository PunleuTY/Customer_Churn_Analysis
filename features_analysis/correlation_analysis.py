from base_analysis import BaseAnalysis
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Class for performing correlation analysis, specifically with relate to Churn
class CorrelationAnalysis(BaseAnalysis):
    def __init__(self, data_path):
        # Initialize the class by calling the parent class constructor
        super().__init__(data_path)

    def perform_analysis(self):
        # Load the dataset for analysis
        df = self.load_data()

        # list of features to analyze their correlation with Churn
        features = ['Age', 'Tenure', 'Usage Frequency', 'Support Calls', 'Payment Delay', 'Total Spend', 'Last Interaction', 'Churn']
        
        # Calculate the correlation between the selected features and Churn
        correlation_churn = df[features].corr()[['Churn']]
        print(correlation_churn)

        # Call the method to plot the heatmap of the correlation matrix
        self.plot_correlation_heatmap(correlation_churn)

    def plot_correlation_heatmap(self, correlation_matrix):
        # Create a heatmap to visualize the correlation between features and Churn
        # annot=True: Show correlation values in the heatmap
        # cmap="coolwarm": Set the color scheme of the heatmap
        # fmt=".2f": Format the annotation values to 2 decimal places
        # linewidths=0.4: Set the linewidth of the gridlines in the heatmap
        sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.4)
        plt.title("Correlation Matrix with Churn") # Title of the heatmap
        plt.show()

if __name__ == "__main__":
    file_path = "d:/year2/term2/python/Project/Customer_Churn_Analysis/data/data_500_rec.csv"
    churn_analysis = CorrelationAnalysis(file_path)
    churn_analysis.perform_analysis()

