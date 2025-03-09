from base_analysis import BaseAnalysis
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
class AgeAnalysis(BaseAnalysis):
    def perform_analysis(self):
        print(f"\n Age Distribution: \n {self.age_distribution()}")
        self.visual_age_distribution()
        print(f"\nChurn Rate by Age  : \n {self.age_churn()}")
        self.visual_age_churn()
        
        plt.show()
    def age_categorize(self, age):
        if age >= 18 and age <= 30:
            return "Young"
        elif age >= 31 and age <= 50:
            return "Middle-aged"
        elif age >= 51 and age <= 65:
            return "Older"
        
    def age_distribution(self):
        return self.df["Age"].value_counts()
    
    def visual_age_distribution(self):
        plt.figure(figsize=(8, 5))
        sns.histplot(self.df['Age'], bins=20, kde=True, color="blue")
        plt.title("Age Distribution of Customers")
        plt.xlabel("Age")
        plt.ylabel("Frequency")
        plt.show()

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
