from base_analysis import BaseAnalysis
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
class AgeAnalysis(BaseAnalysis):
    def perform_analysis(self):
        print("Running Age Distribution Visualization : ")
        self.visual_age_distribution()

        print("Running Churn Rate by Age :")
        self.visual_age_churn()

        # Categorizing age groups
        self.categorize_age_groups()
        print("\nChurn Rate by Age Group:\n", self.df.groupby("Age Group")["Churn"].mean() * 100)
        self.visual_age_churn_by_group()
    
        plt.show()

    def categorize_age_groups(self):
        bins = [18, 30, 50, 65]  # Define the age group ranges
        labels = ["Young", "Middle-aged", "Older"]
        self.df["Age Group"] = pd.cut(self.df["Age"], bins=bins, labels=labels, right=True)

    def visual_age_churn_by_group(self):
        plt.figure(figsize=(8, 5))
        sns.barplot(x='Age Group', y='Churn', data=self.df, estimator=lambda x: np.mean(x) * 100, palette="coolwarm")
        plt.title("Churn Rate by Age Group")
        plt.xlabel("Age Group")
        plt.ylabel("Churn Rate (%)")

        
    def age_distribution(self):
        return self.df["Age"].value_counts()
    
    def visual_age_distribution(self):
        plt.figure(figsize=(8, 5))
        sns.histplot(self.df['Age'], bins=20, kde=True, color="blue")
        plt.title("Age Distribution of Customers")
        plt.xlabel("Age")
        plt.ylabel("Frequency")

    def age_churn(self):
        result = self.df.groupby("Age")["Churn"].mean() * 100
        print(result)
        return result
    
    def visual_age_churn(self):
        plt.figure(figsize=(8, 5))
        sns.boxplot(x='Churn', y='Age', data=self.df, palette="coolwarm")
        plt.title("Age vs. Churn Rate")
        plt.xlabel("Churn (0 = No, 1 = Yes)")
        plt.ylabel("Age")
    


if __name__ == "__main__":
    data_path = "../data/data_500_rec.csv"
    age_analysis = AgeAnalysis(data_path)
    age_analysis.perform_analysis()
