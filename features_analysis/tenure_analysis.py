from base_analysis import BaseAnalysis

# Import Libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class TenureAnalysis(BaseAnalysis):
    def perform_analysis(self):
        df = self.load_data()
        
        # Calculate Average of Tenure
        tenure_average = df["Tenure"].mean()
        print(f"Average Tenure: {round(tenure_average)} month\n")
        
        # Tenure Distribution
        self.tenure_group_distribution(df)
        print("Creating Tenure Distribution: ")
        print(df.head())
        
        # Tenure Churn Rate by Group
        tenure_churn_rate = self.churn_rate_by_group(df)
        print("\nCalculate churn rate by Tenure Group: ")
        print(tenure_churn_rate)
        
        # Tenure churn rate by group visualization
        self.churn_rate_visualization(tenure_churn_rate)
        
    
    def categorize_tenure(self, tenure):
        if tenure <= 12:
            return "New Customer"
        elif tenure >= 13 and tenure <= 36:
            return "Engage"
        elif tenure >= 37:
            return "Loyal" 
    
    def tenure_group_distribution(self, df):
        df["Tenure Group"] = df["Tenure"].apply(self.categorize_tenure)
        
    def churn_rate_by_group(self, df):
        return df.groupby("Tenure Group")["Churn"].mean() * 100
    
    def churn_rate_visualization(self, tenure_churn_rate):
        # Plot churn rate by age group
        plt.figure(figsize=(8, 5))
        sns.barplot(x = tenure_churn_rate.index, y = tenure_churn_rate.values, palette = "coolwarm")
        plt.title("Churn Rate by Tenure Group")
        plt.ylabel("Churn Rate (%)")
        plt.xlabel("Tenure Group")
        plt.ylim(0, 100)
        plt.show()
        
if __name__ == "__main__":
    path = "data/data_500_rec.csv"
    obj = TenureAnalysis(path)
    obj.perform_analysis()
        