# Import abstract base class
from base_analysis import BaseAnalysis

# Import Libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Support Call Analysis Class
class SupportCallAnalysis(BaseAnalysis):
    # Perform support call analysis method
    def perform_analysis(self):
        # Load dataset
        df = self.load_data()
        
        # Caculate average value of support calls
        support_call_average = df["Support Calls"].mean()
        print(f"Average Support Calls: {round(support_call_average)} times.")
        
        # Correlation between support call and churn
            # Calcualte peason correlation between Churn and Support Calls
        support_churn_correlation = df["Churn"].corr(df["Support Calls"])
        print(f"Correlation between Support Calls and Churn: {support_churn_correlation:.2f}")
        
        # Visualization correlation
        self.correlation_visualiation(df)
        
    def correlation_visualiation(self, df):
        # Set figure dimension of 8 inches by 5 inches
        plt.figure(figsize = (8, 5))
        # Create scatterplot for representing correlation
            # x axis represent Support Calls column
            # y axis represent Churn column
            # Set transparency level of value 0.5
        sns.scatterplot(x = df["Support Calls"], y = df["Churn"], alpha = 0.5)
        plt.xlabel("Support Calls") # Label for x aixs
        plt.ylabel("Churn") # Label of y axis
        plt.title("Scatter Plot: Support Calls vs Churn") # Title of figure
        plt.show() # Display figure

if __name__ == "__main__": # Testing in the module
    path = "data/data_500_rec.csv" # Data path
    support_call_obj = SupportCallAnalysis(path) 
    support_call_obj.perform_analysis()