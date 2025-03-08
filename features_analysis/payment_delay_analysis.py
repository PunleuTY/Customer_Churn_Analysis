from base_analysis import BaseAnalysis

# Import Libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

class PaymentDelayAnalysis(BaseAnalysis):
    def perform_analysis(self):
        # load data set
        df = self.load_data()
        
        # Calculate payment delay average
        payment_delay_average = df["Payment Delay"].mean()
        print(f"Payment Delay Average: {round(payment_delay_average)} months.")
        
        # Payment Delay and Churn correlation
        payment_churn_correlation = df["Payment Delay"].corr(df["Churn"])
        print(f"Correlation between Payment Dela and Churn: {payment_churn_correlation:.2f}")
        
        # Scatter plot visualization
        self.correlation_visualiation(df)
        
    def correlation_visualiation(self, df):
        # Assuming you have the dataframe 'df' already loaded
        plt.figure(figsize = (8, 5))

        # Scatter plot with 'Payment Delay' on the x-axis and 'Churn' on the y-axis
        plt.scatter(df['Payment Delay'], df['Churn'], alpha=0.5)

        # Adding labels and title
        plt.title('Scatter Plot: Payment Delay vs. Churn')
        plt.xlabel('Payment Delay')
        plt.ylabel('Churn')
        # Show the plot
        plt.show()
        


if __name__ == "__main__":
    path = "data/data_500_rec.csv"
    obj = PaymentDelayAnalysis(path)
    obj.perform_analysis()