# Import Abstract Base Class
from base_analysis import BaseAnalysis

# Import Libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Payment Delay Analysis Class
class PaymentDelayAnalysis(BaseAnalysis):
    # Payment Delay Analysis Method
    def perform_analysis(self):
        # load data set
        df = self.load_data()
        
        # Calculate payment delay average
        payment_delay_average = df["Payment Delay"].mean()
        print(f"Payment Delay Average: {round(payment_delay_average)} months.")
        
        # Payment Delay and Churn correlation
        # Calculate correlation value between Payment Delay and Churn
        payment_churn_correlation = df["Payment Delay"].corr(df["Churn"])
        print(f"Correlation between Payment Dela and Churn: {payment_churn_correlation:.2f}")
        
        # Call Scatter plot visualization method
        self.correlation_visualiation(df)
        
    # Correlation Visualiaztion Method
    def correlation_visualiation(self, df):
        # Define figure size of 8 inches by 5 inches
        plt.figure(figsize = (8, 5))
        # Create scatter plot
            # x axis represent value of Payment Delay
            # y axis represent value of Churn
            # Transparency level of value 0.5
        sns.scatterplot(x = df['Payment Delay'], y = df['Churn'], alpha = 0.7)
        # Scatter plot title
        plt.title('Scatter Plot: Payment Delay vs. Churn')
        # label of x axis
        plt.xlabel('Payment Delay')
        # label of y axis
        plt.ylabel('Churn')
        # Show the plot
        plt.show()
        


if __name__ == "__main__": # Testing in the module
    path = "data/data_500_rec.csv"
    obj = PaymentDelayAnalysis(path)
    obj.perform_analysis()